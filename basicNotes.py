#THIS FILE WILL NOT RUN PROPERLY .  This is simply notes 


#Indentation is extreamly important for Python as the language relies on spacing instead of traditional brackets. Ex. 4 spaces is traditional for if else statements


#Print Statments
print("Hello World!")
print("Hola")
print("Yo tengo un lapiz")


#Variables ###################################################################################################################################################

#Python has no command for declaring a variable.  But it will do it automatically.
#Variables are case sensitive (So variable y =/ Y)
x = 7               #Python will recognize this as a integer value
y = "4"             #Python will recognize this as a string value  (These variables can be also declared using single quotes)
#In python, you can assign values to multiple variables in one line
#y,x,z = "Tacos"


#Global variables are those that can be used anywhere in a file
#Local variables are created inside functions or conditional statments
x = "awesome"
def function():
  x = "fantastic" #Instance of a local variable (These variables can not be used outside of the program)
  print(x)
function()
print("Python is " + x)
#If you want to use a local variable as a global variable, then use the global keyword
#Ex.
def function1():
  global x 
  x = "TSPMPFKM"
print(x)


#Casting (Changing the primitive types of variables)/ Declaring Variables
x1 = str(3)   #Becomes a string value of '3'
x2 = int (3)  #Becomes a integer value of 3
x3 = float(3) # Becomes a float point (aka double) value of 3.0

#There are several data types in python
#Text type: str
#Numeric Types: int, float, complex
#Sequence Types: list, tuple, range
#Mapping Type: dict
#Set Types: set, frozenset
#Boolean Type: bool
#Set Types: set, frozenset
#Boolean Types: bool
#Binary Types: bytes, bytearray, memoryview
#None Type: NoneType

#Getting Variable type data
# Use type() function
x = 5
y = "John"
print(type(x))
print(type(y))

#Type Casting/Conversion
x = 1
y = 2.8
z = 1j
#Ex.
a = float(x)
b = int(y)
c = complex(x)

#Python doesnt have a random function, but it does have a module called 'random' that can be used to create random numbers
import random
print(random.randrange(1,10))


#Strings ###################################################################################################################################################
# Single and double quotes are interchangable: 'hello' is the same as "hello"
#Multiline Strings are declared using 3 single or double quotes
x = '''HELLO
HOWOEKFWREOM
PIDFNPSDFN'''

#Strings are arrays, they start at an index of 0 at the first character
a = "Hello World!"
print(a[1]) #Prints out e

#You can iterate over a string since they're just arrays
for x in "tacos":
  print(x)

#String Length
print(len(a))

#You can check a string by using the 'in' keyword
txt = "Sup my dog"
print("dog" in txt) #Prints true or false
#in can also be used for if statments
if "free" in txt:
  print("Yes, 'free' is present")
#You can add in 'not' in front of a 'in' keyword to result in the opposite

#You can return a range of characters by using slice
b = "Hello World!"
print(b[2:5]) #prints out llo (the 5 is not inclusive)
print(b[2:]) #  Leaving the second number tells the program to print from position 2 to the end
#print(b[-5,-2]) #Negative indexes are just reversed versions of the index.  0 Starts at the last character of the string. 

#Modifying Strings/ String methods
a = "Hello World"
print(a.upper()) # Capitalizes the entire string
print(a.lower()) #Lowercases the entire string
print(a.strip()) #Removes white space. ~ Space before and/or after actual text
print(a.replace("H","J")) #Finds the string literal from the first argument and replaces it with the second argument
print(a.split(",")) #Splits the string between the argument and returns an array with both ends (['Hello', ' World!'])

#Formating Strings
#You can not combine different primitive types to make a single one
#For example, you can not have a variable with a integer value and string value simultaneously 
#You would use F String to format those value together
age = 36
price = 36
txt = f"My name is John, I am {age}"  #You use {} and place the placeholder between it to make it into a string Literal
txt = f"The price is {price:.2f} dollars" #This incudes a modifier.  .2f means to place it by two decimal points
txt = f"The price is {20*23} dollrs" # You can do operations with f strings.
print(txt)

