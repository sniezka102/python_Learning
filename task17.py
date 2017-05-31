"""
Question 17 -- Level 2
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
	D 100
	W 200
D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
	500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
print("add the logged deposit and withdrawal values\n")
inputData = []
netAmount = 0 
while True:
  logInput = input()
  inputData.append(logInput)
  if not logInput:
    break


for item in inputData:
  if item.startswith('D'):
    test = item.split(" ")
    netAmount += int(test[1])
  elif item.startswith('W'):
    test = item.split(" ")
    netAmount -= int(test[1])
    
print ("netAmount = ", netAmount)