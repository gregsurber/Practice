#*************************************************************************
# Strings
#*************************************************************************
mystring = ""
string1 = "210450 Oct 17 20:29 Information ESENT 916 DllHost"

# How to assign values to a dict
# string to string
mystring1 = string1

# string to list after splint
mystring1 = string1.split()
mystring1 = string1.split(" ", 3)       # number of splots from the beginning -- 3 in this example
mysubstring = mystring1[0:3]            #slicing, indexing
# string formatting from date time information
import datetime
dt = datetime.datetime.now()
dtstr = f"{dt.month}/{dt.year} {dt.hour}:{dt.minute}:{dt.second}"
eventidstr = '102930'
mystring = f"ID={eventidstr}: {dtstr}"

# How to access values with slicing
mystring[0]
mystring[-1]
mystring[0:10]
mystring[12:30]
mystring[::-1] # reverses the string

# How to travers the list
# replace(), strips(), [r|l]find('x')
newstring = mystring.replace('2019', '2020') # not IN PLACE

test = '    tes t1   '
#strip()
test.lstrip()
test.rstrip()
test.strip()
#find()
test.find('t')
test.rfind('t')
# other methods
test.startswith(' ')
test[0].isnumeric()
test[1].isspace()
len(test)
