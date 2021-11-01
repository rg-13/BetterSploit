#default locations
sqldir="/usr/share/sqlmap"
fidir="/usr/share/fimap"
joomdir="/usr/share/joomscan"
comdir="/usr/share/commix"
subdir="/usr/share/sublist3r"
sho="/usr/local/bin/shodan"
jexboss="/usr/share/jexboss"
wpscan="/usr/share/wpscan/wpscan.rb"
metasploit="/usr/share/metasploit-framework"
nuclei="/usr/share/nuclei"
nuclei_templates="/usr/share/nuclei/templates"
nuclei_modules="/usr/share/nuclei/modules"
nuclei_plugins="/usr/share/nuclei/plugins"
httpx="/usr/share/httpx"
dirsearch="/usr/share/dirb"
dirsearch_db="/usr/share/dirb/wordlists/common.txt"
dirsearch_db_ext="/usr/share/dirb/wordlists/common_ext.txt"
dirsearch_db_big="/usr/share/dirb/wordlists/big.txt"
dirsearch_db_big_ext="/usr/share/dirb/wordlists/big_ext.txt"
dirsearch_db_big_all="/usr/share/dirb/wordlists/big_all.txt"
dirsearch_db_big_all_ext="/usr/share/dirb/wordlists/big_all_ext.txt"

