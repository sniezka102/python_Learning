"""
Question 31
Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print "It is an odd number".
Hints:
Use % operator to check if a number is even or odd.
"""
def checkEvenOddNumber(number):
    if number % 2 == 0:
        print (number, ' It is an even number')
    else:
        print(number, ' It is an odd number')

checkEvenOddNumber(11)
checkEvenOddNumber(100)
