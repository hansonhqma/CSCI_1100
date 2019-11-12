import random

def printboard(board): #func for printing the board
    for row in range(len(board)): #for every row
        line = ""
        for col in range(len(board)): #for every column
            line += "{:>5}".format(board[row][col]) #prints with 5 spaces of padding to the left
        print(line)

def flatten(list): #function to flatten nested list
    out = []
    for sublist in list:
        for item in sublist:
            out.append(item)
    return out

class trainer: #clas trainer
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.position = [boardsize //2, boardsize //2] #row, col
        self.moves = ['N', 'E', 'S', 'W']
        self.movehash = {'N':(-1,0), 'E':(0,1), 'S':(1,0), 'W':(0,-1)}
        self.catch = [False, False, False, True]
        self.log = [0,0]
        self.turn = 0
        return

    def move_trainer(self):
        return random.choice(self.moves), random.random()


    def move(self, direction):
        bearing = self.movehash[direction]
        self.position[0] += bearing[0]
        self.position[1] += bearing[1]
        return

    def throw_pokeball(self):
        outcome = random.choice(self.catch)
        if outcome:
            self.catch.append(True)
        self.catch.sort()
        return outcome

    def check_boundary(self):
        rowflag = self.position[0] == 0 or self.position[0] == (self.boardsize-1) #True if on edge
        colflag = self.position[1] == 0 or self.position[1] == (self.boardsize-1) #True if on edge
        return not(rowflag or colflag) #False if on edge

def run_one_simulation(boarddata, metadata): #function run_one_simulation
    t = trainer(size) #initialize class trainer instance
    while t.check_boundary():
        movement = t.move_trainer()
        t.move(movement[0])
        if movement[1] < p: #sees pokemon
            t.log[0] += 1 #Saw a pokemon
            if t.throw_pokeball(): #Caught pokemon
                t.log[1] += 1
                boarddata[t.position[0]][t.position[1]] += 1 #if caught, add one to the given board position
            else: #Missed pokemon
                boarddata[t.position[0]][t.position[1]] -= 1 #if missed, subtract one to the given board position
        t.turn += 1 #Turn update
    metadata.append(t.turn) #append metadata with the number of turns
    return

if __name__ == "__main__": #main
    #User inputs
    size = input("Enter the integer grid size => ")
    print(size)
    p = input("Enter a probability (0.0 - 1.0) => ")
    print(p)
    iter = input("Enter the number of simulations to run => ")
    print(iter+"\n")
    size, p, iter= int(size), float(p), int(iter)

    #Global var declaration
    random.seed(11*size) #seed initilization
    metadata = []
    boarddata = []
    for i in range(size):
        boarddata.append([0]*size) #creates boarddata list

    for i in range(iter):
        run_one_simulation(boarddata, metadata) #runs simulation for specified number of times
    flattened = flatten(boarddata)
    printboard(boarddata)
    print("Average number of turns in a simulation was {:.2f}".format(sum(metadata)/len(metadata)))
    print("Maximum number of turns was {} in simulation {}".format(max(metadata), metadata.index(max(metadata))+1))
    print("Minimum number of turns was {} in simulation {}".format(min(metadata), metadata.index(min(metadata))+1))
    print("Best net missed pokemon versus caught pokemon is {}".format(max(flattened)))
    print("Worst net missed pokemon versus caught pokemon is {}".format(min(flattened)))
