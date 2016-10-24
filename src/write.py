# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import json

def write(list, name,type):
	if type == "dict":
		with open(name,'w') as f:
			json.dump(list, f,indent=2) 
	else: 
		with open(name, 'w') as f:
			row = len(list)
			col = len(list[0])
			for i in range(row):
				for j in range(col):
					f.write(str(list[i][j]))
					f.write(",")
				f.write('\n')

