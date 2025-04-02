# ##control structures 
# if statement,is used to execute a block of code if a certain condition is true.
# for example
x = 5
if x > 10:
    print("x is greater than 10") #so this code could not be executed because its False
# if x < 10:
#     print("x is less than 10") 
 

#  # Elif statement 
#  # short for else if statement aka is used to check if another initial  condition is false
#  # for example 
# if x > 10:
#     print("x is greater than 10")
# elif x ==5:
#     print("x is equal to 5") 


# #Else statement 
# #is used to execute a block of code if all the conditions in the if and elif statements are False.
# #for example 
# if x > 10:
#     print("x is greater than 10")
# elif x ==3:
#     print("x is equal to 3") 
# else:
#     print("x is not greater than 10 and not equal to 3")


# #Nested if statements
# #used to check multiple conditions 
# #for example 
# y = 3
# if x > 10:
#   if y == 3:
#       print("x is greater than 10 and y is equal to3")
#   else:
#       print("x is not greater than 10")

# register = 'absent'
# name = 'wesley'
# if register == 'present':
#       print(f"{name} is {register}") 
# else: 
#       print(f"{name} is {register}") 


# code indentation  
# if statement is indented by 4 spaces
# if statement without indentation will raise an error
# for example
# x = 5
# if x > 10:
# print("x is greater than 10") #this will raise an error because the if statement is not indented

##F-string are type of string formatting that allows you to embed expressions inside string literals, using curly braces {}.
# for example
# name = "wesley"
# age = 22
# print(f"My name is {name} and i am {age} years old")


# username = "admin"
# password = 1234 


# if username == "admin" and password == 1234:
#      print("welcome admin")
# else: 
#      print("invalid password") 

A = 90
B = 80
C = 70
D = 60

marks = 100
marks = int(input("Enter your marks: "))
if marks >= A and marks <= 100:
    print("You have an A")
elif marks >= B and marks <= 89:
    print("You have a B")
elif marks >= C and marks <= 79:
    print("You have a C")
elif marks >= D and marks <= 69:
    print("You have a D")
elif marks < 60:
    print("You have an E")
else:
    print("you have failed")
