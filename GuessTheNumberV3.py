# Guess the Number Game V3
# Creator: D Styles

import os

playAgain = "YES"

def CheckGuesses(setNumber):
    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    while setNumber != guess:
        if setNumber < guess:
            print("\nIt looks like your guess is too high. Tyr a lower number. \n")
        else:
            print("\nIt looks like your guess is too low. Tyr a higher number. \n")
        guess = int(input("Please enter your next guess: "))

    print("\n")
    print("Congratulations you got it.\n")
    


while playAgain == "YES":

    os. system('clear')

    print("Welcome to Guess The Number Game.\n")
    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    os. system('clear')

    CheckGuesses(numberToGuess)

    playAgain = input("Do you wish to play again? YES/NO ") 
