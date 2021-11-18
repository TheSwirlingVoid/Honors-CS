from math import factorial
from random import choice

def blastoff_iterative(n):
    """ This function uses iteration to display a countdown from a number (n)
        to 1 and print "blastoff" when it gets to 0. """
    for i in range(n, 0, -1):
        print(i)
    print("blastoff!")


def blastoff_recursive(n):
    """ This function uses recursion to display a countdown from a number (n)
        to 1 and print "blastoff" when it gets to 0. """
    if n > 0:
        print(n)
        blastoff_recursive(n-1)
    else:
        print("blastoff!")
    pass


def sumN_iterative(n):
    """ Function to return the sum from 1 to a number using iteration """
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sumN_recursive(n):
    """ Function to return the sum from 1 to a number using recursion """
    if n != 1:
        return n + sumN_recursive(n-1)
    else:
        return 1
    pass

def fac(n):
    if n != 1:
        return n * factorial(n-1)
    else:
        return 1

def coinflip(n):
    coin = choice(["heads", "tails"])
    if n > 1:
        nextCoin = coinflip(n-1)
        if coin == "heads":
            return [1 + nextCoin[0],0 + nextCoin[1]]
        else:
            return [0 + nextCoin[0],1 + nextCoin[1]]
    else:
        if coin == "heads":
            return [1,0]
        else:
            return [0,1]

def main():

    # n = int(input("Enter a value for n: "))
    # blastoff_iterative(n)
    # blastoff_recursive(n)

    # n = int(input("Enter a value for n: "))
    # print(sumN_iterative(n))
    # print(sumN_recursive(n))

    # n = int(input("Enter a value for n: "))
    # print(fac(n))
    # print(factorial(n))

    n = int(input("Enter a value for n: "))
    results = coinflip(n)
    print("Heads: %i, Tails: %i" % (results[0], results[1]))

main()
