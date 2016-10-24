from math import *
import numpy as np
import random
import scipy  as SP

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD

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


class Grid:
	def __init__(self):
		self.state = 1
		self.conflict_id = []
		self.conflict_prob = []
		self.sfloor = []
		self.dynamic = 0
		self.alpha = 0.7
		self.pass_group = [-1,-1,-1]

	def set(self, state):
		self.state = state

	def add_static(self, static):
		self.sfloor.append(static)

	def move_in(self, pid, prob):
		self.conflict_id.append(pid)
		self.conflict_prob.append(prob)

	def handler_conflict(self):
		#print self.conflict_id
		if len(self.conflict_id) > 1:
			rand = random.random()*sum(self.conflict_prob)
			cul_pro = []
			cul_ite = 0
			
			for i in range(len(self.conflict_prob)):
				cul_ite = cul_ite + self.conflict_prob[i]
				cul_pro.append(cul_ite)
			
			for j in range(len(cul_pro) - 1):
				if (rand <= cul_pro[0]): 
					ind = self.conflict_id[0]
					break
				elif (rand > cul_pro[j] and rand <= cul_pro[j+1]):
					ind = self.conflict_id[j+1]
					break
		else:
			ind = self.conflict_id[0]
		return ind

	def resetconflict(self):
		self.conflict_id = []
		self.conflict_prob = []

	def fill_state(self):
		self.state = 0.2

	def decay_dynamic(self):
		if self.dynamic > 0:
			temp = random.random()
			if temp < self.alpha:
				self.dynamic -= 1

	def update_dynamic(self):
		if self.dynamic < 10:
			self.dynamic += 1 

	def empty_state(self):
		self.state = 1

	def getsfloor(self):
		return self.sfloor

	def getdynamic(self):
		return self.dynamic

	def getstate(self):
		return self.state

	def getconflict_id(self):
		return self.conflict_id


	def update_group(self, group_id):
		if group_id == -1:
			self.pass_group.pop()
			self.pass_group.insert(0, group_id)
		else:
			self.pass_group[0] = group_id

	def get_group(self):
		return self.pass_group


############################################
ins = open("map.txt","r")
data = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	data.append(numbers)

state = SP.array(data)


static = []
ins = open("static1.txt","r")

stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)

