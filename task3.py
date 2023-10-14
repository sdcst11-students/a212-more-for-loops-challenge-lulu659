#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

x = input("Enter username: ")
y = input("Enter password: ")
if x in users:
    for i in range(len(users)):
        if x == users[i]:
            if passwords[i] == y:
                print("Username and password match")
            else:
                print("Try again")
else:
    print("Try again")