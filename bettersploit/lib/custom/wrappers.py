#GO GO IMPORTATIONS!
import os
import sys
import time
import random
import string
import subprocess
from subprocess import Popen, PIPE

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
xsstrike="/usr/share/xsstrike"
httpx="/usr/share/httpx"
dirsearch="/usr/share/dirb"
dirsearch_db="/usr/share/dirb/wordlists/common.txt"
dirsearch_db_ext="/usr/share/dirb/wordlists/common_ext.txt"
dirsearch_db_big="/usr/share/dirb/wordlists/big.txt"
dirsearch_db_big_ext="/usr/share/dirb/wordlists/big_ext.txt"
dirsearch_db_big_all="/usr/share/dirb/wordlists/big_all.txt"
dirsearch_db_big_all_ext="/usr/share/dirb/wordlists/big_all_ext.txt"
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
        self.waybackurls = "waybackurls"
        self.whatweb = "whatweb"
        self.wpscan = wpscan
        self.amass = "amass"
        self.zaproxy = "zaproxy"
        self.jexboss = jexboss
        self.dirsearch = dirsearch
        self.shodan = sho
        self.dirb = "dirb"
        self.commix = "commix"
        self.nmap = "nmap"
        self.nuclei = "nuclei"
        self.assetfinder = "assetfinder"
        self.dnsrecon = "dnsrecon"
        self.subfinder = "subfinder"
        self.sublist3r = "sublist3r"
        self.joomscan = "joomscan"
        self.nikto = "nikto"
    
        self.nuclei_templates = nuclei_templates
        self.nuclei_modules = nuclei_modules
        self.nuclei_plugins = nuclei_plugins
        self.dirsearch = dirsearch
        self.dirsearch_db = dirsearch_db
        self.dirsearch_db_ext = dirsearch_db_ext
        self.dirsearch_db_big = dirsearch_db_big
        self.dirsearch_db_big_ext = dirsearch_db_big_ext
        self.dirsearch_db_big_all = dirsearch_db_big_all
        self.dirsearch_db_big_all_ext = dirsearch_db_big_all_ext
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

    def dirsearch_db_big(self):
        self.dirsearch_db_big_ext = self.dirsearch_db_big_ext + '\n' + self.dirsearch_db_big_ext_default
        self.dirsearch_db_big_all = self.dirsearch_db_big_all + '\n' + self.dirsearch_db_big_all_default
        self.dirsearch_db_big_all_ext = self.dirsearch_db_big_all_ext + '\n' + self.dirsearch_db_big_all_ext_default
        self.dirsearch_db_small_ext = self.dirsearch_db_small_ext + '\n' + self.dirsearch_db_small_ext_default
        self.dirsearch_db_small_all = self.dirsearch_db_small_all + '\n' + self.dirsearch_db_small_all_default
        self.dirsearch_db_small_all_ext = self.dirsearch_db_small_all_ext + '\n' + self.dirsearch_db_small_all_ext_default

    def dirsearch_db_small(self):
        self.dirsearch_db_big_ext = self.dirsearch_db_big_ext + '\n' + self.dirsearch_db_small_ext_default
        self.dirsearch_db_big_all = self.dirsearch_db_big_all + '\n' + self.dirsearch_db_small_all_default
        self.dirsearch_db_big_all_ext = self.dirsearch_db_big_all_ext + '\n' + self.dirsearch_db_small_all_ext_default
        self.dirsearch_db_small_ext = self.dirsearch_db_small_ext + '\n' + self.dirsearch_db_small_ext_default
        self.dirsearch_db_small_all = self.dirsearch_db_small_all + '\n' + self.dirsearch_db_small_all_default
        self.dirsearch_db_small_all_ext = self.dirsearch_db_small_all_ext + '\n' + self.dirsearch_db_small_all_ext_default
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def host_set(self, host):
        self.host = host
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            print("[+] Host is set to: " + self.host)
    
    def set_url(self, url):
        self.url = url
        if self.url == "":
            print("[!] URL is empty")
            sys.exit()
        else:
            print("[+] URL is set to: " + self.url)
