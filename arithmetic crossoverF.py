# (c) Arithmetic Crossover
import random
p1 = [10,15,20,22,32]
p2 = [11,14,23,24,28]
Arithmatic_Crossover = [(x+y)/2 for x,y in zip(p1,p2)]
print(Arithmatic_Crossover)
