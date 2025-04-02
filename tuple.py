"""
TUPLE
Tuples are used to store multiple items in single variable.
A tuple is a collection which is ordered and unchangeable 
they are written with round brackets.

EXAMPLE :
"""

# thistuple = ("apple","banana","cherry")
# print(thistuple)


"""
Tuple items
are ordered, unchangeable and allow duplicate values.
are indexed,the first item has index [0],the sec item has index [1] etc.


ORDERED

When we say that tuples are ordered,it means that items have a defined order,
and that order will not change.


UNCHANGEABLE 

Tuples are unchangeable, meaning that we cannot change ,add or remove items after the tuple has been created.


ALLOW DUPLICATES

Since tuples are indexed,they can have items with the same value:

EXAMPLE :
"""

# thistuple = ("apple","banana","cherry","apple","cherry")
# print(thistuple)


"""
TUPLE LENGTH
To determine how many items a tuple has ,use the len()function.

EXAMPLE :
"""
# thistuple = ("apple","banana","cherry","apple","cherry")
# print(len(thistuple))


"""
CREATE A TUPLE WITH ONE ITEM 
To do that ypu have to add a comma after the item or py will not recognize it as a tuple.

EXAMPLE :
"""

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))


"""
Tuple Items - Data Types
Tuple items can be of any data type:

Example
String, int and boolean data types:

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
A tuple can contain different data types:

Example
A tuple with strings, integers and boolean values:

# tuple1 = ("abc", 34, True, 40, "male")
"""
"""
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

Example
Using the tuple() method to make a tuple:
"""
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

a list and a tuple they allow duplicate members but the diff is 
a tuple is unchangeable and a list is changeable 

a set and a dictionary they dont allow duplicate members but the only difference is that a set is unordered , unchangeable and unindexed and a dictionary is changeable.

"""


"""
CHECK IF ITEM EXISTS 

to determine if a specified item is present in a tuple us the word in keyword:

EXAMPLE :
CHECK IF APPLE IS PRESENT IN THE TUPLE 
"""
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#    print("YES,'apple' is in the fruits tuple")
"""
PYTHON - UPDATE TUPLES 

tuples are unchangeable ,meaning you can not add,change or remove, BUT
there is a work around, you can convert the tuple into a list ,change the list , and convert the list back.
  

EXAMPLE :
CONVERT A TUPLE INTO A LIST ,ADD "orange",and convert it back into a tuple.

"""

# thistuple = ("apple","banana","cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)


"""
REMOVE ITEMS 

just like as said before you cannot add or remove items in a tuple,
but there is a work around to remove a tuple just as we did above we can convert it into a 
list and remove  items into the list and convert it back into a tuple.

example :
convert the tuple into a list and remove 'apple' and convert it back into a tuple 

"""
# thistuple = ("apple","banana","cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y) 
 
"""
DELETE A TUPLE 
YOU CAN DELETE A TUPLE COMPLETELY
                                             
EXAMPLE :
"""
# thistuple = ("apple","banana","cherry")
# del thistuple
# print(thistuple)# it will read an error because tuple will no longer exist.


"""
UNPACKING TUPLES 
when we create a tuple , we are normally assigning values to it. this is called "packing
a tuple :

for example 
fruits = ("apple","banana")
 but in python we are also allowed to extract the values back into variables.
 this is called unpacking.

 EXAMPLE:

"""
# cars = ("bmw","audi","mustang")
# (red, yellow, pink ) = fruits
# print(red)
# print(yellow)
# print(pink) 

### the number of variables must match the number of values in the tuple 
### if not , you must use an asterisk to collect the remaining values list.


##USING ASTERISK

"""
if the number of variables is less than the number of values ,you can add an * 
to the variable name and the values will be assigned to the variable as a list:

FOR EXAMPLE:

"""

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

###if the asterisk is added to another variable name than the last,py will assign values to the
##variable until2 number of values left matches the number of variables left

# tup1= (1,2,3,4,5)
# tup2 = (5,6,7,8,9)
# print(tup1 + tup2)
# print(tup1 * 2)
# print(len(tup1))
# print(max(tup1))
# print(min(tup1))

# x = list(tup2)
# print(x)
# tup2 = tuple(x)
# print(tup2)
 
# tuple  = ("john", "peter", "vicky")
# sorted(tuple)
# print(tuple)

# sorted(tup1) #this will sort the tuple in ascending order
# print(tup1)

names = ("john", "peter", "vicky", "james", "jane")
names.sort()
print(names)
# names.sort(reverse = "True")
# print(names)
# names.sort(reverse = "False")
# print(names)