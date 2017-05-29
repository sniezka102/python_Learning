"""
Question 10 - Level 2
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
break

Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""

lines = []
print("add the text line, write 'break' if you want to finish action\n")
while (True):
  inputString = input()
  if inputString == 'break':    #?????????
    break;                      #????????
  else:
    lines.append(inputString)


lines = "".join(lines) #The method join() returns a string in which the string elements of sequence                     #have been joined by str separator.
words = lines.split(" ")

allWords = set(words) #Test if every element in the set is in other.

print(" ".join(sorted(allWords))) #sortowanie

