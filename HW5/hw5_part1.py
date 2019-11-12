import random

class trainer: #Class trainer
    def __init__():
        return

    def move_trainer(): #trainer class func move_trainer
        print("Directions:", ['N', 'E', 'S', 'W'])
        print("Selected "+str(random.choice(['N', 'E', 'S', 'W']))+", value {:.2f}".format(round(random.random(),2))) #prints choice and random value
        return

    def throw_pokeball(nfalse, ntrue): #trainer class throw_pokeball
        n = [] #initialize list of boolean values
        for i in range(nfalse): #building falses
            n.append(False)
        for i in range(ntrue): #building trues
            n.append(True)
        print("Booleans:", n) #prints range of values
        print("Selected {}".format(random.choice(n))) #prints a random selection
        return

if __name__ == "__main__":
    tr = trainer

    size = input("Enter the integer grid size => ")
    print(size)
    f = input("Enter the integer number of Falses => ")
    print(f)
    t = input("Enter the integer number of Trues => ")
    print(t)
    f, t, size = int(f), int(t), int(size)
    print("Setting seed to", (11*size))
    random.seed(11*size) #seed initilization
    for i in range(10): #runs move_trainer 5 times, and throw_pokeball 5 times
        if i < 5:
            tr.move_trainer()
        else:
            tr.throw_pokeball(f, t)
