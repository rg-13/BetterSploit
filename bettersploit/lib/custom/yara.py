from os import times
import os
import yara
from gitgrab import GitGrab


class Yara:
    def __init__(self, rule_path):
        self.rules = None
        self.rules_repo = gitgrabber.GitRepo("https://github.com/advanced-threat-research/Yara-Rules.git")
        self.rules_path = "/custom/yara_rules/"
        
    def get_rules_from_repo(self):
        repo = self.rules_repo
        if dir.exists(self.rule_path):
            print("[+] Rules directory exists")
            print("[+] Getting rules from repo")
            gitgrabber.GitRepo.clone(repo, self.rule_path)
        else:
                print("[-] Rules directory does not exist")
                print("[-] Creating rules directory")
                os.mkdir(self.rule_path)
                print("[+] Getting rules from repo")
                gitgrabber.GitRepo.clone(repo, self.rule_path)
        for root, dirs, files in os.walk(self.rule_path):
            for file in files:
                if file.endswith(".yar"):
                    print("[+] Loading rule {}".format(file))
                    rule_path = os.path.join(root, file)
                    rule_name = file.split(".yar")[0]
                    rule_content = open(rule_path, "r").read()
                    self.add_rule(rule_name, rule_content)
        print("[+] Rules loaded")
        print("[+] Compiling rules")
        self.complie_rules()
        print("[+] Rules compiled")


    def scan_exe(self, file_path):
        for root, dirs, files in os.walk(self.rule_path):
            for file in files:
                if file.endswith(".yar"):
                    print("[+] Loading rulse {}".format(file))
                    rule_path = os.path.join(root, file)
                    rule_name = file.split(".yar")[0]
                    rule_content = open(rule_path, "r").read()
                    self.add_rule(rule_name, rule_content)
                    self.complie_rules()
                if self.yara_match_rule(file_path, rule_name):
                    print("[+] Match found")
                    print("[+] Rule: {}".format(rule_name))
                    print("[+] File: {}".format(file_path))
                    print("[+] Match: {}".format(self.yara_match_rule(file_path, rule_name)))
                    print("[+] Time: {}".format(times()))
                    print("[+] Signature: {}".format(self.yara_match_rule(file_path, rule_name)))
                    matches = self.rules.match(file_path)
                return matches

    def match_rule(self, file_path, rule_name):
        matches = self.rules.match(file_path)
        for match in matches:
            if match.rule == rule_name:
                return True
        return False
    
    def yara_match_rule(self, file_path, rule_name):
        matches = self.rules.match(file_path)
        for match in matches:
            if match.rule == rule_name:
                return True
        return False
    

    def load_rules(self):
        self.rules = yara.compile(self.rule_path)

    def scan(self, file_path):
        matches = self.rules.match(file_path)
        return matches
    
    def scan_string(self, string):
        matches = self.rules.match(data=string)
        return matches

    def scan_file(self, file_path):
        matches = self.rules.match(file_path)
        return matches
    
    def remove_rule(self, rule_name):
        self.rules.remove_rule(rule_name)
    
    def get_rule(self, rule_name):
        return self.rules.get_rule(rule_name)
    
    def get_rules(self):
        return self.rules.rules
    
    def complie_rules(self):
        self.rules.compile()
    
    
    def make_rule(self, rule_name, rule_content):
        self.rules.add_rule(rule_name, rule_content)
        self.rules.save(self.rule_path)

    def add_rule(self, rule_name, rule_content):
        self.rules.add_rule(rule_name, rule_content)
    
    def add_rule_from_file(self, rule_name, rule_file_path):
        self.rules.add_rule(rule_name, rule_file_path)

    def add_rule_from_string(self, rule_name, rule_string):
        self.rules.add_rule(rule_name, rule_string)
    
    def add_rule_from_dict(self, rule_name, rule_dict):
        self.rules.add_rule(rule_name, rule_dict)
    
    def scan_and_print(self, file_path):
        matches = self.rules.match(file_path)
        for match in matches:
            print(match)
    
    def yara_version(self):
        return yara.__version__
    
    def scan_object(self, obj):
        matches = self.rules.match(data=obj)
        return matches
    
    def yara_template(self):
        return yara.template

    def yara_compiler(self):
        return yara.compiler

    def yara_rules(self):
        return yara.rules   

    def yara_match(self):
        return yara.match



    #if __name__ == "__main__":


        # Example usage
        #scan_object(obj) # Scan object
        #scan_string(string) # Scan string
        #scan_file(file_path) # Scan file
        #scan_and_print(file_path) # Scan file and print matches
        #make_rule(rule_name, rule_content) # Make rule
        #add_rule(rule_name, rule_content) # Add rule
        #add_rule_from_file(rule_name, rule_file_path) # Add rule from file
        #add_rule_from_string(rule_name, rule_string) # Add rule from string
        #add_rule_from_dict(rule_name, rule_dict) # Add rule from dict
        #remove_rule(rule_name) # Remove rule
        #complie_rules() # Compile rules
        #get_rule(rule_name) # Get rule
        #get_rules() # Get all rules
        #yara_version() # Get yara version
        #yara_template() # Get yara template
        #yara_compiler() # Get yara compiler
        