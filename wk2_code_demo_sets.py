#*************************************************************************
# Set
#*************************************************************************
# How to define a set

set1 = set(['a1', 'a2', 'a3', 'a2', 'a4', 'a5'])
set2 = {'b1', 'b2', 'a1', 'a1', 'b5'}

# to print the elements in a set
for d in set1:
    print(d)

# The following is done in the Python shell:
>>> set1 = set(['a1', 'a2', 'a3', 'a2', 'a4', 'a5'])
>>> set2 = {'b1', 'b2', 'a1', 'a1', 'b5'}
>>> set1<=set2
False
>>> set1>=set2
False
>>> set1|set2
{'a5', 'a3', 'a2', 'a4', 'b2', 'b1', 'b5', 'a1'}
>>> set1&set2
{'a1'}
>>> set1-set2
{'a4', 'a5', 'a3', 'a2'}
>>> set2-set1
{'b2', 'b1', 'b5'}
>>> len(set1)
5
>>> len(set2)
4
>>> a = set('foo')
>>> a
{'f', 'o'}
>>>