#Escape Characters
#Some characters are illegal to use within strings, they can also be used to insert things within string too
#Example: You can not use double quotes within a string with double quotes and vice versa with single quotes
txt = "We are the \"Tacos\" from USA" #Use a \ in front of an illegal character to include it within the string

#\' Single Quote
#\\ Backslash
#\n New line
#\r Carriage Return
#\t Tab
#\b backspace
#\f Form Feed
#\ooo Octal value
#\xhh Hex value

#String Methods
#Methods to manipulate strings
#Most common ones are 
#capitalize() Converts the first character to upper case
#count() Returns the number of times a specific value occurs in a string
#find() Searches the string for a specific value and returns the position of where it was found
#index() Finds the index of the string for a specific value 
# Full list here https://www.w3schools.com/python/python_strings_methods.asp


#Booleans #########################################################################################################################################################
#A boolean represents either true or false 
#Ex.
print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

#Python uses conditionals for if else statments
a = 200
b = 300
if b > a: #Conditional: This returns a boolean
  print("b is greater than a") #Conditional returns true
else:
  print("a is greater than b") #Conditional returns false

#The bool() function can be used to evaluate any variable/Value
#It will always return true except for the following instances
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Used to check if a variable is a certain data type
x = 200
print(isinstance(x, int)) #First is the variable name, second is the desired primitive type


#Operators ###############################################################################################################################################
#These are used to preform operations on variables and values such as addition and subtraction
# +	 Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y (Like division, but instead of the exact value, it returns the quotiant rounded down to an integer)

#Assignment Operators 
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3

#Comparison Operators 
#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	
#<=	Less than or equal to	x <= y


#Python Lists/ Arrays ###########################################################################################################################################

#4 differnt list types.  List, Tuple, Set, and Dictionary
#List - Ordered and changeable. 
#Tuple - Ordered and unchangable
#Set - Unordered, unchangable, and unindexed. No duplicates
#Dictionary - Ordered and changable.  No duplicates

#Arrays (commonly known as lists) are used to store multiple items ina single variable 
#Example of a list
hello = ["apple", "tacos", "idk"]
print(hello)
#Lists can be any data type
list1 = [1,2,3,4] #Int
list2 = ["apple", "bannana", "pencil"] #String
list3 = [True, False, True, False] #Boolean
#Lists can contain multiple different types of data
list4 = ["Hello","Bye", 4, 3, True, False, 2.3]
#In the type() function, lists are considered as the data type of list
#EX. 
print(type(list2)) #Returns list
#list() function (constructor) can be used as another method of declaration
thislist = list(("apple", "bannana", "tacos")) #When using list() function, you must use double brackets
print(thislist)

#Accessing list items

#If you want a specific item you would reference its index
aListlol = [1,2,3,4]
print(aListlol[1]) #References 2
#Negative indexing also works, starting from the final item in the list as index 0 and going on
print(aListlol[-1]) #Prints out 3
#Ranges of indexes can be accomplished by using [#:#] format
print(aListlol[1:4]) #Prints out 2,3,4
#Ranges can work even if it's missing a number
print(aListlol[:3])#Starts from the begining  all the way to the index
print(aListlol[1:])#Starts from the index to the end
#If you want to check if a specific value is in a list, you can use the 'in' keyword
if 3 in aListlol:
  print("3 is indeed in this list")

#Changing list items

#Just refer to the index of the list if you want to change it
list2 = ["Hello", "Bye", "Cya"]
list2[0] = "No"
print(list2[0]) #Prints out no
#You can also change a range of item values
list2[0:2] = ["NO","MONEY","TODAY"]
print(list2)
#If your range is larger than the amount of items it's replacing, it will set the range of the indexes and replace it with the intended change and leave white space
thislist = ["apple", "banana", "cherry"]
thislist[0:3] = ["watermelon"]
print(thislist) #Results in just printing 'watermellon'
#Inseting items
#Use the inset() Method to insert at item at a specified index
list2.insert(2,"Taco")
print(list2) #only inserts it, does not replace it.  All the values after the index and itself move up an index

#Adding items to lists

