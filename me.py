###intro 

print("Welcome!!")

print("To your own hell, you made deals with the devils, face it!")


"""
Variables examples:

"""
fav_numbers = 7,3,21
nickname  = "Wesnash"
name = "Wesley"
surname = "doesn't really matter!"
sec_name = "Tadiwanshe"
girlFriend = "not of your concern"
age = 22
DoB = 2002
lbs  = 56.9
most_used_num = 21
place_holder = 7.3

### multiple VARIABLES 
name,surname,sec_name,nickname =  "Wesley","doesn't really matter!","Tadiwanshe","Wesnash"
name = surname = sec_name = nickname = "Wesnash"

## GLOBAL VARIABLES AND LOCAL VARIABLES IN A FUNCTION 

nick_name = "WESNASH" ##global variable

def mina():# function 
    nick_name = "tadiwanashe"### local variable
    print(f"The Greatest is {nick_name} that's me.")

mina()# calling out the function 
print(f"The Greatest is {nick_name} that's me."+ nick_name )

print(fav_numbers)
print(nickname)
print(name)
print(surname)
print(sec_name)
print(nickname)
print(girlFriend)
print(age)
print(DoB)
print(lbs)
print(most_used_num)
print(place_holder)

##ADDING OPERATORS TO VARIABLES 
print(name + surname + sec_name + nickname )

### SEPARATING VARIABLES WITH A COMMA 
print(name,surname,sec_name,nickname)



"""
DATA TYPES 

EXAMPLES:
"""


nickname  = str("Wesnash")
name = str("Wesley")
surname = str("doesn't really matter!")
sec_name =str( "Tadiwanshe")
age = int(22 )
DoB = int( 2002)
lbs  = float(56.9)
most_used_num = int( 21)
place_holder = float( 7.3)
car_collection = list(("BMW","SUPRA","RAM","LANDROVER"))
name_order =  tuple(("Wesnash","Wesley"))
myself =  dict(
    nick_name = "Wesnash",

    age = 22
)
fav_fruits =  set(("apple", "banana", "cherry"))
street_num = bool(21)

##slicing


print(nickname[1:3])
print(name[:4])
print(nickname[-1:-2])
print(girlFriend[0:-1])


##lists

##creating a list 
car_collection = ["BMW","SUPRA","RAM","LANDROVER"] ##  a list has square brackets 
fav_fruits =  ["apple", "banana", "cherry"]
###adding an element 
car_collection.append("CAMARO")

##REMOVING 

car_collection.remove("RAM")

###slicing 

car_collection_likkle_set = car_collection[1:-6]

###finding length 

print(len(car_collection))


#extend method 
car_collection.extend(fav_fruits)
print(car_collection)

car_collection.reverse()
print(car_collection)




####list methods 
"""
append() adds element at the end of the list 
clear() removes all the elements from the lis
copy() returns a copy of the list
count() returns the number of elemts of the specified value
extend()add the elements of a list or any iterable, to the end of current list 
index()retuns the index of the first element with the the specified value 
insert()adds an element at the specified position
pop()removes the element at  the specified positon 
remove() removes the item with the specified value 
reverse() reverses the order of the list
sort() sorts the list 
""" 

##dictionary 

myself = {
    "name": "wesley",
    "age": 22,
    "location": "mufakose"
}
## a dictionary contains curly brackets,semi-colon,a key and a value and a key is quoted.

mother =  {
    "name": "chengetai",
    "age": 39,
    "occupation":"botswana"

}

father = {
    "name": "forward",
    "age": 49,
    "occupation": "botswana"
}

mom = {
    "name": "chipo",
    "age": 39,
    "occupation": "bindura"
}

print(myself)
print(mother)
print(father)
print(mom)
print(len(mom))
print(type(mother))
"""
x = mom("name") ## accessing the key in a dictionary 
x = mom.get("occuaption") ##also anotherr method to get a key in a dictionary
x = mother.keys() ##this method returns all the keys in the dictionary 

print(x)

mom["condition"] = "healthy"
##this updates the dictionary as well 

print(x)

x = mom.values()### returns all the values
"""
###remove 
mom.pop("age")
print(mom)### removes the value with the specified name 


mom.popitem()
print(mom)### removes the last inserted item 

