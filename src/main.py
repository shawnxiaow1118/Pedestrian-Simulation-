#-*- coding: utf-8 -*-
# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

#outer package
from math import *
from Pedestrian_Class import *
from read import *
from build_map import *
from visual import *
from ped_update import *
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

############################################

state = read("map")
static = []
for i in range(1,9):
    name_open = "static" + str(i)
    stat = read(name_open)
    static.append(stat)
##########################################

Map = build_map(state, static)
    
"""total = 45
while (total < 100):
    total = total + 1
    global time, config, pedes,num_out,generatorSet,count, statictics
    global Length, Width, length, width, row_start, col_start
    data = read("map")
    config = data
    pedes = []
    num_out = 0
    count = 0
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
    read_map2_generator(Map)

    signal = True
    while (signal):
        time += 1
        p = GammaRandom(generatorSet)
        count = count + len(p)
        if(count < 30000):
            for ped in p:
                ped.set_start(time)
            pedes = pedes+p
        del p[:]
        num_out = ped_update(pedes,Map,num_out,time,statictics)
        if len(pedes)==0 and count > 29000:
            print "######complete#######"
            heat = []
            for i in range(length):
                row = []
                for j in range(width):
                    row.append(Map[i][j].get_sum())
                heat.append(row)
            heat_name = "wxheat" + str(total) + ".txt"
            ped_name = "wxPedestrian" + str(total) + ".json"
            write(heat,heat_name,'list')
            write(statictics, ped_name,"dict")
            signal = False
        print "people in road: ",len(pedes)
        for i in range(0, length):
            for j in range(0, width):
                config[i,j] = Map[i][j].getstate()

        print "people out map: ",num_out
        print "################" """

#print Map[12][100].getstate(),Map[11][100].getstate(),Map[19][100].getstate()
#ped_update(pedes, Map)
read_map2_visual(Map)
read_map2_generator(Map)
visual()   	