#Use the append() method to add things to the end of the list
list = [1,2,3,4,5,6,6,7,8,9,90,]
list.append(1)
print(list) #adds 1 to the end of the list
#If you want to combine two lists together, you can use the extend() method
list1 = [1,2,4]
list2 = [5,6,7,]
list1.extend(list2)
print(list1) #Prints out 1,2,4,5,6,7

#Removing items in a list

#Use remove() function to remove a specific item in a list
list = ["sandwich", "men", "tacos"]
list.remove("men")#If there are several instances of the targeted value in the list, Python will remove the first instance of it
#If you want to remove a specific index, you would use the pop() function
list.pop(1) # If a value is not specified, the pop() method removes the last item in the list
print(list)

#An alternative to pop() is the keyword del
del list[0]
del list #Without specifying a index, del can delete the entire list

#If you want to clear a list you would use clear() method
list90 = ["sandwich", "men", "tacos"]
list90.clear()

#Loop lists

#A common way to iterate over lists is by using a for statment
#Example
list90 = [1,2,3,4,5,6,7]
for x in list90: #Guarentees that it will loop over every single element
  x += x

#You can also iterate using the list's index
for i in range(len(list90)):
  print(list[i]) 

#Same thing could be done with while loops
i = 0 
while i < len(list90):
  print(list[i])
  i = i + 1

#List Comprehension

#A shorter syntax to create a new list based on a differnt list 
#Lets say you want to make a list of names that has the letter n within them.  
#Without list comprehension
people = ["Jake", "Jack", "Ann", "Anna", "Mark"]
people2 = []
for x in people:
  if "n" in x:
    people2.append(x)
print(people2)

#With list comprehension
people3 = [x for x in people if "n" in x] #You dont always need the if statment | you can just have [x for x in people]
print(people3)

#Below is the syntax template for list comprehension
#newlist = [expression for item in iterable if condition == True]
#Expression = Thing you want program to do for every iteration 
#Item = Variable used as index to reference an element
#Iterable = Previous list used to create the new list.  Could also be an object, like a range function
#Condition = Conditional statment 

#Sorting lists

#sort() Sorts the list alphanumerically, ascending, by default.  It is also case sensitive, sorting the capital letters being sorted before the lower case ones
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #Function
print(thislist)

#Sorts the list in numeric order
thislist = [100, 50, 65, 82, 23]
thislist.sort() #Function
print(thislist)

#If you want to do descending order, you would have to use the argument reverse = true
#Function would look like:
thislist.sort(reverse=True)

#You can have a custom sort function by using the 'key=' keyword
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #Doesnt always has to be a function though, could be a simple argument such as str.lower
print(thislist)
#If you straight up just want to reverse the order of a list, just use the function reverse()
list90.reverse()

#Copying lists

#You cant copy a list by doing list1 = list2.  This only makes list1 reference list two and not actually changing the contents of list 1
#You must use the copy() method instead
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#You can also use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Joining lists 

#Just use concatenation to combine two or more lists in Python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#If you need more accuracy or customization, use a for statment with append() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#List Methods

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list


#Python Tuples#############################################################################################################################################
# A tuple is a data type to store collctions of data; similarly to list, set, and dictionary
#Tuple is ordered and unchangeable 
#Ordered means that the items have a defined order that can not change 
#Unchangeable means that you cannot change, add, or remove items froma tuple after it has been created.
#Tuples has an index, meaning that there can be duplicate values

thistuple = ("apple", "banana", "cherry") #This is a tuple
thislist = ["apple", "banana", "cherry"] #This is a list

#Accessing tuples
#Everything from lists can and will apply to tuples

#Updating tuples

#Tuples are unchangeable or immuntable, but you can simply just convert the tuple into a list, change the list. and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Since you are converting the tuple into a list, everything from list will apply

#Looping a tuple and combining tuples are the same as a list

#Tuples methods (Rly can be used for anything though)
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


#Python Sets ##########################################################################################################################################################
#Sets is a collection that is unordered, unchangable, and unindexed
#Being unindexed means that sets do not allow for duplicated data
# set is created using {} brackets
thisset = {1,2,4,5,6,7,}
####### Set items are unchangable, but you can add and remove items #########

