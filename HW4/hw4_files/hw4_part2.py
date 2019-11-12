import hw4_util

data = hw4_util.read_university_file("university_data.csv")
names = []
for sublist in data:
    names.append(sublist[0]) #appends all names in data

def find_university(name):
    if name not in names:
        return False, -1 #if the name specified is not in the predefined list, return False and the -1 index
    else:
        return True, int(names.index(name)) #if it is in the predefined list, return True, and the index

uname = input("University name => ")
print(uname)
ufirst = input("Line number for first university to compare (1-1000) => ")
print(ufirst)
uscnd = input("Line number for second university to compare (1-1000) => ")
print(uscnd)

if find_university(uname)[0] == False:
    print("University not found")
else:
    print("First university: {}".format(data[int(ufirst)][0]))
    print("Second university: {}\n".format(data[int(uscnd)][0]))
    print(" "*25+"{0:>12}{1:>12}{2:>12}".format("First", "Second", "Yours"))
    for i in range(len(data[0][1:])):
        print("{0:>25}{1:>12}{2:>12}{3:>12}".format(data[0][1:][i],data[int(ufirst)][1:][i],data[int(uscnd)][1:][i],data[find_university(uname)[1]][1:][i]))
