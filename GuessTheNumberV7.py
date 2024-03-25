# Guess the Number Game V6
# Creator: D Styles

import os #This is a extra library that adds extra functions to Python. This will be used to clear the terminal screen when needed
import random
import time

# def pickOS(): # Function no longer required as the os.name function identifies the OS
#     selectedOS = int(input("\n\nWhat Operating System are you running this game on? \n * Mac OS = 1 \n * Windows = 2 \n   "))
#     return selectedOS



def clearScreen(): #This function will select the correct clear screen command depending of the OS selcted
    if os.name == "posix":
        os. system('clear')
    else:
        os. system('cls')



def randomNumber():
    difficulty = int(input("Easy = 1, Medium = 2, Hard = 3, Extra Hard = 4"))
    if difficulty == 1:
        ranNum = random.randint(0,10)
    elif difficulty == 2:
        ranNum = random.randint(0,50)
    elif difficulty == 3:
        ranNum = random.randint(0,100)
    elif difficulty == 4:
        ranNum = random.randint(0,250)
    else:
        print("\n Incorrect choise. Please try again.")
        time.sleep(1)
        randomNumber()

    return ranNum




def CheckGuesses(setNumber): # This function checks the Player 2 guesses against the number set by Player 1
    
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



# Main Program below.

playAgain = "YES"


while playAgain == "YES" or playAgain == "Y": # added or "Y" just in case people did not enter the full YES
    #print(os.name) #output statement to identify the value returned by os.name
    
    #whichOS = pickOS() #fills whichOS with the returned value from the pickOS function
    #whichOS no longer needed as os.name can identify the OS and then the correct clear screen command can be used
    
    clearScreen() #calls the clearScreen function. This no longer needs the whichOS passed as the os.name is being used to automatically identify the OS fo the computer.
    
    print("Welcome to Guess The Number Game.\n")

    print("Would you like to play 1 Player of 2 Player?")
    print("1 Player = 1 \n2 player = 2\n")
    numberOfPlayers = int(input())
    if numberOfPlayers == 2:
        numberToGuess = int(input("Player 1 please set a number between 1 and 100 for PLayer 2 to guess. "))
    else:
        numberToGuess = randomNumber()
        
    clearScreen()
    
    print(numberToGuess) # debugging output statement.

    playerName = CheckGuesses(numberToGuess)
    
    playAgain = input("Do you wish to play again? YES/NO ")
    playAgain = playAgain.upper() # Changes the players input to be all uppercase to ensure a consistant data entery format to test against



print("Thank you for playing " + playerName)
