# Scopes and Namespaces Example

def scope_test():
    def do_local():
        spam = "Local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "Nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope: ", spam)

# Class Example
class MyClass:
    ''' Simple Class Program '''
    def __init__(self):
        self.data = []
    i = 1290
    def f(self):
        return 'hello world'
obj = MyClass()
print("I value:", obj.i)
print("Function value: ", obj.f())

#Method Object
xf = obj.f
num = 10
while num == 10:
    print("Function value using Object Method Concept: ", xf())
    break
print("Docstring :",obj.__doc__)


#Class Example 2

class Complex:
    def __init__(self, real, img):
        self.r = real
        self.i = img
x = Complex(2.0, -8.6)

#Instance Objects
x.counter = 2
while x.counter < 5:
    x.counter = x.counter * 2
print("Intsance Object: ", x.counter)
print("Real Part:", x.r)
print("Imaginary Part:", x.i)


# Class and Instance Variables

class Dog:
    kind = 'golden retriever'  # class variable
    #tricks = []
    def __init__(self, name):
        self.name = name       # instance variable
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)
leia = Dog('Leia')
brownie = Dog('Brownie')
print("Leia's kind :", leia.kind)
print("Brownie's kind :", brownie.kind)
print("Leia's name: ", leia.name)
print("Brownie's name: ", brownie.name )
leia.add_trick('bonding')
brownie.add_trick('cutie')
print("Leia's trick: ", leia.tricks)
print("Brownie's trick: ", brownie.tricks)

#Random Remarks
class Warehouse:
    purpose = 'storage'
    region = 'west'
w1= Warehouse()
print("W1 Warehouse Prpose: ", w1.purpose, "W1 Warehoue Region: ", w1.region)
w2 = Warehouse()
w2.region = 'east'
print("W2 Warehouse Prpose: ", w2.purpose, "W2 Warehoue Region: ", w2.region)

#Class Example

class Example:
    def __init__(self, value):
        self.value = value  # data attribute

    def print_value(self):
        print(self.value)  # referencing the 'value' attribute
        self.add_to_value(100)

    def add_to_value(self, amount):
         print(self.value + amount)  
e = Example(10)
e.print_value()

def greet(self):
    print(f"Hello from {self.name}!")

#Function defined outside of the class
class Person:
    def __init__(self, name):
        self.name = name

# Assign the function to a class attribute
Person.greet = greet

# Now instances of Person can call the greet method
p = Person("Alice")
p.greet()  

#Funtion assigned to local variableof a class

def say_goodbye(self):
    print(f"Goodbye from {self.name}!")

class Person:
    def __init__(self, name):
        self.name = name
        # Assigning function as a local variable inside the class
        self.farewell = self.say_goodbye
    def say_goodbye(self):
        print(f"Goodbye from {self.name}!")

p = Person("Bob")
p.farewell()

#Overriding 

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the base class method 
        # (or) Animal.speak(self, arguments)
        print("Dog barks")  # Extend the behavior with new functionality

# Create a Dog instance
dog = Dog()
dog.speak()


#Multiple Inheritance

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()  # Calls the next method in the MRO

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()  # Calls the next method in the MRO

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()  # Calls the next method in the MRO

d = D()
d.greet()

print(D.mro())

#Private Variables
class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
    __update = update
class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

# map = MappingSubclass()
# map.update(23,78)

#exec() and eval()

class MyClass:
    def __init__(self):
        self.name = "MyClass"

    def exec_example(self):
        code = "print(self.name)"
        exec(code)  # exec does not consider MyClass as the current class

    def eval_example(self):
        code = "self.name"
        result = eval(code)  # eval does not consider MyClass as the current class
        print(result)

obj = MyClass()
obj.exec_example()  
obj.eval_example() 

#getattr, setattr, delattr

class MyClass:
    def __init__(self):
        self.name = "MyClass"
    
    def set_name(self, new_name):
        setattr(self, 'name', new_name)  # set name dynamically
    
    def get_name(self):
        return getattr(self, 'name')  # get name dynamically
    
    def del_name(self):
        delattr(self, 'name')  # delete name dynamically

# Testing the code
obj = MyClass()
print(obj.get_name())  # Output: MyClass
obj.set_name("NewClass")
print(obj.get_name())  # Output: NewClass
obj.del_name()

#Dataclasses
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

leia = Employee('Leia', 'computer lab', 1000)
print("Leia Dept:", leia.dept)
print("Leia Salary: ", leia.salary)

#Iterator
s = 'subha'
it = iter(s)
print("Iterator: ", it)
print("Next IItem :",next(it))
print("Next IItem :",next(it))

print("Next IItem :",next(it))

print("Next IItem :",next(it))

print("Next IItem :",next(it))

# print("Next IItem :",next(it)) #Error 



class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print("Value :",char)

#Generators

def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]
for char in reverse('subha'):
    print("Reverse character: ", char)

#Generator Expression 

print("Sum: ", sum(i*i for i in range(10)))

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

# Example list of graduates
graduates = [
    Student("Alice", 3.9),
    Student("Bob", 3.8),
    Student("Charlie", 4.0),
    Student("Diana", 3.7)
]

valedictorian = max((student.gpa, student.name) for student in graduates)

# valedictorian now holds a tuple like (4.0, "Charlie")
print(f"The valedictorian is {valedictorian[1]} with a GPA of {valedictorian[0]}")