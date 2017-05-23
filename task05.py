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
