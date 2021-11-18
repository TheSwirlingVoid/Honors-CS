"""
Description: Provides the structure for a visual GUI-based swindle object.
Author: Raj Sugavanam
Date: Oct 2021
"""

from os.path import isfile
from book import *
from graphics import *
from guiElements import Button
from time import sleep

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
def getChoiceKeyboard(intMin, intMax, promptText, gw):
    """ Lets the user type a response after the Text object of promptText. 
        removes the text after choice is made. This function does not 
        undraw the promptText after it is done. """
    promptTextClone = promptText.getText() # To compare to when a user uses Backspace 
                                           # (which prevents prompt text deletion).
    finalInput = ""
    while True: # Allow user to visually type their name
        userKeyboardInput = gw.checkKey()
        if userKeyboardInput != "Return":
            currentText = promptText.getText() # This is compared to 
                                               # the clone prompt text
                                               # to prevent prompt deletion.
            if userKeyboardInput == "BackSpace":
                # If user pressed backspace
                if currentText != promptTextClone:
                    # ^ Checks if there are chars 
                    # that can be deleted
                    finalInput = finalInput[:-1] # slice a char off the string
                    promptText.setText(promptText.getText()[:-1]) # Update text
            else:
                # If they typed a number, add it to what they are typing
                if userKeyboardInput.isnumeric():
                    finalInput += userKeyboardInput
                    promptText.setText(promptText.getText() + userKeyboardInput) # Update text
        else:
            # If they confirmed their name with enter
            try:
                numInput = int(finalInput)
                if numInput >= intMin and numInput <= intMax:
                    return numInput
            except:
                pass
#--------------------------------------------------------------------------------------------------------    
def getChoiceButton(gw, buttons):
    while True:
        userInput = gw.getMouse() # get user click
        for button in buttons:
            # If the user clicked the currently iterated button
            if button.clickOperation(userInput, 0.5, color_rgb(100,100,100), gw):
                return button.getText() # Return the text for identification
#--------------------------------------------------------------------------------------------------------        
def undrawAll(gw):
    """ undraw everything in gw """
    gw.undrawAll()
#--------------------------------------------------------------------------------------------------------        

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
        return "Available Books: %s, Owner: %s, Owned Books: %s, Page Length: %i" % (self.getAvaliableBooks(), self.getOwner(), self.getOwnedBooks(), self.getPageLength())
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
    def removeAvailableBookAtIndex(self, idx):
        """ remove a book at a specific index, return the removed element """
        return self.availableBooks.pop(idx)
#--------------------------------------------------------------------------------------------------------
    def addOwnedBook(self, book):
        """ add an book to the list of owned books """
        self.ownedBooks.append(book)
#--------------------------------------------------------------------------------------------------------
    def showOwned(self, gw, waitBackButton):
        """ display owned books. set waitBackButton to True if not in the read function. """
        ownedBooks = self.getOwnedBooks()
        if waitBackButton: 
            backButton = Button(50, 100, 1, Point(gw.getWidth()*0.5, gw.getHeight()*0.75), 1, color_rgb(0,0,0), "Back", 15)        
        gwWidthCenter = gw.getWidth()/2
        gwHeight = gw.getHeight()

        if len(ownedBooks) == 0:
            noBooks = Text(Point(gwWidthCenter, gwHeight/2), "You don't have any books!\nPurchase a book to read it.")
            noBooks.setSize(15)
            noBooks.draw(gw)

            if waitBackButton: 
                backButton.setLocation(Point(gw.getWidth()*0.5, gwHeight*0.9))
                backButton.drawButton(False, gw)

        else:

            if waitBackButton: 
                backButton.drawButton(False, gw)

            valueY = 0.1 # increases in a loop to draw rows of books
            ownedBooksText = Text(Point(gwWidthCenter, gwHeight*valueY), "Owned Books:")
            ownedBooksText.setSize(15)
            ownedBooksText.draw(gw)

            for i in range(len(ownedBooks)):
                valueY += 0.05 # change the y value to draw at by a little
                # i+1 so that the number on the right starts at 1
                bookText = Text(Point(gwWidthCenter, gwHeight*valueY),
                    "%i: %s" % (i+1, ownedBooks[i].toString()))
                bookText.setSize(12)
                bookText.draw(gw)
        
        while waitBackButton: # Make the user click the back button to exit the function
                mouse = gw.getMouse()
                if backButton.clickOperation(mouse, 0.5, color_rgb(100,100,100), gw):
                    backButton.undraw()
                    undrawAll(gw)
                    return
