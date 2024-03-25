# Guess the Number Game V4
# Creator: D Styles

import os  #This is a extra library that adds extra functions to Python. This will be used to clear the terminal screen when needed

def CheckGuesses(setNumber):
    
    guesses = []  #creates a blank list that will be used to keep track of all the guesses made by the player
    
    print("\n")
    guess = int(input("Player Two. Please enter your guess: "))

    guesses.append(guess)

    print("\n")
    print(guesses) #debugging output statement to check that the list is being updated with the players guessed values

    while setNumber != guess: #This loop will continue while ever the play guesses incorrectly
    
        if setNumber < guess:
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
    
    
    #The below three lines saves the players name and their guesses to an external file
    saveFile = open("SaveFile.txt", "a")
    saveFile.write(name +  " guessed " + str(guesses) + "\n")
    saveFile.close
    
    return name #Sends the value from the name variable back to the main program.



playAgain = "YES"

while playAgain == "YES" or playAgain == "Y":

    os. system('clear') #Clears the Terminal screen on a Mac

    print("Welcome to Guess The Number Game.\n")
    numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))

    os. system('clear') #Clears the Terminal screen on a Mac

    playerName = CheckGuesses(numberToGuess)
    
    playAgain = input("Do you wish to play again? YES/NO ")
    playAgain = playAgain.upper()

print("\n")
print("Thank you for playing " + playerName)
