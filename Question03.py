"""
Question 03 - level 1
With a given integral number n, write a program to generate a dictionary that contais (i, i*i)
such that is an integral number between 1 and n (both included)
and then the program should print the dictionary
Supposed the following input is supplied to the program:
8
then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


creation of the empty dictionary, sometimes the dictionary is named hash

"""
# the simplest way suggested by the book author

n = input("please, give me the number")
n = int(n)



for i in range (1, n+1):
	d[i] = i * i
	
print (dictionaryVal)

"""
response
add value 8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

