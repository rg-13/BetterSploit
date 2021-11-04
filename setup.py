from setuptools import setup, find_packages

setup(
	name='BetterSploit',
	version='1',
	packages= find_packages(),
	url='',
	license='',
	author='RG13Development',
	author_email='',
	description='',
	install_requires=open("bettersploit/requirements.txt").read().split("\n"),
	scripts="bettersploit",
	long_descrption=open("README.md").read(),
	long_desscription_content_type="text/markdown"
)
