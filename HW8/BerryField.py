'''
Hello TA who's grading my paper, here is a little explanation of why my code for the field might look kind of awkward:


After writing the nested list that basically everyone wrote for their field class, I realized that this form
of data storage for the berry field results in a loss of data, after printing it with the T's, B's, and X's
denoting bears/tourists.

As such, I pivoted to a n*n*3 dimensional "array", which is basically just a triple nested list (please I'm begging you let me use numpy)

1. The first layer represents the raw count of berries at each location
2. The second layer shows positions of bears, where each position denotes the amount of bears currently there
	- A "1" means a bear is on that spot, a "0" means no bear
3. The third layer is the same as the second layer, except for tourists instead of bears

Printing the field is done by looking at each "stack" at each location, and looking at the existence of bears and tourists, and
then constructing a fourth "layer", to be printed

This way, the field is represented correctly, all while retaining the necessary data

This is why when you see "self.fieldList[row][col][0]", its calling the number of berries at (row,col)

"self.fieldList[row][col]" returns by reference a list of size 3, the 1st, 2nd, and 3rd index being berries, bears, and tourists respectively

'''
class BerryField():
	def __init__(self, fieldList):
		self.size = len(fieldList)
		self.fieldList = fieldList

	def __str__(self):
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
					# such needs adjacent values to be updated first before it updates


