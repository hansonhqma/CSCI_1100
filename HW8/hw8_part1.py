from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist
import json

def update(ab=[], at=[], rb=[], rt=[]): #update method for all players
	for obj in ab:
		obj.update()
	for obj in at:
		obj.update()
	for obj in rb:
		obj.update()
	for obj in rt:
		obj.update()	

def print_feature_layer(layer): #debugging method to "peer" into different layers of field
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

def extract_feature_layer(layer): #same as print feature layer but this returns as a nested list
	if layer > 2 or layer < 0:
		return
	featurelayer = []
	for row in field:
		r = []
		for stack in row:
			r.append(stack[layer])
		featurelayer.append(r)

	return featurelayer

def sum_stacked(nested): #nested list summation method for counting berries
	s = 0
	for sublist in nested:
		for item in sublist:
			s += item
	return s

def cycle(iter):
	print("\nTurn: {}".format(iter+1))
	f.update()
	update(active_bears, active_tourists)

	bactivity, tactivity = [], []

	for bear in active_bears:
		bactivity.append(bear.active)

	for tourist in active_tourists:
		tactivity.append(tourist.active)

	while True:
		try:
			i = bactivity.index(False)
			print(active_bears[i])
			active_bears.pop(i)
			bactivity.pop(i)
		except:
			break

	while True:
		try:
			i = tactivity.index(False)
			print(active_tourists[i])
			active_tourists.pop(i)
			tactivity.pop(i)
		except:
			break

	print("Field has {} berries.".format(sum_stacked(extract_feature_layer(0))))
	print(f)
	print("Active Bears:")
	for bear in active_bears:
		print(bear)
	print("\nActive Tourists:")
	for tourist in active_tourists:
		print(tourist)
	print()

if __name__ == "__main__": #main method

	jstring = input("Enter the json file name for the simulation => ")
	print(jstring)
	bears, tourists = [], []
	f = open(jstring) #CHANGE THIS
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

	print("\nField has {} berries.".format(sum_stacked(extract_feature_layer(0))))
	print(f)
	print("Active Bears:")
	for bear in active_bears:
		print(bear)
	print("\nActive Tourists:")
	for tourist in active_tourists:
		print(tourist)