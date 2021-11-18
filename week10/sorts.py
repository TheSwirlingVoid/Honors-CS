from math import ceil
from random import shuffle
from time import time


def insertionSort(L):
	#Loop through each index
	for i in range(1, len(L)):

		for numCheck in range(i): #Loop that provides the offsetIndex from the time the element was originally compared
			newIndex = i-numCheck

			secondElement = L[newIndex]
			firstElement = L[newIndex-1]

			if secondElement < firstElement: #If the front element is less than the back, swap them
				tempSecondElement = secondElement
				tempFirstElement = firstElement
						
				L[newIndex] = tempFirstElement
				L[newIndex-1] = tempSecondElement

			else: #Move on to the next element if the two compared elements are sorted
				break

def bubbleSort(L):
	while True:
		numSwaps = 0
		for i in range(1, len(L)): #-1 so that it doesn't go out of bounds (since starting at 1)

			if L[i] < L[i-1]: # Swap the elements if the front element is less than the previous
				tempSecondElement = L[i]
				tempFirstElement = L[i-1]
				L[i] = tempFirstElement
				L[i-1] = tempSecondElement
				numSwaps+=1
		if numSwaps == 0: #If the list has gone through a run without swapping anything, the list is sorted
			return

def selectionSort(L):
	for i in range(len(L)):
		min_idx = i
		for j in range(i, len(L)):
			if L[j] < L[min_idx]:
				min_idx = j
		tmpFirst = L[min_idx]
		tmpSecond = L[i]
		L[i] = tmpFirst
		L[min_idx] = tmpSecond

def merge(L1, L2, L):
	idx1 = 0
	idx2 = 0
	Lidx = 0
	while idx1 < len(L1) and idx2 < len(L2):
		element1 = L1[idx1]
		element2 = L2[idx2]
		if element1 < element2:
			L[Lidx] = element1
		else:
			L[Lidx] = element2

def mergeSort(L):
	listLength = len(L)
	halfList = listLength//2

	if listLength > 1: 
		L1 = L[:halfList]
		L2 = L[halfList:]

		mergeSort(L1)
		mergeSort(L2)
		merge(L1,L2,L)


def main():

	N = 10000
	L = [ ]
	listCopy = [ ]
	for i in range(N):
		L.append(i)
		listCopy.append(i)
	
	shuffle(L)
	unsortedList = L

	listClone = unsortedList
	t1 = time()
	insertionSort(listClone)
	t2 = time()
	print("insertion sort time: %8.4f" % (t2-t1))

	listClone = unsortedList
	t1 = time()
	bubbleSort(listClone)
	t2 = time()
	print("bubble sort time: %8.4f" % (t2-t1))

	listClone = unsortedList
	t1 = time()
	selectionSort(listClone)
	t2 = time()
	print("insertion sort time: %8.4f" % (t2-t1))

	assert L == listCopy

main()