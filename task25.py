#-*- -coding: utf-8 -*-
"""
Question 25 - Level 1
Question:
   Define a class, which have a class parameter and have a same instance parameter.
Hints:
   Define a instance parameter, need add it in __init__ method. You can init a object with
   construct parameter or set the value later


the class parameter is the parametr which is created in the class pole.
the instance parameter
"""
class CreateTheInstance:
    theClassParameter = "fruit" #określane jako zmienna statyczna
    def __init__(self,theClassParameter):
#teraz przypiszą instację klasy do utworzonego parametru
        self.theClassParameter = theClassParameter

objectClass = CreateTheInstance("apple") #utworzenie obiektu instancji
objectClass01 = CreateTheInstance("pineapple")
#najpierw poprzez nazwę klasy odnoszę się do parametru statycznego klasy
#natomiast przez utowrzenie obiektu i przepisanie do niego jakiegoś argumentu
#powoduje wydruk argumentu przekazanego do klasy
print('first ', CreateTheInstance.theClassParameter,' is = ', objectClass01.theClassParameter)
print('second ', CreateTheInstance.theClassParameter,' is = ', objectClass.theClassParameter)

