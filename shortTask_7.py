"""
Question 86
By using list comprehension, please write a program to print the list after
removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

"""
createdList = [12,24,35,70,88,120,155]
listOfPairedValueAndItsIndex = list(enumerate(createdList))
"""
newList = []

print(listOfPairedValueAndItsIndex)
for item in listOfPairedValueAndItsIndex:
    if listOfPairedValueAndItsIndex.index(item) % 2 != 0:
        newList.append(item)
print(newList)
"""

newList = [item for item in listOfPairedValueAndItsIndex if listOfPairedValueAndItsIndex.index(item) % 2 != 0]
print(newList)
=========
"""
Question 87
By using list comprehension, please write a program generate a 3*5*8 3D array
whose each element is 0.
Hints:
Use list comprehension to make an array.
"""
n = 3
m = 5
h = 8
matrix = [[[0 for kolumn in xrange(h)] for kolumn in xrange(m)] for row in xrange(n)]

print(matrix)
print("\n")
print("\n")
print([0 for k in xrange(3)])
print([0 for k in xrange(5)])
print([0 for k in xrange(8)])
===============
"""

Question 88
By using list comprehension, please write a program to print the list
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

"""

lista = [12,24,35,70,88,120,155]
genListOfTuple = list(enumerate(lista))
genIndexList = []
for item in genListOfTuple:
    genIndexList.append(genListOfTuple.index(item))

#first combination
newList = []
for item in genListOfTuple:
    if genListOfTuple.index(item) != 0 and genListOfTuple.index(item) != 4 and genListOfTuple.index(item) != 5:
        newList.append(item)

print(newList)

#the second one combination
newList = [item for item in genListOfTuple if genListOfTuple.index(item) != 0 and genListOfTuple.index(item) != 4 and genListOfTuple.index(item) != 5]
print(newList)
===================
"""
Question 89
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].
Hints:
Use list's remove method to delete a value.

"""
lista = [12,24,35,24,88,120,155]

newList = [item for item in lista if item != 24]

print(newList)
======
# -*- coding: utf-8 -*-
"""
Question 90
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.


set jest nieuporządkowaną kolekcją

Sets can be used to carry out mathematical set operations like union, intersection,
difference and symmetric difference. We can do this with operators or methods.

Let us consider the following two sets for the following operations.

union - część wspólna

intersection jest to wyszukanie części współnej porównywanych list


"""
list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]

#utworzenie set z dostępnych list
list1 = set(list1)
list2 = set(list2)
#sprawdzenie części współnej
print(list1 & list2)
=========
"""
Question 91
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print
this list after removing all duplicate values with original order reserved.
Hints:
Use set() to store a number of values without duplicate.

"""
lista = [12,24,35,24,88,120,155,88,120,155]
lista = set(lista)

print(sorted(lista))
======
"""
Question 92
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class
and "Female" for Female class.
Hints:
Use Subclass(Parentclass) to define a child class.

"""
class Person:

    def getGender(self,gender = 0):
        print('unknown')

class Male(Person):
    def getGender(self,gender = 'Male'):
        print (gender)

class Female(Person):
    def getGender(self,gender = 'Female'):
        print(gender)


obj = Person()
obj.getGender()
obj1 = Male()
obj1.getGender()
obj2 = Female()
obj2.getGender()
=======

"""
Question 93
Please write a program which count and print the numbers of each character
in a string input by console.
Example:
If the following string is given as input to the program:
	abcdefgabc
Then, the output of the program should be:
	a,2
	c,2
	b,2
	e,1
	d,1
	g,1
	f,1
Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

"""
print("write abc's string, we will count how many times the letters are available")
textData = input()
textCollection = {}
for item in textData:
  textCollection[item] = textCollection.get(item,0)+1

for item in textCollection.keys():
  print(item,textCollection[item])

=======
"""
Question 94
Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
	rise to vote sir
Then, the output of the program should be:
	ris etov ot esir
Hints:
Use list[::-1] to iterate a list in a reverse order.

"""

print("set a string")
consoleInput = input()

print(consoleInput[::-1])

=========
"""
Question 95
Please write a program which accepts a string from console
and print the characters that have even indexes.
Example:
If the following string is given as input to the program:
	H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
	Helloworld
Hints:
Use list[::2] to iterate a list by step 2.

"""
print("write sentence like H1e2l3l4o5w6o7r8l9d")
text = input()
print(text[::2])

=======
# coding=utf-8
"""
Question 96
Please write a program which prints all permutations of [1,2,3]
Hints:
Use itertools.permutations() to get permutations of list.

generowanie wartości, zbiory każda wartość z każdą
"""
import itertools
L = [1,2,3]
print(list(itertools.permutations(L)))
=======
# coding=utf-8
"""
Question 97
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
Hint:
Use for loop to iterate all possible solutions.

"""

def solveChineeseProblem(legs,heads):
    for henNum in range(heads+1):
        rabbitNum = heads - henNum
        if 2 * henNum + 4 * rabbitNum == legs:
            return henNum, rabbitNum
    return ('not possible to resolve it')


headr = 35
leg = 94

problemSolution = solveChineeseProblem(leg,headr)

print("hen number = ", problemSolution[0], " rabbit number = ", problemSolution[1])

========
