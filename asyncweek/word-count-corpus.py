from string import punctuation


def insertionSortCounts(wordScores):
	""" insertion sort a list of list with format [string, int]. """
	for i in range(1, len(wordScores)):
		for indexOffset in range(i):   # checks backwards from original position
			newIndex = i-indexOffset            # shifts the original index left
            # check alphabetical order
			if wordScores[newIndex][0] < wordScores[newIndex-1][0]:

				firstVal = wordScores[newIndex-1]    # copy previous and current
				secondVal = wordScores[newIndex]

				wordScores[newIndex] = firstVal
				wordScores[newIndex-1] = secondVal

			else:
				break

def changeOccurences(occurences, word):
    """ increment the occurence count of a word in a nested list structured
        [string, integer]. """
    for element in occurences:                   # append to occurence if exists
        if element[0] == word:
            element[1]+=1
            return
    occurences.append([word, 1])         # if occurence doesn't exist, create it

def getWordCounts(wordList):
    """ count the occurences of each word in a list and return it as a
        nested list. """
    wordCounts = []
    for word in wordList:
        changeOccurences(wordCounts, word)
    return wordCounts

def getWords(filename):
    """ get a list of all words from a file. Duplicates allowed,
        case insensitive, no punctuation. """
    infile = open(filename, 'r')
    words = []
    for line in infile:
        lineWords = line.strip().split()
        for word in lineWords:
            for i in range(len(punctuation)):            # strip all punctuation
                puncMark = punctuation[i]
                word = word.strip(puncMark)
            if word.isalpha():       # check if alpha after removing punctuation
                words.append(word.lower())                 # add processed words
    infile.close()
    return words

def saveCounts(wordCounts, filename):
    """ save word counts to a file """
    outfile = open(filename, "w")
    for occurence in wordCounts:                      # write occurences to file
        outfile.write("%s,%i\n" % (occurence[0], occurence[1]))
    outfile.close()

def updateWordCounts(addendfilename, sumfilename):
    """ update the the sum file's counts by adding the addend's counts to it. """
    newPairs = []                           # accumulates updated wordCount file
    outfile = open(sumfilename, "r+")
    infile = open(addendfilename, "r")
    currentLine = outfile.readline().strip()                    # initial values
    currentPair = currentLine.split(",")
    for line in infile:
        mobyPair = line.strip().split(",")
        while currentPair[0] < mobyPair[0]:     # if alphabetical pos not passed
            currentLine = outfile.readline().strip()          # update line read
            if currentLine == "":
                outfile.close()
                infile.close()
                return
            currentPair = currentLine.split(",")
        # will be at appropriate position to write or overwrite
        print("%s--%s" %(mobyPair[0], currentPair[0]))
        if mobyPair[0] != currentPair[0]:               # if entry doesn't exist
            newPairs.append("%s,%s\n" % (mobyPair[0], mobyPair[1]))
        else:                                            # else replace existing
            newPairs.append("%s,%s\n" % 
                       (currentPair[0], int(mobyPair[1]) + int(currentPair[1])))

        
    outfile.close()
    outfile = open(sumfilename, "w")         # write saved updated file from mem
    for line in newPairs:
        outfile.write(line)
    infile.close()

def main():

    bookWords = getWords("moby_dick.txt")
    wordCounts = getWordCounts(bookWords)
    insertionSortCounts(wordCounts)
    saveCounts(wordCounts, "word-count-moby.txt")
    updateWordCounts("word-count-moby.txt", "wordCounts.txt")

main()