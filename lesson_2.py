# === Data Types ===
# --- Immutables

# snake_case - better to use in python community
# camelCase

# --- Mutables
# If we change list1, and list2 equals list1, both lists will be changed

# In Python, we do not have arrays, we have lists instead

# to check in terminal in what memory "cell" a created obj is located: id(previously_created_var_name)
# if var's value is rewritten to another value, its id will be the same
# to start doing smth with vars in terminal - first write python3 in terminal

# _______________

# - Numbers - integers (immut)

# to check var type: type(my_var). Output: <class 'int'>


# ---Data Types

# Integer is an object
# dir(a)
# a.bit_count
# help(a)


# ! Garbage Collector
# If at list one var is referring to our obj - the object is alive.
# As soon as no var is referring to the obj - it will be marker as obj to remove by garb.coll.
# When there will be lack of memory, the obj will be deleted
# In general, in Python there is no need to take care of memory leak

# ---Float (immut)
# Complex number - sqr from -1

# a += 1 (incl. /, *, //, etc)
# // - we divide but take only int, without float nums

# When we divide int by int - we receive float
# if we want to make int - a float one, we just write int with a comma (2.0)

# ---Strings (immut)

# obj with a string cannot be changed. After using string methods, only the reference of "a" will be changed, not a as an obg=j

# a = "hello {}"
# a.format("Inn")
# output: 'hello Inn'

# To make string with several rows: 'hello\nworld' or
# '''hello
# ...world'''

# Strings support ariphmetical operations (concatenations - +, *)

# To turn str into int use int(string_value)


# None (immut)
# Better to use as a default value (NoneType class)
# dir(a) - to check methods
# help(a) - to check description


# --- MUTABLE OBJECTS

# Lists (mut)
# len(a) - to check the length of the obj

# matrix: [[0, 1], [2, 3]]
# What not to do:
# 1. a[0] = a - reference on itself
# output: [[. . .], [2, 3]]
# 2. a = [], b = [a]
# a[0] = b
# output: [[[. . .]]]

# a + [1] - concatenation

# --- Tuple
# Tuple do not save data, only references to the data, so we can put lists in tuples. It's like a multiple references
# So, tuple is immutable - this is the main diff between tup and list. It cannot be changed.
# Should we put mutable values into immutable tuple - NO.
