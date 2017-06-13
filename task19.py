"""
Question 19 - Level 3
Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
 age and height are numbers. The tuples are input by console. The sort criteria is:
	1: Sort based on name;
	2: Then sort based on age;
	3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
	Tom,19,80
	John,20,90
	Jony,17,91
	Jony,17,93
	Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), 
('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. 
We use itemgetter to enable multiple sort keys.
"""
"""
the itemgetter - return the callable object, by using the __getitem__ methodif multiple items are specified, return a tuple of lookup values
After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).

- w przypadku słownika, należy wyszukiwać po kluczach,
- w przypadku listy, tuplles i stringu należy szukać po indeksach lub dzielić na mniejsze parametry

The items can be any type accepted by the operand’s __getitem__() method. Dictionaries accept any hashable value.
Lists, tuples, and strings accept an index or a slice:

>>>
>>> itemgetter(1)('ABCDEFG')
'B'
>>> itemgetter(1,3,5)('ABCDEFG')
('B', 'D', 'F')
>>> itemgetter(slice(2,None))('ABCDEFG')
'CDEFG'
"""

import operator
print("add information about the user, please add name, age and height")
clientData = []
while (True):
  consoleInput = input()
  if not consoleInput:
    break
  consoleInput.split(",")
  tuple(consoleInput)
  clientData.append(consoleInput)

print (sorted(clientData, key=operator.itemgetter(0,1,2)))
