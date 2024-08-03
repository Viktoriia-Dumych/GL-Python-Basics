"""
List Operators

a = [1, 2, 3, 4, 5]

To extract the last value:
len(a)
a[len(a)]-1]

or

a[-1]

Slices:

a[1:-1]
a[1:4] - from 1st to last specified
a[:4] from the first till the specified
a[:] - all items
a[1:4:2] -
a[::2] - every 2nd item


________________________________________

if - elif - else

bools - True, False -- bool()
0 / -0 is the only int that will be False. Same for 0.0
empty strings/lists/etc will be False
None will be False

Equals
1 == 1 - True
1 == 2 - False
a == [] - True
id(a) == id([]) - False

Not equal
!=

True and False == False
True or False == True
not True == False
not False == True

----------------------

to be sure that value will exist - make value = None first
pass do nothing
"""
# a = None
#
# if not ((1 > 2) or (2 < 3)) and [1]:
#     print("True")
#     a = 2
#     if True:
#         if False:
#             print("True")
#         else:
#             print("False")
# elif False:
#     pass
# elif True:
#     print(14)
# elif True:
#     print(16)
# else:
#     print("False")
#     a = 3
# print(a)

a = [2, 4, 6, 8]
b = 0

for i in a:
    if i != a[-1]:
        print(i, end=", ")
    else:
        print(i)

# for i in a:
#     b += i
#     print(i)
#     if i % 2:
#         print("odd")
#     else:
#         print("even")
# print(f"b = {b}")

for i in a:
    print(i)
    if i % 2:
        print("odd")
    else:
        print("even")
        continue
    print("accumulate odd number {}".format(i))
    b += i

print(b)
print("--------")
# ! else in for loop can be executed only if break was not run in the loop
# continue - is used when iteration has no point in its execution, however we need the next step.
# Also, it does not affect the else part in for loop

# a = range(100)
a = [2, 7, 6, 8]
# b = [0, 1, 2, 3]
# x range - from python 2

for i in range(len(a)):
    print(i)
    if a[i] % 2:
        print("odd")
        a[i] = None
    else:
        print("even")

print(a)

# -------
# While - requires bool
# internal loop = while True

a = 0
while a < 9:
    a += 1
    print(a)

else:
    print(f"{a+1} longer than {a}")



