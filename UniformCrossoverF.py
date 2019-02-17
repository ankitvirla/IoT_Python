# (a) Uniform Crossover

import random
Mask = input("Enter each chromosome for mask separated by space ")
list1  = Mask.split()
print("Your mask is",list1)

Parent1 = input("Enter each chromosome for parent1 separated by space ")
list2  = Parent1.split()
print("First Parent is",list2)

Parent2 = input("Enter each chromosome for parent2 separated by space ")
list3  = Parent2.split()
print("Second Parent is",list3)

children1 = []
children2 = []


if list1[0] == '1':
    children1.append(list2[0])
else:
    children1.append(list3[0])

if list1[1] == '1':
   children1.append(list2[1])
else:
    children1.append(list3[1])

if list1[2] == '1':
    children1.append(list2[2])
else:
    children1.append(list3[2])

if list1[3] == '1':
    children1.append(list2[3])
else:
    children1.append(list3[3])

if list1[4] == '1':
    children1.append(list2[4])
else:
    children1.append(list3[4])

print(children1)











