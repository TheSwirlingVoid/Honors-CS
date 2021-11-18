"""
Author: Raj Sugavanam
Description: Creates a silly-text version of a specified string, repeating each letter of that string a specified amount of times.
Date: September 2021
"""

def repeatChars(string, n):
    """ repeat all chars in a string n times """
    firstElement = string[0]                                    # get first char
    if len(string) <= 1:                      # base case: strlen is 1 character
        return firstElement*n                      # first char repeated n times
    else:                                       # first char*n w/ recurse result
        return firstElement*n + repeatChars(string[1:], n)

def getPositiveInteger(prompt):
    """ gets a positive integer from the user """
    while True:
        userInput = input(prompt).strip()
        try:
            integerUserInput = int(userInput)        # convert user input to int
            if integerUserInput < 0:                           # validate it >=0
                print("Please enter a number greater than or equal to 0.")
            else:
                return integerUserInput
        except ValueError:                           # if user entered a non-int
            print("Please enter a valid integer.")



def main():
    string = input("string: ")                                 # get user string
    num = getPositiveInteger("num: ")                          # get user number
    repeatedString = repeatChars(string,num)
    print(repeatedString)                                         # print result

main()
