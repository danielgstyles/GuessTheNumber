# Guess the Number Game V1
# Creator: D Styles

import os

playAgain = "YES"

os. system('clear')

while playAgain == "YES":

    print("Welcome to Guess The Number Game.\n")
    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    os. system('clear')

    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    while numberToGuess != guess:
        print("\n It looks like you did not guess the number correctly. \n")
        guess = int(input("Please enter your next guess: "))

    print("\n")
    print("Congratulations you got it.\n")
    playAgain = input("Do you wish to play again? YES/NO ")
    print("\n")
