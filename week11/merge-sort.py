from random import shuffle

"""                       INSTRUCTIONS
        When you get this up and running, copy-paste your merge() and
        mergeSort() functions into your sorts.py file.
        This way, all of your sorting algorithms will be in one place.    """

def merge(leftL, rightL, L):
    """ Implement the merge() function below and you should be good to go """

    lenLeftL = len(leftL)
    lenRightL = len(rightL)
    idxList = 0
    idxL = 0
    idxR = 0
    while True:
        if idxL < lenLeftL and idxR < lenRightL:
            leftElement = leftL[idxL]
            rightElement = rightL[idxR]

            if leftElement < rightElement:
                L[idxList] = leftElement
                idxL+=1
            else:
                L[idxList] = rightElement
                idxR+=1
        else:
            if idxL >= lenLeftL and idxR >= lenRightL:
                return L
            elif idxL >= lenLeftL:
                L[idxList] = rightL[idxR]
                idxR+=1

            elif idxR >= lenRightL:
                L[idxList] = leftL[idxL]
                idxL+=1
        idxList+=1
    


def mergeSort(L):
    if len(L) > 1:
        half = len(L) // 2		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


def main():
    N = 10
    L = []
    for i in range(N):
        L.append(i)
    
    cloneL = L
    cloneL.sort()
    shuffle(L)
    # print(L)
    mergeSort(L)
    assert cloneL == L
    print(cloneL)
    print(L)

main()
