import base64
import datetime
import json
import os.path
import sys

import requests
from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20_Poly1305
from lib.database import bettersploitdb
from termcolor import cprint


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
		self.ivKey = ColdStorage.ivKey
		self.nonce = ColdStorage.nonce
		self.useCipher = ColdStorage.useCipher
		self.bagofFiles = ColdStorage.bagofFiles
		self.fileDescription = ColdStorage.fileDescription

	def verifyfileexists(self, path_to_file=str(), check_recursive=bool()):
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

	def start_encryption(self, collected_files, store_to_db=bool(), owner=os.getlogin()):
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
						"Tag": str(base64.urlsafe_b64encode(tag).decode("utf-8")),
						"Owner": f"{owner}"
					}
				})
			return self.fileDescription

if __name__ == "__main__":
	a = ColdStorage()
	t = a.verifyfileexists("/home/notroot/projects/py/rg13/test123", False)
	print(a.start_encryption(t, True))