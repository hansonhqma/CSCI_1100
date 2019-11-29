'''

Author - Hanson Ma

hanson.hq.ma@gmail.com

https://www.github.com/hansonhqma

'''
import string

class autocorrect: #class autocorrect
    def __init__(self, word, dct, chars):
        self.word = word
        self.dictionary = dct
        self.chars = chars
        self.dropset = set()
        self.insertset = set()
        self.swapset = set()
        self.replaceset = set()
        self.likely = []
        self.results = dict()

        self.wordset = set(list(self.dictionary.keys()))

    #TODO Add lexicographic sorting case exception - DONE
    def matchhandler(self, matchlist): #handles the list of possible matches, sorting them in frequency order
        out = []
        tosort = []
        for item in matchlist:
            freq = float(self.dictionary[item])
            tosort.append((freq, item))
        sortedlist = sorted(tosort, reverse=True)
        for item in sortedlist:
            out.append(item[1])
        return out


    def checkfound(self):
        if self.word in list(self.dictionary.keys()):
            self.likely += [self.word]
            return True
        else:
            return False

    def checkdrop(self):
        for i in range(len(self.word)): #builds list of drop variants
            self.dropset.add(self.word[:i]+self.word[i+1:])

        #dropset built
        matches = list(self.dropset.intersection(self.wordset))
        if len(matches) > 0:
            self.likely += matches
            return True
        else:
            return False

    def checkinsert(self): #builds insert variants using ascii_lowercase string
        alpha = list(string.ascii_lowercase)
        for letter in alpha:
            self.insertset.add(letter + self.word)
            for i in range(len(self.word)+1):
                self.insertset.add(self.word[:i]+letter+self.word[i:])
        #insertset built
        matches = list(self.insertset.intersection(self.wordset))
        if len(matches) > 0:
            self.likely += matches
            return True
        else:
            return False

    def checkswap(self): #builds swap variants
        for i in range(len(self.word)-1):
            swapped = self.word
            back, fwd = self.word[i], self.word[i+1] #foward and back indexing to construct all swap variants
            swapped = list(swapped)
            swapped[i], swapped[i+1] = fwd, back
            swapped = "".join(swapped)
            self.swapset.add(swapped)

        #swapset built
        matches = list(self.swapset.intersection(self.wordset))
        if len(matches) > 0:
            self.likely += matches
            return True
        else:
            return False

    def checkreplace(self): #builds replace variants using char library
        for i in range(len(self.word)):
            letterswaps = self.chars[self.word[i]]
            for swap in letterswaps:
                word = list(self.word)
                word[i] = swap
                word = "".join(word)
                self.replaceset.add(word)

        #replaceset built
        matches = list(self.replaceset.intersection(self.wordset))
        if len(matches) > 0:
            self.likely += matches
            return True
        else:
            return False

    def checknomatch(self):
        if len(self.likely) == 0:
            return True
        else:
            return False

    def main(self):
        self.results = [self.checkfound(), self.checkdrop(), self.checkinsert(), self.checkswap(), self.checkreplace(), self.checknomatch()] #internal variable containing values of each test
        self.likely = self.matchhandler(self.likely) #match handling to sort the list of matches

globaldictionary, globalchars = dict(), dict()

def main():
    dictfile = input("Dictionary file => ")
    print(dictfile)
    inputfile = input("Input file => ")
    print(inputfile)
    keyboardfile = input("Keyboard file => ")
    print(keyboardfile)

    dictfile, inputfile, keyboardfile = open(dictfile), open(inputfile), open(keyboardfile)

    words = []

    #construct dictionary of dictionary file
    while True:
        line = dictfile.readline()
        if line == "":
            break
        line = line.strip().split(",")
        globaldictionary[line[0]] = line[1]

    #construct dictionary of keyboard data
    while True:
        line = keyboardfile.readline()
        if line == "":
            break
        line = line.strip().split(" ")
        globalchars[line[0]] = line[1:]

    #construct list of words to check
    while True:
        line = inputfile.readline()
        if line == "":
            break
        line = line.strip()
        words.append(line)

    for item in words:
        corrected = autocorrect(item, globaldictionary, globalchars) #object instantiation
        corrected.main()

        if corrected.results[0]:
            print("{:<15} -> {:<15} {}".format(corrected.word, corrected.word, ":FOUND"))
        elif corrected.results[5]:
            print("{:<15} -> {:<15} {}".format(corrected.word, corrected.word, ":NO MATCH"))
        else:
            for i in range(len(corrected.likely)):
                if i == 3:
                    break
                print("{:<15} -> {:<15} {} {}".format(corrected.word, corrected.likely[i], ":MATCH", i+1))

if __name__ == "__main__": #main function
    main()