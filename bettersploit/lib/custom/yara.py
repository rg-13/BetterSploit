import yara


class Yara:
    def __init__(self, rule_path):
        self.rule_path = rule_path
        self.rules = None

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
        self.rules.save(self.rule_path)
    
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
    
    

    if __name__ == "__main__":


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
        