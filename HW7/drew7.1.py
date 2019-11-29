def found(dictionary, word):                            #start of defining functions
    if word in dictionary:
        return 0
    else:
        return 1
            
def replace(dictionary, word):
    replist = set()
    j = ''
    for i in range(len(word))
        characterlist = keys_dict[words[i]]
        for character in characterlist:
            word = list(word)
            word[i] = character
            word = "".join(word)
            if word in dictionary:
                replist.add(word)

    sub = list(word)
    end = sub[-1]
    for h in range(len(keys_dict[end])):
        sub[-1] = keys_dict[end][h]
        novus = j.join(sub)
        if novus in dictionary:
                replist.add(novus)
    return replist

def swap(dictionary, word):
    j = ''
    swaplist = set()
    for i in range(1, (len(word))):
        wlist = list(word)
        itempop = wlist.pop(i)
        wlist.insert((i-1), itempop)
        newword = j.join(wlist)
        if newword in dictionary:
            swaplist.add(newword)
    return swaplist

def drop(dictionary, word):
    j = ''
    droplist = set()
    for i in range((len(word))):
        wlist = list(word)
        wlist.pop(i)
        neword = j.join(wlist)
        if neword in dictionary:
            droplist.add(neword)
    return droplist
    
def insert(dictionary, word):
    j = ''
    insertlist = set()
    for i in range(len(word)):
        wlist = list(word)
        for h in letters:
            wlist.insert(i,h)
            word_new = j.join(wlist)
            if word_new in dictionary:
                insertlist.add(word_new)
    return insertlist
        



dict_file = input('Dictionary file => ')
print(dict_file)
word_input = input('Input file => ')
print(word_input)
keyboard = input('Keyboard file => ')
print(keyboard)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', \
           'w', 'x', 'y', 'z']
dictionary = open(dict_file)
words = open(word_input)
keys = open(keyboard)
dict_order = dict()
dict_set = set()
input_list = []                         #end of basic variable assignment
keys_dict = dict()

for line in dictionary:                         #start of basic computations and creation of dict() and set() based on files
    line = line.strip()
    line = line.split(',')
    dict_set.add(line[0])
    dict_order[line[0]] = float(line[1])

for line in words:
    line = line.strip()
    input_list.append(line)

for line in keys:
    line = line.strip()
    line = line.split()
    dict_keys = []
    for i in range(1,len(line)):
        dict_keys.append(line[i])
    keys_dict[line[0]] = dict_keys

for item in input_list:                 #start of main computation using functions
    if found(dict_set, item) == 0:
        print(('{:<15} {:<18} {}').format(item,'-> '+item,':FOUND'))
        continue
    else:
        word_set = drop(dict_set, item) | swap(dict_set, item) | replace(dict_set, item) | insert(dict_set, item)
        word_set = sorted(word_set)
    if len(word_set) == 0:
        print(('{:<15} {:<18} {}').format(item,'-> '+item,':NO MATCH'))
        continue
    order = []
    for i in word_set:
        order.append(dict_order[i])
    neworder = order.copy()
    fwords = []
    i = 0
    if len(word_set) == 2:
        i+=1
    elif len(word_set) == 1:
        i+=2
    w = 1
    while i < 3:
        index = neworder.index(max(neworder))
        neworder.pop(index)
        neworder.insert(index,0)
        fwords.append(word_set[index])
        print(('{:<15} {:<18} {}').format(item,'-> '+word_set[index],':MATCH '+str(w)))
        w+=1
        i += 1









