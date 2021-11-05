#GO GO IMPORTATIONS!
import os
import sys
import time
import random
import string
import subprocess
from subprocess import Popen, PIPE
import pandas as pd

#default locations
sqldir="/usr/share/sqlmap"
fidir="/usr/share/fimap"
joomdir="/usr/share/joomscan"
comdir="/usr/share/commix"
subdir="/usr/share/sublist3r"
sho="/usr/local/bin/shodan"
jexboss="/usr/share/jexboss"
cmsmap = "/usr/share/cmsmap"
nuclei="/usr/share/nuclei"
nuclei_templates="/usr/share/nuclei/templates"
nuclei_modules="/usr/share/nuclei/modules"
xsstrike="/usr/share/xsstrike"
httpx="/usr/share/httpx"
dirsearch="/usr/share/dirb"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Wrappers:
    def __init__(self):
        self.sqlmap="sqlmap"
        self.fimap="fimap"
        self.gobuster="gobuster"
        self.httpx="httpx"
        self.subjack = "subjack"
        self.waybackhosts = "waybackhosts"
        self.whatweb = "whatweb"
        self.wpscan = wpscan
        self.amass = "amass"
        self.zaproxy = "zaproxy"
        self.jexboss = jexboss
        self.dirsearch = dirsearch
        self.shodan = sho
        self.dirb = "dirb"
        self.dirb_big = "dirb_big"
        self.dirb_small = "dirb_small"
        self.dirb_common = "dirb_common"
        self.cmsmap = "cmsmap"
        self.commix = "commix"
        self.nmap = "nmap"
        self.nuclei = "nuclei"
        self.assetfinder = "assetfinder"
        self.dnsrecon = "dnsrecon"
        self.subfinder = "subfinder"
        self.sublist3r = "sublist3r"
        self.joomscan = "joomscan"
        self.nikto = "nikto"
        self.httprobe = "httprobe"
        self.httprobe_headers = "httprobe -H"
        self.httprobe_all = "httprobe -a"
        self.httprobe_all_headers = "httprobe -a -H"
        self.dnsrecon_domains = "dnsrecon -d"
        self.dnsrecon_subs = "dnsrecon -s"
        self.dnsrecon_brute = "dnsrecon -b"
        self.dnsrecon_all = "dnsrecon -a"
        self.dnsrecon_all_brute = "dnsrecon -a -b"
        self.dnsrecon_all_subs = "dnsrecon -a -s"

        self.metasploit = metasploit
        self.msfconsole = "msfconsole"
        self.msfvenom = "msfvenom"
        self.msfpg = "msfpg"
        self.msfpg_list = "msfpg -l"
        self.msfpg_list_all = "msfpg -l -a"


    
        self.nuclei_templates = nuclei_templates
        self.nuclei_modules = nuclei_modules
        self.nuclei_plugins = nuclei_plugins
        self.dirsearch = dirsearch
        self.host = ""
        self.nmap_options = ''
        self.nmap_ports = ''
        self.nmap_output = ''
        self.nmap_output_file = ''
        self.nmap_output_dir = ''
        self.nmap_output_file_name = ''
        self.nmap_output_file_ext = ''
        self.nmap_output_file_path = ''

        self.sqlmap_options = ''
        self.sqlmap_output = ''
        self.sqlmap_output_file = ''
        self.sqlmap_output_dir = ''
        self.sqlmap_output_file_name = ''
        self.sqlmap_output_file_ext = ''
        self.sqlmap_output_file_path = ''
        self.fimap_options = ''
        self.fimap_output = ''
        self.fimap_output_file = ''
        self.fimap_output_dir = ''
        self.fimap_output_file_name = ''
        self.fimap_output_file_ext = ''
        self.fimap_output_file_path = ''
        self.joomscan_options = ''
        self.joomscan_output = ''
        self.joomscan_output_file = ''
        self.joomscan_output_dir = ''
        self.joomscan_output_file_name = ''
        self.joomscan_output_file_ext = ''
        self.joomscan_output_file_path = ''

        self.commix_options = ''
        self.commix_output = ''
        self.commix_output_file = ''
        self.commix_output_dir = ''
        self.commix_output_file_name = ''
        self.jexboss_options = ''
        self.jexboss_output = ''
        self.jexboss_output_file = ''
        self.jexboss_output_dir = ''
        self.jexboss_output_file_name = ''
        self.jexboss_output_file_ext = ''
        self.jexboss_output_file_path = ''

        self.sublist3r_options = ''
        self.sublist3r_output = ''
        self.sublist3r_output_file = ''
        self.sublist3r_output_dir = ''
        self.sublist3r_output_file_name = ''
        self.sublist3r_output_file_ext = ''
        self.sublist3r_output_file_path = ''

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

        self.httpx_options = ''
        self.httpx_output = ''
        self.httpx_output_file = ''
        self.httpx_output_dir = ''
        self.httpx_output_file_name = ''
        self.httpx_output_file_ext = ''
        self.httpx_output_file_path =  ''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def host_set(self, host):
        self.host = host
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            print("[+] Host is set to: " + self.host)
    
    def set_host(self, host):
        self.host = host
        if self.host == "":
            print("[!] host is empty")
            sys.exit()
        else:
            print("[+] host is set to: " + self.host)

    def load_dirb_lists(self, list_type=None):
        if list_type == None:
            print("[!] No list type specified")
            sys.exit()
        else:
            switch = {
                self.dirb_big: "https://raw.githubusercontent.com/v0re/dirb/master/wordlists/big.txt",
                self.dirb_small: "https://raw.githubusercontent.com/v0re/dirb/master/wordlists/small.txt",
                self.dirb_common: "https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt",

            }
            self.dirb_lists = switch.get(list_type)
            if self.dirb_lists == "dirb_big":
                pd.read_csv(self.dirb_big,header=None,encoding = "ISO-8859-1")[0].to_list()
            elif self.dirb_lists == "dirb_small":
                pd.read_csv(self.dirb_small,header=None,encoding = "ISO-8859-1")[0].to_list()
            elif self.dirb_lists == "dirb_common":
                pd.read_csv(self.dirb_common,header=None,encoding = "ISO-8859-1")[0].to_list()
            else:
                print("[!] No list type specified")
                sys.exit()
            print("[+] Loaded " + self.dirb_lists)
