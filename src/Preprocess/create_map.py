# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import scipy as SP
import random as RD

'''Create the Framework'''
x = SP.zeros([140, 200])

'''Map Modeling'''
## Modeling the Stadium
# Stand
x[15:122,80:135]=0.8
# Field
x[40:90,90:125]=0.6

## Modeling the Exit
# Exit to the South
x[15,125:135]=0.2
x[15,105:115]=0.2
# Exit to the East
x[110:122,134]=0.2
x[75:85,134]=0.2
x[35:45,134]=0.2
x[15:25,134]=0.2
# Exit to the North
x[121,125:135]=0.2
x[121,85:100]=0.2
# Exit to the West
x[90:98,80]=0.2
x[35:40,80]=0.2

## Modeling the main road
# North Avenue NW
x[5:15,0:200]=1
# TechWood Dr NW
x[0:140,135:142]=1
# Cherry St NW
x[10:130,5:12]=1
# Bobby Dodd Way NW -> 3rd St NW
x[122:130,5:180]=1
# Williams St NW
x[50:130,174:180]=1
x[5:55,185:190]=1
# Half "Loop"
x[85:130,25:31]=1
x[85:130,55:61]=1
x[85:90,25:61]=1
# Loop
x[70:73,25:70]=1
x[45:48,25:70]=1
x[45:73,25:28]=1
x[45:73,67:70]=1
# Others 
# East
x[50:55,180:185]=1
x[88:91,135:180]=1
# North
x[130:140,25:31]=1
x[130:140,48:52]=1
x[130:140,75:80]=1
x[130:140,108:113]=1
# West
x[90:98,55:80]=1
x[70:90,58:61]=1
x[68:71,10:26]=1
x[47:50,10:26]=1
x[10:46,35:40]=1
x[35:40,37:80]=1

'''Save the Map'''
SP.savetxt('map.txt', x, fmt ='%.1f')



## ***This section is just for testing purpose***
## ***Please kindly disregard***
ins = open("map.txt", "r")
data = []
for line in ins:
    number_strings = line.split() 
    numbers = [float(n) for n in number_strings] 
    data.append(numbers) 

data = SP.array(data)
