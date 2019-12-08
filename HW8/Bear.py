class Bear:
	def __init__(self, pos, dir, fieldList):
		self.dir  = dir
		self.loc = pos
		self.dir_vectormap = {"N":(-1,0),"E":(0,1),"S":(1,0),"W":(0,-1),\
							"NE":(-1,1), "SE":(1,1), "SW":(1,-1), "NW":(-1,-1)}
		self.pose = self.dir_vectormap[self.dir]
		self.fieldList = fieldList
		self.fieldList[pos[0]][pos[1]][1] += 1
		self.sleepstate = 0
		self.eaten = 0
		self.active = True

	def __str__(self):
		if self.active:
			if self.sleepstate > 0:
				return "Bear at ({},{}) moving {} - Asleep for {} more turns".format(self.loc[0], self.loc[1], self.dir, self.sleepstate)
			else:
				return "Bear at ({},{}) moving {}".format(self.loc[0], self.loc[1], self.dir)
		else:
			self.loc = self.vector_add(self.loc, self.pose)
			return "Bear at ({},{}) moving {} - Left the Field".format(self.loc[0], self.loc[1], self.dir)

	def vector_add(self, t1, t2):
		return (t1[0]+t2[0], t1[1]+t2[1])

	def posn(self, value): #position normalizer
		return max(min(value, len(self.fieldList)-1),0)
	
	def next_movement_valid(self): #compares raw position with normalized position to determine if the next move is valid or not
		current = self.loc
		raw_next = self.vector_add(current, self.pose)
		normalized_next = (self.posn(raw_next[0]), self.posn(raw_next[1]))
		if raw_next == normalized_next:
			return True
		else:
			return False

	def update(self, epoch=1): #TODO, fix inactivity after wake
		
		for i in range(epoch):
			if self.active:
				if self.sleepstate == 0: #not asleep
					
					# RUNTIME:

					self.eaten = 0
					while True:
						if self.fieldList[self.loc[0]][self.loc[1]][2] > 0: #tourist exists on same spot
							self.sleepstate = 3
							break

						else: #tourist not on spot
							while self.fieldList[self.loc[0]][self.loc[1]][0] > 0:
								self.fieldList[self.loc[0]][self.loc[1]][0] -= 1
								self.eaten += 1
								if self.eaten >= 30:
									return



							self.fieldList[self.loc[0]][self.loc[1]][1] -= 1 # remove self from boardstate
							
							if not self.next_movement_valid():
								#if the next move is not valid, it must be running off the edge; set inactive, break method.
								self.active = False #deem inactive
								return

							self.loc = self.vector_add(self.loc, self.pose) # update self position
							self.loc = self.posn(self.loc[0]), self.posn(self.loc[1]) # normalize self position
							self.fieldList[self.loc[0]][self.loc[1]][1] += 1 #update board with self position
				
				if self.sleepstate > 0:
					#is asleep
					self.sleepstate -= 1
					return

		return