'''

Author - Hanson Ma

hanson.hq.ma@gmail.com

https://www.github.com/hansonhqma

'''

import textwrap

def formatandprint(text): #simple print function using textwrap
    text = textwrap.wrap(text)
    for line in text:
        print(line)

def findtitle(ftitles, query): #find the title given some string query
    for title in ftitles:
        if query.lower() in title.lower():
            return "\nFound the following title: " + title, title
    return "\nThis title is not found!\n", False


if __name__ == "__main__": #main statement
    while True:
        titles, names, subjects = open("titles.txt"), [], []
        while True:
            line = titles.readline()
            if line == "":
                break
            line = line.strip().split("|")
            names.append(line[0])
            subjects.append([])
            subjects[-1] += line[1:]
        title = input("Enter a title (stop to end) => ")
        print(title)
        if title == "stop":
            break
        foundtitle = findtitle(names, title) #runs findtitle function
        print(foundtitle[0])
        if foundtitle[1] == False:
            continue

        titleindex = names.index(foundtitle[1]) #finds title index in list of titles
        beasts = "Beasts in this title: " + ", ".join(sorted(subjects[titleindex]))
        formatandprint(beasts)

        commmontitles = [] #list of common titles
        selfset = set(subjects[titleindex]) #builds set of subjects
        for othertitle in names:
            compareset = set(subjects[names.index(othertitle)])
            if len(selfset.intersection(compareset)) >= 1: #core logic behing common titles
                commmontitles.append(othertitle)
        commmontitles.remove(foundtitle[1]) #removing self, since for loop iterates through all
        commmontitles = sorted(commmontitles)
        common = "Other titles containing beasts in common: " + ", ".join(commmontitles)
        print("")
        formatandprint(common)
        selfsubjects = subjects[titleindex]
        subjects.pop(titleindex)
        beasts = []
        for sublist in subjects:
            for item in sublist:
                beasts.append(item) #flatten list
        only = "Beasts appearing only in this title: " + ", ".join(sorted(set(selfsubjects).difference(set(beasts))))
        print("")
        formatandprint(only)
        print("")
