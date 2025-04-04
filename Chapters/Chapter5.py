#List => mutable; homogeneous elements; access over iterating a list

'''
num =[1,4,5,8,9,10]
#index
index = num.index(4,1,4) #2nd parameter start value; 3rd parameter end value; within that range find the index of the element
print(index)

#pop
num.pop(2)

#remove
num.remove(10)
print(num)

#insert
num.insert(2,90)
print(num)

#append
num.append(100)
print(num)

#extend
num.extend([200,300])
print(num)

#Count
print(num.count(200))

#reverse
num.reverse()
print(num)

#copy
print(num.copy())

#sort
num.sort()
print(num)

'''
#List as Stack

stack = [1,8,9]
stack.append(3)
stack.append(67)
print("Stack:", stack)
print("Stack Pop Item1:", stack.pop())
print("Stack Pop Item2:", stack.pop())
stack.append(100)
print("Final Stack Item ", stack)

#List as Queue
from collections import deque
queue = deque(['Apple', 'Orange', 'Strawberry', 'Pineapple'])
queue.append('Pomo')
queue.append('Mango')
print("Queue :", queue)
print("Pop Item 1: ", queue.popleft())
print("Pop Item 2: ", queue.popleft())
print("Final Queue :", queue)


#List Comprehension

squares = list(map(lambda x: x ** 2, range(10)))
print("Square Numbers: ", squares)
squares = [x ** 2 for x in range(10)]
print("Square Numbers using Comprehensions: ", squares)


#List Comprehension: if list values are different, then print in tuples in pair
numbers = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("Numbers: ", numbers)

#List Comprehension Example
vec = [-4, -2, 0, 7, 9]

#Apply function to all elements
result = [abs(x) for x in vec]
print("Result :", result)

freshfruit = ['  banana', '  loganberry ', '  passion fruit ']
print("Result after Strip: ", [weapon.strip() for weapon in freshfruit])

#Creating list of two tuples like (number, square)

result = [(x, x ** 2) for x in range(7)]
print("Result of two tuples: ", result)

#Flatten the nested List
vector = [[1,2,3], [4,5,6], [7,8,9]]
result= [ele for num in vector for ele in num]
print("Result after Flattening: ",result)

#Pi value using List Comprehension 

from math import pi
result = [str(round(pi, i)) for i in range(1, 7)]
print("Pi values: ", result)

#Nested List Comprehension

#Transpose of Matrix
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matrix_result = [[row[i] for row in matrix] for i in range(4)]
print("Transpose of a Matrix: ", matrix_result)

#Using zip = > Zip groups elements by columns instead of rows
print("Using Zip: ", list(zip(*matrix)))  # *matrix unpacks the row

#del statement; we can use slicing here
num = [9,7,-2, 70, 27, 21]
del num[0]
print("After deletion :", num)
del num[1:3]
print("After deletion :", num)
del num[:] # deletes entire list values
print("After deletion :", num)

#Tuples => immutable (tuples, strings, numbers); contains heterogeneous elements; access via unpacking: (a,b) = t; so a=1234, b =54321; or indexing: t[1]

t = 12345, 54321, 'hello!'
print("t[0]th element: ", t[0])
print("Tuple: ",t) # Here all elements are packed in a tuple. This is known as tuple packing

#Nested Tuples
nested_Tuples = t, (7,8,9,10)
print("Nested Tuples: ", nested_Tuples)

#Flatten the Nested Tuple
flatten_Tuple = [ele for each_tuple in nested_Tuples for ele in each_tuple]
print("Flatten Tuple :", flatten_Tuple)

#namedtuple -provides immutable objects with named fields. It improves readability by providing meaningful names for each element
#namedtuple(typename, field_names)

from collections import namedtuple
codecademyStudent = namedtuple('codecademyStudent', ['username', 'courses'])
student1 = codecademyStudent(username='Foo', courses=['Python', 'Computer Science'])
student2 = codecademyStudent(username='Bar', courses=['Javascript', 'Web Development'])
print("Student 1:", "Username:", student1.username, "| Courses involvement:", student1.courses)
print("Student 2:", "Username:", student2.username, "| Courses involvement:", student2.courses)

#Cresting empty tuple
empty = ()
print("Empty Tuple: ", empty)

#Creating single tuple element
single_element = 'Subha',
print("Single Element in a tuple: ", single_element)

# Sequence Unpacking the Tuples
x, y, z = t
print("Unpacking Tuples: x = ",x, "y = ",y, "z = ", z )

#Sets => Unordered with no duplicates; Uses of Sets - membership testing (in,not in)and eliminnating duplicates
#It supports union, intersection, difference and symmetric difference
#To create empty set, use set(), not {} it creates empty dictionary

words = {'hi', 'hello', 'welcome', 'namasthe'}
print("Set: ", words)
print('hi' in words)

example_Set1 = set('abcdefghxyzw')
example_Set2= set('wxyzabcdpq')
print("Difference: ", example_Set1 - example_Set2)
print("Intersection: ", example_Set1 & example_Set2)
print("Or: ", example_Set1 | example_Set2)
print("Symmetric Difference: ", example_Set1 ^ example_Set2)

#Set Comprehension
result = {x for x in 'Subha' if x not in 'aeiou'}
print(result)


#Dictionary - associative memories or associative arrays
#Keys are always strings and numbers - immutable objects. Tuples can be used as key when it contains strings, numbers or tuples.
#Can use del to delete. If key is already there, then new key overrides the old key. If non existent keys are there, then gets error when extracting a value.
#Empty Dictionary
new_Dict = {}

#list(d) returns all the keys in a list in insertion order. 
#To check single key in the dictonary, use in keyword

example = {'jack': 4098, 'sape': 4139}
example['less'] = 200
print("Dictionary: ", example)
del example['sape']
example['sound'] = 'high'
print("Dictionary: ", example)
print(list(example))
print(sorted(example))
print('sound' in example)

#Dict constructor
result = dict([('sound', 123), ('name', 'Virat')])
print("Result Dictionary: ", result)

#Dictionary Comprehension
result = {i: i*2 for i in (2, 4, 6)}
print("Dict Comprehension: ", result)

#Looping Techniques

example_Dictionary = {'name': 'Virat', 'occupation':'crickter', 'age': 37}
for key, value in example_Dictionary.items():
    print("Key: ",key, " Value: ", value)

#Index and Value can be retrieves at same time using enumerate() in sequence
for index, value in enumerate([1,2,3,4]):
    print("Index: ", index, " Value: ", value)

for index, value in enumerate((1,2,3,4)):
    print("Index: ", index, " Value: ", value)

for index, value in enumerate({1,2,3,4}):
    print("Index: ", index, " Value: ", value)

#To loop over 2 or moew sequences at same time, use zip()
questions = ['name', 'age', 'fav dish']
answers = ['Sara', 12, 'Briyani']
for questions, answers in zip(questions, answers):
    print("What is your {0}? It is {1}".format(questions, answers))

#To loop over in reverse
for i in reversed(range(1, 10, 2)):
    print("Reversed numbers: ", i)

#To loop a sorted order - sorted()- returns new sorted list
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print("Sorted List: ", i)


#Precedence

not
and
or
is,is not, in, not in