"""
Description: Allows the user to interact with their swindle using UI elements.
Author: Raj Sugavanam
Date: Oct 2021
"""

from guiSwindle import *
from os.path import isfile
from time import sleep
from guiElements import Button
from graphics import *

def newUser(gw):
    
    introText = Text(Point(gw.getWidth()/2, gw.getHeight()*0.4),
        "Since this is the first time you used it, \nlet's customize your Swindle...")
    introText.setSize(15)
    introText.draw(gw)

    namePrompt = "Please enter your name: "
    nameText = Text(Point(gw.getWidth()/2, gw.getHeight()*0.5), namePrompt)
    nameText.setSize(15)
    nameText.draw(gw)

    ownerString = ""
    while True: # Allow user to visually type their name
        userKeyboardInput = gw.checkKey()
        if userKeyboardInput != "Return":

            currentText = nameText.getText()
            if userKeyboardInput == "BackSpace":
                # If user pressed backspace
                if currentText != namePrompt:
                    # ^ Checks if there are chars 
                    # that can be deleted
                    ownerString = ownerString[:-1] # slice a char off the string
                    nameText.setText(nameText.getText()[:-1]) # Update text
            else:
                # If they didn't delete a letter
                if userKeyboardInput[:6] == "Shift_":
                    # 7: because it could be SHIFT_L or SHIFT_R
                    userKeyboardInput = userKeyboardInput[7:].upper()
                ownerString += userKeyboardInput
                nameText.setText(nameText.getText() + userKeyboardInput) # Update text
        else:
            # If they confirmed their name with enter
            nameText.undraw()
            introText.undraw()
            welcomeText = Text(Point(gw.getWidth()/2, gw.getHeight()*0.5), "Welcome to %s's Swindle v1.0!" % ownerString)
            welcomeText.setSize(15)
            welcomeText.draw(gw)
            sleep(3) # Intended delay so graphics aren't instantaneous
            welcomeText.undraw()
            break
    return ownerString
    # print("\nSince this is the first time you used it,")
    # print("let's customize your Swindle...")
    # owner = str(input("\nPlease enter your name: "))

def mainMenu(gw):

    buyButton = Button(50, 100, 1, Point(gw.getWidth()/2, gw.getHeight()*0.2), 1, color_rgb(0,0,0), "Buy a Book", 10)
    showOwnedButton = Button(50, 100, 1, Point(gw.getWidth()/2, gw.getHeight()*0.4), 1, color_rgb(0,0,0), "Show Owned Books", 8)
    readButton = Button(50, 100, 1, Point(gw.getWidth()/2, gw.getHeight()*0.6), 1, color_rgb(0,0,0), "Read a Book", 10)
    exitButton = Button(50, 100, 1, Point(gw.getWidth()/2, gw.getHeight()*0.8), 1, color_rgb(0,0,0), "Exit", 15)

    buttons = []

    buyButton.drawButton(False, gw)
    showOwnedButton.drawButton(False, gw)
    readButton.drawButton(False, gw)
    exitButton.drawButton(False, gw)

    buttons.append(buyButton)    
    buttons.append(showOwnedButton)
    buttons.append(readButton)
    buttons.append(exitButton)    

    userChoice = 0
    while True:
        userInput = gw.getMouse()
        userChoice = 0
        if buyButton.clickOperation(userInput, 0.5, color_rgb(100,100,100), gw):
            userChoice = 1
        elif showOwnedButton.clickOperation(userInput, 0.5, color_rgb(100,100,100), gw):
            userChoice = 2
        elif readButton.clickOperation(userInput, 0.5, color_rgb(100,100,100), gw):
            userChoice = 3
        elif exitButton.clickOperation(userInput, 0.5, color_rgb(100,100,100), gw):
            userChoice = 4

        if userChoice != 0:
            for button in buttons:
                button.undraw()

            return userChoice

def saveData(swindle):
    """ saves the data upon exit. Name is contained in the first line, 
        then rows available books, then rows of owned books."""
    outfile = open("enhancedSwindle_Data.txt", "w")

    outfile.write("%s\n" % swindle.getOwner())
    for book in swindle.getAvailableBooks():
        outfile.write("AVAILABLE:%s,%s,%i,%s,%i\n" % (book.getTitle(), book.getAuthor(), int(book.getYear()), book.getFilename(), book.getBookmark()))
    for book in swindle.getOwnedBooks():
        outfile.write("OWNED:%s,%s,%i,%s,%i\n" % (book.getTitle(), book.getAuthor(), int(book.getYear()), book.getFilename(), book.getBookmark()))
    

def startSwindle(gw):
    """ reads the user's name from a file if it exists,
        or asks them to set up their swindle with their name """
    userName = ""
    if isfile("enhancedSwindle_Data.txt"):
        infile = open("enhancedSwindle_Data.txt", "r")
        userName = infile.readline().strip()
        welcomeMessage = Text(Point(gw.getWidth()/2, gw.getHeight()*0.5), "Welcome back, %s!" % userName)
        welcomeMessage.setSize(15)
        welcomeMessage.draw(gw)
        sleep(3)
        welcomeMessage.undraw()
    else:
        userName = newUser(gw) # Display instructions and get user's name
                               # Create a new Swindle ereader for them
    return Swindle(userName)

def undrawAll(gw):
    """ undraw everything in gw """
    gw.undrawAll()

def main():

    gw = GraphWin("Swindle", 600, 750)
    userSwindle = startSwindle(gw)

    while True:
        menuChoice = mainMenu(gw)         # Display ereader's main menu
        undrawAll(gw) # clear previous UI
        if menuChoice == 1:
            userSwindle.buy(gw)           # View available books with option to buy
        elif menuChoice == 2:
            userSwindle.showOwned(gw, True)     # View owned books
        elif menuChoice == 3:
            userSwindle.read(gw)          # Choose a book to read
        else:
            saveData(userSwindle)
            break                       # Turn off ereader (quit the program)


main()
