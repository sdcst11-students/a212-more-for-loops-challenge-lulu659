#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

for i in range(3):
    x = input("Enter user name: ")
    guessesleft = 3
    if x == expectedUsername:
        y = input("Enter password: ")
        guessesleft = 3
        if y == expectedPassword:
            print("Access granted")
            exit()
else:
    print("Access denied")