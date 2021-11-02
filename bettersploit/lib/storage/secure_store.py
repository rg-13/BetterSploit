import base64
import hashlib
import os.path

from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20_Poly1305
from bettersploit.lib.database import bettersploitdb


class ColdStorage:
	ivKey = get_random_bytes(32)
	nonce = get_random_bytes(24)
	useCipher = ChaCha20_Poly1305.new(key=ivKey, nonce=nonce)
	bagofFiles = [ ]
	fileDescription = {}

	def __init__(self):
		"""
		Defining a few constants, setting keylength to 32 bytes, and the number used once to 24. both are maximum size
		for this specific cipher.
		"""
		self.hashUse = hashlib.sha512()
		self.ivKey = ColdStorage.ivKey
		self.nonce = ColdStorage.nonce
		self.useCipher = ColdStorage.useCipher
		self.bagofFiles = ColdStorage.bagofFiles
		self.fileDescription = ColdStorage.fileDescription

	def verifyfileexists(self, path_to_file=str(), check_recursive=bool()):
		"""
		Make sure we are reading and encrypting an actual file or directory, throwing error if either of those 2 fail.
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

	def start_encryption(self, collected_files, store_to_db=bool(), owner=os.getlogin()):
		"""
		Encrypt specified tool with a sha512 sum of the encrypted data to ensure when used to send file over the wire
		that the data has remained intact. Can be combined with the full key.nonce.ciphertext to ensure data integrity
		during transport across the wire.
		"""
		if isinstance(collected_files, list) and store_to_db is True:
			for item in collected_files:
				dir, fname = os.path.split(item)
				collected_files.remove(item)
				for line in open(item, "rb"):
					cfr, tag = self.useCipher.encrypt_and_digest(line)
				self.fileDescription.update({
					f"{fname}": {
						"Key": str(base64.urlsafe_b64encode(self.ivKey).decode("utf-8")),
						"Nonce": str(base64.urlsafe_b64encode(self.nonce).decode("utf-8")),
						"Cipher Used": "ChaCha20_Poly1305",
						"Cipher Text": str(base64.urlsafe_b64encode(cfr).decode("utf-8")),
						"Encrypted Data SHA512": self.hashUse.update(cfr),
						"Tag": str(base64.urlsafe_b64encode(tag).decode("utf-8")),
						"Owner": f"{owner}"
					}
				})
			return self.fileDescription

	def uploadtodatabase(self, is_private=bool(), file_list="", loop=False):
		#@todo fix this later, this works for now.
		if file_list is None:
			if is_private is True and isinstance(file_list, list):
				loop=True
			elif is_private is True and isinstance(file_list, str):
				loop=False
			elif is_private is False and isinstance(file_list, list):
				loop = True
			else:
				loop = False

			pushtodb = bettersploitdb.BetterDatabase()
			pushtodb.rollingLog(os.getlogin(), f"secure stored:{file_list} as Private: {is_private}", None, None)
			if loop is True:
				for item in file_list:
					pushtodb.buildToolsList(item, "custom_tool", "custom_tool", True)
			else:
				pushtodb.buildToolsList(file_list, "custom_tool", "custom_tool", True)
		else:
			raise Exception(f"Cannot upload type: {file_list} to the database.\nActually need something.\n")