#======================
#Wrappers:
#======================

    def sqlmap(self, host):
        self.host_set(host)
        self.sqlmap_options = '-u ' + self.url + ' --batch --random-agent --threads 10 --level 3 --risk 3 --timeout 10 --smart --dbs --tamper=url --dbs --dbms=mysql --dbms=mssql --dbms=oracle --dbms=postgres --dbms=sqlite --dbms=sqlserver --dbs --tables --columns --forms --dump --dbs --sql-query --tor --tor-type=socks5 --tor-port=9050 --tor-control-port=9051 --tor-control-addr=
        self.sqlmap_output = subprocess.check_output(self.sqlmap_options, shell=False)

    def fimap(self, host):
        self.host_set(host)
        self.fimap_options = '-u ' + self.url + ' -t 10 -m 10 -o ' + self.host + '_fimap.txt'
        self.fimap_output = subprocess.check_output(self.fimap_options, shell=False)

    def joomscan(self, host):
        self.host_set(host)
        self.joomscan_options = '-u ' + self.url + ' -t 10 -m 10 -o ' + self.host + '_joomscan.txt'
        self.joomscan_output = subprocess.check_output(self.joomscan_options, shell=False)
    
    def jexboss(self, host):
        self.host_set(host)
        self.jexboss_options = '-u ' + self.url + ' -t 10 -m 10 -o ' + self.host + '_jexboss.txt'
        self.jexboss_output = subprocess.check_output(self.jexboss_options, shell=False)

    def sublist3r(self, host):
        self.host_set(host)
        self.sublist3r_options = '-d ' + self.host + ' -o ' + self.host + '_sublist3r.txt'
        self.sublist3r_output = subprocess.check_output(self.sublist3r_options, shell=False)

    def nuclei(self, host):
        self.host_set(host)
        self.nuclei_options = '-t ' + self.nuclei_threads + ' -v ' + self.nuclei_verbosity + ' -e ' + self.nuclei_engine + ' -m ' + self.nuclei_modules + ' -o ' + self.host + '_nuclei.txt'
        self.nuclei_output = subprocess.check_output(self.nuclei_options, shell=False)
    
    def wpscan(self, host):
        self.host_set(host)
        self.wpscan_options = '-u ' + self.url + ' --batch --disable-tls-checks --disable-tls-fingerprint --disable-color --log ' + self.host + '_wpscan.txt'
        self.wpscan_output = subprocess.check_output(self.wpscan_options, shell=False)

    def dirsearch(self, host):
        self.host_set(host)
        self.dirsearch_options = '-u ' + self.url + ' -w ' + self.dirsearch_db_big_ext + ' -x ' + self.dirsearch_db_big_all + ' -x ' + self.dirsearch_db_big_all_ext + ' -x ' + self.dirsearch_db_small_ext + ' -x ' + self.dirsearch_db_small_all + ' -x ' + self.dirsearch_db_small_all_ext + ' -o ' + self.host + '_dirsearch.txt'
        self.dirsearch_output = subprocess.check_output(self.dirsearch_options, shell=False)
    
    def httpx(self, host):
        self.host_set(host)
        self.httpx_options = '-u ' + self.url + ' -o ' + self.host + '_httpx.txt'
        self.httpx_output = subprocess.check_output(self.httpx_options, shell=False)
    
    def dirb(self, host):
        self.host_set(host)
        self.dirb_options = '-u ' + self.url + ' -w ' + self.dirb_db_big_ext + ' -w ' + self.dirb_db_big_all + ' -w ' + self.dirb_db_big_all_ext + ' -w ' + self.dirb_db_small_ext + ' -w ' + self.dirb_db_small_all + ' -w ' + self.dirb_db_small_all_ext + ' -o ' + self.host + '_dirb.txt'
        self.dirb_output = subprocess.check_output(self.dirb_options, shell=False)

    def gobuster(self, host):
        self.host_set(host)
        self.gobuster_options = '-u ' + self.url + ' -w ' + self.gobuster_db_big_ext + ' -w ' + self.gobuster_db_big_all + ' -w ' + self.gobuster_db_big_all_ext + ' -w ' + self.gobuster_db_small_ext + ' -w ' + self.gobuster_db_small_all + ' -w ' + self.gobuster_db_small_all_ext + ' -o ' + self.host + '_gobuster.txt'
        self.gobuster_output = subprocess.check_output(self.gobuster_options, shell=False)

    def whatweb(self, host):
        self.host_set(host)
        self.whatweb_options = '-v -a 3 -t 100 -k -o ' + self.host + '_whatweb.txt ' + self.host
        self.whatweb_output = subprocess.check_output(self.whatweb_options, shell=False)

    def assetfinder(self, host):
        self.host_set(host)
        self.assetfinder_options = '-subs-only -subs-url ' + self.url + ' -subs-list ' + self.assetfinder_db_big_ext + ' -subs-list ' + self.assetfinder_db_big_all + ' -subs-list ' + self.assetfinder_db_big_all_ext + ' -subs-list ' + self.assetfinder_db_small_ext + ' -subs-list ' + self.assetfinder_db_small_all + ' -subs-list ' + self.assetfinder_db_small_all_ext + ' -o ' + self.host + '_assetfinder.txt'
        self.assetfinder_output = subprocess.check_output(self.assetfinder_options, shell=False)
    
    def subfinder(self, host):
        self.host_set(host)
        self.subfinder_options = '-d ' + self.host + ' -o ' + self.host + '_subfinder.txt'
        self.subfinder_output = subprocess.check_output(self.subfinder_options, shell=False)
    
    def waybackurls(self, host):
        self.host_set(host)
        self.waybackurls_options = '-d ' + self.host + ' -o ' + self.host + '_waybackurls.txt'
        self.waybackurls_output = subprocess.check_output(self.waybackurls_options, shell=False)
    
    def theharvester(self, host):
        self.host_set(host)
        self.theharvester_options = '-d ' + self.host + ' -l 100 -b all -f ' + self.host + '_theharvester.txt'
        self.theharvester_output = subprocess.check_output(self.theharvester_options, shell=False)

    def amass(self, host):
        self.host_set(host)
        self.amass_options = 'enum -d ' + self.host + ' -o ' + self.host + '_amass.txt'
        self.amass_output = subprocess.check_output(self.amass_options, shell=False)

    def sublist3r(self, host):
        self.host_set(host)
        self.sublist3r_options = '-d ' + self.host + ' -o ' + self.host + '_sublist3r.txt'
        self.sublist3r_output = subprocess.check_output(self.sublist3r_options, shell=False)

    
        