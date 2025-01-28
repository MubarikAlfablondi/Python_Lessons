#variables and simple data types

message = "hello world 2!"
print(message)

# I've created a variable named message, which is connected to a value 

message = "another hello world for the books!"
print(message)

#I can change the value of a variable in my program at any time and python will always keep track of its current value. 

#Note: variables names can only contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. 
#Note Cont.: for example "message_1" works but not "1_message"

#Spaces are not allowed as it will cause future errors
#Avoid using python keywords and functions as variable names, as example don't use print as a variable.abs
#Python has particular reserved names for a programmatic purpose. 
#understand that spelling is an important factor within variables and other functions

#Variables are Labels 
#Variables are often described as boxes you can store values in. 
# "" and '' are both a string

name = "ada lovelance"
print(name.title())

#the .title() is usually called a method, which helps preform the funtion of having the first letter of first name and last name upper case

name = "mubarik alfablondi"
print(name.upper())
# this method uppercases all the letters towardsd my name, each method has its own functions for what you'll be using for it! 

first_name = "mubarik"
last_name = "alfablondi"
full_name = f"{first_name} {last_name}"
print(full_name)

#the f is called an f-string. The f is for format, because python formats the string by replacing the name of any variable in braces with its value. 

first_name = "mubarik"
last_name = "alfablondi"
full_name = f"{first_name} {last_name}"
print(f"hello, {full_name.title()}")

#I can also use f-strings to compose a message, and then assign the entire message to a variable

first_name = "mubarik"
last_name = "alfablondi"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)
#Placing a tab upon my python code
print("\tPython")
#adding a new line
print("this\nis a test\n on new lines")
#Note: i can also combine the two \n\t for tab and new line in a print funtion

#r.strip method able to take away the extra space your needing within left right or both sides.
fav_language = 'R is my fav. '
print(fav_language.rstrip())


