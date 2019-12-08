class Tourist:

	def __init__(self, row, col, fieldList):
		self.row = row
		self.col = col
		self.fieldList = fieldList
		self.fieldList[self.row][self.col][2] += 1

		self.observing = []
		self.lastSeen = 0

		self.distances = []
		self.active = True

		self.build_distances()

	def __str__(self):
		if self.active:
			return "Tourist at ({},{}), {} turns without seeing a bear.".format(self.row, self.col, self.lastSeen)
		else:
			return "Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(self.row, self.col, self.lastSeen)
	def euclid_distance(self, r, c):
		return ((self.row-r)**2+(self.col-c)**2)**0.5

	def build_distances(self):
		self.observing = []
		self.distances = []
		b_list = [] #raw list of second layer
		bear_coordinates = [] #empty list of coordinate tuples
		for row in self.fieldList:
			for itemmlist in row:
				b_list.append(itemmlist[1]) #build flattened list of second layer

		for i in range(len(b_list)): #index flattened list
			if not b_list[i] == 0: #if bear exists
				for j in range(b_list[i]): #for number of bears at that spot
					brow = i//len(self.fieldList) #get row
					bcol = i%len(self.fieldList) #get col
					bear_coordinates.append((brow, bcol)) #append coordinate to coordinate list as tuple

		for coordinate in bear_coordinates:
			e_distance = self.euclid_distance(coordinate[0], coordinate[1])
			self.distances.append(e_distance)
			if e_distance <=4:
				self.observing.append(coordinate)


	def update(self, epoch=1):
		for i in range(epoch):
			if self.active:
				self.build_distances()
				observing = len(self.observing)

				if observing == 0: #if it doesnt see a bear
					self.lastSeen += 1 #update last seen

				if self.fieldList[self.row][self.col][1] > 0: #if bear on the same spot
					self.active = False #state to false
					self.fieldList[self.row][self.col][2] -= 1 #remove self from spot

				elif self.lastSeen >= 3: #hasnt seen a bear in 3 turns
					self.active = False #state to inactive
					self.fieldList[self.row][self.col][2] -= 1 #goes home

				elif observing >= 3: #if it sees 3 or more bears
					self.active = False #state to inactive
					self.fieldList[self.row][self.col][2] -= 1 #remove self from layer

				elif observing > 0: #if it sees a bear
					self.lastSeen = 0

				
				
		return
		

