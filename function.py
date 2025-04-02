"""
PYTHON FUNCTIONS
is a block of code which only runs when it is called.
you can pass data,known as parameters, into a function.
can return data as a result.


### Creating a Function
In Python a function is defined using the def keyword:

syntax:
def function_name(parameters or arguments):
    # block of code-to be executed
    function_name() #calling a function,return value.


 ## why do we need functions?
- to avoid repetition of code./ reduce code duplication.
- makes the code easier to understand./organisation of data and code.
- makes the code easier to test.
- makes the code easier to debug.
- makes the code easier to maintain.
- makes the code more readable.
- makes the code reusable.
- makes the code more efficient.

 
FOR EXAMPLE:
"""
# def greet():
#     print("Welcome to Python Functions")

# greet()
#The function greet() does not have any parameters.

### a function with one parameters
# we need parameters to pass data to a function.

#Example:
# def greet(name):
#     print("Welcome to Python Functions", name)
# greet(input("Enter your name: "))
#The function greet() has one parameter name.
 #if you just want to use strings thats when you only use print and input functions.

 ### miltiple parameters
 ##for example:


# def add(a,b):
#     return a + b ## beacuse we need a value to be returned.
# ##now we want to create a variable for the function add
# # result = add(2,3)## this means we are now comparing results and add.
# print(add(2,3)) ## we using print because we have created a variable.


#first we define a function with def
#then we give the function a name
#then we give the function parameters inside the parenthesis
#then we give the function a block of code to be executed inside the function.
#then we call the function by using the function name and passing the parameters.
#then we print the result of the function.

"""
POSITIONAL ARGUMENTS 
arguments are passed according to their order.

for example:
"""
# def power (base ,exponent) :
#     return base ** exponent
# print(power(2,3))
"""
KEY WORD ARGUMENT 

"""
"""
DEFAULT ARGUMENT
 A default argument in Python is a value that you specify in a function definition.  
 This value is automatically used if no argument is provided when the function is called.
 It’s a way to make parameters optional.



"""

# def greet (name = ""):
#     print(f"HELLO,{name}")

# greet()



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


"""
nested functions 


FOR EXAMPLE :
"""
# def outer():
#     print("this is outer function")
#     def inner():
#         print("this is inner function")
#         outer() 
#         inner()
# outer() ##calling a global function inside a local function..


def global_function():
    print("my function")

global_function()

def another_function():
    global_function()
global_function()

       
