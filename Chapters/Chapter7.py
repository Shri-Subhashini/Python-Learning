#Formatted strings

year = 2025
event = 'Cricket'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)) 

# str() and repr()

s = 'Hello, world'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(repr((x,y, ('leia', 'brownie'))))

# template class
from string import Template

t = Template("Hello, $name! You have $count new messages.")
result = t.substitute(name="Alice", count=5)
print(result)

# Formatted String Literals
import math
print(f'The value of pi is approximately {math.pi:.3f}.') # f - fixed point notation


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')  # minimum field width of 10 characters. d = decimal (format as an integer); Right-aligned by default for numbers


animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')


bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# Strinf Format - str.format()

print("Hi, Hello {}".format('Subha'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This is {other}'.format(other = 'table'))
print('Story of {0} is extremely {nice}'.format('Pandavas', nice = 'awesome'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
'''
0 → Refers to the first (and only) argument passed to .format(), which is table.
[Jack], [Sjoerd], [Dcab] → Access the keys inside the dictionary.
:d → Format as decimal integer (used for number formatting).

'''
fruits = {'apple': 10, 'orange': 20}
print('Jack: {0[Jack]:d}; Sjoerd: {1[apple]:d}; Dcab: {0[Dcab]:d}'.format(table, fruits))  # similar to table['jack] -> {0[Jack]}
print('Jack: {Jack:d}; Sjored: {Sjoerd:d}; Dcab: {orange:d}'.format(** table, **fruits))

table = {k: str(v) for k, v in vars().items()}  
print(table)
message = " ".join([f'{k}:'+ '{' + k + '};' for k in table.keys()])
print(message.format(**table))

'''
Each key is the name of a variable (as a string)
Each value is the string version of that variable’s value
You're iterating over all variable names (k) from the dictionary.
Eg: x: {x}; y: {y}; name: {name};

'''
for x in range(1, 11):
    print('{0:2} {1:3} {2:4d}'.format(x, x*x, x*x*x))  #2 - minimum width for the integer; d - decimal integer (its optional to mention)

#Manual String Formatting

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end = ' ')  # Return the string right justified in a string of length width; rjust(3) - 3 refers to width
    print(repr(x*x*x).rjust(4))
print('12'.zfill(5))
print('-2.9'.zfill(5))


#Old string formatting
import math
print('Value of pi is approximately %5.3f' %math.pi)


