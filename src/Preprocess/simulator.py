# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Simulator ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

row_start = 0
col_start = 0
length = 140
width = 200


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
    global time, config, x, y 
    global Length, Width, length, width, row_start, col_start
    time = 0

    ##map = open("map.txt", "r")
    ##config = []
    ##for line in map:
    ##	number_strings = line.split() 
    ##	numbers = [float(n) for n in number_strings] 
    ##	config.append(numbers) 
    config = SP.array(st_matrix)
    Length, Width = config.shape
    ##x = 10
    ##y = 30
    ##config[x,y]=0.9
    

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
    global time, config
    time += 1
    config = SP.array(st_matrix)
    ##tmp_x = x
    ##tmp_y = y
    ##d = RD.randrange(4)
    ##if d == 0 and (y+1)%Length != 0 and config[x,y+1] == 1:
	##tmp_y = y + 1 
    ##if d == 1 and (x+1)%Width != 0 and config[x+1,y] == 1:
	##tmp_x = x + 1
    ##if d == 2 and y != 0 and config[x,y-1] == 1:
	##tmp_y = y - 1
    ##if d == 3 and x != 0 and config[x-1,y] == 1:
	##tmp_x = x - 1

    ##config[x,y] = 1
    ##x = tmp_x
    ##y = tmp_y
    ##config[x,y] = 0.9

    #config[RD.randrange(row_start,row_start+length), RD.randrange(col_start,col_start+width)] = 0.9


import pycxsimulator
pSetters = [rowF,colF,lengthF,widthF]
pycxsimulator.GUI(parameterSetters = pSetters).start(func=[init,draw,update])