#Since set has no index, you can not simply refer to an element with a index
#For loops you may just want to use a for statment to iterate everything in a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Adding set items

#If you want to add items to a set, you can use the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#If you want to combine two sets, you can use the update()method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #It doesn't need to be a set, it can be anything including lists,tuple, and dictionaries
print(thisset)

#Removing items in a set

#remove() when an argument is used, will remove the value: If the argument doesn't exist in the list, it will return an error
#discard() Same thing as remove(), however, it will never return an error
#pop() used to remove a random item
#clear() clears an entire set
#'del' deletes an entire set

#Looping a set

#Just use a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Joining sets

#Union() Returns a new list with a combination of two sets | could also be used for the exact samething
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Union() can be used on multiple sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#Update() Inserts the items from a list to another list.  It does not return a new list, but instead changing a list with the new added values
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Joining Sets

#Primary methods to join sets together

#union() & update() joins all items from both sets
#Union() - Creates a new set 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Update() - Updates only 1 set with both sets' items
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersection() only keeps the duplicates #Also creates a new set 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#Difference() keeps the items from the first set that are not in other sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#symmetric_difference() keeps all the items except the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) 

#Python Dictionaries #######################################################################################################################################
#Similar to hashmaps, dictionaries in python have a pair to pair system of organization with keys
#Dictionary items are ordered, changeable, and do not allow duplicates
#Example: Dictionaries are written with curly brackets, and have keys and values
#The first value is refered to as the key, the second is the value.  Together, they make a single item in the dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Acessing infomration 

#As dictionaries in python have a key-value relationship, you would access the items of a dictionary by referring to its key name 
#Ex.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] #Would return Mustang

#You can also use a method called get() which does the samething
x = thisdict.get("model") #Prints out Mustang

#If you want a list of keys, you can used the method keys() to return a list of them 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x) #Returns 'dict_keys(['brand', 'model', 'year'])'

#If you want just the values, use the values() method
x = thisdict.values()

#If you want to access all the pairs, you can use the items() method
x = thisdict.items()

#Changing Items

#Changing value information is easy.  Just reference the key in the operation statement
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#You can also use the update() method to change the value of a key
thisdict.update({"year": 2020})


#Adding Items

#Adding items is exactly the same as changing items.  Since dictionaries can't have duplicates, python will automatically know if you're updating or adding something new
#For example, if you declare this line 'thisdict["year"] = 2018' and the "year" key isn't in the dictionary, python will just add it to the dictionary
#If it is there, python will replace the value associated with the pair. 

#Removing Items

#There are several methods to remove items from a dictionary.  
#The main ones are

#pop() - Removes a specific item by stating it's key as an argument
#popitem() - Removes the last item in the dictionary
#del - removes the item with the specific key name (Can delete the entire dictionary if needed)(Is a keyword)
#clear() - Empties the entire dictionary, does NOT delete it

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "Yellow"
}
thisdict.pop("model") #Deletes a specific item
thisdict.popitem() #Removes the last item
del thisdict["year"] # Deletes a specific item or 'del thisdict' (Deletes the entire dictionary)
thisdict.clear() # Empties the dictionary

#Looping through a dictionary

#Use a for loop if you want to iterate through a dictonary
#When looping through a dictionary, the return value are the KEYS of the dictionary, but there are methods to return the values as well

#Example - Prints out all the keys of the dictionary
for x in thisdict:
  print(x)

#Alternatively you can use the keys() method
for x in thisdict.keys():
  print(x)

#Printing values in a dictionary
for x in thisdict:
  print(thisdict[x])

#Alternatively you can use the values() method
for x in thisdict.values():
  print(x)

#If you want to print both items and keys simultaneously, use the items()method

for x, y in thisdict.items():
  print(x,y)

#Copying Dictionaries

#(Standard practice) When it comes to objects you can not directly copy it over by using just = (Ex. dict2 = dict1) since it will just make dict2 reference dict1
#Use the copy() method to copy items over 
#Ex.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Or, you can also use the dict() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries

#Just like conditional if statments, a dictionary can contain dictionaries 

 #A dictionary that contain three dictionaries
