#-------    
import os
import sys
import time
import requests
import nmap3 as nmap

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
class nmapper:
    def __init__(self):
        self.host = ""
        self.nmap_options = ''
        self.nmap_ports = ''
        self.nmap_output = ''
        self.nmap_output_file = ''
        self.nmap_output_dir = ''
        self.nmap_output_file_name = ''
        self.nmap_output_file_ext = ''
        self.nmap_output_file_path = ''
        self.nmap_output_file_path_name = ''
        
    #
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
    

    
    def search_nmap(self, nse_module):
            if self.find_nmap:
                for root, dirs, files in os.walk(self.nmap_dir):
                    for x in files:
                        if x.endswith(".nse"):
                            if x.contains(nse_module):
                                self.nse_modules.append(x)
                if len(self.nse_modules) == 0:
                    print(bcolors.FAIL + "No NSE modules found" + bcolors.ENDC)
                else:
                    for x in self.nse_modules:
                        nse_module.append(x)
                    for x in self.nse_modules:
                        self.nse_module = x


    def quick_scan(self, host):
        self.host = host
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host)
    
    def full_scan(self, host):
        self.host = host
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args="-sS -sV -sC -O")
    

    def nmap_scan(self, host, nmap_script):
        self.host = host
        self.nmap_script = nmap_script
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args=f"--script={self.search_nmap(nmap_script)}")
    
    
    def nmap_scan_top_ports(self, host, top_ports):
        self.host = host
        self.top_ports = top_ports
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args=f"-p {self.top_ports}")

    def nmap_scan_top_ports_all(self, host, top_ports):
        self.host = host
        self.top_ports = top_ports
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args=f"-p {self.top_ports} -sS -sV -sC -O")

    def nmap_scan_top_ports_script(self, host, top_ports, nmap_script):
        self.host = host
        self.top_ports = top_ports
        self.nmap_script = nmap_script
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args=f"-p {self.top_ports} --script={self.search_nmap(nmap_script)}")

    def nmap_scan_top_ports_script_all(self, host, top_ports, nmap_script):
        self.host = host
        self.top_ports = top_ports
        self.nmap_script = nmap_script
        if self.host == "":
            print("[!] Host is empty")
            sys.exit()
        else:
            return nmap.scan_top_ports(self.host, args=f"-p {self.top_ports} --script={self.search_nmap(nmap_script)} -sS -sV -sC -O")

    def load_scan(self, xml_file):
        self.xml_file = xml_file
        if self.xml_file == "":
            print("[!] XML file is empty")
            sys.exit()
        else:
            return nmap.load_scan_from_xml(self.xml_file)