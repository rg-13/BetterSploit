import cmd
import os
import sys
import time
import glob
import random
import random
import wrappers as tools
import tshark_shell as tshark
import yara_cmd as yara_shell
import yara as yara_lib
from nmapper import nmap_scan
import subprocess
#import bettersploit.lib.custom as bsp

ascii_art=[
'''
╔══╗───╔╗─╔╗─────╔═══╗──╔╗────╔╗
║╔╗║──╔╝╚╦╝╚╗────║╔═╗║──║║───╔╝╚╗
║╚╝╚╦═╩╗╔╩╗╔╬══╦═╣╚══╦══╣║╔══╬╗╔╝
║╔═╗║║═╣║─║║║║═╣╔╩══╗║╔╗║║║╔╗╠╣║
║╚═╝║║═╣╚╗║╚╣║═╣║║╚═╝║╚╝║╚╣╚╝║║╚╗
╚═══╩══╩═╝╚═╩══╩╝╚═══╣╔═╩═╩══╩╩═╝
─────────────────────║║
─────────────────────╚╝''',
'''
██████╗░███████╗████████╗████████╗███████╗██████╗░░██████╗██████╗░██╗░░░░░░█████╗░██╗████████╗
██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝╚█████╗░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║██████╔╝██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░''',

'''

█▄▄ █▀▀ ▀█▀ ▀█▀ █▀▀ █▀█ █▀ █▀█ █░░ █▀█ █ ▀█▀
█▄█ ██▄ ░█░ ░█░ ██▄ █▀▄ ▄█ █▀▀ █▄▄ █▄█ █ ░█░''',

"""
██████████████████████████████████████████████████████████████████████
█▄─▄─▀█▄─▄▄─█─▄─▄─█─▄─▄─█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█▄─▄▄─█▄─▄███─▄▄─█▄─▄█─▄─▄─█
██─▄─▀██─▄█▀███─█████─████─▄█▀██─▄─▄█▄▄▄▄─██─▄▄▄██─██▀█─██─██─████─███
▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀""",


"""
░█▀▀█ █▀▀ ▀▀█▀▀ ▀▀█▀▀ █▀▀ █▀▀█ ░█▀▀▀█ █▀▀█ █── █▀▀█ ─▀─ ▀▀█▀▀ 
░█▀▀▄ █▀▀ ──█── ──█── █▀▀ █▄▄▀ ─▀▀▀▄▄ █──█ █── █──█ ▀█▀ ──█── 
░█▄▄█ ▀▀▀ ──▀── ──▀── ▀▀▀ ▀─▀▀ ░█▄▄▄█ █▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ──▀──""",
  

"""
───────────────▄▄───▐█
───▄▄▄───▄██▄──█▀───█─▄
─▄██▀█▌─██▄▄──▐█▀▄─▐█▀
▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌
▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄
BᴇᴛᴛᴇʀSᴘʟᴏɪᴛ


"""

]






class CMDCenter(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        #self.bettersploit = bettersploit

        self.prompt = "bettersploit> "
        self.intro = random.choice(ascii_art)
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
        self.tools = tools
        self.nmap = nmap_scan
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
        self.dirb = tools.dirb
        self.dirsearch = self.dirsearch
        self.jexboss = self.tools.jexboss
        self.joomscan = self.tools.joomscan
        self.gobuster = self.tools.gobuster
        self.cmsmap = self.tools.cmsmap
        self.harvest = self.tools.theharvester
        self.yara = yara_shell()
        self.tshell = tshark_shell()
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
        "sqlmap <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.sqlmap(url)
            else:
                print("[!] Please enter a URL")

    def pass_env(self):
        return self.config


    def do_yara(self):
        "opens YARA interactive shell"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            yara_shell = YaraShell()
            yara_shell.cmdloop()

    
    def do_wireshark(self):
        "opens wireshark(tshark) interactive shell"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            tshark_shell = TsharkShell()
            tshark_shell.cmdloop()              

    def do_dnsrecon(self, domain):
        "dnsrecon <domain>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.dnsrecon(domain)
            else:
                print("[!] Please enter a domain")

    def do_nuclei(self, domain):
        "nuclei <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.nuclei(domain)
            else:
                print("[!] Please enter a domain")
            
    def do_nikto(self, url):
        "nikto <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.nikto(url)
            else:
                print("[!] Please enter a URL")
        
    def do_httpx(self, url):
        "httpx <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.httpx(url)
            else:
                print("[!] Please enter a URL")
    
    def do_dirsearch(self, url):
        "dirsearch <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.dirsearch(url)
            else:
                print("[!] Please enter a URL")
        
    def do_sublist3r(self, domain):
        "sublist3r <domain>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:        
            if domain:
                self.sublist3r(domain)
            else:
                print("[!] Please enter a domain")

    def do_subjack(self, domain):
        "subjack <domain>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.subjack(domain)
            else:
                print("[!] Please enter a domain")
        
    def do_amass(self, domain):
        "amass <domain>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if domain:
                self.amass(domain)
            else:
                print("[!] Please enter a domain")

    def do_dirb(self, url, type=None):
        "dirb <url> [type]"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                switch = {
                    'big': self.dirb_big,
                    'small': self.dirb_small
                }
                if type == "big":
                    self.tools.dirb_big(url)
                elif type == "small":
                    self.tools.dirb_small(url)
                elif type == "common":
                    self.tools.dirb_common(url)
                else:
                    print("[!] Please enter a type")

    def do_jexboss(self, url):
        "jexboss <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else: 
            if url:
                self.jexboss(url)
            else:
                print("[!] Please enter a URL")
    
    def do_joomscan(self, url):
        "joomscan <url>"
        if self.still_running():
            print("[!] Please wait until the previous command has finished")
        else:
            if url:
                self.joomscan(url)
            else:
                print("[!] Please enter a URL")
    
    def do_gobuster(self, url):
        "gobuster <url>"
        if self.still_running():
            if url:
                self.gobuster(url)
            else:
                print("[!] Please enter a URL")
    
    def do_harvest(self, url):
        "harvest <url>"
        if self.still_running():
            if url:
                self.harvest(url)
            else:
                print("[!] Please enter a URL")
    
    def do_cmsmap(self, url):
        "cmsmap <url>"
        if self.still_running():
            if url:
                self.cmsmap(url)
            else:
                print("[!] Please enter a URL")
    
    def do_nmap(self, url, scan_type=None):
        "nmap <url> [type]"
        if self.still_running():
            if url:
                self.nmap.nmap_scan(url, scan_type)
            else:
                print("[!] Please enter a URL")

if __name__ == '__main__': 
    CMDCenter().cmdloop()
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

