# Guess the number from 1 to 10
import random

secret = random.randint(1, 10)
print("Hi, let's play \"Guess the number\"")
playerWon = False   # This boolean is known as a "flag"
while playerWon is False:
    guess = int(input("Enter a number between 1 and 10!"))
    if guess == secret:
        playerWon = True
        print("Congrats! ", secret)
    else:
        print("Nope. Try again!")
