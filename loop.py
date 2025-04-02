### Loops
##is a way to repeat a block of code multiple times. 
# There are two types of loops in Python, for loop and while loop.


##while loop
# The while loop is used to iterate over a block of code as long as the test expression (condition) is true.
# The test expression is given inside the parenthesis ().
# The block of code inside the loop will be executed as
# long as the expression is true.
# The block of code inside the loop should be indented.
# The loop continues until the test expression is false.
# The while loop is used when the number of iterations is not known in advance.
# for example : when you want to take input from the user until the user enters a specific value.
# The while loop is also used to iterate over a sequence like list, tuple, string, etc.
"""i = 0
while i < 5:
    print(i)
    i += 1 
    """#increment the value of i by 1,it will create numbers from 0 to 4
#to increment is to add a fixed value to a variable
#to decrement is to subtract a fixed value from a variable
#so in this case 1 is added to i each time the loop runs until i is less than 5
#so i is 0,1,2,3,4 added by 1 each time the loop runs.
#when i is 5 the loop stops because the condition is false.
#The loop will run until the condition is false.

# guess = 0
# answer = 7
# while guess != answer:
#     guess = int(input("you guessed wrong,guess again: "))
# print("You guessed it right!")


#####GUESS NUMBER 
"""
answer = 7
guess = int(input("Guess a number: "))
while guess != answer:
    if guess > answer:
        print("Guess Again! The number is higher")  

    else:
        print("Guess Again! The number is lower")

    guess = int(input("Wrong number,Guess again: "))
print("You guessed it right!")    

"""
"""
#The loop will run until the condition is false.
###KUDZIS CODE 

while n!= 7:
    if n < 7:
        print('Your number is less than the expected number')
        n = int(input(f'Guess another value greater than {n}: '))  
    else:
        print('Your number is greater than the expected number')
        n = int(input(f'Guess another value less than {n}: '))  
print('You won')
"""


"""
INFINITE LOOP
#An infinite loop is a loop that runs indefinitely and never stops.
#The condition of the loop is always true.
#An infinite loop can be created using the while loop.
#The while loop runs as long as the condition is true.
#If the condition is always true, the loop will run indefinitely.
For example:
while True:
    print("Hello, World!")
#The loop will run indefinitely because the condition is always true.
"""


# ####car game
# command =  ''



# while True:
#     command =  input("enter command ").lower()
#     if command == 'start':
#         print("Car started...")
#     elif command == 'stop':
#         print("Car stopped...")
#     elif command == 'help':
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that...")


## count down
# n = 10
# while n >  0:
#     print(n)
#     n -= 1
 #The loop will run indefinitely because the condition is always true.
       #The while loop runs as long as the condition is true.
              #The condition of the loop is always true.

"""
FOR LOOP
is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
are used to repeat a code of blocks multiple times in a sequence.
Syntax:
for element in sequence:
    # block of code

The for loop iterates over a sequence.
The sequence can be a list, tuple, string, sets,dictionary, or any other iterable object.
The block of code inside the loop should be indented.
The loop continues until the sequence is exhausted.
The for loop is used when the number of iterations is known in advance.

Example:
"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

#The for loop iterates over the fruits list.
"""
looping through a string 
for example : loop through the letters in "banana"->
"""
# for x in "banana":
#     print(x)
#The for loop iterates over the string "banana".

"""
the break statement 
is used to exit the loop.
The break statement is used to exit the loop.
we can stop the loop before it has looped through all the items.

FOR EXAMPLE :
"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break


""" 

THE CONTINUE STATEMENT

is used to skip the current iteration of the loop and continue with the next iteration.
WE CAN STOP THE CURENT SITUATION AND CONTINUE WITH THE NEXT ITERATION.
FOR EXAMPLE:
 """
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

#The loop will skip the iteration where x is "banana".

"""
THE RANGE () FUNCTION
"""
# num = 10
# while num > -1:
#     print(num)
#     num -= 1


    ### even numbers]
 ### for example:
for x in range(2, 11, 2):
    print(x)

    ##1 to 50 but it must skip the number that is diviblr by 5

    ##for example :
 

