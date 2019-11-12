import syllables

def asl(text): #function asl returns the average sentence length
    count = []
    wcount = 0
    for word in text:
        if '.' not in word and '!' not in word and '?' not in word: #if the word is not a sentence closer
            wcount += 1 #add one to a count of words
        else:
            count.append(wcount + 1) #if it is a sentence closer, finalize this count and put it in a list
            wcount = 0
    return sum(count)/len(count) #returns average


def phw(text): #function phw returns the percent hard words and a list of them
    checkedwords = []
    for word in text:
        wordsuffix = str(word[-1*min(2,len(word))]+word[-1]) #creates a string of the last two letters of a word
        if syllables.find_num_syllables(word.lower()) >= 3 and '-' not in word: #checks for case 1
            checkedwords.append(word)
        elif syllables.find_num_syllables(word.lower()) == 3 and wordsuffix not in ('ed', 'es'): #checks for case 2
            checkedwords.append(word)
    return len(checkedwords)/len(text)*100, checkedwords #returns the percent hard words, and a list of the hard words

def asyl(text): #function asyl returns the average syllables for a paragraph
    s = 0
    for word in text:
        s += syllables.find_num_syllables(word) #for every word in the paragraph, add the syllable count to an integer object
    return s/len(text) #return this integer object

def gfri(text): #basic gfri function
    return 0.4*(asl(text)+phw(text)[0])

def fkri(text): #basic fkri function
    return 206.835-1.015*asl(text)-86.4*asyl(text)

#print statements
utext = input("Enter a paragraph => ")
print(utext)
utext = utext.split()
print("Here are the hard words in this paragraph:\n"+str(phw(utext)[1]))
print("Statistics: ASL:{ASL:.2f} PHW:{PHW:.2f}% ASYL:{ASYL:.2f}".format(ASL = asl(utext), PHW = (phw(utext)[0]), ASYL = (asyl(utext))))
print("Readability index (GFRI): {:.2f}".format(gfri(utext)))
print("Readability index (FKRI): {:.2f}".format(fkri(utext)))
