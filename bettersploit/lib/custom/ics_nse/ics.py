import nmap
import os
import sys
import time
from random import randint


class ICSScan:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.random_nse = False
        self.timeout = timeout
        self.result = {}
        self.nmap_result = ''
        self.host = host
        self.timeout = timeout
        self.nse_location = 'bettersploit/lib/custom/ics_nse/'
        self.script_list = [self.nse_location + 'Siemens-SIMATIC-PLC-S7.nse','Siemens-WINCC.nse','Siemens-SCALANCE.nse','SIEMENS-HMI-miniweb.nse', 'Siemens-CommunicationsProcessors.nse']
        self.port = 80, 161, 137
        self.nmap_result = self.nmap_scan()


    def get_nmap_result(self):
        return self.nmap_result

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port
    
    def get_timeout(self):
        return self.timeout
    
    def random_nse(self, script_list):
        return script_list[randint(0, len(script_list) - 1)]

    def nmap_scan(self):
        nm = nmap.PortScanner()
        if self.random_nse:
            script = self.random_nse(self.script_list)
            nm.scan(hosts=self.host, ports=self.port, arguments='-sV -sC -sT -Pn -p ' + str(self.port) + ' --script ' + ','.join(self.script_list) + ' --open -T4 -n -oX -')
        else:
           nm.scan(hosts=self.host, ports=self.port, arguments='-sV -sC -sT -Pn -p ' + str(self.port) + ' --script ' + ','.join(self.script_list) + ' --open -T4 -n -oX -')
           self.nmap_result = nm.get_nmap_last_output()
           return self.nmap_result
