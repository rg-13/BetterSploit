import os
import string
import secrets
import psycopg2
import json


class BetterDatabase:
	def __init__(self):
		self.baseDirectory = "/opt/BetterSploit"
		self.libDirectory = f"{self.baseDirectory}/lib/"
		self.customDirectory = f"{self.baseDirectory}/lib/custom/"
		self.toolsDirectroy = f"{self.libDirectory}/tools"
		self.genUserList = []
		self.dbaseHost = "localhost"
		self.dbasePort = 5432
		self.dbaseUser = "postgres"
		self.dbasePassword = ""
		self.dbaseName = "bettersploit_main"
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
		self.cursor = self.connectionString

	def createdb(self, first_run=bool(), userlist=""):
		if first_run is True:
			self.cursor.execute('''
				create table if not exists bettersploit_sploits
				(
					id         serial                                             not null
						constraint bettersploit_sploits_pkey
							primary key,
					datetime   timestamp with time zone default CURRENT_TIMESTAMP not null,
					version    text,
					cve        text
						constraint bettersploit_sploits_cve_key
							unique,
					path       text
						constraint bettersploit_sploits_path_key
							unique,
					desciption text                                               not null
				);
				alter table bettersploit_sploits
					owner to bettersploit;
			
			create table if not exists public.bettersploit_log
			(
				id                   serial not null
											constraint bettersploit_log_pk
											primary key,
				bettersploit_user          text   not null,
				bettersploit_function_used text,
				target               text,
				where_is_result      text
			);
			alter table public.bettersploit_log
				owner to bettersploit;
			create table if not exists public.bettersploit_tools
			(
				id               serial                                             not null
					constraint bettersploit_tools_pkey
						primary key,
				datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
				lang             text,
				path             text
					constraint bettersploit_tools_path_key
						unique,
				types             text,
				purpose          text
			);
			alter table public.bettersploit_tools
				owner to bettersploit;
			create table if not exists public.bettersploit_loots
			(
				id               serial                                             not null
					constraint bettersploit_loots_pkey
						primary key,
				datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
				operating_system text,
				host             text,
				local_path       text,
				type_of_loot     text,
				persist          boolean,
				best_cve         text,
				used_cve         text
			);
			alter table public.bettersploit_loots owner to bettersploit;
			create table if not exists public.bettersploit_data
			(
				id       serial                                             not null
					constraint bettersploit_data_pkey
						primary key,
				dtg      timestamp with time zone default CURRENT_TIMESTAMP not null,
				when_run text
			);
			alter table public.bettersploit_data
				owner to bettersploit; 
			create table if not exists public.bettersploit_evaders
			(
				id             serial                              not null,
				dategroup      timestamp default CURRENT_TIMESTAMP not null,
				evadername     text,
				evaderdoes     text,
				evadercommands text,
				evaderpath     text,
				evaderfulldesc text
			);
			
			alter table bettersploit_evaders
				owner to bettersploit;
			
			create unique index bettersploit_evaders_evadercommands_uindex
				on bettersploit_evaders (evadercommands);
			
			create unique index bettersploit_evaders_evadername_uindex
				on bettersploit_evaders (evadername);
			
			create unique index bettersploit_evaders_evaderpath_uindex
				on bettersploit_evaders (evaderpath);
			'''
			)
		if isinstance(userlist, list):
			pw = ''
			digits = string.digits
			asciilower = string.ascii_lowercase
			asciiupper = string.ascii_uppercase
			all = asciiupper + asciilower + digits
			for item in userlist:
				for _ in range(15):
					pw += secrets.choice(all)
				self.cursor.execute(f"CREATE ROLE {item} WITH LOGIN ENCRYPTED PASSWORD '{pw}'")
				self.cursor.execute(f"GRANT SELECT,INSERT,UPDATE ON ")
				self.genUserList.append(f"{item}:{pw}")

	def buildSploits(self, path=str(), checkcustom=bool(), customdir=str()):

		if path is not None:
			for dirpath, dirname, filenames in os.walk(path):
				for fname in filenames:
					if fname.endswith('json'):
						fullName = os.path.join(dirpath, fname)
						with open(fullName, "r", encoding="utf-8") as exp:
							try:
								for key in json.load(exp):
									if key['name']:
										name = key['name']
									if key['html_url']:
										gh_path = key['html_url']
									if key['description']:
										desc = key['description']
									self.cursor.execute('''INSERT INTO bettersploit_sploits(version, cve, path, desciption) VALUES(%s,%s,%s,%s)''', ('No Data', name, gh_path, desc))
							except (KeyError, psycopg2.IntegrityError) as e:
								print(f"[ !! ] Appears as though, we have a key error: \n-> {e}")
								pass