"""
del mother["occupattion"]
print(mother)## this del keyword eomes the item with specified key name
### it can also delete the dictionary completely for examaple:
# del mom 
# print(mom) this will cause an error because "mom" no longer exists

father.clear()
print(father)## this method empties the dictionary 
"""

####sets 

artist = {"young thug","gunna","tory lanez"}#usede to store multiple items 
#sets are unchangeable but you add or remove items 

##for example:

friends =  {"hiltoney","henrixy","keith"}
ex = {"lizzie","purpose","rose"}
num = {1,2,3,4,5}
even = {2,4,6,8,10}
mixed = {3,True,"current",21.1}
bool = {False,True,False,True}

print(artist)
print(ex)
print(even)
print(num)
print(friends)
print(bool)
print(mixed)

print(len(artist))
print(len(ex))
print(len(friends))
print(len(artist))
print(len(num))
print(len(bool))
print(len(mixed))


print(type(mixed))
print(type(artist))
print(type(num))


Artist= set(("adele","ice spice","nick minaj"))# the set constructor
print(Artist)

print("young thug" in artist)
print('keith' in friends)
print(1 in num)
print(True in bool)


artist.add("tunchi")
ex.add("mufaro")
friends.add("kingston")
# even.add(12,14)
num.add(7)

print(artist)
print(ex)
print(friends)
print(num)
# print(even)


artist.remove("young thug")
ex.remove("mufaro")
friends.remove("kingston")
# even.remove(12,14)
num.remove(3)

print(artist)
print(ex)
print(friends)
print(num)
# print(even)

artist.discard("tory lanez")
ex.discard("lizzie")
friends.discard("hiltoney")
# even.discard(8,10)
num.discard(2)

print(artist)
print(ex)
print(friends)
print(num)
# print(even)



thistuple = ("apple","banana","cherry")
print(thistuple)


thistuple = ("apple","banana","cherry","apple","cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) 

# cars = ("bmw","audi","mustang")
# (red, yellow, pink ) = fruits
# print(red)
# print(yellow)
# print(pink) 

for me in artist:
    print(me)

for fruit in fav_fruits:
    print(fruit)

for mycar in car_collection:
    print(mycar)

for friend in friends:
    print(friend)

for b in bool:
    print(b)

# for me in range (len(artist)):
#     print(artist[me])

# for fruit in range(len(fav_fruits)) :
#     print(fav_fruits[fruit])

# for mycar in range (len(car_collection)):
#     print(car_collection[mycar])

# for friend in range (len(friends)):
#     print(friends[friend])

# for b in range (len(bool)):
#     print(bool[b]) 



# loops
for me in artist:
    print(me)
    if me == "tory lanez":
        break

for fruit in fav_fruits:
    print(fruit)

    if fruit =="banana":
        break

for mycar in car_collection:
    print(mycar)
    if mycar == "RAM":
        break

for friend in friends:
    print(friend)

    if friend == "henrixy":
        break

for b in bool:
    print(b)

    if b == True:
        break

for me in artist:
    if me == "tory lanez":
       continue 
print(me)

for fruit in fav_fruits:
    if fruit =="banana":
        continue
print(fruit)

for mycar in car_collection:
    if mycar == "RAM":
        continue
print(mycar)

for friend in friends:
    if friend == "henrixy":
        continue
print(friend)


for b in bool:
  
    if b == True:
        continue
print(b)


i = 0
while i < 7:
    print(i)
    i += 1 

n = 10
while n >  0:
    print(n)
    n -= 1

num = 3

while num < 10:
    print(num)
    num += 1


# while me < 6:
#     print(me)
#     me += 1
# else:
#     print(f"{me}is no longer less than 6")

while n!= 7:
    if n < 7:
        print('Your number is less than the expected number')
        n = int(input(f'Guess another value greater than {n}: '))  
    else:
        print('Your number is greater than the expected number')
        n = int(input(f'Guess another value less than {n}: '))  
print('You won')



def myfunc():
    global x
    x = "brilliant"  ### if you use the global keyword the variable belongs to the global scope.
    
myfunc()

print("Wesnash is " + x) 


x = "awesome" ###i would have called off this variable and the one 
##inside the function will be  working, because of the keyword called out inside the function.

def myfunc():
    global x
    x = "brilliant"

myfunc()


print ("Wesnash is " + x)










