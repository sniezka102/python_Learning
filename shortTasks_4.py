"""
Question 53
Please raise a RuntimeError exception.
hints
use raise() to raise an exception

https://docs.python.org/3/tutorial/errors.html#raising-exceptions

"""
raise RuntimeError('what is it??????!!!!!!!')

#----------------------#
"""
Question 54
Write a function to compute 5/0 use try/except to catch the exceptions

"""


try:
    print(5/0)
except:
    print("do you really want to divide by zero?")


try:
    print(50/2)
except:
    print("do you really want to divide by zero?")
#------------------#

# -*- -coding: utf-8 -*-
"""
Question 55
Define a custom exception class which takes a string message as attribute.
hint
To define a custom exception, we need to define a class inherited from Exception.

"""

class ExceptionClass(Exception):
    def __init__(self,string):
        self.string = string
    try:
        print(self.string)
    except:
        print("\tthis is not a string")

print("the int value was added")
classObj = ExceptionClass(10293)
#-------------#
"""
Question 56
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
	john@google.com
Then, the output of the program should be:
	john
In case of input data being supplied to the question,
it should be assumed to be a console input.

"""
print("write the email address as username@companyname.com")
email = input()
cutEmail = email.split("@")

userName = str(cutEmail[0])
print(userName)
#-------------------#
"""
Question 57
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
	john@google.com
Then, the output of the program should be:
	google
In case of input data being supplied to the question,
it should be assumed to be a console input.
Hints:
	Use \w to match letters.

"""
print("write the email address as username@companyname.com")
email = input()
cutEmail = email.split("@")
#print(cutEmail)
companyName = str(cutEmail[1])
companyName = companyName.split(".")
print(companyName[0])
---
import re

emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print (r2.group(2))
#==============#different solution
import re
print (re.findall("\d+",inputData))
#d oznacza digit

#----------------------#
#-*- -coding utf-8 -*-
"""
Question 58
Print a unicode string "hello world".

Hints:
Use u'strings' format to define unicode string.

"""
guString = "hello world"
print(u"\guString")

#------------------#
"""
Question 59
Write a program to read an ASCII string
and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

"""
print("write the ascii string")
text = input()
convertToUnicode = unicode(text)
convertToUnicode2 = (text,"utf-8")
print(convertToUnicode)
print(convertToUnicode2)
#---------------------------------#

"""
Question 60
Write a special comment to indicate a Python source code file is in unicode.
Hints:
"""
	# -*- coding: utf-8 -*-
#------------------------------------#
"""
Question 61
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
	5
Then, the output of the program should be:
	3.55
In case of input data being supplied to the question,
it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float

"""
print("write value to compute the function")
n = input()
computeFun = 0
if n > 0:
    for item in range (1,n+1):
        computeFun += (float(item) / float(item + 1))
    print(float(computeFun))
else:
    print("n is lower than zero")
#============#
"""
Question 62
Write a program to compute:
	f(n)=f(n-1)+100 when n>0
and f(0)=1
	with a given n input by console (n>0).

Example:
If the following n is given as input to the program:
	5
Then, the output of the program should be:
	500
In case of input data being supplied to the question,
it should be assumed to be a console input.
Hints:
We can define recursive function in Python.

"""
def funSum(N):
    if N == 0:
        return 1
    else:
        return funSum(N-1)+100

print("write the value")
n = input()

if n > 0:
    print(funSum(n))
else:
    print("the n is lower than zero")
#===============#
"""
Question 63
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.


"""
def fibonacciSequence(val):
    if val == 0:
       return 0
    elif val == 1:
       return 1
    else:
       return (fibonacciSequence(val-1) + fibonacciSequence(val-2))

print("add the value to calculate the ficoacci sequence")
n = 7
if n > 0:
    print(fibonacciSequence(n))
else:
    print('the n is below the zero')
