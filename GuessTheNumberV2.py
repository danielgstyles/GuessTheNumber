# Guess the Number Game V2
# Creator: D Styles

import os

playAgain = "YES"

while playAgain == "YES":

    os. system('clear')

    print("Welcome to Guess The Number Game.\n")
    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    os. system('clear')

    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    while numberToGuess != guess:
        if numberToGuess < guess:
            print("\nIt looks like your guess is too high. Tyr a lower number. \n")
        else:
            print("\nIt looks like your guess is too low. Tyr a higher number. \n")
        guess = int(input("Please enter your next guess: "))


    print("\n")
    print("Congratulations you got it.\n")
    playAgain = input("Do you wish to play again? YES/NO ")
    print("\n")
