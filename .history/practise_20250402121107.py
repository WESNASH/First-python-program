# print("hello, World")

# variables in python 
# x = 5
# y = "unknown"

#This is a comment
# print("Hello, World!")

"""
Ths is a comment 
written in just 
more than just one line
"""

# print("hey, my babe!")


# variable 
"""
variable are containers for storing data
"""
#creating variables 
"""
Python has no command fo declaring a variable.
A variable is created the moment you first assign a value to it.

x = 5
y = 'John'
print(x)
print(y)
 variable dont need to be declared with any particular type
 and can even change type after they have been set.
 FOR EXAMPLE :
"""
# x = 4 # is of type int 
# x = 'Sally' # is of type string 


"""
CASTING
If you want to specify the type of variable ,this can be done with casting.

EXAMPLE 

x = str(3) # x will be "3"
y = int(3) # y wil be 3
z = float(3)# z will be 3.0
"""

#GET THE TYPE 
# You can get the data type of a variable with the type()function.
# EXAMPLE:
# x = 5
# y = "John"

# print(type(x))
# print(type(y))

# python variable -
#Multiple Values
# EXAMPLE 
# x,y,z = 'orange','banana','cherry'
# print(x)
# print(y)
# print(z)
#make sure the number of variables matches the number of values.
# or else you will get an error.
# One value to multiple values in one line:

# x = y = z = 'orange'
# print(x)
# print(y)
# print(z)
"""
Unpack a collection
 if you have a collection of values in a list ,tuple etc.Py allows you to
 extract the values into variables , this is called unpacking

 EXAMPLE:
"""
# fruits = ["apple","banana","cherry"]
# x,y,z = fruits 
# print(x)
# print(y)
# print(z)

# ### Unpacking a collection and assigning values to multiple variable in one line are almost the same just that
# ### unpacking a collection is unpacking a list in one line.

# # Output Variables
# # The Python print() function is often used to output variables.

# # Example
# x = "Python is awesome"
# print(x)
# # In the print() function, you output multiple variables, separated by a comma:

# # Example
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# # You can also use the + operator to output multiple variables:

# # Example
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)
# # Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# # For numbers, the + character works as a mathematical operator:

# # Example
# x = 5
# y = 10
# print(x + y)
# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# Example
# x = 5
# y = "John"
# print(x + y)
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

# Example
# x = 5
# y = "John"
# print(x, y)



###Py - Global Variables 
"""
variables that are created outside of a function (as all of the above )
are known as global variables.
can be used by every one ,both inside of functions and outside.

EXAMPLE :
"""

# x = "awesome"

# def myfunc():
#     print("I am " + x)
# myfunc()

"""
if you create a variable with the same name inside a function,this variable will
be local and can only be used inside the function,the global
variable with the same will remain as it was, global and with the original value.

EXAMPLE :

"""
# def myfunc():
#     x = "fantastic" ###LOCAL MEANING INSIDE A FUNCTION!!! and cam only be used inside a function not outside its function.

#     print("I am " + x)
# myfunc()

# print("python is " + x) ### thus global variable will remain as it was ,global and with the original value.


"""
THE GLOBAL KEYWORD 
normally, when you create a variable inside a function, that variable is local,
and can only be used inside that function.

to create a global variable inside a function , you can use the GLOBAl keyword.

EXAMPLE:
"""

# def myfunc():
#     global x
#     x = "brilliant"  ### if you use the global keyword the variable belongs to the global scope.
    
# myfunc()

# print("Wesnash is " + x) 


# x = "awesome" ###i would have called off this variable and the one 
###inside the function will be  working, because of the keyword called out inside the function.

# def myfunc():
#     global x
#     x = "brilliant"

# myfunc()


# print ("Wesnash is " + x)



"""
#####TYPE CONVERSION 

#YOU CAN CONVERT FROMM ONE TYPE TO ANOTHER WITH THE int(),float(),
# and complex() methods.

###EXAMPLE: =
x = 1 # int
y = 2.0 # float
z = 1j # complex 


#convert from int to float
a = float(x)

#convert from float to int 
b = int(y)

#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""


###RANDOM NUMBER
"""
Py does not have a random()function to make a random number,but
python has a built-in module called random that can be used to 
make random numbers:

###EXAMPLE 
"""
# import random 

# print(random.randrange(10,100))
   




   

### VINCENT AKUNETSA 
# username = ('admin')
# password = 1234
# username = input("Enter your name: ")
# password = int(input("Enter your password: "))

# if username == 'admin' and password == 1234:
#     print("Welcome to the system")
# else: 
#     print("Invalid username or password") 

# temp  = 30 
# condition = "sunny"
# temp = int(input("Enter the temperature: "))
# condition = input("Enter the condition: ")
# if temp >= 30 and condition == "sunny":
#     print(f"The weather is {condition}")
# else: 
#     print(f"The weather is {condition}")


# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers = int(input("enter a number: '"))



    
