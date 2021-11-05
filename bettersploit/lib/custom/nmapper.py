#-------    
import os
import sys
import time
import requests
import subprocess
from subprocess import SW_HIDE, Popen, PIPE
import socket


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
class nmap_scan:

    def __init__(self):
        self.ip = "ip"
        self.port =  "port"
        self.nmap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nmap')
        self.nmap_args = ""
        self.nmap_scan_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nmap_scan_output.txt')
        self.http_nse = "http-*","ssl-*"
        self.all_network_nse = "afp-*", "ftp-*", "http-*", "imap-*", "ldap-*", "mssql-*", "mysql-*", "nfs-*", "nntp-*", "pop3-*", "rdp-*", "smb-*", "smtp-*", "snmp-*", "ssh-*", "telnet-*", "vmauthd-*", "vnc-*", "xmpp-*"
        self.smb_nse = "smb-*"
        self.ssh_nse = "ssh-*"
        self.dns_nse = "dns-*"
        self.ftp_nse = "ftp-*"
        self.smtp_nse = "smtp-*"
        self.mysql_nse = "mysql-*"
        self.mssql_nse = "mssql-*"
        self.oracle_nse = "oracle-*"
        self.postgres_nse = "postgres-*"
        self.rdp_nse = "rdp-*", "ms-wbt-*"
        self.vnc_nse = "vnc-*"
        self.telnet_nse = "telnet-*"
        self.xmpp_nse = "xmpp-*", "jabber-*"
        self.cloud_nse = "aws-*", "azure-*", "cloud-*", "digitalocean-*", "gcp-*", "hcloud-*", "linode-*", "packet-*", "vultr-*"
        self.cve_nse = "cve-*"
        self.nse_list = self.http_nse, self.all_network_nse, self.smb_nse, self.ssh_nse, self.dns_nse, self.ftp_nse, self.smtp_nse, self.mysql_nse, self.mssql_nse, self.oracle_nse, self.postgres_nse, self.rdp_nse, self.vnc_nse, self.telnet_nse, self.xmpp_nse, self.cloud_nse

        self.all_ports = "1-65535"
        self.cloud_ports = "1-65535"
        self.smb_ports = "139,445"
        self.ssh_ports = "22", "2222"
        self.dns_ports = "53", "5300"
        self.ftp_ports = "21", "2100", "2101"
        self.smtp_ports = "25", "2525"
        self.http_ports = "80,443", "8080", "8443"
        self.smb_ports = "445", "139"
        self.rdp_ports = "3389"
        self.telnet_ports = "23", "2323", "2324"
        self.vnc_ports = "5900", "5901"
        self.xmpp_ports = "5222", "5269"
        self.mysql_ports = "3306", "3316", "3389", "4444", "5432"
        self.postgres_ports = "5432", "5433"
        self.mssql_ports = "1433", "1434"
        self.ssh_ports = "22", "2222", "2223"
        self.dns_ports = "53", "853", "8686", "8888"
        self.network_ports = "22,2222,2223,53,853,8686,445,139"
        self.nmap_timeout = "--max-rtt-timeout=500ms"
    
    def nmap_scan_output(self):
        with open(self.nmap_scan_output, 'w') as f:
            f.write(self.nmap_scan.stdout.read())
        f.close()
        return self.nmap_scan_output

    def get_ip(domain):
        try:
            domain = socket.gethostbyname(domain)
            return domain
        except socket.gaierror:
            print("Could not resolve hostname")
            sys.exit()

    def nmap_scan_output_read(self):
        with open(self.nmap_scan_output, 'r') as f:
            self.nmap_scan_output_read = f.read()
        f.close()
        return self.nmap_scan_output_read

    def set_host(self, host):
        self.host = self.get_ip(host)
        return host
    
    def run_nmap(self, host, port, nse, timeout):
        self.set_host(host)
        self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse)
        self.nmap_scan = subprocess.Popen([self.nmap_path, self.nmap_args, self.ip, self.port, self.timeout], stdout=PIPE, stderr=PIPE)
        self.nmap_scan_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nmap_scan_output.txt')
        self.nmap_scan_output_read = self.nmap_scan_output()
        return self.nmap_scan_output_read  


    def scan_host(self, host, port, scan_type=None):
        self.set_host(host)
        if host == None:
            print("[!] Please enter a host to scan")
            sys.exit()
        if scan_type == None:
            print("[!] Please enter a scan type")
            sys.exit()
        nse_libs = {
            "http": self.http_nse,
            "network": self.all_network_nse,
            "smb": self.smb_nse,
            "ssh": self.ssh_nse,
            "dns": self.dns_nse,
            "ftp": self.ftp_nse,
            "smtp": self.smtp_nse,
            "mysql": self.mysql_nse,
            "mssql": self.mssql_nse,
            "oracle": self.oracle_nse,
            "postgres": self.postgres_nse,
            "rdp": self.rdp_nse,
            "vnc": self.vnc_nse,
            "telnet": self.telnet_nse,
            "xmpp": self.xmpp_nse,
            "cloud": self.cloud_nse,
            "cve": self.cve_nse,
            "all": self.nse_list
        }

        if scan_type in nse_libs:
            if nse_libs == self.nse_list:
                port = self.all_ports
                for nse in nse_libs:
                    self.run_nmap(host, port, nse, self.timeout)
            elif nse_libs == self.http_nse:
                port = self.http_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.all_network_nse:
                port = self.network_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.cloud_nse:
                port = self.cloud_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.smb_nse:
                port = self.smb_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(self.smb_ports, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.ssh_nse:
                port = self.ssh_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(self.ssh_ports, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.dns_nse:
                port = self.dns_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(self.dns_ports, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.ftp_nse:
                port = self.ftp_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(self.ftp_ports, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.smtp_nse:
                port = self.smtp_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(self.smtp_ports, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.all_network_nse:
                port = self.network_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.smb_nse:
                ports = self.smb_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.ssh_nse:
                ports = self.ssh_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.dns_nse:
                ports = self.dns_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.ftp_nse:
                ports = self.ftp_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.smtp_nse:
                ports = self.smtp_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.cve_nse:
                ports = self.all_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.mysql_nse:
                ports = self.mysql_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.mssql_nse:
                ports = self.mssql_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.oracle_nse:
                ports = self.oracle_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            elif nse_libs == self.postgres_nse:
                ports = self.postgres_ports
                self.nmap_args = "-sV -Pn -p {} --script {}".format(port, nse_libs)
                self.run_nmap(host, port, nse_libs, self.timeout)

            else:
                print("[!] Please enter a valid scan type")
                sys.exit()
        else:
            nse_libs = self.nse_list
            self.run_nmap(host, port, nse_libs, self.timeout)
            

    def nmap_scan_output_read(self):
        with open(self.nmap_scan_output, 'r') as f:
            self.nmap_scan_output_read = f.read()
        f.close()
        return self.nmap_scan_output_read