#--------------------------------------------------------------------------------------------------------
    def showAvailable(self, gw, waitBackButton):
        """ display available books. set waitBackButton to True if not in the buy function. """

        availableBooks = self.getAvailableBooks()
        if waitBackButton: 
            backButton = Button(50, 100, 1, Point(gw.getWidth()*0.5, gw.getHeight()*0.75), 1, color_rgb(0,0,0), "Back", 15)
        gwWidthCenter = gw.getWidth()/2
        gwHeight = gw.getHeight()

        if len(availableBooks) == 0:
            if waitBackButton:
                noBooks = Text(Point(gw.getWidth()/2, gw.getHeight()/2), "You don't have any books!\nPurchase a book to read it.")
                noBooks.setSize(15)
                noBooks.draw(gw)
                # Offset back button to leave room for text
                backButton.setLocation(Point(gw.getWidth()*0.5, gwHeight*0.9))
                backButton.drawButton(False, gw)
        else:

            if waitBackButton: 
                backButton.drawButton(False, gw)

            valueY = 0.1 # increases in a loop to draw rows of books
            availableBooksText = Text(Point(gw.getWidth()/2, gw.getHeight()*valueY), "Available Books:")
            availableBooksText.setSize(15)
            availableBooksText.draw(gw)
            
            for i in range(len(availableBooks)):
                valueY += 0.05 # change the y value to draw at by a little
                # i+1 so that the number on the right starts at 1
                bookText = Text(Point(gw.getWidth()/2, gw.getHeight()*valueY),
                    "%i: %s" % (i+1, availableBooks[i].toString()))
                bookText.setSize(12)
                bookText.draw(gw)
                

        while waitBackButton: # Make the user click the back button to exit the function
                              # If back button is enabled
            mouse = gw.getMouse()
            if backButton.clickOperation(mouse, 0.5, color_rgb(100,100,100), gw):
                backButton.undraw()
                undrawAll(gw)
                return
#--------------------------------------------------------------------------------------------------------
    def buy(self, gw):
        """ lets the user buy a book and add it to their owned books """
        self.showAvailable(gw, False)
        availableBooks = self.getAvailableBooks()

        if len(availableBooks) != 0:
            userChoiceText = Text(Point(gw.getWidth()*0.5, gw.getHeight()*0.8), "Which book would you like to buy?\n(0 to skip): ")
            userChoiceText.setSize(15)
            userChoiceText.draw(gw)
            intChoice = getChoiceKeyboard(0, len(self.getAvailableBooks()), userChoiceText, gw)
            userChoiceText.undraw()

            if intChoice == 0: # If the user decided to back out, 
                               # stop the function
                undrawAll(gw)
                return

            removedBook = self.removeAvailableBookAtIndex(intChoice-1) # -1 to shift the number back to the index format
            self.addOwnedBook(removedBook)
            undrawAll(gw)

            userChoiceText = Text(Point(gw.getWidth()*0.5, gw.getHeight()*0.5), "\nYour purchase of \"%s\" was successful!" % removedBook.getTitle())
            userChoiceText.setSize(15)
            userChoiceText.draw(gw)
            sleep(3)
        else:
            noBooks = Text(Point(gw.getWidth()*0.5, gw.getHeight()*0.5), "There are no available books\nto buy!")
            noBooks.setSize(15)
            noBooks.draw(gw)

            backButton = Button(50, 100, 1, Point(gw.getWidth()*0.5, gw.getHeight()*0.75), 1, color_rgb(0,0,0), "Back", 15)
            backButton.drawButton(False, gw)
            while True: # Make the user click the back button to exit the function
                        # If they cannot buy books
                mouse = gw.getMouse()
                if backButton.clickOperation(mouse, 0.5, color_rgb(100,100,100), gw):
                    backButton.undraw()
                    undrawAll(gw)
                    return
        undrawAll(gw)
