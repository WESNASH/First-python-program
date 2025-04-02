###SETS 
"""
myset = {"apple","banana",cherry"}



they are used to store multiple values in a single variable.
is a collection which is unordered,unchangeable*,and unindexed.

### note that set items are unchangeable ,but you can remove items and add new items  

thisset = {"apple", "banana", "cherry"}
print(thisset)

UNORDERED 
means that the the items in a set do not have a defined order.
set items can appear in different order every time you use them,
and cannot be referred to by index or key.

UNCHANGEABLE 

set items are unchangeable ,meaning thta we cannot change the items after the set has been created.
"""

# my_set = {"apple","banana","cherry"}
# print(type(my_set)) #<class 'set'>


# SET ITEMS
# set items are unordered, so you cannot be sure in which order the items will appear.

"""
union() method returns a new set with all items from both sets.
 my_set_2 = {1,2,3,4,5}
my_set_3 = {6,7,8,9,10}

union_set =my_set_2 | my_set_3
print(union_set) # {1,2,3,4,5,6,7,8,9,10}
union_set = my_set_2.union(my_set_3)
print(union_set) # {1,2,3,4,5,6,7,8,9,10}

###intersection 
is a method that returns a new set containing items that are present in both sets.
### for example :
"""
my_set_2 = {1,2,3,4,5}
my_set_3 = {4,5,6,7,8}
intersection_set = my_set_2 & my_set_3
print(intersection_set) # {4,5}

