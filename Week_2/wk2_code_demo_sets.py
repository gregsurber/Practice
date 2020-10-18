#*************************************************************************
# Set
#*************************************************************************
# How to define a set

set1 = set(['a1', 'a2', 'a3', 'a2', 'a4', 'a5'])
set2 = {'b1', 'b2', 'a1', 'a1', 'b5'}

# to print the elements in a set
for d in set1:
    print(d)

# Find common elements in 2 sets
def common_members(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")

a = [1,2,3,4,5]
b = [5,6,7,8,9]
common_members(a, b)

a = [1,2,3,4,5]
b = [6,7,8,9]
common_members(a, b)

# The following is done in the Python shell:
# >>> set1 = set(['a1', 'a2', 'a3', 'a2', 'a4', 'a5'])
# >>> set2 = {'b1', 'b2', 'a1', 'a1', 'b5'}
# >>> set1<=set2
# False
# >>> set1>=set2
# False
# >>> set1|set2
# {'a5', 'a3', 'a2', 'a4', 'b2', 'b1', 'b5', 'a1'}
# >>> set1&set2
# {'a1'}
# >>> set1-set2
# {'a4', 'a5', 'a3', 'a2'}
# >>> set2-set1
# {'b2', 'b1', 'b5'}
# >>> len(set1)
# 5
# >>> len(set2)
# 4
# >>> a = set('foo')
# >>> a
# {'f', 'o'}
# >>>
