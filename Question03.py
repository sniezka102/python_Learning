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
# in current solution I created two separate list, and then I added them to the dictionary
# I used the zip function

n = 8

newDict = {}

keyList = []
for value in range (1,n+1):
	keyList.append(value)

#print (keyList)
	
valueList = []
for values in range (1,n+1):
	val = values ** 2
	valueList.append(val)
	
#print (valueList)

#Below was used the zip() function which help to merge to separate lists in one matrix

newZipper = zip(keyList, valueList)

#next step is adding the matrix to dictionary
newDict = dict(newZipper)

print (newDict)