#Logistic with Linear
#code by AnkitBirla

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
df = pd.read_csv ('D:\Book2.csv')
height = np.array(df['Height'])
gender = np.array(df['Gender'])

heightmean = np.mean(height)
print(heightmean)

gendermean = np.mean(gender)
print(gendermean)

slope1 = np.sum((height-heightmean)*(gender-gendermean))
slope2 = np.sum((height-heightmean)*(height-heightmean))
b1 = slope1/slope2
print("B1 is",b1)


b0 = gendermean- b1*heightmean
print("B0 is",b0)

ynew =[]
sigmoidnew = []

for i in range(len(height)):
    y = b0+b1*height[i]
    ynew.append(y)
    sigmoid = np.exp(y)
    sigmoidd = (sigmoid/(1+sigmoid))
    sigmoidnew.append(sigmoidd)
    #print(ynew)
print("y is",ynew)
print("Sigmoid is",sigmoidnew)

threshold = 0.5

for i in range(len(sigmoidnew)):
    if(sigmoidnew[i]<=0.5):
        print("Female")
    else:
        print("Male")
        
    
        


      


        

        
plt.scatter(height,gender)
plt.plot(height,ynew,  color = 'red')

plt.show()


