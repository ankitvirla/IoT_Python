import random
p1 = [10,15,20,22,32]
p2 = [11,14,23,24,28]

point1 = int(len(p1)/2.5)
print(point1)
point2 = int(len(p1)/1.2)
print(point2)

##length = len(p1)
##length1 = length-1
##print(length1)
##point1 = random.randint(0,length1)
##point2 = random.randint(0,length1)

child1 = p1[:point1]+p2[point1:point2]+p1[point2:]
print(child1)
child2 = p2[:point1]+p1[point1:point2]+p2[point2:]
print(child2)
