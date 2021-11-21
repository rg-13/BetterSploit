#-------    
import os
import sys
import time
import requests
import subprocess
from subprocess import  Popen, PIPE
import socket
import argparse



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
        self.upnp_nse = "upnp-*", "upnp-info"
        self.cve_nse = "cve-*"
        self.list_all = "afp-*", "ftp-*", "http-*", "imap-*", "ldap-*", "mssql-*", "mysql-*", "nfs-*", "nntp-*", "pop3-*", "rdp-*", "smb-*", "smtp-*", "snmp-*", "ssh-*", "telnet-*", "vmauthd-*", "vnc-*", "xmpp-*"
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
        self.upnp_tcp_ports = "1900"
        self.upnp_udp_ports = "5000"
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
    
    def set_port(self, port):
        self.port = port
        return port
    
    def set_nmap_args(self, nmap_args):
        self.nmap_args = nmap_args
        return nmap_args
    
    def set_nmap_path(self, nmap_path):
        self.nmap_path = nmap_path
        return nmap_path
    
    def set_nmap_timeout(self, nmap_timeout):
        self.nmap_timeout = nmap_timeout
        return nmap_timeout
    
    def set_nmap_scan_output(self, nmap_scan_output):
        self.nmap_scan_output = nmap_scan_output
        return nmap_scan_output
    
    def set_http_nse(self, http_nse):
        self.http_nse = http_nse
        return http_nse
    
    def set_all_network_nse(self, all_network_nse):
        self.all_network_nse = all_network_nse
        return all_network_nse
    
    def set_smb_nse(self, smb_nse):
        self.smb_nse = smb_nse
        return smb_nse
    
    def set_ssh_nse(self, ssh_nse):
        self.ssh_nse = ssh_nse
        return ssh_nse
    
    def set_dns_nse(self, dns_nse):
        self.dns_nse = dns_nse
        return dns_nse
    
    def set_ftp_nse(self, ftp_nse):
        self.ftp_nse = ftp_nse
        return ftp_nse
    
    def set_smtp_nse(self, smtp_nse):
        self.smtp_nse = smtp_nse
        return smtp_nse
    
    def set_mysql_nse(self, mysql_nse):
        self.mysql_nse = mysql_nse
        return mysql_nse
    
    def set_mssql_nse(self, mssql_nse):
        self.mssql_nse = mssql_nse
        return mssql_nse
    
    def set_postgres_nse(self, postgres_nse):
        self.postgres_nse = postgres_nse
        return postgres_nse
    
    def set_vnc_nse(self, vnc_nse):
        self.vnc_nse = vnc_nse
        return vnc_nse
    
    def set_xmpp_nse(self, xmpp_nse):
        self.xmpp_nse = xmpp_nse
        return xmpp_nse
    
    def set_upnp_nse(self, upnp_nse):
        self.upnp_nse = upnp_nse
        return upnp_nse
    
    def set_all_ports(self, all_ports):
        self.all_ports = all_ports
        return all_ports
    
    def set_cloud_ports(self, cloud_ports):
        self.cloud_ports = cloud_ports
        return cloud_ports
    
    def set_smb_ports(self, smb_ports):
        self.smb_ports = smb_ports
        return smb_ports
    
    def set_ssh_ports(self, ssh_ports):
        self.ssh_ports = ssh_ports
        return ssh_ports
    
    def set_dns_ports(self, dns_ports):
        self.dns_ports = dns_ports
        return dns_ports
    
    def set_ftp_ports(self, ftp_ports):
        self.ftp_ports = ftp_ports
        return ftp_ports
    
    def set_smtp_ports(self, smtp_ports):
        self.smtp_ports = smtp_ports
        return smtp_ports
    
    def set_mysql_ports(self, mysql_ports):
        self.mysql_ports = mysql_ports
        return mysql_ports
    
    def set_mssql_ports(self, mssql_ports):
        self.mssql_ports = mssql_ports
        return mssql_ports
    
    def set_postgres_ports(self, postgres_ports):
        self.postgres_ports = postgres_ports
        return postgres_ports

    def set_network_ports(self, network_ports):
        self.network_ports = network_ports
        return network_ports
    
    def set_upnp_tcp_ports(self, upnp_tcp_ports):
        self.upnp_tcp_ports = upnp_tcp_ports
        return upnp_tcp_ports
    
    def set_upnp_udp_ports(self, upnp_udp_ports):
        self.upnp_udp_ports = upnp_udp_ports
        return upnp_udp_ports
    
    def set_nmap_scan(self, nmap_scan):
        self.nmap_scan = nmap_scan
        return nmap_scan
    
    def set_nmap_scan_output_read(self, nmap_scan_output_read):
        self.nmap_scan_output_read = nmap_scan_output_read
        return nmap_scan_output_read
    
    def set_nmap_scan_output_write(self, nmap_scan_output_write):
        self.nmap_scan_output_write = nmap_scan_output_write
        return nmap_scan_output_write
    
    def set_nmap_scan_output_write_file(self, nmap_scan_output_write_file):
        self.nmap_scan_output_write_file = nmap_scan_output_write_file
        return nmap_scan_output_write_file
    


    def get_ip(self, host):
        try:
            ip = socket.gethostbyname(host)
            return ip
        except socket.gaierror:
            print("[-] Error: Hostname could not be resolved. Exiting")
            sys.exit()
        
    def get_hostname(self, ip):
        try:
            hostname = socket.gethostbyaddr(ip)
            return hostname
        except socket.herror:
            print("[-] Error: Could not resolve hostname. Exiting")
            sys.exit()
     
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
            "upnp": self.upnp_nse,
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

            elif nse_libs == self.upnp_nse:
                port = self.upnp_tcp_ports + "," + self.upnp_udp_ports
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

    def nmap_scan_output_write(self, nmap_scan_output_write):
        with open(self.nmap_scan_output, 'w') as f:
            f.write(nmap_scan_output_write)
        f.close()

    def nmap_scan_output_append(self, nmap_scan_output_append):
        with open(self.nmap_scan_output, 'a') as f:
            f.write(nmap_scan_output_append)
        f.close()


def main():
    parser = argparse.ArgumentParser(description='Nmap Scanner')
    parser.add_argument('-t', '--target', help='Target IP address', required=True)
    parser.add_argument('-p', '--ports', help='Port range to scan', required=False) 
    parser.add_argument('-s', '--scan', help='Scan type', required=False)   
    parser.add_argument('-o', '--output', help='Output file', required=False)
    parser.add_argument('-d', '--debug', help='Debug mode', required=False)
    args = parser.parse_args()

    if args.target:
        target = args.target
    else:
        print("[!] Please enter a target IP address")
        sys.exit()
    
    if args.ports:
        ports = args.ports
    else:
        ports = None
    
    if args.scan:
        scan = args.scan
    else:
        scan = None
    
    if args.output:
        output = args.output
    else:
        output = None
    
    if args.debug:
        debug = args.debug
    else:
        debug = None
    
    NmapScan = nmap_scan(target, ports, scan, output, debug)
    NmapScan.nmap_scan()
    

if __name__ == '__main__':
    main()