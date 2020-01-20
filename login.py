#from account import *
import os.path
from os import path

def main():
    confirmed = False
    while not confirmed:
        choice = input('Welcome!\nLogin  or  Create an Account\nType \"login\" or \"create\"\n')
        print(choice)

        if choice == 'login':
            print('Login to Your Account\n')
            email = input('Email: ')
            password = input('Password: ')
        
            if getAccount(email, password):
                print('Logged in!')
                confirmed = True
            else:
                print('Login faled. Try Again\n')
        elif choice == 'create':
            print('Create an Account\n')
            first = input('First name: ')
            last = input('Last name: ')
            confirmed = False
            email = None
            while not confirmed:
                email = input('Email address: ')
                if email == 'q':
                    break
                if validate(email):
                    confirmed = True
                    if path.exists(email[:email.find('@')]+'.txt'):
                        confirmed = False
                        print('An account with the email ' + email + ', has already been created.\nLogin or use a diffent email.\n')
                        
            if email == 'q':
                break  
            password = input('Password: ')
            confirmed = False

            while not confirmed:
                secPass = input('Confirm Password: ')
                if secPass == password:
                    confirmed = True
                else:
                    print('Passwords did not match. Try again')

            confirmed = False    
            uIndex = email.find('@')
            url = email[0:uIndex] + '.txt'
            with open(url, 'w') as f:
                f.write(first + '\n' + last + '\n' + email + '\n' + password)
                print("Account Created and saved in " + url + ". Now log in!")


        

def getAccount(e, p):
    uIndex = e.find('@')
    url = e[0: uIndex] + '.txt'
    if path.exists(url):
        with open(url, 'r') as f:
            f_contents = f.readlines()
            if f_contents[3] == p:
                return True
    return False

def validate(email):
    if len(email) < 5:
        return False
    param1 = email.find('@')
    if param1 > 0:
        param2 = email.find('.', param1)
        if param2 > 0:
            return True

main()