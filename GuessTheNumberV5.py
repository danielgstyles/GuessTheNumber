# Guess the Number Game V5
# Creator: D Styles

import os #This is a extra library that adds extra functions to Python. This will be used to clear the terminal screen when needed

def pickOS():
    selectedOS = int(input("\n\nWhat Operating System are you running this game on? \n * Mac OS = 1 \n * Windows = 2 \n   "))
    return selectedOS

def clearScreen(WhichOS): #This function will select the correct clear screen command depending of the OS selcted
    if WhichOS == "Windows":
        os. system('cls')
    else:
        os. system('clear')

def CheckGuesses(setNumber):
    
    guesses = [] #creates a blank list that will be used to keep track of all the guesses made by the player
    
    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    guesses.append(guess)

    print("\n")
    print(guesses) #debugging output statement to check that the list is being updated with the players guessed values

    while numberToGuess != guess: #This loop will continue while ever the play guesses incorrectly
    
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
    whichOS = pickOS() #fills whichOS with the returned value from the pickOS function
    
    clearScreen(whichOS) #calls the clearScreen function passing the value held in the whichOS variable
    
    print("Welcome to Guess The Number Game.\n")

    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    clearScreen(whichOS)

    playerName = CheckGuesses(numberToGuess)
    
    playAgain = input("Do you wish to play again? YES/NO ")
    playAgain = playAgain.upper()


print("Thank you for playing " + playerName)
