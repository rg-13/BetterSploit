import cmd
from bettersploit.lib.database.bettersploitdb import BetterDatabase

aa = BetterDatabase()

class dbShell(cmd.Cmd):
	intro = ''
	prompt = "[ + ] betterspliot DB [ + ]//->"

	def runcreatedb(self):
		'''
		Create
		'''
		aa.createdb()

	def loadTools(self, arg):

		"""
		This requires 3 args to be passed.
		Action: The action to take
		Directory: Directory to parse over.
		Puser: who owns it
		Purpose: What purpse this tool serves(seperate by underscore)
		Type: What does it do? Maintain access? Exfil data? Proxy traffic?(use 1 word or seperate by underscore[ _ ])
		
		ex: loadTools custom /path/to/custom notroot access maintain_Access
		"""
		args = str(arg).split(" ")
		if args[0] == "build":
			aa.buildToolsList('', '', '', '', '', '', "build")
		else:
			aa.buildToolsList(directory=args[1], purpose=args[3], type=args[4], is_private=args[5],
									 private_user=args[2], store_encrypted=args[6], method=args[0])
	def querysploits(self, arg):
		'''
		Expects 2 args, seperated by space.
		cve: cve number or name to look for
		host: host you are trying to use against. default is empty.

		ex: querysploits zerologon 127.0.0.1
		'''
		args = str(arg).split(" ")
		if len(args) == 1:
			aa.query_Sploits(cve=args[0], host='')
		else:
			aa.query_Sploits(cve=args[0], host=args[1])

	def querytools(self, arg):
		'''
		querytools language method
		'''
		args = str(arg).split(" ")
		if len(args) == 1:
			aa.queryTools(lang=args[0], method='')
		else:
			aa.queryTools(lang=args[0], method=arg[1])

	def buildsploits(self, arg):
		'''
		buildsploits update
		OR
		buildsploits /path/to/json/files custom
		'''
		args = str(arg).split(" ")
		if args[0] == 'update':
			aa.buildSploits('', False, True)
		elif len(args) == 2 and args[1] != "custom":
			aa.buildSploits(args[0], False, False)
		else:
			aa.buildSploits(args[0], True, False)

	def buildEvasions(self, arg):
		'''
		buildEvasions /path/to/evasion/yaml/file(s)
		'''
		args = str(arg).split(" ")
		if args[0]:
			aa.buildEvasionList(arg[0])


	def queryTools(self, arg):
		'''
		queryTools language method
		'''
		args = str(arg).split(" ")
		if len(args) == 2:
			aa.queryTools(args[0], args[1])

	def countmods(self):
		'''
		how many things do we have in the db
		'''
		aa.modCount()
