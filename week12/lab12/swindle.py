"""
Description: Provides the structure for a swindle object.
Author: Raj Sugavanam
Date: Oct 2021
"""


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
    """ lets the user pick a number between a specific min and max. the promptText is displayed/asked to the user. """
    
    while True:
        userChoice = input(prompt)
        try: # incase their input cannot be converted to an integer
            num = int(userChoice)
            # if the number is between or at the min and max
            if min <= num <= max:
                return num
            else:
                print("\nEnter a number between %i and %i!" % (min, max))
        except:
            print("\nPlease enter a numerical value!")
        

class Swindle(object):
    """ class for a single Swindle object """
#--------------------------------------------------------------------------------------------------------
    def __init__(self, owner):
        """ constructor for swindle object, given ________________________ """
        self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
        ###  DATA FIELDS TO BE COMPLETED BY YOU  ###
        self.owner = owner
        self.ownedBooks = []
        self.pageLength = 20
#--------------------------------------------------------------------------------------------------------
    def __str__(self):
        """ pretty-print info about this object """
        return "Available Books: %s, Owner: %s, Owned Books: %s, Page Length: %i" % (self.availableBooks, self.owner, self.ownedBooks, self.pageLength)
#--------------------------------------------------------------------------------------------------------
    def getAvaliableBooks(self):
        return self.availableBooks
#--------------------------------------------------------------------------------------------------------
    def getOwner(self):
        return self.owner
#--------------------------------------------------------------------------------------------------------
    def getOwnedBooks(self):
        return self.ownedBooks
#--------------------------------------------------------------------------------------------------------
    def getPageLength(self):
        return self.pageLength
#--------------------------------------------------------------------------------------------------------
    def setOwner(self, newOwner):
        self.owner = newOwner
#--------------------------------------------------------------------------------------------------------
    def setPageLength(self, newPageLength):
        self.pageLength = newPageLength
#--------------------------------------------------------------------------------------------------------
    def showOwned(self):
        """ print owned books """
        if len(self.ownedBooks) == 0:                   # If there are no owned books
            print("\nYou don't have any books! Purchase a book to read it.")
        else:
            print("\nOwned Books:")
            for i in range(1, len(self.ownedBooks)+1):  # display owned books
                print(" %i: %s" % (i, self.ownedBooks[i-1].toString()))
#--------------------------------------------------------------------------------------------------------
    def showAvailable(self):
        """ print available books """
        if len(self.availableBooks) == 0:      # If there are no available books
            print("\nThere are no available books to buy!")
        else:
            print("\nAvailable Books:")        # display available books
            for i in range(1, len(self.availableBooks)+1): 
                print(" %i: %s" % (i, self.availableBooks[i-1].toString()))
#--------------------------------------------------------------------------------------------------------
    def buy(self):
        """ lets the user buy a book and transfer it from available to owned books """
        self.showAvailable()
        if len(self.availableBooks) != 0:
            intChoice = getChoice(0, len(self.availableBooks), 
                                "\nWhich book would you like to buy? (0 to skip): ")
            if intChoice != 0:                         # if the user didn't skip
                book = self.availableBooks.pop(intChoice-1)
                self.ownedBooks.append(book)
                print("\nYour purchase of %s was successful!" % book.getTitle())
#--------------------------------------------------------------------------------------------------------
    def read(self):
        """ lets the user read a book that they own """
        self.showOwned()

        if len(self.ownedBooks) != 0: # If the user has books, ask them which book
                               # they want to read.
            userChoice = getChoice(0, len(self.ownedBooks), 
                                  "\nWhich book would you like to read? (0 to skip): ")
            if userChoice != 0: # if the user chose to skip
                self.displayText(self.ownedBooks[userChoice-1]) # -1 to 
                                                           # shift it back to index format 
                                                           # (since choices were ordered 1,2,3,4...)
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