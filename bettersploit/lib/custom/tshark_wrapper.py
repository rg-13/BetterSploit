import pyshark


class Shark:
    def __init__(self, interface):
        self.interface = interface
        self.cap = pyshark.LiveCapture(interface)
        self.cap.sniff(timeout=10)

    def get_packets(self):
        return self.cap.sniff_continuously(packet_count=10)

    def get_packet_count(self):
        return len(self.cap.sniff_continuously(packet_count=10))

    def get_packet_count_by_protocol(self, protocol):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol))

    def get_packet_count_by_protocol_and_port(self, protocol, port):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port))

    def get_packet_count_by_protocol_and_port_and_ip(self, protocol, port, ip):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port + " and ip.src==" + ip))

    def get_packet_count_by_protocol_and_port_and_ip_and_mac(self, protocol, port, ip, mac):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port + " and ip.src==" + ip + " and ether.src==" + mac))

    def get_packet_count_by_protocol_and_port_and_ip_and_mac_and_dns(self, protocol, port, ip, mac, dns):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port + " and ip.src==" + ip + " and ether.src==" + mac + " and dns.qry_name==" + dns))

    def get_packet_count_by_protocol_and_port_and_ip_and_mac_and_dns_and_dns_type(self, protocol, port, ip, mac, dns, dns_type):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port + " and ip.src==" + ip + " and ether.src==" + mac + " and dns.qry_name==" + dns + " and dns.type==" + dns_type))

    def get_packet_count_by_protocol_and_port_and_ip_and_mac_and_dns_and_dns_type_and_dns_class(self, protocol, port, ip, mac, dns, dns_type, dns_class):
        return len(self.cap.sniff_continuously(packet_count=10, filter=protocol + " port " + port + " and ip.src==" + ip + " and ether.src==" + mac + " and dns.qry_name==" + dns + " and dns.type==" + dns_type + " and dns.class==" + dns_class))

    def live_capture(self, interface):
        self.cap.sniff(iface=interface)
    
    def live_capture_with_filter(self, interface, filter):
        self.cap.sniff(iface=interface, filter=filter)

    def live_capture_with_filter_and_timeout(self, interface, filter, timeout):
        self.cap.sniff(iface=interface, filter=filter, timeout=timeout)

    def remote_capture(self, interface, remote_host, remote_port):
        self.cap.remote_capture(interface, remote_host, remote_port)
    
    def remote_capture_with_filter(self, interface, remote_host, remote_port, filter):
        self.cap.remote_capture(interface, remote_host, remote_port, filter)

    def save_file(self, file_name):
        self.cap.save_file(file_name)

    def save_file_with_filter(self, file_name, filter):
        self.cap.save_file(file_name, filter)
    
    def remote_save_file(self, file_name, remote_host, remote_port):
        self.cap.remote_save_file(file_name, remote_host, remote_port)

    


