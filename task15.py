"""
Question 15 -- Level 2
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program:
	9
Then, the output should be:
	11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
def swappedLetterToDigitInFormula(formulas):
  swappedValues = []
  for item in formulas:
    swappedValues = formulas.replace(item, a)
  return swappedValues



a = input ("write one value")
sumcia = 0

formula = "a+aa+aaa+aaaa"
swappedValues = swappedLetterToDigitInFormula(formula)

splitedFormula = (str(swappedValues)).split("+")

for item in splitedFormula:
  sumcia += int(item)


print("changed formula = ", swappedValues)
print("suma = ", sumcia)