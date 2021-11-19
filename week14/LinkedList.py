from node import *

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

    def deleteHead(self):
        """ deletes the first element of the linked list. """
        deletedItem = None
        if self.size == 0:                             # return none if len == 0
            return deletedItem
        elif self.size == 1:                         # delete all if one element
            deletedItem = self.head.getItem()
            self.head = None
            self.tail = None
        else:                                        # reassign head for len > 1
            deletedItem = self.head.getItem()
            self.head = self.head.getNext()  
        self.size -= 1
        return deletedItem

    def deleteTail(self):
        """ deletes the last element of the linked list; 
            return the deleted item. """
        deletedItem = None
        if self.size == 0:
            return deletedItem

        elif self.size == 1:
            deletedItem = self.tail.getItem()
            self.head = None
            self.tail = None
        else:                                
            deletedItem = self.tail.getItem()
            newTail = self.head              
            for index in range(self.size - 1):
                newTail = newTail.getNext()
            self.tail = newTail
        self.size -= 1
        return deletedItem                          

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
        """ return first index of node containing item """
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
        elif index <= self.size:            # if valid index, add the element in
            curr = self.head
            for i in range(index-1):
                curr = curr.getNext()
            previousElement = curr
            nextElement = curr.getNext()
            newElement = Node(item)
            previousElement.setNext(newElement)
            newElement.setNext(nextElement)
            self.size += 1

    def pop(self, index):
        """ remove the item from the linked list at given index, return item """
        if index == 0:                    
            return self.deleteHead()
        elif index < self.size:        # if valid index, remove element at index
            curr = self.head
            for i in range(index - 1):
                curr = curr.getNext()
            previousElement = curr
            removedElement = curr.getNext()
            nextElement = removedElement.getNext()
            previousElement.setNext(nextElement)
            self.size -= 1                                    
            return removedElement.getItem()

    def remove(self, item):
        """ remove the specified item from the linked list """
        index = self.index(item)
        if index != -1:
            self.pop(index)

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