#-------    
import os
import sys
import time
import argparse
import requests
from random import randint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#-------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#-------
class pavelow:
    def __init__(self):
        self.sql = sqldir
        self.fi = fidir
        self.joom = joomdir
        self.com = comdir
        self.sub = subdir
        self.sho = sho
        self.nuclei = nuclei
        self.nuclei_templates = nuclei_templates
        self.nuclei_modules = nuclei_modules
        self.nuclei_plugins = nuclei_plugins
        self.httpx = httpx
        self.dirsearch = dirsearch
        self.dirsearch_db = dirsearch_db
        self.dirsearch_db_ext = dirsearch_db_ext
        self.dirsearch_db_big = dirsearch_db_big
        self.dirsearch_db_big_ext = dirsearch_db_big_ext
        self.dirsearch_db_big_all = dirsearch_db_big_all
        self.dirsearch_db_big_all_ext = dirsearch_db_big_all_ext
        self.jexboss = jexboss
        self.wpscan = wpscan
        self.host = ""
        self.help = ''
        self.banner = ''
        self.nmap = ''
        self.nmap_options = ''
        self.nmap_ports = ''
        self.nmap_output = ''
        self.nmap_output_file = ''
        self.nmap_output_dir = ''
        self.nmap_output_file_name = ''
        self.nmap_output_file_ext = ''
        self.nmap_output_file_path = ''
        self.sqlmap = ''
        self.sqlmap_options = ''
        self.sqlmap_output = ''
        self.sqlmap_output_file = ''
        self.sqlmap_output_dir = ''
        self.sqlmap_output_file_name = ''
        self.sqlmap_output_file_ext = ''
        self.sqlmap_output_file_path = ''
        self.fimap = ''
        self.fimap_options = ''
        self.fimap_output = ''
        self.fimap_output_file = ''
        self.fimap_output_dir = ''
        self.fimap_output_file_name = ''
        self.fimap_output_file_ext = ''
        self.fimap_output_file_path = ''
        self.joomscan = ''
        self.joomscan_options = ''
        self.joomscan_output = ''
        self.joomscan_output_file = ''
        self.joomscan_output_dir = ''
        self.joomscan_output_file_name = ''
        self.joomscan_output_file_ext = ''
        self.joomscan_output_file_path = ''
        self.commix = ''
        self.commix_options = ''
        self.commix_output = ''
        self.commix_output_file = ''
        self.commix_output_dir = ''
        self.commix_output_file_name = ''
        self.jexboss = ''
        self.jexboss_options = ''
        self.jexboss_output = ''
        self.jexboss_output_file = ''
        self.jexboss_output_dir = ''
        self.jexboss_output_file_name = ''
        self.jexboss_output_file_ext = ''
        self.jexboss_output_file_path = ''
        self.sublist3r = ''
        self.sublist3r_options = ''
        self.sublist3r_output = ''
        self.sublist3r_output_file = ''
        self.sublist3r_output_dir = ''
        self.sublist3r_output_file_name = ''
        self.sublist3r_output_file_ext = ''
        self.sublist3r_output_file_path = ''
        self.shodan = ''
        self.shodan_options = ''
        self.shodan_output = ''
        self.shodan_output_file = ''
        self.shodan_output_dir = ''
        self.shodan_output_file_name = ''
        self.shodan_output_file_ext = ''
        self.shodan_output_file_path = ''
        self.wpscan = ''
        self.wpscan_options = ''
        self.wpscan_output = ''
        self.wpscan_output_file = ''
        self.wpscan_output_dir = ''
        self.wpscan_output_file_name = ''
        self.wpscan_output_file_ext = ''
        self.wpscan_output_file_path = ''
        self.nuclei_threads = 30
        self.nuclei_verbosity = 1
        self.nuclei_engine = 'standard'
        self.nuclei_options = ''
        self.nuclei_output = ''
        self.nuclei_modules = 'all, web, database, network, system, exploit'
        self.nuclei_output_file = ''
        self.nuclei_output_dir = ''
        self.nuclei_output_file_name = ''
        self.nuclei_output_file_ext = ''
        self.nuclei_output_file_path = ''
        self.nuclei_templates = 'cves, fuzzing, default-logins, vulnerabilities, web_discovery_all'
        self.nuclei_modules = "discovery", "brute", "vuln", "creds", "enum", "gather", "report", "web"
        self.nuclei_
        self.httpx = ''
        self.httpx_options = ''
        self.httpx_output = ''
        self.httpx_output_file = ''
        self.httpx_output_dir = ''
        self.httpx_output_file_name = ''
        self.httpx_output_file_ext = ''
        self.httpx_output_file_path = ''
        self.dirsearch = ''
        self.dirsearch_options = ''
        self.dirsearch_output = ''
        self.dirsearch_output_file = ''
        self.dirsearch_output_dir = ''
        self.dirsearch_output_file_name = ''
        self.dirsearch_output_file_ext = ''
        self.dirsearch_output_file_path = ''
        self.dirsearch_db_big_ext = ''
        self.dirsearch_db_big_all = ''
        self.dirsearch_db_big_all_ext = ''
        self.dirsearch_db_small_ext = ''
        self.dirsearch_db_small_all = ''
        self.dirsearch_db_small_all_ext = ''
        
    
    def nmap(self, host):
        self.nmap = "nmap"
        self.nmap_options = "-sV -sC -sS -sU -p- -oX"
        self.nmap_output_file_name = "nmap_" + host
        self.nmap_output_file_ext = "xml"
        self.nmap_output_file_path = self.nmap_output_dir + self.nmap_output_file_name + "." + self.nmap_output_file_ext
        self.nmap_output = self.nmap + " " + self.nmap_options + " " + self.nmap_ports + " " + host + " > " + self.nmap_output_file_path
        print(bcolors.OKGREEN + self.nmap_output + bcolors.ENDC)
        os.system(self.nmap_output)
        print(bcolors.OKGREEN + "Nmap output saved to: " + self.nmap_output_file_path + bcolors.ENDC)
    
    def sqlmap(self, host):
        self.sqlmap = "sqlmap"
        self.sqlmap_options = "-u" + host + " --batch --random-agent --threads 10 --risk 2 --level 3 --timeout 10 --smart --dbs --tables --columns --dump --dbms --techniques --banner --stats-only --save-session " + self.sqlmap_output_file_path
        self.sqlmap_output_file_name = "sqlmap_" + host
        self.sqlmap_output_file_ext = "txt"
        self.sqlmap_output_file_path = self.sqlmap_output_dir + self.sqlmap_output_file_name + "." + self.sqlmap_output_file_ext
        self.sqlmap_output = self.sqlmap + " " + self.sqlmap_options + " > " + self.sqlmap_output_file_path
        print(bcolors.OKGREEN + self.sqlmap_output + bcolors.ENDC)
        os.system(self.sqlmap_output)

    def fimap(self, host):
        self.fimap = "fimap"
        self.fimap_options = "-u" + host + " -o" + self.fimap_output_file_path
        self.fimap_output_file_name = "fimap_" + host
        self.fimap_output_file_ext = "txt"
        self.fimap_output_file_path = self.fimap_output_dir + self.fimap_output_file_name + "." + self.fimap_output_file_ext
        self.fimap_output = self.fimap + " " + self.fimap_options + " > " + self.fimap_output_file_path
        print(bcolors.OKGREEN + self.fimap_output + bcolors.ENDC)
        os.system(self.fimap_output)

    def joomscan(self, host):
        self.joomscan = "joomscan"
        self.joomscan_options = "-u" + host + " -o" + self.joomscan_output_file_path
        self.joomscan_output_file_name = "joomscan_" + host
        self.joomscan_output_file_ext = "txt"
        self.joomscan_output_file_path = self.joomscan_output_dir + self.joomscan_output_file_name + "." + self.joomscan_output_file_ext
        self.joomscan_output = self.joomscan + " " + self.joomscan_options + " > " + self.joomscan_output_file_path
        print(bcolors.OKGREEN + self.joomscan_output + bcolors.ENDC)
        os.system(self.joomscan_output)
    
    def commix(self, host):
        self.commix = "commix"
        self.commix_options = "-u" + host + " --dbs --tables --columns --dump --dbms --techniques --banner --stats-only --save-session " + self.commix_output_file_path
        self.commix_output_file_name = "commix_" + host
        self.commix_output_file_ext = "txt"
        self.commix_output_file_path = self.commix_output_dir + self.commix_output_file_name + "." + self.commix_output_file_ext
        self.commix_output = self.commix + " " + self.commix_options + " > " + self.commix_output_file_path
        print(bcolors.OKGREEN + self.commix_output + bcolors.ENDC)
        os.system(self.commix_output)

    def sublist3r(self, host):
        self.sublist3r = "sublist3r"
        self.sublist3r_options = "-d" + host + " -o" + self.sublist3r_output_file_path
        self.sublist3r_output_file_name = "sublist3r_" + host
        self.sublist3r_output_file_ext = "txt"
        self.sublist3r_output_file_path = self.sublist3r_output_dir + self.sublist3r_output_file_name + "." + self.sublist3r_output_file_ext
        self.sublist3r_output = self.sublist3r + " " + self.sublist3r_options + " > " + self.sublist3r_output_file_path
        print(bcolors.OKGREEN + self.sublist3r_output + bcolors.ENDC)
        os.system(self.sublist3r_output)
    
    def wpscan(self, host):
        self.wpscan = "wpscan"
        self.wpscan_options = "-u" + host + " --batch --disable-tls-checks --disable-colors --no-banner --no-update --random-agent --threads 10 --timeout 10 --wordlist " + self.wpscan_output_file_path
        self.wpscan_output_file_name = "wpscan_" + host
        self.wpscan_output_file_ext = "txt"
        self.wpscan_output_file_path = self.wpscan_output_dir + self.wpscan_output_file_name + "." + self.wpscan_output_file_ext
        self.wpscan_output = self.wpscan + " " + self.wpscan_options + " > " + self.wpscan_output_file_path
        print(bcolors.OKGREEN + self.wpscan_output + bcolors.ENDC)
        os.system(self.wpscan_output)
    
    def dirsearch(self, host):
        self.dirsearch = "dirsearch"
        self.dirsearch_options = "-u" + host + " -w " + self.dirsearch_wordlist + " -x " + self.dirsearch_exclude_dirs + " -t " + self.dirsearch_threads + " -e " + self.dirsearch_extensions + " -o " + self.dirsearch_output_file_path
        self.dirsearch_output_file_name = "dirsearch_" + host
        self.dirsearch_output_file_ext = "txt"
        self.dirsearch_output_file_path = self.dirsearch_output_dir + self.dirsearch_output_file_name + "." + self.dirsearch_output_file_ext
        self.dirsearch_output = self.dirsearch + " " + self.dirsearch_options + " > " + self.dirsearch_output_file_path
        print(bcolors.OKGREEN + self.dirsearch_output + bcolors.ENDC)
        os.system(self.dirsearch_output)

    def dirb(self, host):
        self.dirb = "dirb"
        self.dirb_options = "-u" + host + " -w " + self.dirb_wordlist + " -r " + self.dirb_recursive + " -o " + self.dirb_output_file_path
        self.dirb_output_file_name = "dirb_" + host
        self.dirb_output_file_ext = "txt"
        self.dirb_output_file_path = self.dirb_output_dir + self.dirb_output_file_name + "." + self.dirb_output_file_ext
        self.dirb_output = self.dirb + " " + self.dirb_options + " > " + self.dirb_output_file_path
        print(bcolors.OKGREEN + self.dirb_output + bcolors.ENDC)
        os.system(self.dirb_output)

    def httpx(self, host):
        self.httpx = "httpx"
        self.httpx_options = "-u" + host + " -o " + self.httpx_output_file_path
        self.httpx_output_file_name = "httpx_" + host
        self.httpx_output_file_ext = "txt"
        self.httpx_output_file_path = self.httpx_output_dir + self.httpx_output_file_name + "." + self.httpx_output_file_ext
        self.httpx_output = self.httpx + " " + self.httpx_options + " > " + self.httpx_output_file_path
        print(bcolors.OKGREEN + self.httpx_output + bcolors.ENDC)
        os.system(self.httpx_output)

    def gobuster(self, host):
        self.gobuster = "gobuster"
        self.gobuster_options = "-u" + host + " -w " + self.gobuster_wordlist + " -e " + self.gobuster_extensions + " -t " + self.gobuster_threads + " -o " + self.gobuster_output_file_path
        self.gobuster_output_file_name = "gobuster_" + host
        self.gobuster_output_file_ext = "txt"
        self.gobuster_output_file_path = self.gobuster_output_dir + self.gobuster_output_file_name + "." + self.gobuster_output_file_ext
        self.gobuster_output = self.gobuster + " " + self.gobuster_options + " > " + self.gobuster_output_file_path
        print(bcolors.OKGREEN + self.gobuster_output + bcolors.ENDC)
        os.system(self.gobuster_output)
    
    def theHarvester(self, host):
        self.theHarvester = "theHarvester"
        self.theHarvester_options = "-d " + host + " -b google -l 100 -s " + self.theHarvester_output_file_path
        self.theHarvester_output_file_name = "theHarvester_" + host
        self.theHarvester_output_file_ext = "txt"
        self.theHarvester_output_file_path = self.theHarvester_output_dir + self.theHarvester_output_file_name + "." + self.theHarvester_output_file_ext
        self.theHarvester_output = self.theHarvester + " " + self.theHarvester_options + " > " + self.theHarvester_output_file_path
        print(bcolors.OKGREEN + self.theHarvester_output + bcolors.ENDC)
        os.system(self.theHarvester_output)

    def whatweb(self, host):
        self.whatweb = "whatweb"
        self.whatweb_options = "-v -a 3 " + host + " -o " + self.whatweb_output_file_path
        self.whatweb_output_file_name = "whatweb_" + host
        self.whatweb_output_file_ext = "txt"
        self.whatweb_output_file_path = self.whatweb_output_dir + self.whatweb_output_file_name + "." + self.whatweb_output_file_ext
        self.whatweb_output = self.whatweb + " " + self.whatweb_options + " > " + self.whatweb_output_file_path
        print(bcolors.OKGREEN + self.whatweb_output + bcolors.ENDC)
        os.system(self.whatweb_output)
    
    def amass(self, host):
        self.amass = "amass"
        self.amass_options = "-d " + host + " -o " + self.amass_output_file_path
        self.amass_output_file_name = "amass_" + host
        self.amass_output_file_ext = "txt"
        self.amass_output_file_path = self.amass_output_dir + self.amass_output_file_name + "." + self.amass_output_file_ext
        self.amass_output = self.amass + " " + self.amass_options + " > " + self.amass_output_file_path
        print(bcolors.OKGREEN + self.amass_output + bcolors.ENDC)
        os.system(self.amass_output)
    
    def subfinder(self, host):
        self.subfinder = "subfinder"
        self.subfinder_options = "-d " + host + " -o " + self.subfinder_output_file_path
        self.subfinder_output_file_name = "subfinder_" + host
        self.subfinder_output_file_ext = "txt"
        self.subfinder_output_file_path = self.subfinder_output_dir + self.subfinder_output_file_name + "." + self.subfinder_output_file_ext
        self.subfinder_output = self.subfinder + " " + self.subfinder_options + " > " + self.subfinder_output_file_path
        print(bcolors.OKGREEN + self.subfinder_output + bcolors.ENDC)
        os.system(self.subfinder_output)

    def sublist3r(self, host):
        self.sublist3r = "sublist3r"
        self.sublist3r_options = "-d " + host + " -o " + self.sublist3r_output_file_path
        self.sublist3r_output_file_name = "sublist3r_" + host
        self.sublist3r_output_file_ext = "txt"
        self.sublist3r_output_file_path = self.sublist3r_output_dir + self.sublist3r_output_file_name + "." + self.sublist3r_output_file_ext
        self.sublist3r_output = self.sublist3r + " " + self.sublist3r_options + " > " + self.sublist3r_output_file_path
        print(bcolors.OKGREEN + self.sublist3r_output + bcolors.ENDC)
        os.system(self.sublist3r_output)

    def nikto(self, host):
        self.nikto = "nikto"
        self.nikto_options = "-h " + host + " -output " + self.nikto_output_file_path
        self.nikto_output_file_name = "nikto_" + host
        self.nikto_output_file_ext = "txt"
        self.nikto_output_file_path = self.nikto_output_dir + self.nikto_output_file_name + "." + self.nikto_output_file_ext
        self.nikto_output = self.nikto + " " + self.nikto_options + " > " + self.nikto_output_file_path
        print(bcolors.OKGREEN + self.nikto_output + bcolors.ENDC)
        os.system(self.nikto_output)


    def dnsrecon(self, host):
        self.dnsrecon = "dnsrecon"
        self.dnsrecon_options = "-d " + host + " -o " + self.dnsrecon_output_file_path
        self.dnsrecon_output_file_name = "dnsrecon_" + host
        self.dnsrecon_output_file_ext = "txt"
        self.dnsrecon_output_file_path = self.dnsrecon_output_dir + self.dnsrecon_output_file_name + "." + self.dnsrecon_output_file_ext
        self.dnsrecon_output = self.dnsrecon + " " + self.dnsrecon_options + " > " + self.dnsrecon_output_file_path
        print(bcolors.OKGREEN + self.dnsrecon_output + bcolors.ENDC)
        os.system(self.dnsrecon_output)


    def nuclei(self, host):
        self.nuclei = "nuclei"
        self.__module__ = "nuclei"
        self.nuclei_options = "-u " + host + " -o " + self.nuclei_output_file_path + " -m " + self.nuclei_modules + " -t " + self.nuclei_threads + " -e " + self.nuclei_engine  + " -v " + self.nuclei_verbose
        self.nuclei_output_file_name = "nuclei_" + host
        self.nuclei_output_file_ext = "txt"
        self.nuclei_output_file_path = self.nuclei_output_dir + self.nuclei_output_file_name + "." + self.nuclei_output_file_ext
        self.nuclei_output = self.nuclei + " " + self.nuclei_options + " > " + self.nuclei_output_file_path
        print(bcolors.OKGREEN + self.nuclei_output + bcolors.ENDC)
        os.system(self.nuclei_output)