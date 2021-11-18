"""
Author: Raj Sugavanam
Description: This program takes movie reviews, extracting all unique words from all the reviews to find the words with the most and least positive reviews associated with it.
Date: Fall 2021
"""

def binarySearch(L, element):
	"""
	Performs a binary search for a specified element in a specified list.

	Params: L (list<>): the list to search through
			element (string/int): the element/value to look for

	Returns: True if element is found, False if not
	"""
	low = 0
	high = len(L)-1

	while low <= high:
		mid = (high+low)//2

		middleElement = L[mid]
		if middleElement == element:
			return True
		elif element < middleElement:
			high = mid-1
		else:
			low = mid+1
	return False

#---------------------------------------------------------------------------------#
def insertionSortScores(wordScores):
	"""
	Takes the wordScore list, and performs an insertion sort based on the ratings.

	Params: wordScores (list<list<int, string>): the file to read the sentiment scores and words from

	Returns: None
	"""
	listWordScores = []
	for word,score in wordScores.items():
		listWordScores.append([word,score])

	for i in range(1, len(listWordScores)):
		offsetIndex = i
		for numCheck in range(i):
			newIndex = i-numCheck
			if listWordScores[newIndex][1] < listWordScores[newIndex-1][1]: # check elements


				firstVal = listWordScores[newIndex-1] # make clone of last and next
				secondVal = listWordScores[newIndex]  # sublists

				listWordScores[newIndex] = firstVal   # swap sublists
				listWordScores[newIndex-1] = secondVal

			else:
				break

	return listWordScores
#---------------------------------------------------------------------------------#
def scoreWord(sentimentRating, desiredWord, wordScores):
	"""
	Creates or adds on to the sentiment score word list with the word and rating associated with it specified.

	Params: sentimentRating (int): a number 0-4 that was associated with the review the word was in
			desiredWord (string): the word to score
			wordScores (list<list<int, string>>): the list of current word score entries
			stopWords (list<string>): the list of words to ignore
	Returns: None
	"""
	numAddRate = int(sentimentRating)-2
	for word in wordScores.keys():
		if word == desiredWord:
			wordScores[word] += numAddRate # change rating/create rating
			return
	wordScores[desiredWord] = numAddRate # if no instance of word existed, add key
#---------------------------------------------------------------------------------#
def getStopWords():
	"""
	Returns a list of words to ignore.

	Params: None

	Returns: (list<string>): the list of words to ignore
	"""
	file = open("stopwords.txt", "r")
	stopWords = []
	for word in file:
		stopWords.append(word.strip())
	return stopWords
#---------------------------------------------------------------------------------#
def readFile(filename, stopWords):
	"""
	Read a file and return it.

	Params: filename (string): the name of the file to read

	Returns: (file) the file found with the specified filename
	"""
	infile = open(filename, "r")
	wordScores = {}
	for line in infile:
		line = line.strip().lower()
		sentimentRating = line[0] 					# get sentiment rating
		wordsInReview = line[1:].split(" ") 		# get sentence
		for word in wordsInReview:
			if word.isalpha() and (binarySearch(stopWords, word) == False):
				# Update word-rating pairs in scoreWord function
				scoreWord(sentimentRating, word, wordScores)
	return wordScores
#---------------------------------------------------------------------------------#
def printWordScores(numLowScores, numHighScores, wordScores):
	""" display scores to user """
	for i in range(1,numHighScores+1): 							   
		print(wordScores[len(wordScores)-i])

	for i in range(0,numLowScores):
		print(wordScores[numLowScores-i])
#---------------------------------------------------------------------------------#

def main():
	stopWords = getStopWords() # Get stop words
	wordScores = readFile("movieReviews.txt", stopWords) # Generate sentiment ratings
	listWordScores = insertionSortScores(wordScores)
	printWordScores(20, 20, listWordScores)

main()