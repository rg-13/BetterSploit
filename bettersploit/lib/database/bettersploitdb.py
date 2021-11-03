import os
import string
import secrets
import psycopg2
import json
import yaml
from termcolor import cprint


class BetterDatabase:
	def __init__(self):
		self.baseDirectory = "/opt/BetterSploit"
		self.libDirectory = f"{self.baseDirectory}/lib/"
		self.customDirectory = f"{self.baseDirectory}/lib/custom/"
		self.toolsDirectroy = f"{self.libDirectory}/tools"
		self.dbaseHost = "localhost"
		self.genUserList = []
		self.dbasePort = 5432
		self.dbaseUser = "postgres"
		self.dbasePassword = ""
		self.dbaseName = "bettersploit"
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

	def createdb(self, userlist):
		pw = ''
		digits = string.digits
		asciilower = string.ascii_lowercase
		asciiupper = string.ascii_uppercase
		all = asciiupper + asciilower + digits
		if userlist is not None:
			for _ in range(15):
				pw += secrets.choice(all)
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
				self.cursor.execute(f"GRANT ALL PRIVILEGES ON public.{userlist}_encrypted_tools TO {self.dbaseUser};")
			self.genUserList.append(f"{userlist}:{pw}")
			self.cursor.execute("COMMIT")
		else:
			raise KeyError(f"Cannot create with empty user: {userlist}")
		if len(self.genUserList) != 0:
			return self.genUserList
		else:
			return [ "No Users were created." ]

	def buildSploits(self, path=str(), checkcustom=bool(), customdir=str()):
		if checkcustom is True and customdir is not None:
			path = customdir
		elif checkcustom is True and customdir is None:
			path = self.customDirectory
		else:
			path = path
		for dirpath, dirname, filenames in os.walk(path):
			for fname in filenames:
				if fname.endswith('json'):
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
								self.cursor.execute(
									'''INSERT INTO bettersploit_sploits(version, cve, path, desciption) VALUES(%s,
									%s,%s,%s)''',
									('No Data', name, gh_path, desc))
						except (KeyError, psycopg2.IntegrityError) as e:
							print(f"[ !! ] Appears as though, we have a key error: \n-> {e}")
							pass

	def buildEvasionList(self, path):
		if path is not None:
			for dirpath, dirname, filenames in os.walk(path):
				for fname in filenames:
					if fname.endswith('yml'):
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

	def buildToolsList(self, directory, purpose, method, is_private):
		try:
			extras = list()
			name_list = list()
			ps = list()
			xml_file = list()
			if method == "build":
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
						grouping = [ directory + '/' + file ]
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
			else:
				if is_private is not True:
					self.cursor.execute(f"INSERT INTO bettersploit_encrypted_tools(path, types, purpose, lang, key, nonce, cipher, tag, hash) VALUES (?,?,?,?)")
				else:
					self.cursor.execute(f"INSERT INTO {os.getlogin()}_encrypted_tools VALUES (path, types, purpose, lang, key, nonce, cipher, tag, hash) VALUES (?,?,?,?,?,?,?,?,?)")
			self.connectionString.commit()
		except psycopg2.OperationalError as e:
			print(f"Error happened when populating the database..\n->{e}")

	def query_Sploits(self, tech=str(), version=str(), host=str()):
		sel_stmt = "SELECT bettersploit_sploits(cve) FROM bettersploit_sploits WHERE bettersploit_sploits(tech) = (?) " \
				   "" \
				   "AND bettersploit_sploits(version) = (?)"
		for row in self.cursor.execute(sel_stmt):
			self.cursor.execute("UPDATE bettersploit_loot(best_cve) WHERE bettersploit_loot(host) = (?)",
								(row[ 1 ], host))
			print(f"Possible best exploit to use would be: {row[ 1 ]}\n For Host: {host}")
			print(
				f"There is an entry in the database located at: SELECT bettersploit_loot(best_cve) FROM "
				f"bettersploit_loot WHERE bettersploit_loot(host) = {host}")
		return True

	def insertLewts(self, lewt=str(), os=str(), cve_used=str(), best_guessed_cve=str(), are_we_persisting=bool(), what_did_we_take=str()):
		print("coming soon.")

	def insertTimeruns(self, what):
		if what is not None:
			self.cursor.execute("INSERT INTO bettersploit_data(when_run) VALUES(%s)", (what,))
		else:
			raise KeyError("")

	def checkForRun(self):
		try:
			for row in self.cursor.execute(
					"SELECT bettersploit_data.when_run FROM bettersploit_data WHERE when_run = 'initial'"):
				if row[ 0 ] is not None:
					return True
				else:
					return False
		except (psycopg2.DatabaseError, psycopg2.OperationalError, TypeError):
			return False

	def queryTools(self, lang, method=''):
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
			   f"| Total Powershell Mods: {psh[ 0 ]} | Total Recon Mods: {recon[ 0 ]} | Total general Items: {gener[0]}","green",
			   attrs=[ "bold" ])

	def rollingLog(self, user, function, target, outfile):
		stmt = "INSERT INTO bettersploit_log(bettersploit_user, bettersploit_function_used, target, where_is_result) " \
			   "VALUES(%s, %s, %s, %s)"
		if user is not None:
			self.cursor.execute(stmt, (user, function, target, outfile))
		else:
			user = os.getlogin()
			self.cursor.execute(stmt, (user, function, target, outfile))


