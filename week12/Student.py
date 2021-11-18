class Student(object):

    def __init__(self, name, gradYear):
        """constructor to create class"""
        self.name = name
        self.gradYear = gradYear
        self.major = "Undecided"

    def __str__(self):
        """if class is ordered to convert to a string"""
        return self.toString()

    def toString(self):
        """display every characteristic of the student"""
        return "Student Name: %s\n   Grad Year: %s\n       Major: %s" % (self.getName(), self.getGradYear(), self.getMajor())

    def getName(self):
        """get the student's name"""
        return self.name

    def getGradYear(self):
        """get the student's graduation year"""
        return self.gradYear

    def getMajor(self):
        """get the student's major"""
        return self.major

    def setName(self, name):
        """set/change the student's name"""
        self.name = name

    def setGradYear(self, gradYear):
        """set/change the student's graduation year"""
        self.gradYear = gradYear

    def setMajor(self, major):
        """set/change the student's major"""
        self.major = major

if __name__ == "__main__":
    raj = Student("Raj Sugavanam", 2023)
    raj.setMajor("Computer Science")
    print(raj)