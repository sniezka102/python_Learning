# coding=utf-8
"""
sprawdzenie warunkow zbudowania trójkąta

"""
import math
A = [0,0]
B = [1,1]
C = [10,12]

def calcSideOfTriangle(a,b):
    sideLength = ((b[1]-a[1])**2 + (b[0]-a[0])**2)**0.5
    return sideLength

AB = int(calcSideOfTriangle(A,B))
print(AB)
AC = int(calcSideOfTriangle(A,C))
print(AC)
BC = int(calcSideOfTriangle(B,C))
print(BC)

if AB == max(AB,AC,BC):
    if (AB == AC + BC):
        print("it is possible to build a triangle")
    else:
        print("not possible to build a trianlge")
elif AC == max(AB,AC,BC):
    if (AC == AB + BC):
        print("it is possible to build a triangle")
    else:
        print("not possible to build a trianlge")
else:
    if (BC == AB + AC):
        print("it is possible to build a triangle")
    else:
        print("not possible to build a trianlge")
