"""
Question 15 -- Level 2
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program:
	9
Then, the output should be:
	11106
	
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

a = input ("add the value")
a = int(a)
computedValue = a + a*a + a*a*a + a*a*a*a
print (computedValue)