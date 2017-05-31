"""
Question 11 - Level 2
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
	Then the output should be:  1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed o be a console input.
"""

digitBinaryNumbers = input("add 4 digit binary numbers, which are separated by the comma\n")
spiltTheDigitBinaryNumbers = digitBinaryNumbers.split(",")
valueDividedByFife = []

for binaryNumber in spiltTheDigitBinaryNumbers:
  convertedDigitNumber = int(binaryNumber, 2) #conversion from binary to digit 
  if (convertedDigitNumber % 5 == 0):
    valueDividedByFife.append(binaryNumber)

print(",".join(valueDividedByFife))

"""
 the grumpy comments up above suggested, the int function takes a second argument, which is the base of the conversion. So it's taking the base 2 (binary) variable bound to p and turning it to a base-10 int, i.e., normal human.

"""


  
