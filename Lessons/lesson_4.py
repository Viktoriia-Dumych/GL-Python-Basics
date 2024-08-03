"""
List comprehensions

"""
# a = []
# for i in range(12):
#     a.append(i)
# print(a)

# --- will be shorter
# b = list(range(15))
# print(b)

# --- will be much shorter
# c = [i for i in range(10)]
# print(c)

# --- using if inside
# d = [i * i for i in range(12) if i % 2 == 0]
# print(d)

# --- unpacking
# * Number of items should be equal to unpack

# a = [1, 2]
# b = a[0]
# c = a[1]
# or equals to
# [b, c] = a
# print(b, c)

# works the same with tuple
# a = [1, 2, 3]
# (b, c) = a

# ---
# d = (1, 2)
# equals to
# d = 1, 2
# b, c, d = a

# How to switch places in the most pythonic way
# a = [1, 2, 3]
# b, c, d = a
# a = 1
# b = 2
# a, b = b, a

# ---

a = [(1, 2), (3, 4)]
b = [i for i in a]

# better to
b = [i + j for i, j in a]

a = {1: 2, 3: 4}
a.items()
b = [i + j for i, j in a.items()]

# same as
# d = {1: 2, 3: 4}
# for key, value in d.items():
#     print(key, value)

# ----
# this will be generator, not tuple
a = (i for i in range(12))
type(a) # generator

# to make it tuple:
a = tuple((i for i in range(12)))

# --- set
a = {i for i in range(12)}
type(a) # set

a = {i % 3 for i in range(12)}

# dictionary
a = {i: i % 3 for i in range(12)}

"""
Built-in types

Booleans: True/False
Operators: and/or/not
Comparisons
Numeric Types: (int, float, etc)
Sequence Types: str, unicode, list, tuple, etc
Set Types: set, frozenset
Mapping Types - dict
File Objects
Other Built-In Types
Special Attributes

"""

"""
File Objects

cat file_name - shows what is in the file - not absolute path
cat /home/folder/folder/file_name - absolute path
Є відносний шлях - потрібно розуміти, в якій dir ми знаходимось
Повний шлях - можна доступитись незалежно від того, де ми знаходимось

!_ Better to always use full path _!



"""

a = open("/Lessons/lesson_1.py", "r")
print(a.read())
print("!!!!!!!") # will add this in the end of the file
print(a.read())
a.close()

# r mode - format of opening the file (read)/ File content is saved the way it was but file must exist
# w mode - file content will be deleted, and we can rewrite file. Can be unexisting. It will add to the end of our file
# always close() the file

# we can read all the file lines or specific ones

# This will rewrite
a = open("/Lessons/lesson_1.py", "w")
a.write("Hello")
a.close()

# --- Functions
# Functions are objects

def f(x:int, y:int):
    return x + y


print(f(4, 6))  # input parameters, can be any type


# duck type
# if we can add strings then we can pass strings into functions

def f2(a, b):
    r = 0
    for i in range(b):
        r += a + 1
    return r


print(f2(1, 2))

locals()
# locals() - returns all the available local vars

a = f2(12, 14)

print(locals())  # r will not be visible because it is not a global value

r = 12
def f3(a, b):
    r = 13
    for i in range(b):
        r += a + 1
    print(r)  # will be 39 (function result)
    return r


print(f3(12, 2))  # will be 39 (function result)

print(r)  # will be 12

# if we write 'global r' - r will be forced to change inside the function, so global r will not be stable

# when it is good to use global vars?

PI_NUMBER = 3.141592653589793  # magic number  # all constants should be written in caps

def round_square(r):
    a = r
    # print(id(a))
    # print(locals())  # will show only local a and r (scope)
    #  print("__________")
    # print(globals())  # will show all global items (scope)
    # print("---")
    return r * 2 * r * PI_NUMBER


round_square(12)
print("_______")
round_square(13)

# -------
#
def f4(conf):
    print(conf["url"])
    print(conf["name"])

f4({"url": "https://www.google.com", "name": "Google"})  # to pass dicts is not recommended

# how to perform correct passing
def f4(protocol, url, name):
    print(url)
    print(name)
    print(protocol)

f4("http", url="https://www.google.com", name="Google")  # positions can be switched, will work the same. Positional must always be before named

# default parameter
def f4(url, name, protocol="https"):  # protocol is now default value. Should always be immutable
    print(url)
    print(name)
    print(protocol)

f4(protocol="wss", url="https://www.google.com", name="Google")  # default protocol is rewritten now

print("___")
# args
def f4(protocol="http", *args):  # usual param -> default params -> args
    for i in args:
        print(i)

f4("wss", "https://www.google.com", "Google")

print("___")

# kwargs
def f4(number, *args, **kwargs):  # kwargs is dict
    for i in kwargs:
        print(i)

f4(12, 13, name="Google", url="https://www.google.com")