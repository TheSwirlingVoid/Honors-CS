"""
Description: A basic book object storing basic info about the book
             and the text of the book.
Author: Raj Sugavanam
Date: October 2021
"""


class Book(object):
    """ class for a single Book object """
#--------------------------------------------------------------------------------------------------------
    def __init__(self, title, author, year, filename):
        """ constructor for book object, given title, author, year, and directory/filename """
        self.title = title
        self.author = author
        self.year = int(year)
        self.filename = filename
        self.bookmark = 0
#--------------------------------------------------------------------------------------------------------
    def __str__(self):
        """ pretty-print info about this object """
        s = "Title: %s, Author: %s, Year: %i, " % (self.title, self.author, self.year)
        s += "Filename: %s, Bookmark: %i" % (self.filename, self.bookmark)
        return s
#--------------------------------------------------------------------------------------------------------
    def getTitle(self):
        return self.title
#--------------------------------------------------------------------------------------------------------
    def getAuthor(self):
        return self.author
#--------------------------------------------------------------------------------------------------------
    def getYear(self):
        return int(self.year)
#--------------------------------------------------------------------------------------------------------
    def getFilename(self):
        return self.filename
#--------------------------------------------------------------------------------------------------------
    def getBookmark(self):
        return int(self.bookmark)
#--------------------------------------------------------------------------------------------------------
    def setTitle(self, newTitle):
        self.title = newTitle
#--------------------------------------------------------------------------------------------------------
    def setAuthor(self, newAuthor):
        self.author = newAuthor
#--------------------------------------------------------------------------------------------------------
    def setYear(self, newYear):
        self.year = int(newYear)
#--------------------------------------------------------------------------------------------------------
    def setFilename(self, newFilename):
        self.filename = newFilename
#--------------------------------------------------------------------------------------------------------
    def setBookmark(self, newBookmark):
        self.bookmark = int(newBookmark)
#--------------------------------------------------------------------------------------------------------
    def toString(self):
        """ class info in text format """
        return "%25s by %20s (%i)" % (self.getTitle(), self.getAuthor(), self.getYear())
#--------------------------------------------------------------------------------------------------------
    def getText(self):
        """retrieve the entire contents of the book as a single string"""
        infile = open(self.filename, "r", encoding='UTF-8')
        bookContents = ""
        for line in infile:
            line = line.strip()
            if line[:1] != "#": #:1 so that index out of range does not occur
                bookContents += line + "\n"
        return bookContents
#--------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    print("Testing the Book class...")
    myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
    "book-database/gettysburg.txt")

    print("Testing toString...")
    print(myBook.toString())

    print("Testing getFilename...")
    print(myBook.getFilename())

    print("Testing getText...")
    text = myBook.getText()
    print(text)                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())

    ################ Write additional tests below ###################

    aliceBook = Book("Incorrect Title", "Not the Author", 1600, "book-database/gettysburg.txt")
    print(aliceBook) # test for __str__

    aliceBook.setTitle("Alice in Wonderland")
    aliceBook.setAuthor("Lewis Carrol")
    aliceBook.setYear(1865)
    aliceBook.setFilename("book-database/alice.txt")
    print(aliceBook.toString())

    print("Default Bookmark:", aliceBook.getBookmark())
    print(aliceBook.getText()[:500])
    aliceBook.setBookmark(2)
    print("New Boomark:", aliceBook.getBookmark(), "\n")

    testBook = Book("Test Book", "Raj Sugavanam", 2021, "book-database/testText.txt")
    print(testBook.getText()[:20])