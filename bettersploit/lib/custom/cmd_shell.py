import cmd
import os
import sys
import time
import glob
import random

from yara import yara
from wrappers import Wrappers


class CMDCenter(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        #self.bettersploit = bettersploit

        self.prompt = "bettersploit> "
        self.intro = "Welcome to bettersploit"
        self.doc_header = "Commands"
        self.ruler = "-"
        self.use_rawinput = True
        self.cmdqueue = []
        self.config = ["%s=%s" % (k, v) for k, v in os.environ.items()]
        self.last_command = ""
        self.last_command_time = time.time()
        self.last_command_result = ""
        self.last_command_error = ""
        self.last_command_error_time = time.time()
        self.last_command_error_result = ""
        self.tools = Wrappers()
        self.nmap = tools.nmap
        self.sqlmap = tools.sqlmap
        self.wpscan = tools.wpscan
        self.dnsrecon = tools.dnsrecon
        self.nuclei = tools.nuclei
        self.nikto = tools.nikto
        self.httpx = tools.httpx
        self.dirsearch = tools.dirsearch
        self.sublist3r = tools.sublist3r
        self.subjack = tools.subjack
        self.wpscan = tools.wpscan
        self.amass = tools.amass
        self.massdns = tools.massdns
        self.massdns_big = tools.massdns_big
        self.massdns_small = tools.massdns_small
        self.wayback = tools.waybackurls
        self.dirb = tools.dirb
        self.dirb_big = tools.dirb_big
        self.dirb_small = tools.dirb_small
        self.dirsearch = tools.dirsearch
        self.jexboss = tools.jexboss
        self.joomscan = tools.joomscan
        self.gobuster = tools.gobuster
        self.wpscan = tools.wpscan
        self.harvest = tools.harvester
            
        #//TO ADD:
        #self.golismero = tools.golismero


#------------------------------------------------------------------------------
        # self.start_time = time.time()
        #self.start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time))
        #self.start_time_str_short = time.strftime("%Y-%m-%d", time.localtime(self.start_time))
        #self.last_time = time.time()
        #self.last_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_time))
        #self.last_time_str_short = time.strftime("%Y-%m-%d", time.localtime(self.last_time))
#------------------------------------------------------------------------------

    def last_command_time(self):
        self.last_command_time = time.time()



    def still_running(self):
        if time.time() - self.last_command_time > 60:
            return False
        else:
            return True
        

    def do_exit(self, args):
        """Exit the program."""
        return True
    
    def do_sqlmap(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.sqlmap(url)
            else:
                print("[!] Please enter a URL")

    def pass_env(self):
        return self.config



    def do_wpscan(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.wpscan(url)
            else:
                print("[!] Please enter a URL")

    def do_dnsrecon(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.dnsrecon(domain)
            else:
                print("[!] Please enter a domain")

    def do_nuclei(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.nuclei(domain)
            else:
                print("[!] Please enter a domain")
            
    def do_nikto(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.nikto(url)
            else:
                print("[!] Please enter a URL")
        
    def do_httpx(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.httpx(url)
            else:
                print("[!] Please enter a URL")
    
    def do_dirsearch(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.dirsearch(url)
            else:
                print("[!] Please enter a URL")
        
    def do_sublist3r(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:        
            if domain:
                self.sublist3r(domain)
            else:
                print("[!] Please enter a domain")

    def do_subjack(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.subjack(domain)
            else:
                print("[!] Please enter a domain")
        
    def do_amass(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.amass(domain)
            else:
                print("[!] Please enter a domain")

    def do_massdns(self, domain, type=None):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                switch = {
                    'big': self.massdns_big,
                    'small': self.massdns_small
                }
                if type:
                    switch[type](domain)
                else:
                    print("[!] Please enter a domain")
            else:
                print("[!] Please enter a domain")
                
    def do_wayback(self, domain):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.wayback(domain)
            else:
                print("[!] Please enter a domain")


    def do_dirb(self, url, type=None):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                switch = {
                    'big': self.dirb_big,
                    'small': self.dirb_small
                }
                if type:
                    switch[type](url)
                else:
                    print("[!] Please enter a URL")
            else:
                print("[!] Please enter a URL")

    def do_jexboss(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else: 
            if url:
                self.jexboss(url)
            else:
                print("[!] Please enter a URL")
    
    def do_joomscan(self, url):
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.joomscan(url)
            else:
                print("[!] Please enter a URL")
    
    def do_gobuster(self, url):
        if self.still_running():
            if url:
                self.gobuster(url)
            else:
                print("[!] Please enter a URL")
    
    def do_harvest(self, url):
        if self.still_running():
            if url:
                self.harvest(url)
            else:
                print("[!] Please enter a URL")
    
    def do_wpscan(self, url):
        if self.still_running():
            if url:
                self.wpscan(url)
            else:
                print("[!] Please enter a URL")
    
    def do_nmap(self, url, scan_type=None):
        if self.still_running():
            if url:
                switch = {
                    "scan": self.nmap_scan,
                    "scan_big": self.nmap_scan_big,
                    "scan_small": self.nmap_scan_small,
                    "scan_full": self.nmap_scan_full,
                    "scan_fast": self.nmap_scan_fast,
                                        "scan_custom": self.nmap_scan_custom
                }
                if scan_type == None:
                    self.nmap_scan(url)
                elif scan_type in switch:
                    switch[scan_type](url)
                else:
                    print("[!] Please enter a valid scan type")
            else:
                print("[!] Please enter a URL")
        else:
            print("[!] Please wait until the previous command has finished")



if __name__ == '__main__': 
    CMDCenter().cmdloop("bettersploit")
    #CMDCenter().do_wpscan("https://www.google.com")
    #CMDCenter().do_nmap("https://www.google.com")
    #CMDCenter().do_nmap("https://www.google.com", "scan_big")  
    #CMDCenter().do_nmap("https://www.google.com", "scan_small")
    #CMDCenter().do_nmap("https://www.google.com", "scan_full")
    #CMDCenter().do_nmap("https://www.google.com", "scan_fast")
    #CMDCenter().do_nmap("https://www.google.com", "scan_custom")
    #CMDCenter().do_dirb("https://www.google.com")
    #CMDCenter().do_dirb("https://www.google.com", "big")
    #CMDCenter().do_dirb("https://www.google.com", "small")
    #CMDCenter().do_joomscan("https://www.google.com")
    #CMDCenter().do_gobuster("https://www.google.com")
    #CMDCenter().do_harvest("https://www.google.com")
    #CMDCenter().do_wpscan("https://www.google.com")

