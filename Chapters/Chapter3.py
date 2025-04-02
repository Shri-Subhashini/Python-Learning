#Arithmetic Operations
print(4+2)
print(2-3*5)
print((50-6*6))
print(30/8)
print(30//8)
print(30%8)
print(11/4)
print(11//4)
print((-11)/4)
print((-11)//4)
print(5**2)
print(2**7)

#String concat
name = "Subha"
print(name + "Shri")

#Escape Sequence
print('doesn\'t')
print("\"Yes,\" they said")
print(r'C:\some\name')

#String Slicing
print(name[:2] + name[2:])
print(name[32:])
print(name[2:32])
print(name[0:6])
print(name[0:])
print(name[3:])
print(name[-2:])
print(name[-2:-3])
print(name[3:1])

#List
list1 = [1, 2, 3] 
list2 = list1
list2.append(4)
print(list1) #[1,2,3,4]
print(list2)  # [1,2,3,4]
id(list1) == id(list2) #True

square = [2, 5, -12, 67]
print(square[-1])
print(square[-3:])

#Extending a list
square + [23, 78, 12, 9] 
print(square)
cubes = [1,8, 27, 56, 125]
cubes[3] = 64
cubes.append(4**2)
print(cubes)

#Shallow copy
list1=[8,9,6,7]
list2 = list1.copy()
list2[1] = 32
print(list2)

#Shallow copy with nested list 
l1 = [[1,2,3,4],[5,6,7,8]]
l2 = l1.copy()
print(l1[1][0])
l1[1][0]= 100
print(l1)
print(l2)
l1.append([2,3,4])
print(l1)
print(l2)

#Deepcopy
import copy
l1 = [1,2,3,4]
l2 = copy.deepcopy(l1)
l2[1] = 100
print(l2)
print(l1)

#Nested Deepcopy
l1 =[[1,2,3,4],[5,6,7,8]]
l2 = copy.deepcopy(l1)
l2[1][0] = 200
print(l2)
print(l1)


#Strings

letters = ['a', 'b', 'c']
letters[1:2] = ['B']
print(letters)
letters[:] = []
print(letters)
print(len(letters))













