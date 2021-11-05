import cmd
import os
import sys
import time
import glob
import random
from bettersploit.lib.custom import *


class CMDCenter(cmd.Cmd):
    def __init__(self, bettersploit):
        cmd.Cmd.__init__(self)
        self.bettersploit = bettersploit
        self.prompt = "bettersploit> "
        self.intro = "Welcome to bettersploit"
        self.doc_header = "Commands"
        self.ruler = "-"
        self.use_rawinput = True
        self.cmdqueue = []
        self.last_command = ""
        self.last_command_time = time.time()
        self.last_command_result = ""
        self.last_command_error = ""
        self.last_command_error_time = time.time()
        self.last_command_error_result = ""
        self.tools = bettersploit.Wrappers
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



    def do_exit(self, args):
        """Exit the program."""
        return True
    
    def do_sqlmap(self, url):
        if url:
            self.sqlmap(url)
        else:
            print("[!] Please enter a URL")

    def do_wpscan(self, url):
        if url:
            self.wpscan(url)
        else:
            print("[!] Please enter a URL")

    def do_dnsrecon(self, domain):
        if domain:
            self.dnsrecon(domain)
        else:
            print("[!] Please enter a domain")

    def do_nuclei(self, domain):
        if domain:
            self.nuclei(domain)
        else:
            print("[!] Please enter a domain")
        
    def do_nikto(self, url):
        if url:
            self.nikto(url)
        else:
            print("[!] Please enter a URL")
        
    def do_httpx(self, url):
        if url:
            self.httpx(url)
        else:
            print("[!] Please enter a URL")
    
    def do_dirsearch(self, url):
        if url:
            self.dirsearch(url)
        else:
            print("[!] Please enter a URL")
        
    def do_sublist3r(self, domain):
        if domain:
            self.sublist3r(domain)
        else:
            print("[!] Please enter a domain")

    def do_subjack(self, domain):
        if domain:
            self.subjack(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_amass(self, domain):
        if domain:
            self.amass(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_massdns(self, domain):
        if domain:
            self.massdns(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_massdns_big(self, domain):
        if domain:
            self.massdns_big(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_massdns_small(self, domain):
        if domain:
            self.massdns_small(domain)
        else:
            print("[!] Please enter a domain")

    def do_wayback(self, domain):
        if domain:
            self.wayback(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_dirb(self, domain):
        if domain:
            self.dirb(domain)
        else:
            print("[!] Please enter a domain")

    def do_dirb_big(self, domain):
        if domain:
            self.dirb_big(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_dirb_small(self, domain):
        if domain:
            self.dirb_small(domain)
        else:
            print("[!] Please enter a domain")
    
    def do_jexboss(self, url):
        if url:
            self.jexboss(url)
        else:
            print("[!] Please enter a URL")
    
    def do_joomscan(self, url):
        if url:
            self.joomscan(url)
        else:
            print("[!] Please enter a URL")
    
    def do_gobuster(self, url):
        if url:
            self.gobuster(url)
        else:
            print("[!] Please enter a URL")
    
    def do_harvest(self, url):
        if url:
            self.harvest(url)
        else:
            print("[!] Please enter a URL")
    
    def do_wpscan(self, url):
        if url:
            self.wpscan(url)
        else:
            print("[!] Please enter a URL")
    
    def do_nmap(self, url):
        if url:
            self.nmap(url)
        else:
            print("[!] Please enter a URL")
    
    def do_nmap_full(self, url):
        if url:
            self.nmap_full(url)
        else:
            print("[!] Please enter a URL")
    
    def do_nmap_fast(self, url):
        if url:
            self.nmap_fast(url)
        else:
            print("[!] Please enter a URL")
    
    def do_nmap_top(self, url):
        if url:
            self.nmap_top(url)
        else:
            print("[!] Please enter a URL")
    
    def do_nmap_all(self, url):
        if url:
            self.nmap_all(url)
        else:
            print("[!] Please enter a URL")
        
    


