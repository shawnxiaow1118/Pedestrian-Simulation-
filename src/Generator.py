# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

import random
import math
from Pedestrian_Class import *
"""GammaDistribution"""
def read_map2_generator(map):
	global Map
	Map = map

def GammaRandom(L):
	Pedes = []
	weighted = []
	for i in range(0,100):
		weighted.append(i)			

	GeneNo = int(random.gammavariate(4.0, 1.0))
	if GeneNo <= 100:
		GeneList = random.sample(weighted, GeneNo)
	else:
		GeneList = range(100)
	for i in GeneList:
		temppede = L[i].generate()
		if(temppede.get_ped_info()['x']!=0):
			Pedes.append(temppede)

	return Pedes


"""Generator"""

class Generator:
	PedesID = 0
	Pedes = []
	def __init__(self,x,y,ID):
		self.x = x
		self.y = y
		self.ID = ID

	def generate(self):
		DestinatinationN = random.choice([0,0,0,1,2,3,5,5,6,7,4,2])
		DestinatinationE = random.choice([0,0,2,2,1,1,5,1,0,0,3,3,5,6,7])
		DestinatinationS = random.choice([0,0,0,1,1,1,2,2,2,3,0,1,2,2,5,7,6])
		DestinatinationW = random.choice([0,0,0,0,2,2,3,3,3,5,7,1,1,1,2,3])
		NewPedes= Pedestrian()
		if self.ID <= 24:
			#North
			if (Map[self.x+1][self.y].getstate() == 1):
				NewPedes.set(self.x + 1, self.y, DestinatinationN, Generator.PedesID,1,Map,0)
			else:
				Generator.PedesID -= 1
		elif self.ID <= 66:
			#East
			if (Map[self.x][self.y+1].getstate() == 1):
				NewPedes.set(self.x, self.y+1, DestinatinationE, Generator.PedesID,1,Map,1)		
			else:
				Generator.PedesID -= 1 
		elif self.ID <= 86:
			#South
			if (Map[self.x-1][self.y].getstate() == 1):
				NewPedes.set(self.x - 1, self.y, DestinatinationS, Generator.PedesID,1,Map,2)
			else:
				Generator.PedesID -= 1 
		else:
			#West
			if (Map[self.x][self.y-1].getstate() == 1):
				NewPedes.set(self.x, self.y-1, DestinatinationW, Generator.PedesID,1,Map,3)
			else:
				Generator.PedesID -= 1 

		Generator.PedesID += 1
		return NewPedes


"""Initiation of Generator"""
















"""a = Generator()
a.show()
print a.PedesID
BB = Generator()
BB.show()
print BB.PedesID
c = Generator()
c.show()
print c.PedesID"""
"""pedes = Pedestrian()
        if self.ID <= 5:
            destination = random.choice([0,1,2,3,4,5,6,7])
            pedes.set(self.x, self.y + 1, destination)"""













"""alpha = 2.0
		beta = 2.0
		maximum_outlet = 10
		error = random.choice([-1,0,1])
		#error used to modify pdedstrian
		x = timestep
		pedestrian_number_gamma= 10 * maximum_outlet * (x ** (alpha - 1) * math.exp(-x / beta)) / (math.gamma(alpha) * beta ** alpha)
		pedestrian generation follow Gamma distribution
		pedestrian_number_witherror = pedestrian_number_gamma + error

		if int(pedestrian_number_witherror) <= maximum_outlet:
			return int(pedestrian_number_witherror)
		else:
			return maximum_outlet

	    def destination(self):
		#Marta = 0, dometery = 1, parking lot = 2,
		LL=[]
		Marta_weight = 0.4
		parkinglot_weight = 0.4
		dometery_weight = 0.2

		ll= random.randrange(0,1)
		if ll in range(0,Marta_weight):
			return 1
		elif ll in range(Marta_weight, Marta_weight + parkinglot_weight):
			return 2
		else:
			return 3"""

