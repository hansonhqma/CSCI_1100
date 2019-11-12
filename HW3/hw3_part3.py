import math

def tpy(bears): #function tourists per year
    if bears < 4 or bears > 15: #checks for preliminary range validity
        t = 0
    else:
        t = min(bears,10)*10000 + max(bears-10,0)*20000 #one-liner for calculating tourists, i sure hope this is impressive, took me a hot minute to figure out cause i
        #didnt want to use if/else conditions
    return t

def find_next(bears, berries, tourists): #function that finds next bears and berries
    return int(max(berries/(50*(int(bears)+1)) + int(bears)*0.60 - (math.log(1+int(tourists),10)*0.1),0)), max((berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05),0)
#user inputs
currentbears = input("Number of bears => ")
print(currentbears)
currentbears = int(currentbears)
currentberries = input("Size of berry area => ")
print(currentberries)
currentberries = float(currentberries)

list = [[],[],[]] #3,length dimension list for keeping track of data

print("Year      Bears     Berry     Tourists")
for i in range(10):
    list[0].append(currentbears)#append statements for the list
    list[1].append(currentberries)
    list[2].append(tpy(currentbears))
    print(str(i+1)+' '*(10-len(str(i+1)))+str(currentbears)+' '*(10-len(str(currentbears)))+"{:.1f}".format(currentberries)+' '*5+str(tpy(currentbears))+' '*(10-len(str(tpy(currentbears)))))
    currentbears, currentberries = find_next(currentbears, currentberries, tpy(currentbears)) #value update

print("\nMin:      "+str(min(list[0]))+' '*9+"{:.1f}".format(min(list[1]))+' '*5+str(min(list[2])))
print("Max:      "+str(max(list[0]))+' '*9+"{:.1f}".format(max(list[1]))+' '*5+str(max(list[2])))
