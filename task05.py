"""
Question 5 - Level 1
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/ - read more
https://learnpythonthehardway.org/book/ex40.html

"""


class InputStringToUppercaseConverter:
    def __init__(self):
        self.data = "" #now the string data was created, it will be initialized
                        #all the time when new object was created

    def getString(self):
        self.data = input("give the string ")

    def printString(self):
        print (self.data.upper())


newObj = InputStringToUppercaseConverter()
newObj.getString()
newObj.printString()


"""
class InputOutString(object):
  def __init__(self):
    self.data = "" #create the data type string - it is suggested by ""

  def getString(self): #metoda do popierania danych z konsoli
    self.data = input("write text: ")

  def printString(self):
    print (self.data.upper())

#create the object
strObj = InputOutString()
#call the funkcjon
strObj.getString()
strObj.printString()


hints:
Use __init__ method to construct some parameters

Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = raw_input()
    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
"""
