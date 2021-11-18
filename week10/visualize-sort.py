"""
Author: Raj Sugavanam
Description: A program that visually sorts a list using the selection sort algorithm.
Date: Fall 2021
"""

from random import shuffle
from random import choice


def printSortStatus(L, minValue):
    """
    Prints the sorting status of the selection sort algorithm.
    
    Parameters: L (list<>): the list to print out
                minValue (string/int): the minimum value found by a run through of the sort
    Returns: None
    """
    print("The minimum value in %s is %i" % (L, minValue))
    if minValue == L[0]:
        print("No change")
    else:
        print("Swap %i and %i" % (L[0], minValue))


def printStarList(L):
    """
    Prints each element of the specified list with an amount of stars equal to that element's value.
    
    Parameters: L (list<>): the list to print out
    Returns: None
    """
    for element in L:
        print("%s--%i" % ("*"*element, element))
    print("\n")


def visualizedSelectionSort(L):
    """
    Selection Sorting function that uses functions to visually display the sorting algorithm in the console.
    
    Parameters: L (list<>): the list to sort
    Returns: None
    """
    print("Original list: %s" % L)
    for i in range(len(L)):

        printStarList(L)
        input("Press Enter to continue...\n")

        min_idx = i
        for j in range(i, len(L)):
           if L[j] < L[min_idx]:
                min_idx = j

        
        tmpMin = L[min_idx]
        tmpFirst = L[i]
        printSortStatus(L[i:], tmpMin)
        L[i] = tmpMin
        L[min_idx] = tmpFirst

    print("\nSelection Sort Complete!")
        

def main():

    L = []
    listRange = 100
    listLength = 20

    ints = range(0,listRange)
    for i in range(0,listLength):
        L.append(choice(ints))
    shuffle(L)
    visualizedSelectionSort(L)

main()