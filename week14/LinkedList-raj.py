from node import *



class LinkedList(object):                                                       

    def __init__(self):                                                         

        self.head = None

        self.tail = None

        self.size = 0



    def __str__(self):

        """ return string representation of linked list """

        s = "head-->"

        curr = self.head                                                        

        for i in range(self.size):                                              

            s += ("(%s)"  %  str(curr.getItem()))

            curr = curr.getNext()

        s +=("<--tail")

        return s



    def __len__(self):                                                          

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

        self.size += 1                                                          
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

        self.size += 1



    def deleteHead(self):                                                       

        deletedNode = Node(None)                                                

        if self.size == 0:

            return deletedNode



        elif self.size == 1:                   # if only one item exists in list

            deletedNode = self.head            # assign old item before deletion

            self.head = None                 # delete the node (head-registered)

            self.tail = None                 # delete the tail (tail-registered)

        else:                                             # if list has >1 items

            deletedNode = self.head            # assign old item before deletion

            self.head = self.head.getNext()  # update head, dereference old head

        self.size-=1

        return deletedNode.getItem()                # return deleted node's item



    def deleteTail(self):

        deletedNode = Node(None)                                                

        if self.size == 0:

            return deletedNode



        elif self.size == 1:                  #--if only one item exists in list

            deletedNode = self.tail            # assign old item before deletion

            self.head = None                 # delete the node (head-registered)

            self.tail = None                 # delete the tail (tail-registered)

        else:                                            #--if list has >1 items

            deletedNode = self.tail            # assign old item before deletion

            newTail = self.head                                  # start at head

            for index in range(self.size-1):      #--repeat getNext() on newTail    

                newTail = newTail.getNext()    # newTail will be desired element

            newTail = self.tail                                                 ### I don't think this works, where is your self.tail reassignment?

        self.size-=1

        return deletedNode.getItem()                # return deleted node's item



    def count(self, item):

        """ count occurences of an item in a list """

        itemCount = 0                                 # number of matching items

        currentNode = self.head                                  # start at head

        for index in range(self.size):       # add count for every matching item

            if currentNode.getItem() == item:

                itemCount+=1                                                    

            currentNode = currentNode.getNext()          # reassign current node

        return itemCount                                   # return num of items



    def index(self, item):

        """ return first index of node containing item """

        currentNode = self.head                                  # start at head

        for index in range(self.size):                      # traverse all items

            if currentNode.getItem() == item:

                return index                             # return first matching

            currentNode = currentNode.getNext()          # reassign current node

        return -1                                              # -1 if not found



    def insert(self, index, item):

        """ insert an item into the linked list at given index """

        currentNode = self.head                                  # start at head

        if index == 0:                    # remove head if they wanted head gone

            self.prepend(item)

                                                           # exit function

        elif index < self.size:    # if index in range to skip unneeded loop run    

            for currentIndex in range(0, self.size):                                ### why is this variable named 'currentIndex' instad of 'i' or 'index'?

                if currentIndex == index-1:       # relink nodes to fit new node

                    previousElement = currentNode

                    nextElement = currentNode.getNext()

                    newElement = Node(item)

                    previousElement.setNext(newElement)   # relink previous node

                    newElement.setNext(nextElement)      # link new node to next

                    self.size+=1                                    # update len

                currentNode = currentNode.getNext()               # iterate node



    def pop(self, index):

        """ remove the item from the linked list at given index """             

        currentNode = self.head                                  # start at head

        if index == 0:                    # remove head if they wanted head gone

            removedItem = currentNode      # save item before deleting          

            self.deleteHead()

            return removedItem.getItem()                  # return unlinked node

        elif index < self.size:

            for currentIndex in range(0, self.size):                                    

                if currentIndex == index-1:        # relink nodes to remove node        

                    previousElement = currentNode                               

                    removedElement = currentNode.getNext()

                    nextElement = removedElement.getNext()



                    previousElement.setNext(nextElement)           # change link        

                    self.size-=1                                    # update len        

                    return removedElement.getItem()       # return unlinked node

                currentNode = currentNode.getNext()               # iterate node



    def remove(self, item):

        """ remove the specified item from the linked list """                  

        currentNode = self.head                                  # start at head

        if currentNode.getItem() == item:            # remove head if match at 0

            self.deleteHead()

            return                                               # exit function

        for i in range(0, self.size-1):        # -1 to not check outside of list

            elementToRemove = currentNode.getNext()

            if elementToRemove.getItem() == item:

                previousElement = currentNode         # relink surrounding nodes

                nextElement = elementToRemove.getNext()



                previousElement.setNext(nextElement)

                self.size-=1                                        # update len

                return                                           # exit function

            currentNode = currentNode.getNext()                   # iterate node



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

