## PyCX 0.2 Realtime Visualization Template
## 
## Written by:
## Chun Wong
## email@chunwong.net
##
## Revised by:
## Hiroki Sayama
## sayama@binghamton.edu
##
## Copyright 2012 Chun Wong & Hiroki Sayama

# keep the following two lines as is
import matplotlib
matplotlib.use('TkAgg')

##=====================================
## Section 1: Import Modules
##=====================================

# i.e., import pylab as PL

##=====================================
## Section 2: Define Model Parameters
##=====================================

# i.e., n = 10000, RD.seed(), etc.

##=====================================
## Section 3: Define Three Functions
##=====================================

def init():
    # initialize system states
    # use 'global' to define global variables
    
def draw():
    # visualize system states using pylab functions
    # use PL.cla() to clear axis before drawing if needed
    # set title or other related visualizations if needed

def step():
    # update system states for one discrete time step
    # use 'global' to modify global variables
    
##=====================================
## Section 4: Import and Run GUI
##=====================================

import pycxsimulator
pycxsimulator.GUI(title='My Simulator',interval=10).start(func=[init,draw,step])
# 'title' and 'interval' are optional
