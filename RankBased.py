import random
import time

count = int(input("How much individuals you want:"))
print("\n")
elements = int(input("How much element you want in each individual:"))
print("\n")
start_range = int(input("Enter the starting range of each element:"))
print("\n")
end_range = int(input("Enter the last range of each element:"))
print("\n")
population = []
summed = []
rank = []
key_value = []


for i in range(count):
    lists = random.sample(range(start_range,end_range),elements)
    summ = sum(lists)
    
    #print(summ)
    population.append(lists)
    summed.append(summ)
    rank.append(i)
    #print(i)
#print(i)
print("\n")
print("Your population is:")
print("")
print("Loading...")
time.sleep(3)
print(population)
print("Fitness of each individual is following:")
print("")
print("Loading...")
time.sleep(4)
print(summed)
print("")
print("The sorted fitness is following with the correspondece rank")
print("")
print("Loading...")
time.sleep(4)
summed.sort()
#print(summed)
#print(rank)
key_value.append(summed)
key_value.append(rank)

print(key_value)



##individula1 = input("Enter 1st individual for population seperate each element by space ")
##list1  = individual1.split()
##print("Your 1st individual is",list1)
##
##individula2 = input("Enter 2nd individual for population seperate each element by space ")
##list2  = individual2.split()
##print("First 2nd individual is",list2)
##
##individual3 = input("Enter 3rd individual for population seperate each element by space ")
##list3  = individual3.split()
##print("Second Parent is",list3)
##
##
##print("Your Population is:")
##pri
##
##mask = random.sample(range(1,35),5)
##print(mask)

