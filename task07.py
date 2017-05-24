"""
Question 7  - Level 2
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. 

Note: i=0,1.., X-1; j=0,1..,Y-1.

Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 



"""


value = input("please add value separated the comma")
data = []
data = value.split(",")

testArray = []

#create the number of columns and rows
X = int(data[0]) #columns
print ("X / columns = ", X)
Y = int(data[1]) #rows
print ("Y / rows = ", Y)

#in current solution was used the two dimentional generator to create the array
testArray = [[i * j for j in range(Y)] for i in range(X)]
print (testArray)

"""
in current case the two-dimenstional arrays: nested generator was used
own hint    - https://snakify.org/lessons/two_dimensional_lists_arrays/


5. Two-dimensional arrays: nested generators
5.1 You can use nested generators to create two-dimensional arrays, placing the generator of the list which is a string, inside the generator of all the strings. Recall that you can create a list of n rows and m columns using the generator (which creates a list of n elements, where each element is a list of m zeros):
    [[0] * m for i in range(n)]

5.2 But the internal list can also be created using, for example, such generator 
    [0 for j in range(m)]. Nesting one generator into another, we obtain

    [[0 for j in range(m)] for i in range(n)]
5.3 How is it related to our problem? The thing is, if the number 0 is replaced by some expression that depends on i (the line number) and j (the column number), you get the matrix filled according to some formula.
  For example, suppose you need to initialize the following array (for convenience, extra spaces are added between items):

1  0  0  0  0  0  0
2  0  1  2  3  4  5
3  0  2  4  6  8 10
4  0  3  6  9 12 15
5  0  4  8 12 16 20

5.4. In this array there are n = 5 rows, m = 6 columns, and the element with row index i and column index j is calculated by the formula a[i][j] = i * j.

As always, you could use generator to create such an array:

[[i * j for j in range(m)] for i in range(n)]

"""