#======================
#Wrappers:
#======================

    def sqlmap(self, host):
        self.host_set(host)
        self.sqlmap_options = '-u ' + self.host + " --batch --random-agent --threads 10 --level 3 --risk 3 --timeout 10 --smart --dbs --tamper=host --dbs --dbms=mysql --dbms=mssql --dbms=oracle --dbms=postgres --dbms=sqlite --dbms=sqlserver --dbs --tables --columns --forms --dump --dbs --sql-query --tor --tor-type=socks5 --tor-port=9050 --tor-control-port=9051"
        self.sqlmap_output = subprocess.Popen(['sqlmap', self.sqlmap_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def fimap(self, host):
        self.host_set(host)
        self.fimap_options = '-u ' + self.host + ' -t 10 -m 10 -o ' + self.host + '_fimap.txt'
        self.fimap_output = subprocess.Popen(['fimap', self.fimap_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         

    def joomscan(self, host):
        self.host_set(host)
        self.joomscan_options = '-u ' + self.host + ' -t 10 -m 10 -o ' + self.host + '_joomscan.txt'
        self.joomscan_output = subprocess.Popen(['joomscan', self.joomscan_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def jexboss(self, host):
        self.host_set(host)
        self.jexboss_options = '-u ' + self.host + ' -t 10 -m 10 -o ' + self.host + '_jexboss.txt'
        self.jexboss_output = subprocess.Popen(['jexboss', self.jexboss_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def sublist3r(self, host):
        self.host_set(host)
        self.sublist3r_options = '-d ' + self.host + ' -o ' + self.host + '_sublist3r.txt'
        self.sublist3r_output = subprocess.Popen(['sublist3r', self.sublist3r_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def nuclei(self, host):
        self.host_set(host)
        self.nuclei_options = '-t ' + self.nuclei_threads + ' -v ' + self.nuclei_verbosity + ' -m ' + self.nuclei_modules + ' -o ' + self.host + '_nuclei.txt'
        self.nuclei_output = subprocess.Popen(['nuclei', self.nuclei_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def cmsmap(self, host):
        self.host_set(host)
        self.cmsmap_options = self.host + ' -F -o ' + self.host + '_cmsmap.txt'
        self.cmsmap_output = subprocess.Popen(['cmsmap', self.cmsmap_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  

    def dirsearch(self, host):
        self.host_set(host)
        self.dirsearch_options = '-u ' + self.host + ' -w ' + self.dirb_common
        self.dirsearch_output = subprocess.Popen(['dirsearch', self.dirsearch_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def httpx(self, host):
        self.host_set(host)
        self.httpx_options = '-u ' + self.host + ' -o ' + self.host + '_httpx.txt'
        self.httpx_output = subprocess.Popen(['httpx', self.httpx_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def dirb(self, host, type='big'):
        self.host_set(host)
        switch = {
            'big': self.dirb_big,
            'small': self.dirb_small,
            'common': self.dirb_common
        }
        self.dirb_options = self.host + ' -w ' + switch.get(type) + ' -o ' + self.host + '_dirb.txt'
        self.dirb_output = subprocess.Popen(['dirb', self.dirb_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


        if type == 'big':
            self.dirb_options = self.host + ' -w ' + self.dirb_db_big + ' -o ' + self.host + '_dirb_big.txt'
        elif type == 'small':
            self.dirb_options = self.host + ' -w ' + self.dirb_db_small + ' -o ' + self.host + '_dirb_small.txt'
        self.dirb_output = subprocess.Popen(['dirb', self.dirb_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def gobuster(self, host):
        self.host_set(host)
        self.gobuster_options = '-e -u ' + self.host + ' -w ' + self.dib_common
        self.gobuster_output = subprocess.Popen(['gobuster', self.gobuster_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def whatweb(self, host):
        self.host_set(host)
        self.whatweb_options = '-v -a 3 -t 100 -k -o ' + self.host + '_whatweb.txt ' + self.host
        self.whatweb_output = subprocess.Popen(['whatweb', self.whatweb_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def assetfinder(self, host):
        self.host_set(host)
        self.assetfinder_options = '-subs-only -subs-host ' + self.host + ' -subs-list ' + self.assetfinder_db_big_ext + ' -subs-list ' + self.assetfinder_db_big_all + ' -subs-list ' + self.assetfinder_db_big_all_ext + ' -subs-list ' + self.assetfinder_db_small_ext + ' -subs-list ' + self.assetfinder_db_small_all + ' -subs-list ' + self.assetfinder_db_small_all_ext + ' -o ' + self.host + '_assetfinder.txt'
        self.assetfinder_output = subprocess.Popen(['assetfinder', self.assetfinder_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def subfinder(self, host):
        self.host_set(host)
        self.subfinder_options = '-d ' + self.host + ' -o ' + self.host + '_subfinder.txt'
        self.subfinder_output = subprocess.Popen(['subfinder', self.subfinder_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    
    def theharvester(self, host):
        self.host_set(host)
        self.theharvester_options = '-d ' + self.host + ' -l 100 -b all -f ' + self.host + '_theharvester.txt'
        self.theharvester_output = subprocess.Popen(['theharvester', self.theharvester_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def amass(self, host):
        self.host_set(host)
        self.amass_options = 'enum -d ' + self.host + ' -o ' + self.host + '_amass.txt'
        self.amass_output = subprocess.Popen(['amass', self.amass_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def sublist3r(self, host):
        self.host_set(host)
        self.sublist3r_options = '-d ' + self.host + ' -o ' + self.host + '_sublist3r.txt'
        self.sublist3r_output = subprocess.Popen(['sublist3r', self.sublist3r_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def dnsrecon(self, host):
        self.host_set(host)
        self.dnsrecon_options = '-d ' + self.host
        self.dnsrecon_output = subprocess.Popen(['dnsrecon', self.dnsrecon_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def nikto(self, host):
        self.host_set(host)
        self.nikto_options = '-host ' + self.host + ' -Format htm -output ' + self.host + '_nikto.txt'
        self.nikto_output = subprocess.Popen(['nikto', self.nikto_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def nmap(self, host):
        self.host_set(host)
        self.nmap_options = '-sV -Pn -p-' + self.host
        self.nmap_output = subprocess.Popen(['nmap', self.nmap_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def httprobe(self, host):
        self.host_set(host)
        self.httprobe_options = '-c -t 100 -p ' + self.host + '_httprobe.txt ' + self.host
        self.httprobe_output = subprocess.Popen(['httprobe', self.httprobe_options], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#================
    
#OVERKILL XD

    def recon_all(self, host):
        self.httprobe(host)
        self.nmap(host)
        self.sublist3r(host)
        self.dnsrecon(host)
        self.amass(host)
        self.theharvester(host)
        self.waybackhosts(host)
        self.subfinder(host)
        self.nuclei(host)
        self.nikto(host)
        self.amass(host)
        self.fimap(host)
        self.sqlmap(host)
        self.dirb(host)
#-------------------------
