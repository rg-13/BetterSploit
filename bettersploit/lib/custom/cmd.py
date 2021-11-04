import cmd, sys
import bettersploit
from bettersploit import *


class Bettersploit(cmd.Cmd):
        self.bsp = bettersploit.Bettersploit()
        intro = 'Bettersploit shell. Type help or ? to list commands.\n'
        prompt = '(bettersploit) '
        file = None

        def do_exit(self, args):
                """Exits the shell."""
                sys.exit()

        def do_back(self, args):
                """Exits the current context."""
                return True
        
        def do_nmap(self, args):
            nmap = self.bsp.nmapper
            nmap.full_scan(args)
            print(nmap.scan_result)
        
        def do_yara_add(self, args):
            yara = self.bsp.yara
            yara.add_rule(args)
            print(yara.rules)
        
        def do_yara_scan(self, args):
            yara = self.bsp.yara
            yara.scan(args)
            print(yara.scan_result)

        def do_yara_rules(self, args):
            yara = self.bsp.yara
            yara.rules()
            print(yara.rules)
        
        def do_yara_remove(self, args):
            yara = self.bsp.yara
            yara.remove_rule(args)
            print(yara.rules)

        def do_yara_clear(self, args):
            yara = self.bsp.yara
            yara.clear_rules()
            print(yara.rules)
        
        def do_yara_load(self, args):
            yara = self.bsp.yara
            yara.load_rules(args)
            print(yara.rules)
        
        def do_yara_save(self, args):
            yara = self.bsp.yara
            yara.save_rules(args)
            print(yara.rules)
    

        def do_set(self, args):
                """Sets a variable to a value."""
                try:
                        name, value = args.split(' ', 1)
                except ValueError:
                        print('usage: set variable value')
                        return
                self.bsp.set(name, value)

        def do_show(self, args):
                """Shows the value of a variable."""
                try:
                        print(self.bsp.get(args))
                except bettersploit.exceptions.VariableNotFound:
                        print('Variable not found.')
        
        def do_unset(self, args):


