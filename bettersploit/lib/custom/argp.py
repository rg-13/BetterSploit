import argparse as ap
import wrappers as tool
import nmapper as nm
import sys
import os
import time

class better_args(ap.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
    
    def parse(self):
        parser = ap.ArgumentParser(description="BetterSploit")
        parser.add_argument("-start", "--start", help="Boots BetterSploit Shell", required=True)
        parser.add_argument("--yara", help="Boots Yara Shell(Scanner)", required=True)
        parser.add_argument("-p", "--port", help="Set ports to scan", required=True)
        parser.add_argument("-t", "--host", help="Target IP or Domain", required=True)
        parser.add_argument("-p", "--port", help="Target port", required=True)
        parser.add_argument("-d", "--delay", help="Delay between scans", required=True)
        parser.add_argument("--nmap", help="Nmap scan", action="append", required=True)
        parser.add_argument("--nmap-args", help="Nmap scan arguments", required=True)
        parser.add_argument("--sqlmap", help="SQLMap scan", action="append", required=True)
        parser.add_argument("--nuceli", help="Nuclei scan", action="append", required=True)
        parser.add_argument("--nuceli-mode", help="Nuclei scan mode", action="append", required=True)
        parser.add_argument("--dirb", help="Dirb scan", action="append", required=True)
        
        args = parser.parse_args()
        return args


    def get_args(self):
        args = self.parse()
        return args
    
    def get_host(self):
        args = self.get_args()
        target = args.host
        return target
    
    def get_port(self):
        args = self.get_args()
        port = args.port
        return port
    
    def get_delay(self):
        args = self.get_args()
        delay = args.delay
        return delay
    
    def get_nmap(self, host):
        args = self.get_args()
        nmap = args.nmap
        nmap_args = args.nmap_args
        nm.nmap_scan(host, nmap, nmap_args)
    
    def get_sqlmap(self, host):
        args = self.get_args()
        sqlmap = args.sqlmap
        tool.sqlmap_scan(host, sqlmap)

    def get_nuclei(self, host):
        args = self.get_args()
        nuclei = args.nuclei
        nuclei_mode = args.nuclei_mode
        tool.nuclei_scan(host)
    
    def get_dirb(self, host):
        args = self.get_args()
        dirb = args.dirb
        tool.dirb_scan(host, dirb)
    

def main():
    args = better_args()
    args.get_start()