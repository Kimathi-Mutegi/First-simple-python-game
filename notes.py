
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

#CLASSES

#Python Classes/Objects
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
#To create a class, use the keyword class:
#Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

#Create Object
#Now we can use the class named MyClass to create objects:

#Example
#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

#The __init__() Function
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#Example
#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Note: The __init__() function is called automatically every time the class is being used to create a new object.

#The __str__() Function
#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:

#Example
#The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

#Example
#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:

#Example
#Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

#Example
#Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
#You can modify properties on objects like this:

#Example
#Set the age of p1 to 40:

p1.age = 40

#Delete Object Properties
#You can delete properties on objects by using the del keyword:

#Example
#Delete the age property from the p1 object:

del p1.age

#Delete Objects
#You can delete objects by using the del keyword:

#Example
#Delete the p1 object:

del p1


#FUNCTIONS

#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function
#In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")

#Calling a Function
#To call a function, use the function name followed by parenthesis:

#Example
def my_function():
  print("Hello from a function")

my_function()

#Arguments

#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

#Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Arguments are often shortened to args in Python documentations.

#Parameters or Arguments?

#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

#Number of Arguments

#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

#Example
#This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If you try to call the function with 1 or 3 arguments, you will get an error:
#Example
#This function expects 2 arguments, but gets only 1:

#def my_function(fname, lname):
  #print(fname + " " + lname)

#my_function("Emil")

#Arbitrary Arguments, *args

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

#Example
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")

#Arbitrary Arguments are often shortened to *args in Python documentations.

#Keyword Arguments

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

#Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

#Arbitrary Keyword Arguments, **kwargs

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#Example
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

#Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:

#Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
#To let a function return a value, use the return statement:

#Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

#Example
def myfunction():
  pass

#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#To specify that a function can have only positional arguments, add , / after the arguments:

#Example
def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

#Example
def my_function(x):
  print(x)

my_function(x = 3)

#But when adding the , / you will get an error if you try to send a keyword argument:

#Example
#def my_function(x, /):
  #print(x)

#my_function(x = 3)

#Keyword-Only Arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:

#Example
def my_function(*, x):
  print(x)

my_function(x = 3)

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

#Example
def my_function(x):
  print(x)

my_function(3)

#But when adding the *, / you will get an error if you try to send a positional argument:

#Example
#def my_function(*, x):
  #print(x)

#my_function(3)

#Combine Positional-Only and Keyword-Only
#You can combine the two argument types in the same function.

#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

#Example
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion
#Python also accepts function recursion, which means a defined function can call itself.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

#Example
#Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