#The inner dictionaries don't need to be named since they are tied to the key of the first dictionary
myfamily = {
  "child1" : {  #Key of outer dictionary 
    "name" : "Emil", #Item of inner dictionary
    "year" : 2004  #Item of inner dictionary
  },
  "child2" : { #Key of outer dictionary 
    "name" : "Tobias",  #Item of inner dictionary
    "year" : 2007 #Item of inner dictionary
  },
  "child3" : { #Key of outer dictionary 
    "name" : "Linus", #Item of inner dictionary
    "year" : 2011 #Item of inner dictionary
  }
}

#Alternatively you can put premade dictionaries into another one. 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#If you need to access them, you need to use two sets of brackets
#Ex.
print(myfamily["child2"]["name"]) #This line first references the first layer of keys, then it references the second layer of keye

#All the previous rules of dictionaries applies to nested dictionaries

#Looping through a dictionary is similar to iterating a 2D array
#Ex.
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


#Python IF ELSE #############################################################################################################################################

#These conditionals can utilize logicla conditions from operators

#Equals: a==b
#Not Equal: a!=b
#Less than: a<b
#Greater than: a>b
#Less than or equal to: a<=b
#Greater than or equal to: a>=b

#Conditional statments end with a : and must have proper indentation
#A lot of programs use curly brackets to signify grouping.  Python soley uses indents to do the same
#Ex.
a = 33
b = 200
if b > a:
  print("b is greater than a") #This line is indented.  

#Elif
#A keyword to signify if else.  Basically, if the previous statment was not true, try this condtional
#Ex.
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else
#Else keyword catches anything that isn't caught by the previous conditons
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short hand if
#Use this if you only have a single statment to execute
if a > b: print("A is greater than b")

#You can also apply shorthand to if..else statements
print("A is greater than B") if a > b else print("B is greater than A")

#You can have multiple else statements on the same line
print("A") if a > b else print("=") if a == b else print("B")

#Logical Operators

#And
# It is used to combine conditonal statements  (Both must be true)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or
#Used to combine conditional statements to signify either or (Only one has to be true)
if a > b or a > c:
  print("At least one of the conditions is True")

#Not
#Used to reverse the result of the conditional statement
if not a > b:
  print("a is NOT greater than b")

#Pass
#If statments can never be empty.  If for some reason you have an if statment with no content, you can use the pass keyword as a place holder and prevent getting an error
if b > a:
  pass


#Python While Loops #######################################################################################################################################################


#A while loop can repeat a set of statements as long as a condition is true 
#Ex.
i = 1
while 1<6: #Repeats 5 times
  print(i)
  i +=1 #While loops must have their condition being incremented, otherwise, they will run indefinitely 


#Break Statement

#This statement is used to end a loop, even if a condition still remains true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continute Statement

#Used to stop a chunk of code and continue to the next one 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Else Statement
#like how an if statement can have an else statement, a while loop may also contain a else conditional 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#For loops#########################################################################################################################################################


#A for loop is used for iterating over a sequence.  (Typically through array values such as a list, tuple, dictionary, set, or string)
#A for loop can execute a set of statements for each element of an array value 

fruits = ["apple", "banana", "cherry"]
for x in fruits: #In this example, you don't need an indexing value as it's just printing everything in the list.  
  print(x)

#A string is considered as an object, meaning you can iterate over one
for x in "banana":
  print(x)

#You can also make 'bannana' into a string variable and it works the same way

#If you want to iterate code a certain amount of times, you can use the range() method to generate a sequence of numbers
#Ex. range(6) will iterate by default in increments of 1.  Thus iterating 0,1,2,3,4,5 (Range is exclusive to the last number)

for x in range(6):
  print(x)

#By default, range() sets 0 as its starting value, but you can specify a starting value by using a common

for x in range(2,6):
  print(x)

#Similar to while loops, you can also use a else statement to run another conditional after the first one 

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#As common standard, Python allows for nested if statements
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Similar to if-statements, a for statment can not be blank, thus you need to use a pass keyword to allow the program to run without errors

for x in [0, 1, 2]:
  pass


