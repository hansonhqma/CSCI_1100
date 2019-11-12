import random

class trainer: #class trainer
    def __init__(self, boardsize):
        self.boardsize = boardsize #boardsize
        self.position = [boardsize //2, boardsize //2] #position in row, col
        self.moves = ['N', 'E', 'S', 'W'] #list of possible moves
        self.movehash = {'N':(-1,0), 'E':(0,1), 'S':(1,0), 'W':(0,-1)} #dictionary of possible directions and their respective position ammendments
        self.catch = [False, False, False, True] #initial boolean list
        self.log = [0,0] #log of pokemon seen and captured
        self.turn = 1 #turn
        return

    def move_trainer(self): #class trainer func move_trainer
        return random.choice(self.moves), random.random() #returns random selection of move and a random value

    def move(self, direction): #class trainer func move
        bearing = self.movehash[direction] #assigns bearing var to value of position ammendment list depending on string direction
        self.position[0] += bearing[0] #makes movement updates
        self.position[1] += bearing[1] #makes movement updates
        return

    def throw_pokeball(self): #class trainer func throw_pokeball
        outcome = random.choice(self.catch) #creates boolean outcome, if pokemon was caught or not
        if outcome:
            self.catch.append(True) #adds true value if caught
        self.catch.sort() #resorts list of boolean values to avoid the need for rebuilding the list everytime
        return outcome

    def check_boundary(self): #class trainer func check_boundary
        rowflag = self.position[0] == 0 or self.position[0] == (self.boardsize-1) #True if on edge
        colflag = self.position[1] == 0 or self.position[1] == (self.boardsize-1) #True if on edge
        return not(rowflag or colflag) #False if on edge


def run():
    size = input("Enter the integer grid size => ")
    print(size)
    p = input("Enter a probability (0.0 - 1.0) => ")
    print(p)
    size, p= int(size), float(p)
    random.seed(size*11) #seed initialization
    t = trainer(size) #creates class trainer instance
    while t.check_boundary(): #while t is in boundaries
        movement = t.move_trainer()
        t.move(movement[0])
        if movement[1] < p: #if sees pokemon
            t.log[0] += 1 #ammend log value
            print("Saw a pokemon at turn {0}, location {1}".format(t.turn, (t.position[0],t.position[1])))
            if t.throw_pokeball(): #if caught
                print("Caught it!")
                t.log[1] += 1 #ammend log value
            else:
                print("Missed ...")
        t.turn += 1 #increase turn number
    print("Trainer left the field at turn {}, location {}.".format(t.turn-1, (t.position[0],t.position[1])))
    print("{} pokemon were seen, {} of which were captured.".format(t.log[0], t.log[1]))
    return
if __name__ == "__main__":
    run() #run all
