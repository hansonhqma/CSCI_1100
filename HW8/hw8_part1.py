from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist
import json

def update(ab=[], at=[], rb=[], rt=[]): #update function for all players
	for obj in ab:
		obj.update()
	for obj in at:
		obj.update()
	for obj in rb:
		obj.update()
	for obj in rt:
		obj.update()	

def extract_feature_layer(layer): #debugging function to extract different layers of field
	if layer > 2 or layer < 0:
		return
	featurelayer = []
	for row in field:
		r = []
		for stack in row:
			r.append(stack[layer])
		featurelayer.append(r)
	out = ""
	for row in featurelayer:
		r = ""
		for item in row:
			r += "{:>4}".format(item)
		out += r + "\n"

	print(out)

if __name__ == "__main__":

	bears, tourists = [], []

	f = open("bears_and_berries_1.json") 
	data = json.loads(f.read())

	size = len(data["berry_field"])
	field=[] #field is a size x size x 3 dimensional list array
	for i in range(size):
		row = []
		for j in range(size):
			row.append([data["berry_field"][i][j],0,0]) #rebuild featuremap style field array
		field.append(row)
	f = BerryField(field)

	active_bears, active_tourists = [], []

	for metadata in data["active_bears"]: #adding active bears
		obj = Bear((metadata[0], metadata[1]), metadata[2], field)
		active_bears.append(obj)

	for metadata in data["active_tourists"]: #adding active tourists
		obj = Tourist(metadata[0], metadata[1], field)
		active_tourists.append(obj)

