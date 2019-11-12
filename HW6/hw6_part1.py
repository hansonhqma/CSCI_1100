'''

Author - Hanson Ma

hanson.hq.ma@gmail.com

https://www.github.com/hansonhqma

'''

class word: #class word to keep things tidy
    def __init__(self, word):
        self.word = word
        self.likely = ""
        self.outcome = ""
        self.swappedvariants = set()
        self.droppedvariants = set()

    def constructcomparitors(self): #construsts self.swappedvariants and self.droppedvariants to compare both cases with dictionary
        self.swappedvariants = set()
        self.droppedvariants = set()
        #build possible drop variants
        for i in range(len(self.word)):
            self.droppedvariants.add(self.word[:i]+self.word[i+1:]) #slices to build possible drop variants

        #build possible swap variants
        for i in range(len(self.word)-1):
            swapped = self.word
            back, fwd = self.word[i], self.word[i+1] #foward and back indexing to construct all swap variants
            swapped = list(swapped)
            swapped[i], swapped[i+1] = fwd, back
            swapped = "".join(swapped)
            self.swappedvariants.add(swapped)

    def generatediff(self): #generates a difference library, values against every word in dictionary
        differencelibrary = []
        for word in dict:
            diffcount = 0
            #normalize length
            diff = abs(len(word) - len(self.word))
            if len(word) > len(self.word):
                myword = self.word + "_"*diff
                comparing = word
            elif len(word) < len(self.word):
                myword = self.word
                comparing = word + "_"*diff
            else:
                myword = self.word
                comparing = word
            for i in range(len(myword)):
                if not myword[i] == comparing[i]:
                    diffcount += 1
            differencelibrary.append(diffcount)
        return differencelibrary #difference library returns as a list of dictionary length, with each item representing the character-wise integer difference between the self.word and the given dictionary item

    def check(self): #check function generates self.likely, the probably word to be typed, and the outcome, which case modifies self.word into self.likely
        self.constructcomparitors()
        swapset = sorted(self.swappedvariants.intersection(set(dict)))
        dropset = sorted(self.droppedvariants.intersection(set(dict)))
        d = self.generatediff()

        if self.word in dict: #check match
            self.likely = self.word
            self.outcome = ":FOUND"
            return 0

        elif len(dropset) > 0: #check drop
            self.likely = list(dropset)[0]
            self.outcome = ":DROP"
            return 1

        elif len(swapset) > 0: #check swap
            self.likely = list(swapset)[0]
            self.outcome = ":SWAP"
            return 2

        elif d.count(1) > 0:
            self.likely = dict[d.index(1)]
            self.outcome = ":REPLACE"
            return 3

        else:
            self.likely = self.word
            self.outcome = ":NO MATCH"
            return 4

if __name__ == "__main__": #main statement
    #global variables
    dictionary = input("Dictionary file => ")
    print(dictionary)
    inputs = input("Input file => ")
    print(inputs)

    dictionary = open(dictionary)
    dict = [] #build dictionary list
    while True:
        line = dictionary.readline()
        if line == "":
            break
        line = line.strip()
        dict.append(line)

    inputfile = open(inputs)
    inputs = []
    while True:
        line = inputfile.readline()
        if line == "":
            break
        line = line.strip()
        inputs.append(line)

    for testing in inputs:
        obj = word(testing)
        obj.check()
        print("{:<15} -> {:<15} {}".format(obj.word, obj.likely, obj.outcome))