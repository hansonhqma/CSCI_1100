import math
char = input("Enter frame character ==> ")# INPUTS
print(char)
height = int(input("Height of box ==> "))
print(height)
width = int(input("Width of box ==> "))
print(width,"\n",sep = '')
blank = ' '
whitecount = (height-3)/2#LOGIC
dimcount = ((width-3-len(str(height))-len(str(width)))/2)
print("Box:") #PRINT STATEMENTS
print((char*width)+("\n"+(str(char+blank*(width-2)+char)))*(int(whitecount)))
print(str(char+blank*int(dimcount)+str(width)+"x"+str(height)+blank*math.ceil(dimcount)+char))
print(((str(char+blank*(width-2)+char))+"\n")*(math.ceil(whitecount)-1)+(str(char+blank*(width-2)+char)))
print(char*width)
