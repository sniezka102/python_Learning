"""
QUestion 27
Define a function that can convert a integer into a string and print it in console.
Hints:
Use str() to convert a number to string.

"""
def convertIntegerToString(convertedValue):
    k = str(convertedValue)
    print(type(k))

print("write number which be converted to the string")
inputValue = input()
convertIntegerToString(inputValue)
