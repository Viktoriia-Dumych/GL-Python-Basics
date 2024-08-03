from time import time

# -------------------
# DOC String

"""
Multi-line string

@number - int
"""

# Useful built-in functions

"""
# ---
open() - to open a file

# ---
eval() - we can execute everything everywhere
a = 1+2
b = "1+a"
output: aval(b) = 4

Better not use eval in prod !

# ---
pow()
tuple()
filter()
len()
range()
print()
type() - return obj type
float()
list()

# ---
input()

a = input("Please enter your password\n")
Can be used for learning tasks / debugging
Better not use it in prod

! Auto scripts may stuck during auto testing with inputs

# ---
reduce() - like map()
repr () - similar to str()
compare() - to compare elements
max()
hasattr() - if a specific attribute is present
round()
hash()
min()
set()
help()
dict()
hex()
slice() - can be used with strings to slice it by an element
dir() - properties
oct()
sorted()

"""

# Modules & Packages

# Modules - python files (e.g. main.py)
# Package - python folders (can be imported with python)

# from <module> import <instance>

"""
e.g.
pack - folder
__init__.py - must always be used
mod.py

if __name__ == '__main__':
    print(__name__)

to import in another file:

import pack.mod as my_mod / from pack.mod import f
from my_mod/mod import MY_FUNC

! Each time we import module, code in the file is executed

my_mod.f(1, 2) - to call for the existing function in the imported file

"""

# to check for python path:
# import sys -> sys.path
# Never add module path inside the package

# Bad Practice
# from pack.mod import *
# Reasons: we do not know what could be changed in our imported modules

# ------------------------
# CLASSES

"""
Python is very object-oriented language
OOP Idea: 

Class - is what defines an object (properties, methods, attributes of the object)
Class can have attributes
Methods - functions inside object
Attributes - vars inside instances
Instances - 
self - pointer to our future class object. So, the first argument should be 'self'

"""


class MyClass:  # class
    # a = 1  # attribute
    # b = 2  # attribute

    def __init__(self):
        self.a = []

    def f1(self):
        self.a.append(1)

    def f2(self):
        self.a.append(2)

    def f3(self):
        self.a.append(3)


a = MyClass()  # instance
b = MyClass()

for i in (a, b):
    i.f1()
    i.f2()
    i.f3()

print(a.a)
print(b.a)

# OOP Principles

"""


1. Encapsulation - one obj is inside another obj

a - visible outside the class (public)
__a - won't be visible outside the class (private)
to print them out, we should write self.__a inside the method
_a - will be visible outside the class but can be changed only with inheritance (protected)


How to hack invisible elements:
a.__a - we can't reach it as it is hidden
instead we can:
a._MyClass__a
can be used for debug

How to know what type to use:

__init__ - magic method that is called by itself when class/new obj is created. Allows us to know time of its creation or amount

(from time import time)

"""


class MyClass2:  # class
    # a = 1  # attribute
    # b = 2  # attribute

    def __init__(self):
        self.__a = []
        self.__creation_time = time()

    def time(self):
        print(f"object was created at: {self.__creation_time}")
        self.__a.append(1)


a = MyClass2()  # instance
print(a.time())

"""
2. Polymorphism - when objects share the same methods. One global idea is implemented inside objects in different ways

"""

class Cat:
    @staticmethod  # decorator - when we do not want to use self
    def say_hi_to(name):
        print(f"Meow - {name}")


class Dog:
    @staticmethod
    def say_hi_to(name):
        print(f"Bow-Wow - {name}")


def say_hi_to(animal, name):  # animal is our object
    animal.say_hi_to(name)


a = Cat()
b = Dog()
# say_hi_to(a, "Luna")
# say_hi_to(b, "Rex")


# Duck typing - means that if our obj has all methods that animal has - it is animal

"""
decorators: forced change of our function

@classmethod - change our method. Instead of self we use cls in function. Reference to class instead of object
"""

"""
3. Inheritance - child inherits methods of its parent

"""

class Cat1:
    @staticmethod  # decorator - when we do not want to use self
    def say_hi_to(name):
        print(f"Meow - {name}")


class Dog1:
    @staticmethod
    def say_hi_to(name):
        print(f"Bow-Wow - {name}")

    @staticmethod
    def bite():
        print("Rrrr")


def say_hi_to(animal, name):  # animal is our object
    animal.say_hi_to(name)
    animal.bite()


class BigDog(Dog1):
    def say_hi_to(cls, name):  # animal is our object
        print(cls)
        print(f"Grrr {name}")

class SmallDog(Dog1):
    @staticmethod
    def bite():
        print("sorry")


a = BigDog()
b = SmallDog()
say_hi_to(a, "Luna")
say_hi_to(b, "Rex")