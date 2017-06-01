"""
Question 10 - Level 2
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
break

Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""

lines = []
print("add the text line, write 'break' if you want to finish action\n")
while (True):
  inputString = input()
  if inputString:
    lines.append(inputString)
   else:
    break


lines = "".join(lines) #The method join() returns a string in which the string elements of sequence                    
words = lines.split(" ")

allWords = set(words) #Test if every element in the set is in other.

print(" ".join(sorted(allWords))) #sortowanie

"""
Maćka sugestie do zmian:
task 10

L20 to jest niepotrzebne, w treści nie ma nic o tym, że to ma być w pętli
L29 widzę, że 'oryginalne' rozwiązanie jest takie samo, ale w treści jest
    że mają być rozdzielone przez whitespace character. Whitespace to też
    na przykład tabulacja.
    https://pl.wikipedia.org/wiki/Znaki_niedrukowalne
    Czy jest w pythonie:
    a) wariant split, który przyjmuje set/array znaków, które są "dzielącymi"? - w zadaniu jest zastosowane metoda podziału 
                                                                                całego tekstu poprzez usunięcie znaków ich dzielących
                                                                                w przypadku białych znaków jest to split(" ")
                                                                              
    b) jakieś utility (coś na stringu?), które zwraca whitecharactersSet? - nie wiem czy dokładnie o to chodzi, ale jest metoda sprawdzająca 
                                                                            czy dany string jest white, jest to .isspace()
                                                                            


"""
