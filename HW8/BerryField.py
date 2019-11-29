class BerryField():
	def __init__(self, fieldList):
		self.size = len(fieldList)
		self.fieldList = fieldList

	def __str__(self):
		#TODO add T, B, X print cases
		out = ""
		for row in self.fieldList:
			line = ""
			for item in row:
				if item[1] == 0 and item[2] == 0: #only berries
					line += "{:>4}".format(item[0])
				
				elif item[1] > 0 and item[2] == 0: #bear but not tourists
					line += "{:>4}".format('B')

				elif item[1] == 0 and item[2] > 0:
					line += "{:>4}".format('T')
				
				else:
					line += "{:>4}".format('X')
			
			out += line + "\n"

		return out

	def posn(self, value): #position normalizer, localizes coordinate within boundaries
		return max(min(value, self.size-1),0)

	def validate_pos(self, row, col):

		#adjacency pairs; normalized coordinates of gridwise adjacent locations
		adj_pairs = [(self.posn(row-1), self.posn(col)),\
					(self.posn(row+1), self.posn(col)),\
					(self.posn(row), self.posn(col+1)),\
					(self.posn(row), self.posn(col-1)), \
					(self.posn(row-1), self.posn(col-1)),\
					(self.posn(row-1), self.posn(col+1)),\
					(self.posn(row+1), self.posn(col-1)),\
					(self.posn(row+1), self.posn(col+1))]

		adj_gradients = []

		for pair in adj_pairs:
			adj_gradients.append(self.fieldList[pair[0]][pair[1]][0]-self.fieldList[row][col][0])
		if adj_gradients.count(10) >= 1:
			return 1
		else:
			return 0

	def update(self, epochs=1): #grow function
		for i in range(epochs):
			for r in range(self.size):
				for c in range(self.size):
					if 1 <= self.fieldList[r][c][0] and self.fieldList[r][c][0] < 10:
						self.fieldList[r][c][0] += 1
			
			for r in range(self.size): #REITERATION NECESSARY FOR UPDATE
				for c in range(self.size):
					increment = self.validate_pos(r,c)
					self.fieldList[r][c][0] += increment
					# reiteration exists because validate_pos checks for adjacency gradients, and as
					# such needs adjacent values to be updated first before it recursively updates


