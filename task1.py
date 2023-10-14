#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
n = random.randint(1, 100)
guessesleft = 10
x=0
while n != x and guessesleft > 0:
    x = int(input("Enter an integer from 1 to 100: "))
    if x > n:
        print("Too high")
    if x < n:
        print("Too low")
    if x == n:
        print("correct")
        break
    guessesleft -= 1
else:
    print("YOU LOST")