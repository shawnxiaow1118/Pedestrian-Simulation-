import random
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