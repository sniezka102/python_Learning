"""
Question 12 -- Level 2
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


"""


wholeEvenNumbersInNumber = []
numb = input("add value in range <1000,3001>")
if (int(numb) >= 1000) and (int(numb) <= 3000):
  if ((int(numb[0])%2)==0) and ((int(numb[1])%2)==0) and ((int(numb[2])%2)==0) and ((int(numb[3])%2)==0):
    wholeEvenNumbersInNumber.append(numb)
  else:
    print("non all of the numbers in number are even")
else:
  print("number = ", num, " is out of range")
print (",".join(wholeEvenNumbersInNumber))
  
"""
current solution obtain hints that data should have been taken from the console. In this case not possible to separate by .join

bellow I will create the solution when few numbers were added from the console

""""
