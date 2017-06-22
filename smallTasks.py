"""
Question 33
Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
"""

def printDictionary():
    slownik = {}
    for item in range (1,21):
        slownik[item] = item ** 2
    print(slownik)

printDictionary()
#-------------------------------------#
"""
Question 34
Define a function which can generate a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
The function should just print the values only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get
key/value pairs.
"""
def printDictionary():
    slownik = {}
    for item in range (1,21):
        slownik[item] = item ** 2
    print(slownik.values())

printDictionary()
#-------------------------#
"""
Question 35
Define a function which can generate a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get
key/value pairs.
"""

def printDictionary():
    slownik = {}
    for item in range (1,21):
        slownik[item] = item ** 2
    print(slownik.keys())

printDictionary()

#-------------------------#
"""
Question 36
Define a function which can generate and print a list where the values
are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
"""
def printList():
    listka = []
    for item in range (1,21):
        listka.append(item ** 2)
    print(listka)

printList()

#--------------------#
"""
Question 36
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to print
the first 5 elements in the list.
"""
def printList():
    listka = []
    for item in range (1,21):
        listka.append(item ** 2)
    print(listka[:5])

printList()

#-----------------------#
"""
Question 37
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to print
the last 5 elements in the list.
"""
def printList():
    listka = []
    for item in range (1,21):
        listka.append(item ** 2)
    print(listka[-5:]) #od piątego elementu do ostatniego czyli do -1

printList()
#--------------------------#
"""
Question 38
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to print
all values except the first 5 elements in the list.
"""
def printList():
    listka = []
    for item in range (1,21):
        listka.append(item ** 2)
    print(listka[5:])

printList()
#---------------------#
"""
Question 39
Define a function which can generate and print a tuple where the value are
square of numbers between 1 and 20 (both included).
"""
def printTuple():
    lista = []
    for item in range (1,21):
        lista.append(item ** 2)
    print(tuple(lista))

printTuple()

#--------------------#
"""
Question 40
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
the first half values in one line and the last half values in one line.
"""
inputTuple = (1,2,3,4,5,6,7,8,9,10)
lista = list(inputTuple)
listaLength = len(lista)
print(lista[:listaLength/2])
print(lista[listaLength/2:])

#-----------------------#
"""
Question 41
Write a program to generate and print another tuple whose values
are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""
inputTuple = (1,2,3,4,5,6,7,8,9,10)
evenNumbers = []
for item in inputTuple:
    if item % 2 == 0:
        evenNumbers.append(item)
    else:
        pass
newTuple = tuple(evenNumbers)
print(newTuple)
#------------------#
"""
Question 42
Write a program which accepts a string as input to print "Yes" if the string is "yes"
or "YES" or "Yes", otherwise print "No".
"""

print('write yes or no :)')
consoleInput = input()
if consoleInput == 'Yes' or consoleInput == 'YES' or consoleInput == 'yes':
    print('Yes')
else:
    print('No')
