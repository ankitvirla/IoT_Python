import numpy as np
import pandas as pd
import math as m
df = pd.read_csv('E:\CA-decisiontree (1).csv')
#print(df.head())

color = np.array(df['color'])
types = np.array(df['type'] )
doors = np.array(df['doors'])
tires = np.array(df['tires'])
classes = np.array(df['class'])
#print(color,types,doors,tires,classes)



#for counting A & B in Classes df

A = 0
B=0
for  i in range(len(classes)):
    if(classes[i]=='A'):
        A= A+1
    if(classes[i]=='B'):
        B= B+1
        
pa = A/len(classes)
pb = B/len(classes)
# Entropy = -p(A)log2 p(A)-p(B)log2 p(B)
entropy = -pa*m.log2(pa)-pb*m.log2(pb)

print("Entropy is",entropy)

#find color information gain
# for counting red,green, blue in color df
red = 0
green = 0
blue = 0
for i in range (len(color)):
    if(color[i]== 'red'):
        red = red+1
    if (color[i]== 'green'):
        green = green+1
    if (color[i]== 'blue'):
        blue = blue+1
        
# find p(v) used in ig(info gain)

pred = red/len(color)
pgreen = green/len(color)
pblue = blue/len(color)


#find h(Sv) parameter
reda = 2/4
greena = 2/6
bluea = 1/4
redb = 2/4
greenb = 4/6
blueb = 3/4
#for i in range(len(color)):
 #   if(color[i]=='red' && classes[i])
    
#find each category entropy
#multiplication of p(v) & h(sv)
#p(v) = probabbility of variable
#h(sv) entropy of variable
redentropy = pred*(-reda*m.log2(reda)-redb*m.log2(redb))
greenentropy = pgreen*(-greena*m.log2(greena)-greenb*m.log2(greenb))
blueentropy = pblue*(-bluea*m.log2(bluea)-blueb*m.log2(blueb))

#find the IG
colorig = redentropy+greenentropy+blueentropy
print("Color Information gain is",colorig)

#####################################################
#find types information gain
# for counting suv,minivan, car in types df
suv = 0
minivan = 0
car = 0
for i in range (len(types)):
    if(types[i]== 'suv'):
        suv = suv+1
    if (types[i]== 'minivan'):
        minivan = minivan+1
    if (types[i]== 'car'):
        car = car+1
        
# find p(v) used in ig(info gain)

psuv = suv/len(types)
pminivan = minivan/len(types)
pcar = car/len(types)


#find h(Sv) parameter
suva = 2/6
minivana = 0
cara = 3/5
suvb = 4/6
minivanb = 3/3
carb = 2/5
#for i in range(len(color)):
 #   if(color[i]=='red' && classes[i])
    
#find each category entropy
#multiplication of p(v) & h(sv)
#p(v) = probabbility of variable
#h(sv) entropy of variable
suventropy = psuv*(-suva*m.log2(suva)-suvb*m.log2(suvb))
minivanentropy = pminivan*(-minivana-minivanb*m.log2(minivanb))
carentropy = pcar*(-cara*m.log2(cara)-carb*m.log2(carb))

#find the IG
typesig = suventropy+minivanentropy+carentropy
print("Type Information gain is",typesig )

#####################################################
#find doors information gain
# for counting 2,4 in doors df
doors1 = 0
doors2 = 0

for i in range (len(doors)):
    if(doors[i]== 2):
        doors1 = doors1+1
    if (doors[i]== 4):
        doors2 = doors2+1
    
        
# find p(v) used in ig(info gain)

pdoors1 = doors1 /len(doors)
pdoors2 = doors2 /len(doors)



#find h(Sv) parameter
doors1a = 4/7
doors2a = 1/7
doors1b = 3/7
doors2b = 6/7

#for i in range(len(color)):
 #   if(color[i]=='red' && classes[i])
    
#find each category entropy
#multiplication of p(v) & h(sv)
#p(v) = probabbility of variable
#h(sv) entropy of variable
doors1entropy = pdoors1*(-doors1a*m.log2(doors1a)-doors1b*m.log2(doors1b))
doors2entropy = pdoors2*(-doors2a-doors2b*m.log2(doors2b))


#find the IG
doorsig = doors1entropy+doors2entropy
print("Doors Information gain is",doorsig )


#####################################################
#find tires information gain
# for counting whitewall, blackwall in tires df
whitewall = 0
blackwall = 0

for i in range (len(tires)):
    if(tires[i]== 'whitewall'):
        whitewall = whitewall+1
    if(tires[i]== 'blackwall'):
        blackwall = blackwall+1
    
        
# find p(v) used in ig(info gain)

pwhitewall =  whitewall/len(tires)
pblackwall = blackwall /len(tires)



#find h(Sv) parameter
whitewalla = 3/6
blackwalla = 2/8
whitewallb = 3/6
blackwallb = 6/8

#for i in range(len(color)):
 #   if(color[i]=='red' && classes[i])
    
#find each category entropy
#multiplication of p(v) & h(sv)
#p(v) = probabbility of variable
#h(sv) entropy of variable
whitewallentropy = pwhitewall*(-whitewalla*m.log2(whitewalla)-whitewallb*m.log2(whitewallb))
blackwallentropy = pblackwall*(-blackwalla*m.log2(blackwalla)-blackwallb*m.log2(blackwallb))


#find the IG
tiresig = doors1entropy+doors2entropy
print("Tires Information gain is",tiresig )

if(colorig> typesig and doorsig and tiresig):
    print("Root Node is Color")
if(typesig> colorig and doorsig and tiresig):
    print("Root Node is Types")
if(doorsig> colorig and typesig and tiresig):
    print("Root Node is Doors")
if(tiresig> colorig and typesig and doorsig):
    print("Root Node is Doors")


    

