"""
Question 64
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence
in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:
	7
Then, the output of the program should be:
	0,1,1,2,3,5,8,13

Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.
"""

def fibcio(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return (fibcio(N-1)+fibcio(N-2))

print("write the value to Fibonacci calculation")
n = input()

if n > 0:
    fibList = (str(fibcio(item)) for item in range(0,n+1))
else:
    print("n is to low")

print(','.join(fibList))
=======================================
"""
Question 65
Please write a program using generator to print the even numbers between 0 and n
in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
	10
Then, the output of the program should be:
	0,2,4,6,8,10
"""
def evenNumberCollection(N):
    for item in range (0,N+1):
        if item % 2 == 0:
            yield (item)


print("write value to calculate the even collection in range (0,n)")
n = input()

evenNumber = []
for item in evenNumberCollection(n):
    evenNumber.append(str(item))


print(','.join(evenNumber))
==================================

"""
Question 66
Please write a program using generator to print the numbers
which can be divisible by 5 and 7 between 0 and n
in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
	100
Then, the output of the program should be:
	0,35,70
"""
def divisibleByFifeAndSeven(N):
    for item in range(N):
        if (item % 5 == 0) and (item % 7 == 0):
            yield item


print("write a range number to generate the list of parameters"
      "divisible by 5 and 7")
rangeValue = input()

values = []
for item in divisibleByFifeAndSeven(rangeValue):
    values.append(str(item))

print(','.join(values))
===============================

"""
Question 67
Please write assert statements to verify that every number
in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.
"""

lista = [2,4,6,8]
lista2 = [1,3,7,8]
print("lista = ", lista)
for item in lista:
    assert (item % 2 == 0)#, ("all items are even")


print ("lista = ", lista2)
for item in lista2:
    assert (item%2 == 0),("not all items are even in the tested list")

=======================
"""
Question 68
Please write a program which accepts basic mathematic expression from console
and print the evaluation result.
Example:
If the following string is given as input to the program:
	35+3
Then, the output of the program should be:
	38
Hints:
Use eval() to evaluate an expression.

"""
print("write the mathematic expresssion")
express = input()

print(eval(express))

#current solution is for python3, in python2 the evaluation is automaticaly calculated
#in Python3 the input is an int than string at is was in python2
===========
