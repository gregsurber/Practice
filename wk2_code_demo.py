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