#--------------------------------------------------------------------------------------------------------
    def read(self, gw):
        """ lets the user read a book that they own """
        self.showOwned(gw, False)
        ownedBooks = self.getOwnedBooks()
        numOwnedBooks = len(ownedBooks)

        if numOwnedBooks != 0:
            userChoiceText = Text(Point(gw.getWidth()*0.5, gw.getHeight()*0.8), "Which book would you like to read?\n(0 to skip): ")
            userChoiceText.setSize(15)
            userChoiceText.draw(gw) 
            intChoice = getChoiceKeyboard(0, numOwnedBooks, userChoiceText, gw)
            userChoiceText.undraw()

            if intChoice == 0: # If the user decided to back out,
                               # stop the function
                undrawAll(gw)
                return
            else:
                self.displayText(ownedBooks[intChoice-1], gw) # -1 to shift it back to index format (since choices were ordered 1,2,3,4...)
        undrawAll(gw)
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
    def displayPage(self, book, gw):
        """ This method displays a single page at a time (300 chars) """
        gwWidth = gw.getWidth()

        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        valueY = 0.1 # controls y value where lines are drawn
        for i in range(pageStart, pageEnd):
            lineTxt = Text(Point(gwWidth/2, gw.getHeight()*valueY), bookLinesList[i]) # display text with Text objects
            lineTxt.setSize(10)
            lineTxt.draw(gw)
            valueY += 0.05
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        showingPageText = Text(Point(gwWidth/2, gw.getHeight()*0.825), "Showing page %d out of %d" % (page, numPages))
        showingPageText.setSize(15)
        showingPageText.draw(gw)
        return

#--------------------------------------------------------------------------------------------------------
    def displayText(self, book, gw):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        graphWinWidth = gw.getWidth()
        graphWinHeight = gw.getHeight()
        pgForwardButton = Button(50,50,1,Point(graphWinWidth*0.8, graphWinHeight*0.9), 1, color_rgb(0,0,0), ">>", 20)
        pgBackButton = Button(50,50,1,Point(graphWinWidth*0.2, graphWinHeight*0.9), 1, color_rgb(0,0,0), "<<", 20)
        quitButton = Button(50,100,1,Point(graphWinWidth*0.5, graphWinHeight*0.9), 1, color_rgb(0,0,0), "Back", 15)
        
        while True:
            undrawAll(gw)
            self.setPageLength(15)
            self.displayPage(book, gw)
            pgForwardButton.drawButton(False, gw)
            pgBackButton.drawButton(False, gw)
            quitButton.drawButton(False, gw)

            

            currentPage = book.getBookmark()
            # user chooses to quit or read the next/previous page
            userChoice = getChoiceButton(gw, [pgForwardButton,pgBackButton,quitButton])
            if userChoice == "Back":               # quit reading and return to ereader
                undrawAll(gw)
                pgForwardButton.undraw()
                pgBackButton.undraw()
                return book
            elif userChoice == ">>":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    endPagesText = Text(Point(graphWinWidth/2, graphWinHeight*0.8), "There are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
                    endPagesText.setSize(15)
                    endPagesText.draw(gw)
            else:                               # return to previous page in the book
                if currentPage > 0:
                    book.setBookmark(currentPage-1)

            pgForwardButton.undraw()
            pgBackButton.undraw()
            quitButton.undraw()
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