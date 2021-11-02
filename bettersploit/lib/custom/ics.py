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
        self.script_list = [self.nse_location + 'proconos-info','omrom-info','fox-info','enip-info','pcworx-info','modbus-discover.nse','bacnet-info.nse','s7-info.nse','Siemens-SIMATIC-PLC-S7.nse','Siemens-WINCC.nse','Siemens-SCALANCE.nse','SIEMENS-HMI-miniweb.nse', 'Siemens-CommunicationsProcessors.nse']
        self.port = 80,102,443,502,530,593,789,1089-1091,1911,1962,2222,2404,4000,4840,4843,4911,9600,19999,20000,20547,34962-34964,34980,44818,46823,46824,55000-55003
        #Breakdown:
        #https://github.com/gnebbia/nmap_tutorial/blob/master/sections/ics_scada.md
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
