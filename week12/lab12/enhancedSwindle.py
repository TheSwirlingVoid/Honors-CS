"""
Description: An enhanced swindle that operates based on a file that saves its books.
Author: Raj Sugavanam
Date: Oct 2021
"""

from os.path import isfile
from book import *

#--------------------------------------------------------------------------------------------------------
def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for book in infile:
        # TODO: read in book info (title, author, year published)
        bookList = book.strip().split(",")
        bookTitle = bookList[0]
        bookAuthor = bookList[1]
        bookYear = int(bookList[2])
        bookFilename = bookList[3]

        # TODO: using the information just obtained from the file, create a
        # Book object with this data and add it to the availableBooks list
        availableBooks.append(Book(bookTitle, bookAuthor, bookYear, bookFilename))
    return availableBooks
#--------------------------------------------------------------------------------------------------------
def getChoice(min, max, prompt):
    """
    Description: Asks the user for a numeric input between two numbers using a specified prompt until
                 they pick a valid number.
    Params: min (int): the lowest number the user can choose
            max (int): the highest number the user can choose
    Returns: (int) the number that the user picked
    """
    
    while True:
        userChoice = input(prompt)
        try:
            num = int(userChoice)
            if num >= min and num <= max:
                return num
            else:
                print("\nInvalid choice!")
        except:
            print("\nPlease enter a numerical value!")
        

class Swindle(object):
    """ class for a single Swindle object """
#--------------------------------------------------------------------------------------------------------
    def __init__(self, owner):
        """ constructor for swindle object, given the owner """
        self.availableBooks = []    # list of Book objects
        self.ownedBooks = []
        self.owner = owner
        self.pageLength = 20 # Initialize all fields normally, except
                             # availableBooks is blank by default.
                             # If the data file exists, fill in
                             # owned books and available books.
                             # If not, leave ownedBooks empty
                             # and fill availableBooks with
                             # everything.
        if isfile("enhancedSwindle_Data.txt"):
            infile = open("enhancedSwindle_Data.txt", "r")
            for line in infile:
                splitLine = line.split(":")
                bookAvailability = splitLine[0]
                # Check if the line being read is a book data line
                if bookAvailability == "AVAILABLE" or bookAvailability == "OWNED":

                    bookData = splitLine[1].split(",")
                    book = Book(bookData[0], bookData[1], bookData[2], bookData[3])
                    book.setBookmark(bookData[4])

                    if bookAvailability == "AVAILABLE":
                        self.availableBooks.append(book)
                    elif bookAvailability == "OWNED":
                        self.ownedBooks.append(book)
        else:
            self.availableBooks = readBookDatabase("bookdb.txt")
#--------------------------------------------------------------------------------------------------------
    def __str__(self):
        """ pretty-print info about this object """
        ###  TO BE COMPLETED BY YOU  ###
        return "Available Books: %s, Owner: %s, Owned Books: %s, Page Length: %i" % (self.availableBooks, self.owner, self.ownedBooks, self.pageLength)
#--------------------------------------------------------------------------------------------------------
    def getAvailableBooks(self):
        """ getter for available books """
        return self.availableBooks
#--------------------------------------------------------------------------------------------------------
    def getOwner(self):
        """ getter for owner """
        return self.owner
#--------------------------------------------------------------------------------------------------------
    def getOwnedBooks(self):
        """ getter for owned books """
        return self.ownedBooks
#--------------------------------------------------------------------------------------------------------
    def getPageLength(self):
        """ getter for page length """
        return self.pageLength
#--------------------------------------------------------------------------------------------------------
    def setOwner(self, newOwner):
        """ setter for owner """
        self.owner = newOwner
#--------------------------------------------------------------------------------------------------------
    def setPageLength(self, newPageLength):
        """ setter for page length """
        self.pageLength = newPageLength
#--------------------------------------------------------------------------------------------------------
    def showOwned(self):
        """ print owned books """
        ownedBooks = self.getOwnedBooks()
        if len(ownedBooks) == 0:
            print("\nYou don't have any books! Purchase a book to read it.")
        else:
            print("\nOwned Books:")
            for i in range(len(ownedBooks)): # display owned books
                print(" %i: %s" % (i+1, ownedBooks[i].toString())) # i+1 so that the number on the
                                                    # right starts at 1
#--------------------------------------------------------------------------------------------------------
    def showAvailable(self):
        """ print available books """
        if len(self.availableBooks) == 0:
            print("\nThere are no available books to buy!")
        else:
            print("\nAvailable Books:")
            for i in range(len(self.availableBooks)): # display available books
                print(" %i: %s" % (i+1, self.availableBooks[i].toString())) # i+1 so that the number on the 
                                                 # right starts at 1
#--------------------------------------------------------------------------------------------------------
    def buy(self):
        """ lets the user buy a book and add it to their owned books """
        self.showAvailable()
        if len(self.availableBooks) != 0: # lack of available books is handled by showAvailale
            intChoice = getChoice(0, len(self.availableBooks), 
                                 "\nWhich book would you like to buy? (0 to skip): ")
            if intChoice == 0: # If the user chose to skip
                return
            removedBook = self.availableBooks.pop(intChoice-1) # -1 to shift the number back to the index format
            self.ownedBooks.append(removedBook)
            print("\nYour purchase of \"%s\" was successful!" % removedBook.getTitle())
#--------------------------------------------------------------------------------------------------------
    def read(self):
        """ lets the user read a book that they own """
        self.showOwned()
        if len(self.ownedBooks) != 0: # If the user has books, ask them which book
                               # they want to read.
            userChoice = getChoice(0, len(self.ownedBooks), 
                                  "\nWhich book would you like to read? (0 to skip): ")
            if userChoice == 0: # if the user chose to skip
                return
            else:
                self.displayText(self.ownedBooks[userChoice-1]) # -1 to shift it back to index format (since choices were ordered 1,2,3,4...)
#--------------------------------------------------------------------------------------------------------
    def getLetter(self):
        """ This method determines what the user wants to do next """
        validChoices = ['n', 'p', 'q']
        while True:
            readingChoice = str(input("\nn (next); p (previous); q (quit): "))
            if readingChoice in validChoices:
                return readingChoice
            print("invalid input, try again")
#--------------------------------------------------------------------------------------------------------
    def displayPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        for i in range(pageStart, pageEnd):
            print(bookLinesList[i])
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, numPages))
        return
#--------------------------------------------------------------------------------------------------------
    def displayText(self, book):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        while True:
            self.displayPage(book)
            currentPage = book.getBookmark()
            choice = self.getLetter()       # user chooses to quit or read the next/previous page
            if choice == "q":               # quit reading and return to ereader
                return book
            elif choice == "n":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:                               # return to previous page in the book
                book.setBookmark(currentPage-1)
        return

#--------------------------------------------------------------------------------------------------------




if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Lionel"
    myswindle = Swindle(owner)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    ################ Write additional tests below ###################
    print("testing buy...")
    myswindle.buy()

    print("testing showOwned...")
    myswindle.showOwned()

    print("testing showAvailable...")
    myswindle.showAvailable()

    print("testing read...")
    myswindle.read()