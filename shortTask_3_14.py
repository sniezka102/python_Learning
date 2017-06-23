
"""
Question 43
Write a program which can filter even numbers in a list by using filter function.
The list is: [1,2,3,4,5,6,7,8,9,10].
"""

L = [1,2,3,4,5,6,7,8,9,10]
filteredResult = filter(lambda x : x % 2 == 0 , range(len(L)))

print(filteredResult)
#-------------------#
"""
Question 44
Write a program which can map() to make a list whose elements
are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""
L = [1,2,3,4,5,6,7,8,9,10]


mappedList = map(lambda x: x**2, L)
print(mappedList)
#-------------------#
"""
Question 45
Write a program which can map() and filter() to make a list whose elements
are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
L = [1,2,3,4,5,6,7,8,9,10]
mapValues = map(lambda x : x ** 2, L)
print(mapValues)
filteredValues = filter(lambda  x: x%2 == 0, mapValues)
print(filteredValues)

#-------------------#
"""
Question 46
Write a program which can filter() to make a list whose elements are even number
between 1 and 20 (both included).
"""
theList = range(1,21)
newGeneratedList = filter(lambda x : x%2 == 0, theList)
print(newGeneratedList)

#-------------------#
"""
Question 47
Write a program which can map() to make a list whose elements are square of numbers
between 1 and 20 (both included).
"""
newList = map(lambda x : x**2, range(1,21))
print(newList)

#-------------------#
#-*- -coding: utf-8 -*-
"""
Question 48
Define a class named American which has a static method called printNationality.

"""

class American:
    @staticmethod       #it is a decorator which convert the function to the static method
    def printNationality():
        print("Nationality")

anAmer = American()
anAmer.printNationality()
American.printNationality()

"""
funkcje statyczne nie zawierają w pythonie parametru (self)
ale są opatrzone dekoratorem @staticmethod

"""
#-------------------#

"""
Question 49

Define a class named American and its subclass NewYorker.
"""
#-------------------#
class American:
    def __init__(self,data):
        self.data = data
    def printCountry(self):
        print(self.data)
class NewYorker(American):
    pass

nationalityClass = American('America')
nationalityClass.printCountry()

cityClass = NewYorker('New York')
print(cityClass.printCountry())
#------------------------#

"""
Question 50
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
"""
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def computeArea(self):
        return round((math.pi * (self.radius ** 2)),2)
areaObj = Circle(5)
print(areaObj.computeArea())

#-----------------#
"""
Question 51

Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area
"""

class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def rectangleAreaComputation(self):
        areaComp = self.length * self.width
        return round(areaComp,2)

rectangleObj = Rectangle(10,20)
print(rectangleObj.rectangleAreaComputation())

#--------------------#
"""
Question 52
Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape,
where Shape's area is 0 by default.

"""

class Shape:
    def __init__(self):
        pass
    def printAreaOfShape(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def printAreaOfShape(self):
        area = self.length ** 2
        print (round(area,2))

squareObj = Square(10)
squareObj.printAreaOfShape()

obj = Shape()
obj.printAreaOfShape()
