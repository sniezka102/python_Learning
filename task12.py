"""
Question 12 -- Level 2
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number 
is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


"""
numbersWithOnlyEvenDigits = []
for item in range (1000,3001):
  number = str(item)
  if ((int(number[0])%2)==0) and ((int(number[1])%2)==0) and ((int(number[2])%2)==0) and ((int(number[3])%2)==0):
    numbersWithOnlyEvenDigits.append(number)
  else:
    pass
print (",".join(numbersWithOnlyEvenDigits))
  
"""
current solution obtain hints that data should have been taken from the console. In this case not possible to separate 
by .join

bellow I will create the solution when few numbers were added from the console

""""
