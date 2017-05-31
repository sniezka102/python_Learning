"""
Question 6 - Level 2
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

"""
import math
#definition of function which take the values from the console and confert it to the list
def convertInputDataToFloat():
  Dvalue = []
  value = input ("write few numbers, please separate them by the comma")
  value = value.split(",")
  for item in value:
    Dvalue.append(int(item))
  return (Dvalue)


D = convertInputDataToFloat()
C = 50
H = 30


#Q calculations

Q =[]
for items in D:
  q = math.sqrt((2* C * items) / H)  #calculations
  Q.append(int(q))
  
print (Q)
