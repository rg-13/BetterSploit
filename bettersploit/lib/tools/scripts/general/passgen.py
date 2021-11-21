import hashlib
import sys
import privy
from tqdm import tqdm

def main():
    # Code goes here
    '''
    print("Coming right up.... :)")
    for i in tqdm(range(int(9e6)), ascii=True, desc="Loading...."):
        pass
    sys.exit(0)
'''

while True:
    with open("SuperSecretPassword.txt", "w+") as f:
        #f.write(hashlib.sha256(input("Enter your password: ").encode()).hexdigest())
        if str(input("[ * ] Would you like to generate a Password? [ * ]\n->")) == "yes":
            print("[ * ] Generating Password....")
            for i in tqdm(range(int(9e6)), ascii=True, desc="Loading...."):
                pass
            f.write(hashlib.sha256(str(input("[ * ] Enter your password: ")).encode('utf-8')).hexdigest())
            print("[ * ] Password has been generated and encrypted!")
            break
'''
    data = b'' #Insert Little Password
    sys.stdout = open('SuperSecretPassword.txt', 'wt')
    hidden = privy.hide(data, ask_for_password())
        print("Welcome to the program")
        main()
    else:
        print("Doesnt Seem Right... Try again!")

        return
'''
def view_hash():
    with open("SuperSecretPassword.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    main()
    view_hash()
