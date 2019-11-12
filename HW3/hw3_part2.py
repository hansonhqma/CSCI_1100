#parameters
board_size = (150,150)
movepairs = {"N":(0,5), "S":(0,-5), "E":(5,0), "W":(-5,0)} #movement hashmap
backuppairs = {"N":(0,-10), "S":(0,10), "E":(-10,0), "W":(10,0)} #losecase hashmap
opposites = {"N":"S", "S":"N", "W":"E", "E":"W"} #opposite direction hashmap

class pikachu:

    def __init__(self):
        self.history = [[75, 75, "None"]] #Where current state is self.history[-1]
        self.record = []

    def move_pokemon(self, direction): #moves pikachu given a direction and returns a new state
        if direction.upper() not in ("N", "S", "E", "W"):
            state = self.history[-1].copy()
        else:
            state = self.history[-1].copy() #creates a copy of the latest state to iterate
            for i in range(len(self.history[-1])-1): #state index addition, "moving" the pokemon
                state[i] += movepairs[direction][i]
                state[i] = min(max(state[i],0),board_size[i])

        state[2] = direction #appending the direction history
        self.history.append(state) #adds current state to history
        return state

    def encounter(self): #moves pikachu given an encounter and returns a new state and an outcome
        state = self.history[-1].copy() #creates a copy of the latest state to iterate
        type = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(type)
        outcome = ""
        if type.lower() == "g":
            if self.history[-1][2].upper() in ("N", "S", "E", "W"): #checks if the previous move direction is valid
                state[0] += backuppairs[self.history[-1][2]][0] #state index addition
                state[1] += backuppairs[self.history[-1][2]][1]
                state[0] = min(max(state[0],0),board_size[0])
                state[1] = min(max(state[1],0),board_size[1])
                state[2] = opposites[state[2]]
                self.history.append(state)
            else:
                state = self.history[-1].copy() #if previous move direction is not valid, the object does not update position
                self.history.append(state)
            self.record.append("Lose")
            outcome = "runs away to"

        elif type.lower() == 'w':
            if self.history[-1][2].upper() in ("N", "S", "E", "W"): #checks if the previous move direction is valid
                state[0] += (movepairs[self.history[-1][2]][0])/5 #state index addition
                state[1] += (movepairs[self.history[-1][2]][1])/5
                state[0] = min(max(state[0],0),board_size[0])
                state[1] = min(max(state[1],0),board_size[1])
                self.history.append(state)
            else:
                state = self.history[-1].copy() #if previous move direction is not valid, the object does not update position
                self.history.append(state)
            self.record.append("Win")
            outcome = "wins and moves to"

        else:
            self.record.append("No Pokemon")
        return state, outcome
#User inputs
turns = input("How many turns? => ")
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
freq = input("How often do we see a Pokemon (turns)? => ")
print(freq)
pika = pikachu()
#Game run
print("\nStarting simulation, turn 0 {} at {}".format(name, (pika.history[-1][1],pika.history[-1][0])))
moves = 0
while moves < int(turns): #iterative loop for turn counting
    i = 0
    while i < int(freq) and moves < int(turns):
        direction = input("What direction does {} walk? => ".format(name))
        print(direction)
        if direction.upper() not in ('N','E','S','W'): #if move is not valid, update loop hyperparameters and move object
            pika.move_pokemon(direction.upper())
            moves += 1
            i += 1
            continue
        pika.move_pokemon(direction.upper())
        moves += 1
        i += 1
    if moves > int(turns): #if moves is ever greater than turns, break the loop
        break

    if i == int(freq): #once it has reached the frequency count, execute an encounter action
        print("Turn {turn}, {name} at {pos}".format(turn = moves, name = name, pos = (int(150-pika.history[-1][1]), int(pika.history[-1][0]))))
        new_state = pika.encounter()
        if not new_state[1] == "": #if the outcome of the encounter is something valid, print an outcome update
            print("{name} {outcome} {pos}".format(name = name, outcome = new_state[1], pos = (int(150-new_state[0][1]), int(new_state[0][0]))))

print("{name} ends up at {pos}, Record: {record}".format(name = name, pos = (int(150-pika.history[-1][1]), int(pika.history[-1][0])), record = pika.record))