#Python Functions ################################################################################################################################################


#A function (aka method) is a block of code that only runs when it is called
#Functions typically pass data (aka parameters) into a function
#Functions can re turn data as a result of running it

#To create a function, you use the def keyword
#Ex.

def a_function():
  print("Hello")

#If you would like to run the function, just use the function name followed by parenthesis

a_function()

#Arguments can be refered to ass information that is passed onto the function
#You would typcally include them within the parenthesis
#Ex.

def some_function(name):
  print("Hello " + name)

some_function("Terry")
some_function("Joe")

#Parameters and arguments can be used interchangably
#Techically speaking however, a parameter refers to the placeholder variable
#An argument refers to the actual value sent to the function


#A function must be called with the correct number of para,eters #Any more or less will result in an error

def random_function(name, age):
  print("hello " + name + " , you are " + str(age) + " years old.")

random_function("Terry", 12)


#Arbitrary Arguemnts, *args

#If there is an undefined amont of arguments that can be passed to a function, use a * before the parameter to allow the parameter to function as a tuple

def my_function(*kids):
  print("The youngest child is " + kids[2]) #kids[2] refers to Linus in the parameter kids
my_function("Emil", "Tobias", "Linus")

#Keyword arguments

#If you want to send arguments without regards to order, you can use 'key = value syntax' to do so
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #order doesn't matter since each argument is assigned directly to the parameter 

#Arbitrary Keyword Arguments, **kwargs

#If you don't know the amount of keyword arguments that will be passed into a function, use two asterisks ** before the parameter name
#If several keyword arguments are inserted into the function, it will instead recieve a DICTIONARY 

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Default parameter Value

#Sometimes a function might have a parameter, but be called without an argument
#A default parameter value can catch it, and substitute it with a default value

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passinga list as an Argument 

#You can send any data type as an argument to a function, and it will be treated the as a data type in the function
#So you can technically just have it act as a new variable
#Ex.

def a_function(students):
  for x in students:
    print(x)
students = ["Kacl"," jack" , "jill", "henry"]
a_function(students)

#Return Values

#Returning a value means that the function will give a value created from it's code
#Typically used for mathematical formulas to give a result

def my_function(x):
  return 5 * x
print(my_function(3))

#Pass Statement

#Similar to if statements, a blank function will just return an error
#If for some reason you want to leave it blank, use the 'pass' keyword

def a_function():
  pass

#Positional-Only Arguments

#There are two different types of arguments, positional arguments and keyword arguments
#Positional arguments are arguments that rely on order to have the correct result.  Ex. a list of parameters might look like (name, age), to correctly use the values, the call must be in order
#Keyword arguments don't rely on order, instead directly assighning the arguments to parameters

#If for some reason you want only positional arguments, insert a ', /' 
def my_function(x, /):
  print(x)
my_function(3)
#Trying to send a keyword argument will only return an error

#Keyword-only arguments

#Add a "*," before the arguments to have a function that only accepts keyword arguments
def my_function(*, x):
  print(x)
my_function(x = 3)
#Vice Versa is true for trying to use a positional argument 

#You can combine the two
#Ex.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion

#Python has recursion, or when a function calls itself 
#Here is an example. 

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1) #Recursion magic 
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#Python Lambda ############################################################################################################################################################

#A lambda in Python refers to an anoymous function, which is a function that is defined without a name.  
#Lambdas are used for creating small, simple functions for short-term use.  

#SYNTAX: lambda arguments : expression
#Lambda functions are automaticlly returned 

#Ex.
x = lambda a : a + 10
print(x(5)) #Kinda seems like it's calling a function

#Lambdas can take any number of arguments , but only have one expression (one like of code)
#Ex.
x = lambda a,b:a*b
print(x(5,6)) #Can be an infinite amount of arguments 

#A lambda typically is an expression that isn't complex enough to warrent a function defined by the 'def' keyword
#However, it is useful as a throw away function

#Ex.
def myfunc(n):
  return lambda a: a*n

#Ex.
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) #This acts as the lambda expression.
print(mydoubler(11))

