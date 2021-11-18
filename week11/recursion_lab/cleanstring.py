"""
Author: Raj Sugavanam
Description: Allows a user to enter a string an remove all of a certain char from it.
Date: September 2021
"""

def removeChar(string, char):
    """ remove occurences of char in string """
    if len(string) == 0:
        return ""
    else:
        if string[0] != char:                   # leave char if no match
            return string[0] + removeChar(string[1:], char)
        else:                                   # remove char if match
            return removeChar(string[1:], char)

def validateSingleChar():
    """ make the user enter a single character """
    while True:
        userInput = input("char: ")
        if len(userInput) == 1:
            return userInput
        else:
            print("Please enter a single character.")

def main():
    string = input("string: ")
    char = validateSingleChar()
    print(removeChar(string, char))

main()