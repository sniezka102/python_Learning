"""

Question 5 - Level 1
Question:
Define a class which has at least two methods:
- getString: to get a string from console input
- printString: to print the string in upper case.
Also please include simple test function to test the class methods.

https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/ - read more
"""


class GetInputFromTheConsole:
  def __init__ (self):
     self.data = ""
  def getString(self):
    self.data = input("add some text ")
    

  def printString(self):
    print (self.data.upper())
  
# create the obcject
strObj2 = GetInputFromTheConsole()

strObj2.getString()
strObj2.printString()
