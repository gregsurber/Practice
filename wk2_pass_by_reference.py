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
