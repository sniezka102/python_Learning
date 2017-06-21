""""
Question 22 - Level 3
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
	New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
	2:2
	3.:1
	3?:1
	New:1
	Python:5
	Read:1
	and:1
	between:1
	choosing:1
	or:2
	to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

napisać program który oblicza częśtość wystąpienia danego słowa w wejściu
dane wyjściowe powinny zostać posortowane
"""

print("please write own sentence")

inputCollection = []        #utworzenie listy aby zebrac slowa z wyrażenie, które zostały podzielone na pojedyncze wyrazy
while True:
    sentence = input()
    inputCollection.append(sentence) #dodanie całego wyrażenia do listy
    if not sentence:
        break
inputCollection = inputCollection[0].split(" ") #podział wyrażenie po spacjach

wordCalculation = {}    #utwprzenie słownika
for item in inputCollection:
    wordCalculation[item] = wordCalculation.get(item, 0) + 1 #utworzenie slownika, gdzie kluczowi, przypisane sa wartosci
                                                    #wyrazy ktore jak juz wystepuja to dodaje sie jeden
                                                    #jak nie to zwracana jest wartość zero

singleWord = list(wordCalculation.keys())
singleWord.sort()
for item in singleWord:
    print(item,':',wordCalculation[item])
