"""
Description: A Node class to be used in a linked list.
Author: Raj
Date: Fall 2021
"""


class Node(object):
    """ A single node object consisting of an item and a next item. 
        To be used in a LinkedList. """
    def __init__(self, item):
        """
        Construct new node, with given item. Next Node initially set to None.
        """
        self.item = item
        self.next = None

    def __str__(self):
        """ return a string representation of the node """
        s = "(%s)" % str(self.item)
        if self.next == None:
            s += "--|"
        else:
            s += "-->"
        return s

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, i):
        self.item = i

    def setNext(self, n):
        self.next = n


if __name__ == "__main__":              # test init, str,s etNext, setItem
    n1 = Node("jeff")
    n2 = Node("zach")
    n3 = Node("lauri")
    n4 = Node("rich")

    n1.setNext(n2)
    print(n1)
    n2.setNext(n3)
    print(n2)
    n3.setNext(n4)
    print(n3)
    n3.setItem("julie")
    # print entire linked list to confirm it looks okay
    print("%s%s%s%s" % (str(n1), str(n2), str(n3), str(n4)))
