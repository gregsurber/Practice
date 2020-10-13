#*************************************************************************
# 2. Dictionary
#*************************************************************************
# How to define an empty dictionary
mydict = {}

# How to initialize a dictionary
# setdefault(key, default_value) returns default value for the associated key when the key is first introduced
# mydict = {'a' : None, 'b' : None, 'c' : None, 'd' : None, 'e' : None}
mydict.setdefault('a', None)
mydict.setdefault('b', None)
mydict.setdefault('c', None)
mydict.setdefault('d', None)
mydict.setdefault('e', None)

# Hoe to assign values to a dict
# examples of different data types
mydict = {'a': 'apple', 'b' : 'ball', 'c' : 'corn'}
mydict1 = {'name' : 'John', 1 : [2,3,4]}
#using dict() constructor
# Note: {} requires ":"  {a:b,...}
#       [] requires ","  [(a,b),...]
mydict2 = dict({'a': 'apple', 'b': 'ball', 'c': 'corn'})
mydict3 = dict([('a','apple'),('b','ball'),('c','corn')])

#How to access values in a list
# access via keys
mydict['a']
mydict.get('b')

#*************************************************************************
# accessing dict
#           key: value, key:value, key:value...
person = {'name': 'John', 'age' : 22, 'status': 'single'}
print(person.get('name'))       # get value from key 'name'
print(person.get('age'))        # get value from key 'age'
print(person.keys())            # get all keys in person
print(person.values())          # get all values from person
person['age'] = 20              # change the value of 'age' to 20
print(person['age'])            # another way to get the value from age
# get() returns default value if key doens't exist
# dict[key] will return an error if the key doesn't exist

#accessing tuple
# similar to list
mytuple = (1,2,3)
another_tuple = (4,5,6)
print(mytuple[0])               # prints value in first position in tuple -- 1 for this example
print(mytuple[-1])              # prints value of last item in tuple -- 3 in this example

print(mytuple+another_tuple)    # concatenates bothe tuples and prints --  (1,2,3,4,5,6) in this example
print(max(mytuple))             # prints value in last position -- 3 in this example
if 3 in mytuple:    
    print('yes')                # prints 'yes' if asked for value exists in mytuple -- it does, so this printsa 'yes'

# tuple cannot be modified directly
# Can't add, can't delete items
# CAN delete the entire tuple

# membership testing
'a' in mydict.keys()            # checing for 'a' as a key
'apple' in mydict.values()      # checking for 'apple' as a value
('a', 'apple') in mydict.items()    # checking for the key-value pair 'a':'apple'

# sorting a dictionary by key
for key in sorted(mydict2):
    print(key, '->', mydict2[key])

# sorting a dictionary by value and then find the associated key via lisify the dictionary
for value in sorted(mydict2.values()):
    KL = list(mydict2.keys())
    VL = list(mydict2.values())
    key = KL[VL.index(value)]
    print(key, '->', value)

# a few more examples 
# cloning a dictionaru with fromkeys()
mydict3={}
mykeys = mydict2.keys()
mydict.fromkeys(mykeys)
values = 0
mydict3.fromkeys(mykeys, values)


# Conversions list -> tuple
# Conversions tuple -> list
# Conversions dict -> tuple
dict1 = {'a': 1, 'b': 2}
tuple(dict1.items())

dict1 = {'a': 1, 'b': 2}
list(dict1.items())
list(dict1.keys())
list(dict1.values())

# no slicing available for dictionary
# since slicing is possible only with integers

# How to add an entry in a dictionary
mydict.setdefault('a', None)
mydict.setdefault('b', None)
mydict.setdefault('c', None)
mydict.setdefault('d', None)
mydict.setdefault('e', None)

mydict['a'] = 'animal'
mydict['b'] = 'beach'
mydict['c'] = 'cat'
mydict['c'] = 'desk'

# mydict = {'a': 'animal', 'b': 'beach', 'c': 'cat', 'd': 'desk', 'e': None}

# How to remove an entry in a dictionary
# pop.('key') removes the entry by returning its associated value
mydict.pop('d')
# popitem() removes the last entry by returning both key and value
mydict.popitem()
# clear() removes all the items
mydict.clear()

# How to traverse the list
mydict2 = dict({'z': 'zebra', 'b': 'ball', 'c': 'corn'})
# iteration via unpacking each tuple
for key, value in mydict2.items():
    print(key, '->', value)

# iteration via items
for item in mydict2.items():
    print(item)

# iterattion via kesy
for key in mydict2.keys():
    print(key)

# iteration via values
for value in mydict2.values():
    print(value)
