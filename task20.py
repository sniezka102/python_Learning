"""
Question:
Define a function with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints:
Consider use yield
"""

def generatorFun(n):
    for item in range (0,n):
        if item % 7 == 0:
            yield item


for item in generatorFun(121):
    print(item, end=' ')