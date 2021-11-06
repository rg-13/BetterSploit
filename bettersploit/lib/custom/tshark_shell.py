#Wireshark Shell for BetterSploit
import cmd
from  tshark_wrapper import Shark

class Sharkshell(cmd.Cmd):
    prompt = 'tshark> '
    intro = 'Welcome to the tshark shell. Type help or ? to list commands.\n'
    self.tshark = Shark(interface='wlan0')

    def do_show(self, line):
        '''Show packets'''
        self.tshark.show()

    def do_filter(self, line):
        '''Filter packets'''
        self.tshark.filter(line)
    
    def do_quit(self, line):
        '''Quit'''
        return True

    def do_remote(self, line):
        '''Remote capture'''
        self.tshark.remote(line)
    
    def do_capture_by_interface(self, line):
        '''Capture packets by interface'''
        self.tshark.capture_by_interface(line)
    
    def do_capture_by_interface_and_filter(self, line):
        '''Capture packets by interface and filter'''
        self.tshark.capture_by_interface_and_filter(line)

    def do_capture_by_interface_and_filter_and_save(self, line):
        '''Capture packets by interface, filter and save'''
        self.tshark.capture_by_interface_and_filter_and_save(line)
    
    def do_capture_live(self, line):
        '''Capture live packets'''
        self.tshark.capture_live(line)
    
    def do_capture_live_and_save(self, line):
        '''Capture live packets and save'''
        self.tshark.capture_live_and_save(line)
    
    def do_save(self, line):
        '''Save packets'''
        self.tshark.save(line)
    
    def do_load(self, line):
        '''Load packets'''
        self.tshark.load(line)
    
    def do_load_and_save(self, line):
        '''Load and save packets'''
        self.tshark.load_and_save(line)
    
    def do_capture_live_and_save_and_filter(self, line):
        '''Capture live packets and save and filter'''
        self.tshark.capture_live_and_save_and_filter(line)
    
    def do_capture_live_and_save_and_filter_and_save(self, line):
        '''Capture live packets and save and filter and save'''
        self.tshark.capture_live_and_save_and_filter_and_save(line)
    


    def do_help(self, line):
        '''Help'''
        print("""
        show - Show packets
        filter - Filter packets
        capture_by_interface - Capture packets by interface
        capture_by_interface_and_filter - Capture packets by interface and filter
        capture_by_interface_and_filter_and_save - Capture packets by interface, filter and save
        capture_live - Capture live packets
        capture_live_and_save - Capture live packets and save
        """)


if __name__ == '__main__':
    TsharkShell().cmdloop()
    #tshark.Tshark().capture_by_interface('eth0')
    #tshark.Tshark().capture_by_interface_and_filter('eth0', 'tcp')
    #tshark.Tshark().capture_by_interface_and_filter_and_save('eth0', 'tcp', 'test.pcap')
    #tshark.Tshark().capture_live('eth0')
    #tshark.Tshark().capture_live_and_save('eth0', 'test.pcap')
    #tshark.Tshark().show()
    #tshark.Tshark().filter('tcp')
    #tshark.Tshark().filter('tcp and port 80')
    #tshark.Tshark().filter('tcp and port 80 and host)
    