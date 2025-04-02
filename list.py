#  is used to store multiple values in a single variable
# # #for example
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# mixed = [1, "apple", 3.1, "banana",True ]
# print(mixed)

#accessing data types in a list
# indexing is used to access an item in a list by referring to the index number.
# we use negative or positive to index an element in a list
# positive indexing starts from 0
# negative indexing starts from -1
# the last number is represented by -1
# the second last number is represented by -2
# # #for example
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])
# print(fruits[-2])

# # #slicing is used to access a range of items in a list by using the colon operator.
# # # we use a method called start:stop:step
# # # start is the first index
# # # stop is the last index
# # # step is the increment
# # #for example
# list_numbers = [10, 20, 30, 40, 50, ]
# print(list_numbers[1:4])
# print(list_numbers[1:3])
# print(list_numbers[1:5:2]) #this will print the first index, the last index and the increment
# print(list_numbers[0:3])


# #modifying a list
# list_numbers[0] = 5
# print(list_numbers)

# adding an element inside a list we have 2 methods 
#append adds an element at the end of a list
# insert inserts an element at a specified position
fruits = ["apple","bananas","orange","peaches"]
# fruits.append("peach")
# print(fruits)
fruits.remove("apple")
print(fruits)
fruits.clear()
print(fruits)




