
# for statement
letters = ['a', 'g', 'b']
for w in letters:
    print(w, len(w))

# range
for i in range(1,5,2):
    print (i)

for i in range(len(letters)):
    print(i, letters[i])

#Enumerate
print(list(enumerate(letters)))
print(list(enumerate(letters, start=2)))

#match statement
class Point:
     def __init__(self, x, y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y = y):
            print(f"Y={y}")
        case Point():
            print("Something")
        case _:
            print("Not a point")
res = Point(0,3)
where_is(res)


#Functions: Fibonacci Series
def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end = " ")
        a, b =  b, a+b
        print()
print(fib(200))

#Default Argument Value

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#Keyword Argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(" This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("Lovely plumage, the", type)
    print("It's", state, "!")
parrot(voltage=3000, action='BRIGHT')   

#Arbitrary Argument List
def concat(*args, sep="/"):
    return sep.join(args)
concat('Hi', 'Hello', 'Rest')

# **kwargs
def parrot(voltage, state='a stiff', action='voom'):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "4 million", "state": "high", "action": "BRIGHT"}
parrot(**d)

#Lambda 
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)






    


       