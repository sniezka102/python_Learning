"""
Question 30
Define a function that can accept two strings as input and print the string
with maximum length in console. If two strings have the same length,
then the function should print al l strings line by line.

Hints:
Use len() function to get the length of a string

"""
def selectTheMaxLenghtString(text1, text2):
    text1Lenght = len(text1)
    text2Lenght = len(text2)
    if text1Lenght > text2Lenght:
        print(text1)
    elif text2Lenght > text1Lenght:
        print(text2)
    else:
        print(text1)
        print(text2)

string1 = 'no to jestem jakims tam sobie tekstem'
string2 = 'co ty tam wiesz to ja jestem jakims tam sobie tekstem'
string3 = 'no bu jestem jakims tam sobie tekstem'
selectTheMaxLenghtString(string1,string2)
selectTheMaxLenghtString(string1,string3)
