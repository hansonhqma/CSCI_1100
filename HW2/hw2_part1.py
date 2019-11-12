import math

def find_volume_sphere(r):
    return float(4/3*math.pi*r**3)

def find_volume_cube(s):
    return float(s**3)

radius = input("Enter the gum ball radius (in.) => ")
print(radius)

sales = input("Enter the weekly sales => ")
print(sales+"\n")

print("The machine needs to hold",math.ceil((int(sales)*1.25)**(1/3)), "gum balls along each edge.")
print("Total edge length is {:.2f} inches.".format(math.ceil((int(sales)*1.25)**(1/3))*float(radius)*2))
print("Target sales were", str(math.ceil(int(sales)*1.25))+", but the machine will hold", math.ceil((int(sales)*1.25)**(1/3))**3-math.ceil(int(sales)*1.25), "extra gum balls.")
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(round(find_volume_cube(math.ceil((int(sales)*1.25)**(1/3))*float(radius)*2)-find_volume_sphere(float(radius))*math.ceil(int(sales)*1.25),2)))
print("or {:.2f} cubic inches if you fill up the machine.".format(round(find_volume_cube(math.ceil((int(sales)*1.25)**(1/3))*float(radius)*2)-find_volume_sphere(float(radius))*math.ceil((int(sales)*1.25)**(1/3))**3,2)))