#Lambda allows for several variations within a single function
#Ex.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #Doubles
mytripler = myfunc(3) #Triples

print(mydoubler(11))
print(mytripler(11))


#Python Classes/Objects ##############################################################################################################################################################

#Python is a OOP
#Almost anything in Python is an object

#Creating a class
#Use the keyword 'class' to make a class
#Ex.

class aClass:
  x = 5

#Creating an object

object = aClass()
print(object.x)


#BOTH OF THESE ARE SPECIAL METHODS THAT ARE RECOGNIZED BY THE PYTHON INTERPRETOR
#THUS THEY HAVE UNIQUE INTERACTIONS WITH YOUR PROGRAM

# _init_() function
#All classes have a function called _init_(), which is always executed when the class is being initiated (Kinda like constructors)
#It's used to assign values to object properties, or other operations that are necessary to do
#Ex.

class person:
  def __init__(self, name, age): #THE FIRST PARAMETER IS GUARANTEED TO REFER TO THE INSTANC OF THE CLASS BECAUSE OF THE SPECIAL METHOD __init__()
    self.name = name
    self.age = age

aPerson = person("John", 5)
print(aPerson.name) #We can print these out since we are specifcally referencing those attributes
print(aPerson.age)


# __str__() Function
#The purpose of an __str__ function is to give a readable version of an instance of an object

class Person:
  def __init__(self, name, age): #Self is typically named self, but it can be named anything else
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})" #F string used to create a readable interface

p1 = Person("John", 36)
print(p1) #Without the __str__() function, it would simply just print out the memory address


#Object Methods

#Methods and functions can be used interchangably.  THe only difference is that a method belongs to a class
#Basically, a method is just a function in a class

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() #p1 - refers to the object: myfunc() - refers to the function in that specific class

#Modifying Attributes
#Simply refer to the object and then the attribute if you want to change it
#Ex.

p1.age = 3

#Deleting Object Properties
#You can delete properties on objects by using the del keyword
#Ex.
del p1.age

#You can also delete an object by just refering to it
#Ex. 
del p1

#Pass statement
#IF you want to leave a class blank for placeholder purposes, 
#Ex.
class Person:
  pass


#Inheritance #################################################################################################################################################################


#Inheritance allows us to define a class that inherits all the methods and properties from anothre class

#Key Terms
#Parent class (aka super class or base class) is the class that is passing down information
#Child class (aka subclass or derived class) is the class that is gaining that information

#There is no specific syntax to make a class into a parent class.  All classes can be parent classes
#Ex.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Child Class
#Pass the parent class as a paremter to the child class to create a link
#Ex.
class Student(Person): #This new class should be the exact same as the Person class, despite the fact that it is blank
  pass

#Since the student class inherited the person class, it should function exactly the same as the person class
#(In a normal situation, when inheriting atrributes/methods, it adds the functionality of the parent class along side the child class)

x = Student("Mike", "Olsen")
x.printname() 

#__init__() Function (Inheritance)
#You may use this function in the child class however, it will override the inheritance of the parent's function
class Student(Person):
  def __init__(self, fname, lname): #Instances of this child class will use this function
   pass

#A child class will typically require more unique attributes compared to the parent class.  In those situations, it is possible to reuse the __init__() function of the parent class
#Ex.
class Student(Person):
    def __init__(self, fname, lname, student_id):
        Person.__init__(self, fname, lname) #Reused here
        self.student_id = student_id #New attribute here

#super() function
#This function will make the child class inherit all the methods and properties from its parent
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #You don't need to state the parent's name.  Using super() will automatically call the parent

#Add properties
#Adding properties(aka attributes) is simple.  Use the naming convention for the class, and then the name of the property and set it as the constructor

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year #This is the new property

x = Student("Mike", "Olsen", 2019)

#Add Methods
#Adding a method is simply the same syntax as just creating a method in any other method
#Notice: If a method in the child class has the same name as the one in the parent class, it will override it. 

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


#Iterators ###########################################################################################################################################################

#An iterator is an objct that contains a countable number of values
#An iterator is an object that can be iterated upon (able to be traversed)
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

#https://www.w3schools.com/python/python_iterators.asp

















































