"""
Description: An enhanced ereader that saves data for the enhanced swindle to read.
Author: Raj Sugavanam
Date: Oct 2021
"""

from enhancedSwindle import *
from os.path import isfile

def newUser():
    print("\nSince this is the first time you used it,")
    print("let's customize your Swindle...")
    owner = str(input("\nPlease enter your name: "))
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    return owner

def mainMenu():
    print("\n--------------------------------------------------\n")
    print("1) Buy/See available books\n2) See owned books\n3) Read a book\n4) Exit\n")
    while True:
        userInput = str(input("---> "))
        try:
            menuChoice = int(userInput)
            if 1 <= menuChoice <= 4:
                return menuChoice
            else:
                print("invalid number, try again")
        except ValueError:
            print("invalid input, try again")

def saveData(swindle):
    """ saves the data upon exit. Name is contained in the first line, 
        then rows available books, then rows of owned books."""
    outfile = open("enhancedSwindle_Data.txt", "w")

    outfile.write("%s\n" % swindle.getOwner())
    for book in swindle.getAvailableBooks():
        outfile.write("AVAILABLE:%s,%s,%i,%s,%i\n" % (book.getTitle(), book.getAuthor(), int(book.getYear()), book.getFilename(), book.getBookmark()))
    for book in swindle.getOwnedBooks():
        outfile.write("OWNED:%s,%s,%i,%s,%i\n" % (book.getTitle(), book.getAuthor(), int(book.getYear()), book.getFilename(), book.getBookmark()))
    

def startSwindle():
    """ reads the user's name from a file if it exists,
        or asks them to set up their swindle with their name """
    userName = ""
    if isfile("enhancedSwindle_Data.txt"):
        infile = open("enhancedSwindle_Data.txt", "r")
        userName = infile.readline().strip()
        print("Welcome back, %s!" % userName)
    else:
        userName = newUser() # Display instructions and get user's name
                             # Create a new Swindle ereader for them
    return Swindle(userName)

def main():

    userSwindle = startSwindle()

    while True:
        menuChoice = mainMenu()         # Display ereader's main menu
        if menuChoice == 1:
            userSwindle.buy()           # View available books with option to buy
        elif menuChoice == 2:
            userSwindle.showOwned()     # View owned books
        elif menuChoice == 3:
            userSwindle.read()          # Choose a book to read
        else:
            saveData(userSwindle)
            break                       # Turn off ereader (quit the program)


main()
