# Pedestrian CA simulator in Python
#
# *** Map Sparsing****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import matplotlib.pyplot as PL
import matplotlib.image as IMG

img=IMG.imread('Stadium.png')
PL.xticks(range(0,200,10))
PL.yticks(range(0,140,10))
PL.grid()
PL.imshow(img,extent=[0,200,0,140])
PL.show()
