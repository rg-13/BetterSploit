import cmd, sys
from bettersploit import yara
yara = yara.Yara()



class Bettersploit(cmd.Cmd):
        intro = 'BetterSploit: YARA Shell. Type help or ? to list commands.\n'
        prompt = '(bettersploit) '
        file = None

        def do_set(self, args):
            yara = self.bsp.yara
            yara.set(args)
            print(yara.set_result)
        
        def do_clear(self, args):
            print(chr(27) + "[2J")

        def do_help(self, args):
            print("""   
        set <option> <value>
        clear
        scan_object <object>
        scan_file <file>
        scan_url <url>
        exit
        back
        yara_add <rule>
        yara_scan <file>
        yara_rules
        yara_remove <rule>
        yara_clear
        yara_load <file>
        yara_save <file>
        yara_test <rule>
        yara_info <rule>
        yara_compile <file>
        yara_version
        yara_update
        yara_info
        yara_help
        yara_license
        yara_sources
        yara_credits
        yara_about
        help
        """)

        def do_scan_object(self, args):
            yara = self.bsp.yara
            yara.scan_object(args)
            print(yara.scan_object_result)
        
        def do_scan_file(self, args):
            yara = self.bsp.yara
            yara.scan_file(args)
            print(yara.scan_file_result)
        
        def do_scan_url(self, args):
            yara = self.bsp.yara
            yara.scan_url(args)
            print(yara.scan_url_result)

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

        def do_yara_test(self, args):
            yara = self.bsp.yara
            yara.test_rule(args)
            print(yara.test_result)
        
        def do_yara_info(self, args):
            yara = self.bsp.yara
            yara.info_rule(args)
            print(yara.info_result)

        def do_yara_compile(self, args):
            yara = self.bsp.yara
            yara.compile_rule(args)
            print(yara.compile_result)
        
        def do_yara_version(self, args):
            yara = self.bsp.yara
            yara.version()
            print(yara.version_result)

        def do_yara_update(self, args):
            yara = self.bsp.yara
            yara.update()
            print(yara.update_result)
        
        def do_yara_info(self, args):
            yara = self.bsp.yara
            yara.info()
            print(yara.info_result)
        
        def do_yara_help(self, args):
            yara = self.bsp.yara
            yara.help()
            print(yara.help_result)
        
        def do_yara_license(self, args):
            yara = self.bsp.yara
            yara.license()
            print(yara.license_result)
        
        def do_yara_sources(self, args):
            yara = self.bsp.yara
            yara.sources()
            print(yara.sources_result)

        def do_yara_credits(self, args):
            yara = self.bsp.yara
            yara.credits()
            print(yara.credits_result)
        
        def do_yara_about(self, args):
            yara = self.bsp.yara
            yara.about()
            print(yara.about_result)


if __name__ == '__main__':
        Bettersploit().cmdloop()
        sys.exit()