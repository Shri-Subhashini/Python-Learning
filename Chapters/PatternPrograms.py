# Program 1

print("############### Program 1 ##################")

for i in range(1,5):
    for j in range(i):
        print("*", end = " ")
    print()

'''
*
* *
* * *
* * * *

'''
print("############### Program 2 ##################")

# Program 2
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end = " ")
    print()   
'''
1
1 2
1 2 3
1 2 3 4

'''

print("############### Program 3 ##################")
#Program 3
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end = " ")
        num += 1
    print()
'''
1
2 3
4 5 6
7 8 9 10
'''
#Program4
print("############### Program 4 ##################")
for i in range(1,5):
    print("* " * ((i*2)-1), end = " ")
    print()
'''
*
* * *
* * * * *
* * * * * * *
'''
#Program 5
print("############### Program 5 ##################")

alph = 65
for i in range(1, 5):
    print((chr(alph) + " ") * ((i*2)-1), end = " ")
    alph += 1
    print()
'''
A
B B B
C C C C C
D D D D D D D
'''
#Program 6
print("############### Program 6 ##################")

alph = 65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(alph), end = " ")
        alph += 1
    print() 
'''
A
B C
D E F
G H I J

'''
#Program 7
print("############### Program 7 ##################")

alph = 65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(alph), end = " ")
    print() 
    alph += 1
'''
A
B B
C C C
D D D D

'''
#Program 8
print("############### Program 8 ##################")

alph = 65
for i in range(1, 5):
    for j in range(i):
        print(chr(alph + j) ,end = " ")
    print()
'''
A
A B
A B C
A B C D

'''
#Program 9
print("############### Program 9 ##################")

rows = 4
for i in range(1, rows+1):
    print(" " * (rows-i), end = "")
    print("* " * (2*i-1))
'''
     *
   * * *
  * * * * *
 * * * * * * *

 '''

#Program 10
print("############### Program 10 ##################")

rows = 4
alph = 65
for i in range(1, rows+1):
    print(" " * (rows-i), end = "")
    print((chr(alph) + " ") * (2*i-1))
    alph += 1
'''
    A
  B B B
 C C C C C
D D D D D D D

'''

#Program 11
print("############### Program 11 ##################")

rows = 4
alph = 65

for i in range(1, rows+1):
    num_char = 2*i-1
    print(" " * (rows-i), end = "")
    for j in range(num_char):
        print(chr(alph), end = " ")
        alph += 1
    print()
''' 
    A
  B C D
 E F G H I
J K L M N O P

'''