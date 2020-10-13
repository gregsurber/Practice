#*************************************************************************
# passing my reference
# calling by preference
#*************************************************************************

def print_list(list1):
    print(list1)
    list1[0] = -999
    print(list1)

a = [1, 3, 9, 2, 'cat', 'dog', 0.24, '"eight"']

a_copy = a
print_list(a_copy)
print(a)
print(a_copy)

print("********************************************")
# This won't work even after you copy, since list is by nature reference.
# then now, you do this
import copy
a_copy = copy.copy(a)
print_list(a_copy)
print(a)            # this has kept the original values
print(a_copy)       

import copy
a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c

print(id(c) == id(d))           # True - d is the same object as c
print(id(c[0]) == id(d[0]))     # True - d[0] is the same object as c[0]

d = copy.copy(c)
print(id(c) == id(d))           # False - d is now a new object
print(id(c[0]) == id(d[0]))     # True - d[0] is the same object as c[0]

d = copy.deepcopy(c)
print(id(c) == id(d))           # False - d is now a new object
print(id(c[0]) == id(d[0]))     # False - d[0] is now a new object