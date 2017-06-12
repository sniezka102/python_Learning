"""
Question 18 -- Level 3
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users. 
Following are the criteria for checking the password:
	1. At least 1 letter between [a-z]
	2. At least 1 number between [0-9]
	1. At least 1 letter between [A-Z]
	3. At least 1 character from [$#@]
	4. Minimum length of transaction password: 6
	5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.

Example
If the following passwords are given as input to the program:
	ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
	ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
In current solution I was used the re.search() which looks along during string not only its beginning, as the re.match()
"""
import re

print("please write few password separated by the comma, we will help you to choose the best ")

passwords = input()
password = passwords.split(",")
print("\n passwords = ", password, "\n")
passwordWithCorrectLenght = []
for item in password:
#verify if the password has the proper length
	if (len(item) < 6):
		print(item,"\t\tpassword too short")
		continue
	elif (len(item) > 12):
		print(item, "\tpassword too long")
		continue
	else:
	  print(item, "\tpassword has the correct length")
	  passwordWithCorrectLenght.append(item)
	  pass
print("CorrectLendght = ", passwordWithCorrectLenght)


correctPasswordColletion = []
for item in passwordWithCorrectLenght:
#  print ("item in second lups")
#vefiry it the numbers, in range [1-9] and the letters is [a-z or A-Z] are in the string
	if not re.search("[a-zA-Z1-9]", item):
	  continue
	elif not re.search("[$#@]",item):
		continue
#verify if the end line parameter was used
	elif re.search("\s",item):
		continue
	else:
		correctPasswordColletion.append(item)
		pass
print("selected passwords = ", correctPasswordColletion)
