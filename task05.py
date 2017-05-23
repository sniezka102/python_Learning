"""
Question 5 - Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""
class GetInputFromTheConsole:
  def getString(self):
    self.data = input("give the string")
    self.printString()

  def printString(self):
    print (self.data.upper())
  
    
newObj = GetInputFromTheConsole()
newObj.getString()

