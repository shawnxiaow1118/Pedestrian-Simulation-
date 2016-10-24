from math import *
import random
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

	def set(self, x, y, des, id, group_id, Map):
		self.x = x
		self.y = y
		self.xf = self.x
		self.yf = self.y
		self.destination = des
		self.group = group_id
		Map[self.x][self.y].fill_state()
		self.id = id

	def next_mov(self, Map):
		S = []
		P = []
		D = []
		ro = len(Map)
		co = len(Map[0])
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