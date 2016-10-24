# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import scipy  as SP
def read(name):
	pth ="./src/Data/"
	name = pth + name + ".txt"
	ins = open(name,"r")
	data = []
	for line in ins:
		number_strings = line.split()
		numbers = [float(n) for n in number_strings]
		data.append(numbers)
	data = SP.array(data)
	return data