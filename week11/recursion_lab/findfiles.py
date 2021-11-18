"""
Author: Raj Sugavanam
Description: Finds files containing a certain pattern in the specified directory and its subdirectories.
Date: September 2021
"""
from os import listdir
from os.path import isdir, expanduser

def patternSearch(pattern, string):
    """ search for a substring in a string """
    strlen = len(string)
    for i in range(0, strlen):                        # for every char in string
        if string[i:i + len(pattern)] == pattern:  # if pattern at char position
            return True                                              # return it
    return False                                       # if not found, return -1

def searchRecursive(dir, pattern):
    """ recursively search a directory for a pattern """
    pathsFound = []                                     # list of matching paths
    try:
        itemList = listdir(dir)
    except PermissionError:
        print("Attempted to check folder %s--access was denied." % dir)
        return pathsFound
    for item in itemList:
        itemPath = "%s/%s" % (dir, item)      # directory path for every subfile
        if isdir(itemPath):                          # add matching subdir files
            pathsFound = pathsFound + searchRecursive(itemPath,pattern)
        elif patternSearch(pattern, item):             # if name matches pattern
            pathsFound.append(itemPath)               # add it to matching paths
    return pathsFound

def getValidDirectory():
    """ makes the user enter a valid directory """
    while True:                                            # Constantly ask user
        userDirectory = input("Directory: ")
        if userDirectory[:2] == "~/":
            userDirectory = expanduser(userDirectory)
        if isdir(userDirectory[2:]):                      # if valid, return dir
            return userDirectory
        else:
            print("Please enter a valid directory.")

def main():
    directory = getValidDirectory()
    pattern = input("Pattern: ")
    foundDirs = searchRecursive(directory,pattern)
    print("")
    for dir in foundDirs:
        print(dir)


main()