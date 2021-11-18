class Counter(object):
    """ An object that keeps track of some value, where the value starts at zero,
        counts up to some maximum value, and then resets back to zero. """

    ###  TO BE IMPLEMENTED BY YOU  ###
    def __init__(self, maxNum):
        self.maxNum = maxNum
        self.currentNum = 0
    
    def __str__(self):
        return "Value: %i (MaxValue: %i)" % (self.currentNum, self.maxNum)

    def increment(self):
        self.currentNum += 1
        if self.currentNum >= self.maxNum:
            self.currentNum = 0
        
    def getValue(self):
        return self.currentNum

    def setValue(self, num):
        if num <= self.maxNum:
            self.currentNum = num




if __name__ == "__main__":      # test code goes here for custom Classes

    c = Counter(60)
    print(c)
    for i in range(10):
        c.increment()
        print(c)

    print("-" * 20)
    print("set counter value to 55")

    c.setValue(55)
    print(c)
    for i in range(10):
        c.increment()
        print(c)
