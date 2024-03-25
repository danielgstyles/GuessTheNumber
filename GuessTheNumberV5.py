# Guess the Number Game V3
# Creator: D Styles

import os

def pickOS():
    selectedOS = int(input("\nWhat Operating System are you running this game on? \n * Mac OS = 1 \n * Windows = 2 \n"))
    return selectedOS

def clearScreen(WhichOS):
    if WhichOS == "MWindows":
        os. system('cls')
    else:
        os. system('clear')

def CheckGuesses(setNumber):
    
    guesses = []
    
    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    guesses.append(guess)

    print("\n")
    print(guesses)

    while numberToGuess != guess:
    
        if numberToGuess < guess:
            print("\nIt looks like your guess is too high. Tyr a lower number. \n")
        else:
            print("\nIt looks like your guess is too low. Tyr a higher number. \n")
        guess = int(input("Please enter your next guess: "))

        guesses.append(guess)

        print("\n")
        print(guesses)


    print("\n")
    print("Congratulations you got it.\n")
    print("\n")
    name = input("Please enter your name: ")
    print("\n")
    saveFile = open("SaveFile.txt", "a")
    saveFile.write(name +  " guessed " + str(guesses) + "\n")
    #saveFile.write(str(guesses))
    saveFile.close
    return name



playAgain = "YES"


while playAgain == "YES":
    whichOS = pickOS()
    
    clearScreen(whichOS)

    print("Welcome to Guess The Number Game.\n")

    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    clearScreen(whichOS)

    playerName = CheckGuesses(numberToGuess)
    
    playAgain = input("Do you wish to play again? YES/NO ")
    playAgain = playAgain.upper()


print("Thank you for playing " + playerName)
