"""
Question 03 - level 1
With a given integral number n, write a program to generate a dictionary that contais (i, i*i)
such that is an integral number between 1 and n (both included)
and then the program should print the dictionary
Supposed the following input is supplied to the program:
8
then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""

n = 8

newDict = {}
#first try - dictionary from two different lists

keyList = []
for value in range (1,n+1):
	keyList.append(value)

#print (keyList)
	
valueList = []
for values in range (1,n+1):
	val = values ** 2
	valueList.append(val)
	
#print (valueList)

#we can use the funciotn zip() to add two lists to one dictionary

newZipper = zip(keyList, valueList)
newDict = dict(newZipper)

print (newDict)