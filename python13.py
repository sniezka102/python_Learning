"""

Question 13 -- Level 2
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.	Suppose the following input 
is supplied to the program:
	hello world! 123
Then, the output should be:
	LETTERS 10
	DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

https://www.tutorialspoint.com/python/string_isalpha.htm 

"""

inputSentence = input("write some text")
lettersCount = 0 
digitCount = 0 
for character in inputSentence:
  if character.isalpha():  #function which give possibility to check if current item is a letter 
    lettersCount += 1
  elif character.isdigit():  #function which give possibility to check if current item is digit 
    digitCount +=1
  else:
    pass  #I need to add the else statement but I didn't have any sentence to use here, that's why I used  the pass statement

print(" LETTERS ", lettersCount, "\n", "DIGITS ", digitCount)


"""
Pass statement:

It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your 
code will eventually go, but has not been written yet
"""
