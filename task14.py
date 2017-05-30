"""

Question 14 -- Level 2
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program:
	Hello world!
Then, the output should be:
	UPPER CASE 1
	LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

inputSentence = input("write some text")
countsUpperLetters = 0 
countsLowerLetters = 0 
for items in inputSentence:
  if items.isupper():  #function which give possibility to check if current letter is an upper letter
    countsUpperLetters += 1
  elif items.islower():  #function which give possibility to check if current letter is a lower letter 
    countsLowerLetters +=1
  else:
    pass  #I need to add the else statement but I didn't have any sentence to use here, that's why I used  the pass statement

print(" UPPER CASE ", countsUpperLetters, "\n", "LOWER CASE ", countsLowerLetters)


"""
Pass statement:

It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet
"""