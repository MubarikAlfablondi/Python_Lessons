#introduction to list
#[] <-- this squere bracket indicates a list, inside is the list of items that are placed

fruit  = ['apple', 'orange', 'water'] #if someone sees this...yes i know water is not a fruit
print(fruit)


fruit  = ['apple', 'orange', 'water'] 
print(fruit[0])#placing brackets towards the variable of the list will print out what you request. 
#numbers will start from 0 - however many you've place upon the list in your variable

fruit  = ['apple', 'orange', 'water'] 
print(fruit[0].title()) # you can also place methods upon the printed brackets. 

fruit  = ['apple', 'orange', 'water'] 
print(fruit[-2])
#python has a special syntax for accessing the last element in a list. If you ask for the item at index "-", python always returns the last item in the list
# This code returns the value 'specialized' this syntax is quite useful because you'll ofen want to access the last item in a list without knowing exactly how long the list is. 

fruit  = ['apple', 'orange', 'water'] 
message = (f"I love {fruit[0].title()}")
print (message)

#---------------
fruit  = ['apple', 'orange', 'water'] 
fruit[2] = 'banannas' #this variable has brackets connecting towards the previous list. I am coding to replace the list of fruit with water to bannanas
print(fruit)

fruit  = ['apple', 'orange', 'water'] 
fruit.append('banannas') #The append method delivers on adding upon the list so i now both have water and banannas
print(fruit)

fruit  = ['apple', 'orange', 'water'] 
fruit.insert(2,'banannas') #the insert method helps with placement of string into the list and this method can be help if + or - value of placement
print(fruit)

fruit  = ['apple', 'orange', 'water'] 
del fruit[0] #the del statement, short for deletion helps remove anything from your list. all your needing is its list placement. 
print(fruit)

fruit  = ['apple', 'orange', 'water'] 
fruit.pop()
print(fruit)

#Note: The pop method will always remove what is last on its list rather than the first thing like apple[0]

fruit  = ['apple', 'orange', 'water', 'banannas']
fruit.remove('apple') 
print(fruit) 
#remove method helps remove a string from the list of varibles by specific name 

fruit  = ['apple', 'orange', 'water', 'banannas']
print(fruit)

too_expensive = 'apple'
fruit.remove(too_expensive)
print(fruit)
print(f'a {too_expensive.title()} is to pricey for me.')
#a coder could def make this a program of what people purchase what within a list but there are many vulnerablities that would need to be checked like spelling, capitalization, numbers...Exception

fruit  = ['apple', 'orange', 'water', 'banannas', '5', '9']
fruit.sort() #this sort method cand sort about any string value to alpabetic order, including numbers.
print(fruit)

fruit  = ['apple', 'orange', 'water', 'banannas', '5', '9']
fruit.sort(reverse=True) #Note: True must be capitlized to function
print(fruit)
#This input towards the method reverse the list and stats it as true to make it function

fruit  = ['apple', 'orange', 'water', 'banannas', '5', '9']
print(sorted(fruit)) #this is a temporary function but it displays as the same thing as the sort method. 

fruit  = ['apple', 'orange', 'water', 'banannas', '5', '9']
fruit.reverse() #this reverses the list ina variable HOWEVER, it does not alphabetically reverse this code
print(fruit)

fruit  = ['apple', 'orange', 'water', 'banannas',]
print(len(fruit)) #another function towards seeing how many items a person has on a list would be the len (length) function. as you can see in my variable list is shows for items which would print 4

