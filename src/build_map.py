# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import scipy  as SP
from Grid_Class import *
from read import *
def build_map(state, static):
	Map = []
	size = state.shape
	ro = size[0]
	co = size[1]
	for r in range(ro):
		row =[]
		for c in range(co):
			temp = Grid()
			temp.set(state[r,c])
			for i in range(0,8):
				temp.add_static(static[i][r,c])
			row.append(temp)
		Map.append(row)
	return Map
