# This function is to test the writing functions for the project for troubleshooting

def main():
    userName = ('username')
    passWord = ('password')
    with open('Usernames-Pass.txt', 'a') as userFile:
        userFile.write(userName)
        userFile.write(passWord)

    userFile.close()
main()