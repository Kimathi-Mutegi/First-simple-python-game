
#LISTS

#Lists are a versatile way to store multiple items in a single variable. Let’s dive into the details:

#1.Creating a List:

#Lists are created using square brackets ([]). For example:

mylist = ["apple", "banana", "cherry"]
print(mylist)

#2.List Properties:

#Ordered: List items have a defined order, and this order remains constant. New items added to a list are placed at the end.
#Changeable: Lists can be modified after creation. You can add, remove, or change items.
#Allow Duplicates: Lists can contain items with the same value.

#3.Accessing List Items:
#List items are indexed, starting from 0. For example:

print("This is index 0;" ,mylist[0]) 

#4.List Length:
#To find the number of items in a list, use the len() function:

print(len(mylist)) 

#5.Data Types in Lists:
#Lists can contain items of any data type (strings, integers, booleans, etc.):

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#6.List Constructor:
#You can also create a list using the list() constructor:

thislist = list(("apple", "banana", "cherry"))  # Note the double round-brackets
print(thislist)


#TUPLES

#A tuple is an ordered, immutable collection of objects in Python. Here are some key points about tuples:
#Creation: Tuples are created by enclosing comma-separated values within parentheses. For example:

mytuple = ("apple", "banana", "cherry")

#Ordered: Tuples maintain the order of their elements, which means the items have a defined sequence that won’t change1.
#Immutable: Once a tuple is created, you cannot modify its contents. Unlike lists, where you can add, remove, or change elements, tuples remain fixed after creation.
#Accessing Items: Tuple items are indexed, starting from 0. For instance, in the tuple mytuple, "apple" has index 0, "banana" has index 1, and so on.
#Allowing Duplicates: Tuples can contain duplicate values. For example:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Length: To find the number of items in a tuple, use the len() function:

print(len(thistuple))  # Prints the length of thistuple

#Single-Item Tuples: To create a tuple with only one item, add a comma after the item:

single_item_tuple = ("apple",)

#Data Types: Tuple items can be of any data type—strings, integers, booleans, or even a mix of types:

mixed_tuple = ("abc", 34, True, 40, "male")

#Type of a Tuple: From Python’s perspective, tuples are objects with the data type ‘tuple’:

print(type(mytuple))  # Outputs: <class 'tuple'>

#Using the tuple() Constructor: You can also create a tuple using the tuple() constructor:

thistuple = tuple(("apple", "banana", "cherry"))  # Note the double round-brackets


#PARAMETERS & ARGUMENTS

#Parameters are the variables listed inside the parentheses in the function definition. They represent the data that you expect to use in your function. Here’s a simple example to illustrate:

def greet(name):  # 'name' is a parameter
    print("Hello, " + name + "!")

#Arguments, on the other hand, are the actual values you pass to the function when you call it. These values are assigned to the corresponding parameters within the function. For instance:

greet("Alice")  # 'Alice' is an argument

#In the above call to greet, “Alice” is the argument that gets passed to the name parameter of the function.
#There are also different types of arguments you can use in Python:

#Positional arguments: are arguments that need to be included in the proper position or order.
#Keyword arguments: allow you to specify arguments by the names of their corresponding parameters, regardless of their order.
#Here’s an example that uses both:

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("Its name is " + pet_name + ".")

describe_pet('hamster', 'Harry')  # Positional arguments
describe_pet(pet_name='Willie', animal_type='dog')  # Keyword arguments

#In the first describe_pet call, “hamster” and “Harry” are positional arguments. In the second call, pet_name='Willie' and animal_type='dog' are keyword arguments12.


#FOR LOOPS

# for loop is used for iterating over a sequence, which can be a list, tuple, dictionary, set, or string. 
#In this example, the for loop will print each item in the fruits list. Python’s for loop doesn’t require an indexing variable to
#be set beforehand, making it quite user-friendly and easy to read.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Even strings are iterable objects, they contain a sequence of characters:
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#With the break statement we can stop the loop before it has looped through all the items:
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print banana:
 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a 
#specified number.
#Using the range() function:
#In this example, the for loop will print each item in the fruits list. Python’s for loop doesn’t require an indexing variable to be 
#set beforehand, making it quite user-friendly and easy to read.

for i in range(6):
    print(i)

#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: 
#range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a
#third parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Note: The else block will NOT be executed if the loop is stopped by a break statement.
#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#NESTED LOOPS
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#In Python, a script is essentially a file containing Python code that is intended to be executed directly. It’s like a set of 
#instructions that tells the computer what to do in a sequence. A script is generally a simpler and shorter program designed to
#perform a single or a few tasks.
