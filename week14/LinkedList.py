"""
Description: A LinkedList class composed of chained-together nodes.
Author: Raj
Date: Fall 2021
"""


from node import *
from random import choice, random

class LinkedList(object):
    """ A type of list that operates 
        on singly-linked and forward-pointing nodes. """
    def __init__(self):
        """ initializes a linked list with no initial nodes. """
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ return string representation of linked list """
        s = "head-->"
        curr = self.head
        for i in range(self.size):
            s  +=  ("(%s)"  %  str(curr.getItem()))
            curr = curr.getNext()
        s  += ("<--tail")
        return s

    def __len__(self):
        """ returns the length of the LinkedList. """
        return self.size

    def append(self, item):
        """ add an item to the end of the list """
        item = Node(item)
        if self.size == 0:            # if no items, make it first and last item
            self.head = item
            self.tail = item
        else:                         # else link tail to this and reassign tail
            self.tail.setNext(item)
            self.tail = item
        self.size  +=  1
        return
        

    def prepend(self, item):
        """add an item to the beginning of the list"""
        item = Node(item)
        if self.size == 0:            # if no items, make it first and last item
            self.head = item
            self.tail = item
        else:                              # else link to head and reassign head
            item.setNext(self.head)
            self.head = item
        self.size  +=  1
        return

    def deleteHead(self):
        """ deletes the first element of the linked list. 
        returns the deleted item. """
        deleted = None
        if self.size == 0:                             # return none if len == 0
            return deleted
        elif self.size == 1:                         # delete all if one element
            deleted = self.head.getItem()
            self.head = None
            self.tail = None
        else:                                        # reassign head for len > 1
            deleted = self.head.getItem()
            self.head = self.head.getNext()  
        self.size -= 1
        return deleted

    def deleteTail(self):
        """ deletes the last element of the linked list; 
            return the deleted item. """
        deleted = None
        if self.size == 0:
            return deleted

        elif self.size == 1:
            deleted = self.tail.getItem()
            self.head = None
            self.tail = None
        else:                                
            deleted = self.tail.getItem()
            newTail = self.head              
            for index in range(self.size - 1):
                newTail = newTail.getNext()
            self.tail = newTail
        self.size -= 1
        return deleted                          

    def count(self, item):
        """ count occurences of an item in a list """
        itemCount = 0                                 # number of matching items
        curr = self.head
        for index in range(self.size):       # add count for every matching item
            if curr.getItem() == item:
                itemCount += 1
            curr = curr.getNext()                           # cycle checked node
        return itemCount

    def index(self, item):
        """ return first index of node containing item.
            returns -1 if the item is not found. """
        curr = self.head
        for index in range(self.size):                      # traverse all items
            if curr.getItem() == item:
                return index
            curr = curr.getNext()                           # cycle checked node
        return -1                                              # -1 if not found

    def insert(self, index, item):
        """ insert an item into the linked list at given index """
        if index == 0:                               # add to head if index is 0
            self.prepend(item)
        elif index <= self.size and index > 0:              # add the element in
            curr = self.head
            for i in range(index-1):                            # list traversal
                curr = curr.getNext()
            previous = curr                                       # relink nodes
            next = curr.getNext()
            new = Node(item)
            previous.setNext(new)
            new.setNext(next)
            self.size += 1
        return

    def pop(self, index):
        """ remove the item from the linked list at given index, return item """
        deleted = None
        if index == 0:                    
            deleted = self.deleteHead()
        elif index < self.size and index > 0:          # remove element at index
            curr = self.head
            for i in range(index - 1):                          # list traversal
                curr = curr.getNext()
            previous = curr                                       # relink nodes
            removed = curr.getNext()
            next = removed.getNext()
            previous.setNext(next)
            self.size -= 1                                    
            deleted = removed.getItem()
        return deleted

    def remove(self, item):
        """ remove the specified item from the linked list """
        index = self.index(item)
        if index != -1:
            self.pop(index)
        return

if __name__ == "__main__":
    LL = LinkedList()
    LL.append("A")
    LL.append("B")
    LL.append("C")
    LL.append("C")
    print(LL.index("C"))
    print(LL.index("D"))
    print(LL.count("A"))
    print(LL)
    LL.insert(0, "A")
    print(LL)
    print("removing", LL.pop(3))
    print(LL)
    print("removing", LL.pop(0))
    print(LL)
    LL.remove("B")
    print("removing B")
    print(LL)
    LL.remove("D")
    print("removing D")
    print(LL)
    LL.insert(100, "D")
    print("inserting D at index 100")
    print(LL)
    LL.insert(3, "D")
    print("inserting D at index 3")
    print(LL)
    print("Deleting tail...")
    LL.deleteTail()
    print(LL)
    print("Deleting head...")
    LL.deleteHead()
    print(LL)
    LL.prepend("F")
    print(LL)
    LL.append("F")
    print(LL)

    item = LL.deleteHead()
    print(item == "A")
    print(len(LL) == 2)
    item = LL.deleteHead()
    print(item == "B")
    print(len(LL) == 1)
    item = LL.deleteHead()
    print(item == "C")
    print(len(LL) == 0)
    item = LL.deleteTail()
    print(item == "None")
    print(len(LL) == 0)

    LL2 = LinkedList()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("\ncreating a new list...")
    print("--------------------  testing prepend()/append  -------------------")
    for i in range(10):
        LL2.append(choice(alphabet))
        LL2.prepend(choice(alphabet))
    print("New LL:", LL2)

    print("\n--------------------  testing count()/remove()  -------------------")
    randomLetter = choice(alphabet)
    print("initial occurences of %s: %i" % (randomLetter, LL2.count(randomLetter)))
    while LL2.count(randomLetter) != 0:
        print("removing 1 occurence of", randomLetter)
        LL2.remove(randomLetter)    
        print("counting occurences of %s: %i" % (randomLetter, LL2.count(randomLetter)))
    print("no occurences of %s. attempting to remove it again." % randomLetter)
    LL2.remove(randomLetter)

    print("\n--------------------  testing pop()  -------------------")
    print("attempting to remove element at index out of bounds:")
    print("element removed:", LL2.pop(len(LL2)+1))
    print("attempting to remove element at index length of list")
    print("element removed:", LL2.pop(len(LL2)))
    print("attempting to remove element at index length of list-1")
    print("element removed:", LL2.pop(len(LL2)-1))
    print("attempting to remove element at index 0")
    print("element removed:", LL2.pop(0))
    print("attempting to remove element at index -1")
    print("element removed:", LL2.pop(-1))

    randomLetter = choice(alphabet)
    print("current LL:", LL2)
    print("\n--------------------  testing insert()  -------------------")
    print("element to insert:", randomLetter)
    print("attempting to insert element at index out of bounds:")
    LL2.insert(len(LL2)+1, randomLetter)
    print("current LL:", LL2)
    print("attempting to insert element at index length of list")
    LL2.insert(len(LL2),  randomLetter)
    print("current LL:", LL2)
    print("attempting to insert element at index length of list-1")
    LL2.insert(len(LL2)-1, randomLetter)
    print("current LL:", LL2)
    print("attempting to insert element at index 0")
    LL2.insert(0, randomLetter)
    print("current LL:", LL2)
    print("attempting to insert element at index -1")
    LL2.insert(-1, randomLetter)
    print("current LL:", LL2)

    randomLetter = choice(alphabet)
    print("\n--------------------  testing index()  -------------------")
    print("element to index:", randomLetter)
    print("indexing", randomLetter)
    print(LL2.index(randomLetter))
    print("indexing '4'")
    print(LL2.index(4))

    print("current LL:", LL2)
    print("\n--------------------  testing deleteHead()/deleteTail()  -------------------")
    print("deleting head and tail...")
    LL2.deleteHead()
    LL2.deleteTail()
    print("current LL:", LL2)

    print("\ncreating a new list...")
    print("--------------------  empty LinkedList()  -------------------")
    LLEmpty = LinkedList()

    print("\n----------  testing count()  ----------")
    print("occurences of A: %i" % LLEmpty.count("A"))

    print("\n----------  testing remove()  ----------")
    print("removing A") 
    LLEmpty.remove("A")

    print("\n----------  testing pop()  ----------")
    print("popping index -1")
    LLEmpty.pop(-1)
    print("popping index 0")
    LLEmpty.pop(0)
    print("popping index 1")
    LLEmpty.pop(1)

    print("\n----------  testing insert()  ----------")
    print("inserting 'A' at index 5")
    LLEmpty.insert(5, "A")
    print("inserting 'A' at index 0")
    LLEmpty.insert(0, "A")
    print("current LL:", LLEmpty)

    print("\n----------  testing deleteHead()  ----------")
    print("attempting to delete head")
    LLEmpty.deleteHead()
    print("current LL:", LLEmpty)

    print("\n----------  testing prepend()  ----------")
    print("prepending 'A'")
    LLEmpty.prepend("A")
    print("current LL:", LLEmpty)

    print("\n----------  testing deleteTail()  ----------")
    print("attempting to delete tail")
    LLEmpty.deleteTail()
    print("current LL:", LLEmpty)

    print("\n----------  testing append()  ----------")
    print("appending 'A'")
    LLEmpty.append("A")
    print("current LL:", LLEmpty)
    



