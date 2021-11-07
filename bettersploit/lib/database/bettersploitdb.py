import os
import string
import secrets
import psycopg2
import json
import yaml
import base64
import hashlib
import os.path

from termcolor import cprint
from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20_Poly1305


class BetterDatabase:
	ivKey = get_random_bytes(32)
	nonce = get_random_bytes(24)
	useCipher = ChaCha20_Poly1305.new(key=ivKey, nonce=nonce)
	bagofFiles = [ ]
	fileDescription = {}

	def __init__(self):
		self.hashUse = hashlib.sha512()
		self.ivKey = BetterDatabase.ivKey
		self.nonce = BetterDatabase.nonce
		self.useCipher = BetterDatabase.useCipher
		self.bagofFiles = BetterDatabase.bagofFiles
		self.fileDescription = BetterDatabase.fileDescription
		self.baseDirectory = "/opt/BetterSploit"
		self.libDirectory = f"{self.baseDirectory}/lib/"
		self.customDirectory = f"{self.baseDirectory}/lib/custom/"
		self.toolsDirectroy = f"{self.libDirectory}/tools"
		self.cvePath = f"{self.baseDirectory}/CVE"
		self.dbaseHost = "localhost"
		self.genUserList = [ ]
		self.dbasePort = 5432
		self.cipherText = ''
		self.tag = ''
		self.dbaseUser = os.environ.get("POSTGRES_USER")
		self.dbasePassword = os.environ.get("POSTGRES_PASSWORD")
		self.dbaseName = os.environ.get("POSTGRES_DB")
		self.inputUserList = os.environ.get("INPUT_USER_LIST")
		self.checkDB = True
		self.overrideCheckDB = False
		self.overrideDBUser = False
		self.verifyUser = True
		self.multiUser = True
		self.connectionString = psycopg2.connect(
			dbname=self.dbaseName,
			user=self.dbaseUser,
			password=self.dbasePassword,
			host=self.dbaseHost
		)
		self.cursor = self.connectionString.cursor()

	def createdb(self):
		'''
		Creating private database tables so users can store their tools into the db as they see fit.
		'''
		pw = ''
		digits = string.digits
		asciilower = string.ascii_lowercase
		asciiupper = string.ascii_uppercase
		all = asciiupper + asciilower + digits
		if os.path.isfile(self.inputUserList):
			with open(self.inputUserList, "r") as inList:
				for userlist in inList.readlines():
					if userlist == "" or userlist is None:
						os.remove(self.inputUserList)
					for _ in range(15):
						pw += secrets.choice(all)
					userlist = userlist.strip("\n")
					self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS public.{userlist}_encrypted_tools(
						id serial not null,
						date_added timestamp default CURRENT_TIMESTAMP not null,
						path text not null,
						types text not null,
						purpose text not null,
						lang text not null,
						key text not null unique,
						nonce text not null unique,
						cipher text not null unique,
						tag text not null unique,
						hash text not null unique
						)
						""")
					if userlist != self.dbaseUser:
						self.cursor.execute(f"CREATE ROLE {userlist} WITH LOGIN ENCRYPTED PASSWORD '{pw}'")
						self.cursor.execute(f"GRANT ALL PRIVILEGES ON public.{userlist}_encrypted_tools TO {userlist}")
						self.cursor.execute(f"GRANT ALL PRIVILEGES ON public.{userlist}_encrypted_tools TO notroot;")
					self.genUserList.append(f"{userlist}:{pw}")
					self.cursor.execute("COMMIT")
		else:
			raise KeyError(f"File did not exist, not generating any private spaces, using the default userspace. "
						   f"inputUserList: {self.inputUserList}")
		if len(self.genUserList) != 0:
			return self.genUserList
		else:
			return [ "No Users were created." ]

	def start_encryption(self, collected_files):
		"""
		Encrypt specified tool with a sha512 sum of the encrypted data to ensure when used to send file over the
		wire
		that the data has remained intact. Can be combined with the full key.nonce.ciphertext to ensure data
		integrity
		during transport across the wire.
		"""
		hashing = self.hashUse

		if isinstance(collected_files, list):
			for item in collected_files:
				dir, fname = os.path.split(item)
				collected_files.remove(item)
				ext = str(fname).split('.')
				if ext[1]:
					print(f"Extension: {ext[1]}")
				else:
					ext = 'None'
				for line in open(item, "rb"):
					self.cipherText, self.tag = self.useCipher.encrypt_and_digest(line)
					hashing.update(self.cipherText)
				self.fileDescription.update({
					"Key": str(base64.urlsafe_b64encode(self.ivKey).decode('utf-8')),
					"Nonce": str(base64.urlsafe_b64encode(self.nonce).decode('utf-8')),
					"Cipher Used": "ChaCha20_Poly1305",
					"Cipher Text": str(base64.urlsafe_b64encode(self.cipherText).decode('utf-8')),
					"Encrypted Data SHA512": str(base64.urlsafe_b64encode(hashing.digest()).decode('utf-8')),
					"Tag": str(base64.urlsafe_b64encode(self.cipherText).decode('utf-8')),
					"Path": f"{item}",
					"Filename": f"{str(fname)}",
					"Ext": f"{ext[1]}"
				}
				)
			return self.fileDescription

	def verifyfileexists(self, path_to_file=str(), check_recursive=bool()):
		"""
		Make sure we are reading and encrypting an actual file or directory, throwing error if either of those 2 fail.
		Path: path to file or folder
		Recursive: Recurse through folder, with this, the script will verify that the specified path is actually a directory or not. throwing error on failure.
		"""
		if path_to_file is not None:
			if check_recursive is True:
				try:
					assert os.path.isdir(path_to_file)
					for path, directories, files in os.walk(path_to_file):
						for directory in directories:
							for file in files:
								self.bagofFiles.append(str(os.path.join(path_to_file, directory, file)))
					return self.bagofFiles
				except AssertionError:
					raise AssertionError("Cannot Recurse on a single file.")
			else:
				try:
					assert os.path.isfile(path_to_file)
					if path_to_file not in self.bagofFiles:
						self.bagofFiles.append(path_to_file)
						return self.bagofFiles
					else:
						raise KeyError("Already Encrypted this tool, check the db and make sure it is in there.")
				except AssertionError:
					raise AssertionError("For directories, specify recursive.")
		else:
			raise Exception("You alseep at the keyboard or something? Stop being spastic.\n\n")

	def buildSploits(self, path, checkcustom, checkupdates):
		'''
		Check PoC from github directory to ensure that all exploits are loaded into the db, or specify a custom
		directory. These need to be in Json format.
		2 positional args needed, path to the exploits, checkcustom=True/False,
		'''
		if checkupdates is True:
			os.system(f"git pull https://github.com/nomi-sec/PoC-in-GitHub {self.cvePath}")
		if checkcustom is True and path is None:
			path = self.customDirectory
		else:
			path = self.cvePath
		for dirpath, dirname, filenames in os.walk(path):
			for fname in filenames:
				if fname.endswith('json'):
					print(f"Identified: {fname}")
					fullName = os.path.join(dirpath, fname)
					with open(fullName, "r", encoding="utf-8") as exp:
						try:
							for key in json.load(exp):
								if key[ 'name' ]:
									name = key[ 'name' ]
								if key[ 'html_url' ]:
									gh_path = key[ 'html_url' ]
								if key[ 'description' ]:
									desc = key[ 'description' ]
								try:
									self.cursor.execute(
										'''INSERT INTO bettersploit_sploits(version, cve, path, desciption) VALUES(%s,
										%s,%s,%s)''',
										('No Data', name, gh_path, desc))
								except Exception:
									print(f"Duplicate CVE Found: {fname}")
									pass
							self.cursor.execute("COMMIT")
						except (KeyError, psycopg2.IntegrityError) as e:
							print(f"[ !! ] Appears as though, we have a key error: \n-> {e}")
							pass

	def buildEvasionList(self, path):
		'''
		Build list of LOLBas into the db to be called at will. 1 positional arg needed:
		path
		These need to be in Yaml format.
		'''
		if path is not None:
			for dirpath, dirname, filenames in os.walk(path):
				for fname in filenames:
					if fname.endswith('yml'):
						if fname is None:
							return True
						evaderName = os.path.join(dirpath, fname)
						with open(evaderName, 'r', encoding='utf-8') as evad:
							evaderLoad = yaml.load(evad)
							try:
								if evaderLoad[ 'Name' ]:
									evName = evaderLoad[ 'Name' ]
								if evaderLoad[ 'Description' ]:
									evDoes = evaderLoad[ 'Description' ]
								if evaderLoad[ 'Commands' ]:
									evComms = evaderLoad[ 'Commands' ][ 0 ][ 'Command' ]
									evDescrip = evaderLoad[ 'Commands' ][ 0 ][ 'Description' ]
								if evaderLoad[ 'Full_Path' ]:
									evPath = evaderLoad[ 'Full_Path' ]
								self.self.cursor.execute(
									'''INSERT INTO bettersploit_evaders(evadername, evaderdoes, evadercommands, 
									evaderpath, evaderfulldesc) VALUES (%s, %s, %s, %s, %s)''',
									(evName, evDoes, evComms, evDescrip, evPath))
							except (KeyError, psycopg2.IntegrityError, psycopg2.ProgrammingError,
									yaml.composer.ComposerError) as e:
								print(f"->\n{e}")
								pass

	def buildToolsList(self, directory, purpose, type, is_private, private_user, store_encrypted, method):
		'''
		Build all tools we have, this can be go scripts, anything. These are tools that can be loaded onto a host for
		pivot/control/data exfil.

		May end up making this accept json format, and can be loaded in that way. Data handling will be much easier.
		'''
		try:
			extras = list()
			name_list = list()
			ps = list()
			xml_file = list()
			general = list()
			if method == "build":
				directory = self.toolsDirectroy
				for file in os.listdir(directory):
					if file.endswith('.py'):
						extras.append(directory + '/' + file)
					elif file.endswith('.txt'):
						name_list.append(directory + '/' + file)
					elif file.endswith('.xml'):
						xml_file.append(directory + '/' + file)
					elif file.endswith('.ps1'):
						ps.append(directory + '/' + file)
					else:
						general.append(directory + '/' + file)
			for item in extras:
				extras.remove(item)
				self.cursor.execute(
					"INSERT INTO bettersploit_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
					(item, "Script", purpose, 'python'))
			for item in name_list:
				name_list.remove(item)
				self.cursor.execute(
					"INSERT INTO bettersploit_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
					(item, "List", purpose, "text"))
			for item in xml_file:
				xml_file.remove(item)
				self.cursor.execute(
					"INSERT INTO bettersploit_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
					(item, "Scan", purpose, "XML"))
			for item in ps:
				ps.remove(item)
				self.cursor.execute(
					"INSERT INTO bettersploit_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
					(item, "Script", purpose, "Powershell"))
			for item in general:
				general.remove(item)
				self.cursor.execute(
					"INSERT INTO bettersploit_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
					(item, "General Purpose", purpose, "General Purpose"))
			else:
				if is_private is not True and private_user is not None:
					self.cursor.execute(f"INSERT INTO bettersploit_encrypted_tools(path, types, purpose, lang, "
										f"hash) VALUES (%s, %s, %s, %s, %s)",
										directory, type, purpose, "Custom")
				elif is_private is True and private_user is not None and store_encrypted is True:
					for item in self.verifyfileexists(directory, True):
						for fname in self.start_encryption(item):
							self.cursor.execute(
								f"INSERT INTO {private_user}_encrypted_tools VALUES (path, types, purpose, lang, key, "
								f"nonce, cipher, tag, hash, fdata) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s))",
								(fname[ 'Path' ], '', purpose, fname['Ext'], fname['Key'], fname['Nonce'],
								 fname['Cipher'], fname['Tag'], fname['Encrypted Data SHA512'], fname['Cipher Text']))
			self.connectionString.commit()
			return True
		except psycopg2.OperationalError as e:
			print(f"Error happened when populating the database..\n->{e}")
			return False

	def query_Sploits(self, cve=str(), host=str()):
		'''
		Pulls loaded exploit information from the database, and presents it on screen.
		2 positional arg:
		cve: title of the cve, or the cve number
		host: host you are trying to use this cve for
		'''
		if cve:
			sel_stmt = f"SELECT bettersploit_sploits(cve) FROM bettersploit_sploits WHERE bettersploit_sploits(cve) like '%{cve}%'"
			for row in self.cursor.execute(sel_stmt):
				self.cursor.execute("UPDATE bettersploit_loot(best_cve) WHERE bettersploit_loot(host) = (?)",
									(row[ 1 ], host))
				print(f"Possible best exploit to use would be: {row[ 1 ]}\n For Host: {host}")
				print(
					f"There is an entry in the database located at: SELECT bettersploit_loot(best_cve) FROM "
					f"bettersploit_loot WHERE bettersploit_loot(host) = {host}")
		else:
			self.cursor.execute("SELECT * FROM bettersploit_sploits LIMIT 50;")
			return self.cursor.fetchall()
		return True

	def insertLewts(self, lewt, os, cve_used, best_guessed_cve,
					are_we_persisting, what_did_we_take, target, on_target_local_path):
		'''
		Store the loots baby!
		'''
		if os is not None:
			if "windows" in os.lower():
				print("Assuming arch is x86 and 64/32")
			elif "arm" in os.lower():
				print("Nice, owned IOT")
			elif "nix" in os.lower():
				print("1337 pwning nix")
			else:
				print("Nice job {}".format(os.lower()))
			if lewt and cve_used and best_guessed_cve and what_did_we_take and target:
				grab_count = f"SELECT successful_uses FROM bettersploit_sploits WHERE cve = '{cve_used}'"
				self.cursor.execute(grab_count)
				aa = self.cursor.fetchone()
				if aa[ 0 ] is not None:
					if aa[ 0 ] > 5:
						print("Appears to be a very popular exploit!\nUses: {}".format(aa))
				c = aa[ 0 ] + 1
				self.cursor.execute(f"UPDATE bettersploit_sploits SET successful_uses = %s WHERE cve = %s",
									(c, cve_used,))
				self.cursor.execute(f"INSERT INTO bettersploit_loots("
									f"operating_system, host, local_path, type_of_loot, persist, best_cve, used_cve)"
									f"VALUES(%s, %s, %s, %s, %s, %s, %s)", (
										os.lower(), target, on_target_local_path,
										what_did_we_take, are_we_persisting, best_guessed_cve, cve_used,
									))
				self.cursor.execute("COMMIT")
				return [ os.lower(), target, on_target_local_path,
						 what_did_we_take, are_we_persisting, best_guessed_cve, cve_used ]
		else:
			raise ValueError(f"Missing needed information:\nloot:{lewt}\nos:{os}\ncve used: {cve_used}\n"
							 f"suggested cve:{best_guessed_cve}\npersist: {are_we_persisting}\n"
							 f"type of loot:{what_did_we_take}\ntarget: {target}\n"
							 f"path on target:{on_target_local_path}\n")

	def queryTools(self, lang, method=''):
		'''
		Query currently loaded tools that are in the database. searching by language, path, use case, and file type.
		'''
		cprint("[ !! ] In order to add to these modules, simply add your new module into the ./data/scripts folder "
			   "and re-run the program. [ !! ]", "red", attrs=[ "bold" ])
		modules = "[ + ] {} modules:\n".format(lang)
		cprint(modules, "green", attrs=[ "blink" ])
		sel_STMT = "SELECT lang, path, purpose, types from bettersploit_tools where bettersploit_tools.lang LIKE %s " \
				   "ESCAPE ''"
		choice_Select = """SELECT * FROM bettersploit_tools WHERE bettersploit_tools.path = %s """
		self.cursor.execute(sel_STMT, (lang,))
		choice_dict = {}
		i = 0
		for row in self.cursor.fetchall():
			choice_dict.update({i: row[ 2 ]})
			cprint("|------------------------------------------------------------------------------|\n", "green",
				   attrs=[ "bold" ])
			cprint(f"{i}->{row[ 1 ]}  |  {row[ 3 ]}  |  {row[ 2 ]}  |  {row[ 0 ]}", "blue", attrs=[ "bold" ])
			cprint("|______________________________________________________________________________|\n", "green",
				   attrs=[ "bold" ])
			i += 1
		cprint("[ !! ] Press enter to return to the main menu. [ !! ]", "red", attrs=[ "bold", "blink" ])
		choice = int(input("[ ? ] Please select your choice. [ ? ]\n->"))
		if choice != '':
			return choice_dict[ choice ]

	def modCount(self):
		'''
		Shows the grand total of everything we have loaded in the database.
		'''
		self.cursor.execute("SELECT COUNT(*) FROM (select lang from bettersploit_tools WHERE lang = 'python') AS "
							"TEMP;")
		python = self.cursor.fetchone()
		self.cursor.execute("SELECT COUNT(*) FROM (select lang from bettersploit_tools WHERE lang = 'text') AS TEMP;")
		text = self.cursor.fetchone()
		self.cursor.execute(
			"SELECT COUNT(*) FROM (select lang from bettersploit_tools WHERE lang = 'powershell') AS TEMP;")
		psh = self.cursor.fetchone()
		self.cursor.execute(
			"SELECT COUNT(*) FROM (select purpose from bettersploit_tools WHERE purpose = 'persistance') AS TEMP;")
		persi = self.cursor.fetchone()
		self.cursor.execute(
			"SELECT COUNT(*) FROM (select purpose from bettersploit_tools WHERE purpose = 'recon') AS TEMP;")
		recon = self.cursor.fetchone()
		self.cursor.execute(
			"SELECT COUNT(*) FROM (select purpose from bettersploit_tools WHERE purpose = 'general') AS TEMP;")
		gener = self.cursor.fetchone()
		cprint(f"| Total Python Mods: {python[ 0 ]} | Total Lists: {text[ 0 ]} | Total persistence mods: {persi[ 0 ]} "
			   f"| Total Powershell Mods: {psh[ 0 ]} | Total Recon Mods: {recon[ 0 ]} | "
			   f"Total general Items: {gener[0]}","green",attrs=[ "bold" ])

	def rollingLog(self, user, function, target, outfile):
		'''
		Team use.
		'''
		stmt = "INSERT INTO bettersploit_log(bettersploit_user, bettersploit_function_used, target, where_is_result) " \
			   "" \
			   "VALUES(%s, %s, %s, %s)"
		if user is not None:
			self.cursor.execute(stmt, (user, function, target, outfile))
		else:
			raise ValueError(f"Value error, user cannot be null: {user}")
		self.cursor.execute("COMMIT")