ins = open("static2.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)
stat = SP.array(stat)
static.append(stat)

ins = open("static3.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)
stat = SP.array(stat)
static.append(stat)

ins = open("static4.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)


ins = open("static5.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)

ins = open("static6.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)

ins = open("static7.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)

ins = open("static8.txt","r")
stat = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	stat.append(numbers)

stat = SP.array(stat)
static.append(stat)

size = state.shape;
ro = size[0]
co = size[1]

##########################################

Map = []
for r in range(ro):
	row =[]
	for c in range(co):
		temp = Grid()
		for i in range(0,8):
			temp.set(state[r,c])
			temp.add_static(static[i][r,c])
		row.append(temp)
	Map.append(row)


class Pedestrian:
	def __init__(self):
		self.group = 0
		self.destination = 0
		self.x = 0
		self.y = 0
		self.id = 0
		self.mov_pro = 0
		self.xm = 0
		self.ym = 0
		self.b = 0.8
		self.bd = 0.02
		self.xf = 0
		self.yf = 0

	def set(self, x, y, des, id, group_id):
		self.x = x
		self.y = y
		self.xf = self.x
		self.yf = self.y
		self.destination = des
		self.group = group_id
		Map[self.x][self.y].fill_state()
		self.id = id

	def next_mov(self):
		S = []
		P = []
		D = []
		d_x = self.x - self.xf
		d_y = self.y - self.yf
		for i in range(0,3):
			for j in range(0,3): 
				if ((self.x+i-1) < 0 or (self.x+i-1) > (ro - 1) or (self.y+i-1) < 0 or (self.y+i-1) > (co - 1)):
					P.append(0)
				else:
					#d_e enhance the direction he comes frm
					d_e = 1
					if(i-1 == d_x and j-1 == d_y):
						d_e = exp(0.5)
					#decay the prob of the direction he has just passed
					d_d = 1
					if(i-1 == -1*d_x and j-1 == -1*d_y):
						d_e = exp(-0.2)					
					s = exp(Map[self.x][self.y].getsfloor()[self.destination] - Map[self.x+i-1][self.y+j-1].getsfloor()[self.destination])
					S.append(s)
					d = exp(self.bd*(Map[self.x+i-1][self.y+i-1].getdynamic() - Map[self.x][self.y].getdynamic()))
					if d < 1:
						d = 1
					D.append(d)
					p = 5.0/4*s*Map[self.x+i-1][self.y+j-1].getstate()*(Map[self.x+i-1][self.y+j-1].getstate() - 0.2)*d_d
					P.append(p)

		P[4] = exp(-1)
		max_val = max(P)
		##print max_val
		index = []
		for i in range(len(P)):
			if P[i] == max_val:
				index.append(i)
		i_3 = int(random.random()*len(index))
		max_index = index[i_3]
		self.xm = self.x + max_index/3 - 1
		self.ym = self.y + max_index%3 - 1
		##print self.x, self.y,"to",self.xm,self.ym,max_index,Map[self.xm][self.ym].getstate()
		##print Map[self.xm][self.ym].getstate()
		self.mov_pro = max_val/sum(P)


	def move(self):
		self.xf = self.x
		self.yf = self.y
	 	self.x = self.xm
	 	self.y = self.ym
	 	#self.mov_pro = 0


	def get_ped_info(self):
		c = {}
		c['x'] = self.x 
		c['y'] = self.y
		c['xm'] = self.xm
		c['ym'] = self.ym
		c['id'] = self.id
		c['mov_pro'] = self.mov_pro
		c['group'] = self.group
 		return c
#################################################

pedes = []
p0 = Pedestrian()
p0.set(13,30,0,1,1)
pedes.append(p0)
p1 = Pedestrian()
p1.set(11,30,0,2,1)
pedes.append(p1)
p2 = Pedestrian()
p2.set(9,30,1,3,1)
pedes.append(p2)
p3 = Pedestrian()
p3.set(34,6,1,4,1)
pedes.append(p3)
p4 = Pedestrian()
p4.set(100,7,1,5,1)
pedes.append(p4)
p5 = Pedestrian()
p5.set(60,7,1,6,1)
pedes.append(p5)
p6 = Pedestrian()
p6.set(10,50,6,7,1)
pedes.append(p6)
p7 = Pedestrian()
p7.set(10,51,6,8,1)
pedes.append(p7)
p8 = Pedestrian()
p8.set(12,100,3,9,1)
pedes.append(p8)
st_matrix = []
st_matrix_row = []
for i in range(ro):
	for j in range(co):
		st_matrix_row.append(Map[i][j].getstate())
	st_matrix.append(st_matrix_row)


#################################################
def init():
    """Map Initializtion"""
    global time, config
    global Length, Width, length, width, row_start, col_start
    time = 0

    map = open("map.txt", "r")
    config = []
    for line in map:
    	number_strings = line.split() 
    	numbers = [float(n) for n in number_strings] 
    	config.append(numbers) 
    config = SP.array(config)
    Length, Width = config.shape
    config[13,30] = 0.2
    config[11,30] = 0.2
    config[9,30] = 0.2
    config[34,6] = 0.2
    config[60,7] = 0.2
    config[100,7] = 0.2
    config[10,50] = 0.2
    config[10,51] = 0.2
    config[12,100] = 0.2
    del pedes[:]
    p0 = Pedestrian()
    p0.set(13,30,0,1,1)
    pedes.append(p0)
    p1 = Pedestrian()
    p1.set(11,30,0,2,1)
    pedes.append(p1)
    p2 = Pedestrian()
    p2.set(9,30,1,3,1)
    pedes.append(p2)
    p3 = Pedestrian()
    p3.set(34,6,1,4,1)
    pedes.append(p3)
    p4 = Pedestrian()
    p4.set(100,7,1,5,1)
    pedes.append(p4)
    p5 = Pedestrian()
    p5.set(60,7,1,6,1)
    pedes.append(p5)
    p6 = Pedestrian()
    p6.set(10,50,6,7,1)
    pedes.append(p6)
    p7 = Pedestrian()
    p7.set(10,51,6,8,1)
    pedes.append(p7)
    p8 = Pedestrian()
    p8.set(12,100,3,9,1)
    pedes.append(p8)
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
    invert_id_index = {}
    move_id = []
    print len(pedes)
    for pedestrian in pedes:
    	index_ped = pedes.index(pedestrian)
    	pedestrian.next_mov()
    	info = pedestrian.get_ped_info()
    	invert_id_index[info['id']] = index_ped
    	if(info['xm']!= info['x'] or info['ym'] != info['y']):
    		Map[info['xm']][info['ym']].move_in(info['id'],info['mov_pro'])
    
    for row in Map:
    	for grid in row:
    		grid.decay_dynamic()
    		grid.update_group(-1)
    		if grid.conflict_id != []:
    			ind = grid.handler_conflict()
    			move_id.append(ind)
    		grid.resetconflict()
    			#handle the group issues, no new group id enters this time
   # print "len pedes",len(pedes),"len invert_id_index",len(invert_id_index)
    del_list = []
    for item in move_id:
    	index = invert_id_index[item]
    	#print index
    	info = pedes[index].get_ped_info()
    	f_x = info['x']
    	f_y = info['y']
    	a_x = info['xm']
    	a_y = info['ym']
    	p_g = info['group']
    	config[f_x,f_y] = 1
    	Map[f_x][f_y].empty_state()
    	config[a_x,a_y] = 0.2
    	Map[f_x][f_y].update_dynamic()
    	#update the grid's group information
    	Map[f_x][f_y].update_group(p_g)
    	Map[a_x][a_y].fill_state()
    	pedes[index].move()
    	if (a_x == 0 or a_x == 139 or a_y == 0 or a_y == 199):
    		del_list.append(index)
    		Map[a_x][a_y].empty_state()
    		config[a_x][a_y] = 1
    		del invert_id_index[item]
    		print "index",index,"len pedes",len(pedes),"ivert",invert_id_index

    for item in del_list:
    	del pedes[item]


##ite = 0
##while(ite < 50):
##	ite  = ite + 1
##	invert_id_index = {}
##	move_id = []
##	for pedestrian in pedes:
##		index_ped = pedes.index(pedestrian)
##		pedestrian.next_mov()
##		info = pedestrian.get_ped_info()
##		invert_id_index[info['id']] = index_ped
##		if(info['xm']!= info['x'] or info['ym'] != info['y']):
##			Map[info['xm']][info['ym']].move_in(info['id'],info['mov_pro'])
##	for row in Map:
##		for grid in row:
##			grid.decay_dynamic()
##			if grid.conflict_id != []:
##				ind = grid.handler_conflict()
##				grid.resetconflict()
##				move_id.append(ind)

##	for item in move_id:
##		index = invert_id_index[item]
##		info = pedes[index].get_ped_info()
##		f_x = info['x']
##		f_y = info['y']
##		a_x = info['xm']
##		a_y = info['ym']
##		Map[f_x][f_y].empty_state()
##		Map[f_x][f_y].update_dynamic()
##		Map[a_x][a_y].fill_state()
##		pedes[index].move()
##	st_matrix = []
##	st_matrix_row = []
##	for i in range(ro):
##		for j in range(co):
##			st_matrix_row.append(Map[i][j].getstate())
##			st_matrix.append(st_matrix_row)
	##print pedes[0].get_ped_info()['x'],pedes[0].get_ped_info()['y']
	##print pedes[1].get_ped_info()['x'],pedes[1].get_ped_info()['y']
	##print pedes[2].get_ped_info()['x'],pedes[2].get_ped_info()['y']
	##print ite
##	info = pedes[0].get_ped_info()
##	if(info['x'] <= 0 or info['x'] >= ro or info['y'] <= 0 or info['y'] >= co):
##		break
	##info1 = pedes[1].get_ped_info()
	##if(info1['x'] <= 0 or info['x'] >= ro or info1['y'] <= 0 or info1['y'] >= co):
##		break

import pycxsimulator
pSetters = [rowF,colF,lengthF,widthF]
pycxsimulator.GUI(parameterSetters = pSetters).start(func=[init,draw,update])    	