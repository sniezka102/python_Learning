"""
Question 71
Please generate a random float where the value is between 10 and 100
using Python math module.

Hints:

Use random.random() to generate a random float in [0,1].
"""
import random
k = []
for item in range (1,10):
    k.append(random.random()*100) #random.random, wywolanie funkcji random z modulu random
                                    #random zwraca tylko wartości z zakresu od 0 do 1, stad
                                    #przemnozenie przez 100
print(k)

=========
"""

Question 72
Please generate a random float where the value is between 5 and 95
using Python random module.

Hints:
Use random.random() to generate a random float in [0,1].

"""
import random
for item in range (0,10):
    print(random.uniform(5,95))

=================
"""
Question 73
Please write a program to output a random even number between 0 and 10 inclusive
using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

"""
import random
k = random.choice([item for item in range(11) if item % 2 == 0])
print(k)
===============
"""
Question 74
Please write a program to output a random number, which is divisible by 5 and 7,
between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

"""
import random
k = random.choice([item for item in range(110) if (item % 5 == 0 and item % 7 == 0)])
print(k)
=======
"""
Question 75
Please write a program to generate a list with 5 random numbers
between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.


random.sample(population,k) - do population uzyty jest xrange
k - the list length, w moim przypadku bedzie do 5

"""
import random
val = random.sample(range(100,200),5)
print(val)
========
"""
Question 76
Please write a program to randomly generate a list with 5 even numbers
between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

"""

import random

k = random.sample([item for item in range(100,200) if item % 2 == 0],5)
print(k)
==========
"""
Question 77
Please write a program to randomly generate a list with 5 numbers,
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
Hints:
Use random.sample() to generate a list of random values.

"""
import random
k = random.sample([item for item in range(1,1000) if item%5==0 and item%7==0],5)
print(k)

#po sample([],k), jest nawias kwadratowy bo tworzymy liste a ktorej zostanie
#wybranych 5 wartosci
=========
"""
Question 78
Please write a program to randomly print a integer number
between 7 and 15 inclusive.
Hints:
Use random.randrange() to a random integer in a given range.


"""
import random
k = random.randrange(7,16)
print(k)
=======
"""
Question:79
Please write a program to compress and decompress the string
"hello world!hello world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
kompresja to zmniejszanie / sciskanie znakow aby zajmowaly mniej miejsca

"""
import zlib

text = 'hello world!hello world! hello world! hello world!'
print(zlib.compress(text))
new = zlib.compress(text)
print(zlib.decompress(new))
=========
"""
Question 80
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.
"""
import timeit
t = timeit.Timer("for i in range(10000):1+1")
print (t.timeit())

======

"""
Question 81
Please write a program to shuffle and print the list [3,6,7,8].
Hints:
Use shuffle() function to shuffle a list.
"""
import random
lista = [3,6,7,8]
k = random.shuffle(lista)
print(k)

=========
"""
Question 82
Please write a program to shuffle and print the list [3,6,7,8].
Hints:
Use shuffle() function to shuffle a list.
"""
import random
print(random.shuffle([3,6,7,8]))

=====
"""
Question 83
Please write a program to generate all sentences where subject is in ["I", "You"]
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
Hints:
Use list[index] notation to get a element from a list.


"""
subjectList = ["I","You"]
verbList = ["Play", "Love"]
objectList = ["Hockey","Football"]
sentences = []
countSenteces = 0
for itemList in subjectList:
    for itemVerb in verbList:
        for itemObj in objectList:
            sentences.append(itemList+' '+ itemVerb+' '+itemObj)
            countSenteces += 1

for item in range (0,countSenteces):
    print(sentences[item])
========
"""
Question 84
Please write a program to print the list
after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

"""

createdList = [5,6,77,45,22,12,24]
oddValuesList = [item for item in createdList if item%2 != 0]
print(oddValuesList)
=====
"""
Question 85
By using list comprehension, please write a program to print the list after
removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.

"""
createdList = [12,24,35,70,88,120,155]
numberNotDivisibleByFifeAndSeven = [item for item in createdList if (item%5 != 0 and item%7 != 0)]
print(numberNotDivisibleByFifeAndSeven)
==========
