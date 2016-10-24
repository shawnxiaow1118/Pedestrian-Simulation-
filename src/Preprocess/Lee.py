import scipy  as SP
import numpy as np

map = open("map.txt", "r")
config = []
for line in map:
	number_strings = line.split() 
	numbers = [float(n) for n in number_strings] 
	config.append(numbers)

config = SP.array(config)
row, col = config.shape
dist = np.ones((row,col))
for r in range(row):
	for c in range(col):
		dist[r,c] = 1000


def Lee(k,i,j):
    if (i+1) < row and config[i+1,j] == 1:
    	if(dist[i+1,j] > k+1):
    		dist[i+1,j] = k+1
    		Lee(k+1,i+1,j)

    if (i-1) > -1 and config[i-1,j] == 1:
    	if(dist[i-1,j]>k+1):
    		dist[i-1,j] = k+1
    		Lee(k+1,i-1,j)
        
    if (j+1) < col and config[i,j+1] == 1:
    	if(dist[i,j+1]>k+1):
    		dist[i,j+1] = k+1
    		Lee(k+1,i,j+1)

    if (j-1) > -1 and config[i,j-1] == 1:
    	if(dist[i,j-1]>k+1):
    		dist[i,j-1] = k+1   		
    		Lee(k+1,i,j-1)
Lee(0,6,0)

SP.savetxt('lee.txt', dist, fmt ='%.1f')
