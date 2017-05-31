"""

Question 7  - Level 2
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 

Note: i=0,1.., X-1; j=0,1..,Y-1.

Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""


input_str = input("add two values ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)] #here also was used the matrix generator
for row in range(rowNum):
   for col in range(colNum):
        multilist[row][col]= row*col  #calculate what should be added to the matrix
print (multilist)

"""
current solution is much better, because in my case I used the matrix generator but I could add what I want
to the matrix instead of using the multilist[row][col] = row*col
"""
