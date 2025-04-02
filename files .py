"""
# FILE HANDLING
# is system that helps us to read, write and manipulate files.
# """
# file = open("file name","mode") ### open function allows us to open a file.
# file.close() ## it closes always when we open the file.



### for example:


# file = open("index.txt","r")
# content = file.read()
# print(content)

# file.close()

# with open("index.txt","r") as file:
#     content = file.read
#     print(content)

# with open("index.txt","a") as file:
#     # file.write("Hello,WORLD/n")
#     # file.write("/n python i messed up")
#     file.write("/ni am tired ")### to add text 

### we wann check if the file exists or not:

# import os
# if os.path.exists("rubbish"): 
os.remove("index.txt")
#     print("file exists")
# else :
#print("does not")   

# import os

# # Specify the file name
# file_name = "example.txt"

# # Get the absolute path
# file_path = os.path.abspath("rubbish")
# print("Absolute file path:", file_path)
 

# os.remove("index.txt")


## we want to ceate a folder 

import os 

 
file_path = "makutonetsa"
os.mkdir(file_path)
print("file created!")
