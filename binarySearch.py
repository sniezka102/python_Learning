"""
Question 69
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
Hints:
Use if/elif to deal with conditions.
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html:

def binarySearch(alist, item):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == item:
9	            found = True
10	        else:
11	            if item < alist[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15
16	    return found
17
18	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19	print(binarySearch(testlist, 3))
20	print(binarySearch(testlist, 13))

"""
sortedList = [3,5,6,8,11,12,14,15,17]

#to jest jak metoda zlotego srodka
def binarySearch(lista,searchingParameter):
    firstCheck = 0
    lastCheck = len(lista)-1
    isFound = False

    while (firstCheck <= lastCheck) and not isFound: #dopoki wartosc 1 jest mniejsza od ostatniej
                                                    #i parametr isFound wciaz nie jest true
        middleCheck = (firstCheck + lastCheck) / 2 #podzial srodka
        if lista[middleCheck] == searchingParameter: #sprawdzenie czy wybrany punkt srodka
                                                    #jest szukanym parametrem
            isFound = True                #jak tak to zwroc ze zostal znaleziony parametr
            return lista.index(searchingParameter) #HERE IS MY OWN INVESTION
        else:
            if searchingParameter < lista[middleCheck]: #only in case the sorted list
                lastCheck = middleCheck - 1
            else:
                firstCheck = middleCheck + 1
    return isFound


print(binarySearch(sortedList,10))
print(binarySearch(sortedList,8))
