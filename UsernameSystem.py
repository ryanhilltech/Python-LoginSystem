# Ryan Hill 13Nov15 SEU
# Username and Password login system

# define main function, print logo, login requirements and main menu.
# Call newUser, mainLogin or exit functions called based on user input

## Problem notes: writing to file not working, exception handling for requirements

import sys
import hashlib
import uuid


# writeFunction is used to write approved usernames and passwords from newUser creation to file
def writeFunction(userName, passWord):
    try:
        with open('Usernames-Pass.txt', 'a') as userFile:
            userFile.write(userName + '\n')
            userFile.write(hash_password(passWord) + '\n')
# exception handling
    except IOError as e:
        print (e)
    except NameError as e:
        print(e)
        
# encrypt password
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# check password    
def check_password(hashPassword, plainPassword):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


# newUser will provide registration information, name, email, password. Check email for @ and .edu. 
# Check password for length 6-10, and at least 1 integer. Save to external file.
def newUser():
    userName = False
    while userName == False:
        try:        
            userName = input("Requirements for the username: Make sure it is an email that includes @ and .edu or .com \n")
            if "@" and '.edu' and '.com' not in userName:
                print('Remember to include the @ symbol and .edu in your Username. \n')
                userName = False
        except NameError as e:
            print(e)
            userName = False
        except ValueError as e:
            print(e)    
            userName = False
            
    passWord = False    
    while passWord == False:
        try:
            passWord = input("Make sure the password is 6-10 characters long and includes at least 1 integer \n") 
            print (len(passWord))
            if len(passWord) not in range(6,11):
                print('The length of the password needs to be between 6 and 10 digits long. \n')
                passWord = False
            if not any(c.isdigit() for c in passWord):
                print('Your password should contain at least 1 integer. \n')
                passWord = False  
        except NameError as e:
            print(e)
            passWord = False
    writeFunction(userName, passWord)
    mainLogin()
        
 
# mainLogin present login requirements same as newUser, verify with external file
def mainLogin():
    print('''

 ______          __   __          _______  __   __  _______  _______  _______  __   __  _______ 
|    _ |        |  | |  |        |       ||  | |  ||       ||       ||       ||  |_|  ||       |
|   | ||        |  |_|  |        |  _____||  |_|  ||  _____||_     _||    ___||       ||  _____|
|   |_||_       |       |        | |_____ |       || |_____   |   |  |   |___ |       || |_____ 
|    __  | ___  |       | ___    |_____  ||_     _||_____  |  |   |  |    ___||       ||_____  |
|   |  | ||   | |   _   ||   |    _____| |  |   |   _____| |  |   |  |   |___ | ||_|| | _____| |
|___|  |_||___| |__| |__||___|   |_______|  |___|  |_______|  |___|  |_______||_|   |_||_______|''')
    
    loginCheck = False
    while loginCheck == False:
        userName = input("Enter username: As a reminder make sure it is an email that includes @ and .edu")
        passWord = input("Enter password: Make sure it is 6-10 characters long and includes 1 number")
        loginCheck = userCheck(userName, passWord)
        if loginCheck == False:
            print ('Username or password not found.')
    print("Login Accepted")

# userCheck  take input from newUser and mainLogin and verify it with the associated requirements and
# verify username and password in the external file.
def userCheck(userName, passWord):
    try:    
        userFile = open("Usernames-Pass.txt", 'r')
        searchFile = userFile.readlines()
        
        for line in searchFile:
            if userName in line:
                for line in searchfile:
                return True 
               
    except IOError as e:
        print(e)
    except NameError as e:
        print(e)
    
    
def main():
    print('''

 ______          __   __          _______  __   __  _______  _______  _______  __   __  _______ 
|    _ |        |  | |  |        |       ||  | |  ||       ||       ||       ||  |_|  ||       |
|   | ||        |  |_|  |        |  _____||  |_|  ||  _____||_     _||    ___||       ||  _____|
|   |_||_       |       |        | |_____ |       || |_____   |   |  |   |___ |       || |_____ 
|    __  | ___  |       | ___    |_____  ||_     _||_____  |  |   |  |    ___||       ||_____  |
|   |  | ||   | |   _   ||   |    _____| |  |   |   _____| |  |   |  |   |___ | ||_|| | _____| |
|___|  |_||___| |__| |__||___|   |_______|  |___|  |_______|  |___|  |_______||_|   |_||_______|''')
    try:
        menu_choice = int(input("Please select one of the following\n 1)Create a new username or password\n 2)Login\n 3)Exit\n"))
    except ValueError as e:
        print (e)
           
    if menu_choice == 1:
            newUser()
    elif menu_choice == 2:
            mainLogin()
    else:
            sys.exit()
main()     
    
