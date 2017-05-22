"""
task 04
Write a program which accepts a sequence of comma-separated numbers from console and generate 
a list and a tuple which contains every number.

Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')

"""
dataMatrix = input("podaj wartoci oddzielone przecinkiem")
#lista = [] - to jest nie potrzebne, ale nie wywołuje błedu
lista = dataMatrix.split(",")
print(lista)

#konwert list to tuple
#tupleData = () - to jest niezbędne, ale nie wywołuje błędu
tupleData = tuple(lista)
print (tupleData)

"""
how to convert list to tuple
lista = []
tuplek = tuple(lista)

how to convert tuple to lista
tuple = ()
lista = list(tuplek)

"""

