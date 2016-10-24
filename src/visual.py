# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import random as RD
from Grid_Class import *
from Pedestrian_Class import *
from read import *
from ped_update import *
from Generator import *
from write import *

from math import *
import scipy  as SP

import matplotlib
matplotlib.use('TkAgg')
import pylab as PL
from path import *
import pycxsimulator

RD.seed()
row_start = 0
col_start = 0
length = 140
width = 200

def read_map2_visual(Map_import):
    global Map 
    Map = Map_import

def rowF (val=row_start):
    """vision start row"""
    global row_start
    row_start = int(val)
    return val

def colF (val=col_start):
    """vision start column"""
    global col_start
    col_start = int(val)
    return val

def lengthF (val=length):
    """vision length"""
    global length
    length = int(val)
    return val

def widthF (val=width):
    """vision width"""
    global width
    width = int(val)
    return val

def init():
    """Map Initializtion"""
    global time, config, pedes,num_out,generatorSet,count, statictics
    global Length, Width, length, width, row_start, col_start
    pedes = []
    num_out = 0
    count = 0
    del pedes[:]
    statictics = []
    time = 0
    config = read("map")
    for i in range(0, length):
        for j in range(0, width):
            Map[i][j].set(config[i,j])


    generatorSet=[]
    # North
    for i in range(125,135):
        g=Generator(121,i,len(generatorSet))
        generatorSet.append(g)
    for i in range(85,100):
        g=Generator(121,i,len(generatorSet))
        generatorSet.append(g)
    # East
    for i in range(110,122):
        g=Generator(i,134,len(generatorSet))
        generatorSet.append(g)   
    for i in range(75,85):
        g=Generator(i,134,len(generatorSet))
        generatorSet.append(g)
    for i in range(35,45):
        g=Generator(i,134,len(generatorSet))
        generatorSet.append(g)
    for i in range(15,25):
        g=Generator(i,134,len(generatorSet))
        generatorSet.append(g) 
    # South
    for i in range(125,135):
        g=Generator(15,i,len(generatorSet))
        generatorSet.append(g)
    for i in range(105,115):
        g=Generator(15,i,len(generatorSet))
        generatorSet.append(g)
    # West
    for i in range(90,98):
        g=Generator(i,80,len(generatorSet))
        generatorSet.append(g)
    for i in range(35,40):
        g=Generator(i,80,len(generatorSet))
        generatorSet.append(g)

    for i in range(0, length):
        for j in range(0, width):
            config[i,j] = Map[i][j].getstate()  
    Length, Width = config.shape
    if row_start > Length:
	row_start = 0
    if col_start > Width:
        col_start = 0
    if row_start+length > Length:
	length = Length - row_start
    if col_start+width > Width:
        width = Width - col_start

def draw():
    PL.cla()
    cmap = matplotlib.cm.nipy_spectral
    PL.pcolor(config[row_start:row_start+length, col_start:col_start+width], vmin = 0, vmax = 1, cmap = cmap)
    PL.axis('image')
    PL.title('t = ' + str(time))

def update():
    global time, config,pedes,G,num_out, count
    time += 1
    p = GammaRandom(generatorSet)
    count = count + len(p)
    num_out = ped_update(pedes,Map,num_out,time,statictics)
    if count < 30000:
    	for ped in p:
    		ped.set_start(time)
    	pedes = pedes+p
        #print "statistics: ",len(statictics)
    	del p[:]
    if len(pedes)==0 and count > 29000:
    	#print "######complete#######"
    	heat = []
    	for i in range(length):
    		row = []
    		for j in range(width):
    			row.append(Map[i][j].get_sum())
    		heat.append(row)
    	write(heat,'heat.txt','list')
    	write(statictics, "Pedestrian.json","dict")
    #print "people in road: ",len(pedes)
    for i in range(0, length):
        for j in range(0, width):
            config[i,j] = Map[i][j].getstate()
    
    #print "people out map: ",num_out
    #print "################"

def visual():
    pSetters = [rowF,colF,lengthF,widthF]
    pycxsimulator.GUI(parameterSetters = pSetters).start(func=[init,draw,update]) 