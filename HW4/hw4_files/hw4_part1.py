import string #used to call the ascii alphabet because who's really gonna write the whole thing out

pword = input("Enter a password => ")
print(pword)
alphabet = list(string.ascii_lowercase)
case = {True:"satisfied", False:"not satisfied"} #dictionary used for validity cases
results = []
validity = ""

def verification(keytext): #wrapper function for all 5 cases
    rule1 = 10 <= len(keytext) and 25 >= len(keytext) and keytext[0].lower() in alphabet #simple one-liner for rule 1
    rule2 = ('@' in keytext or '$' in keytext) and '%' not in keytext #simple one-liner for rule 2
    rule3flag11, rule3flag12, rule3flag2 = 0, 0, 0 #separating rule 3 into different subrules
    for character in keytext:
        if character.islower():
            rule3flag11 += 1
        if character.isupper():
            rule3flag12 += 1
        if character in ['1','2','3','4']:
            rule3flag2 += 1
    rule3 = (rule3flag11 >= 1 and rule3flag12 >= 1) or rule3flag2 >= 1 #declaring rule 3 based on conditions of subrules
    for i in range(len(keytext)): #runs until either the string index runs out or it does not identify an underscore following an uppercase letter
        if keytext[i] in list(string.ascii_uppercase):
            if i+1 == len(keytext):
                rule4 = False
                break
            if keytext[i+1] == '_':
                rule4 = True
            else:
                rule4 = False
                break
        else:
            rule4 = True
    for character in keytext:
        if character in ['1','2','3','4','5','6','7','8','9']: #checks number presence for rule 5
            if int(character) >= 4:
                rule5 = False
                break
            else:
                rule5 = True
        else:
            rule5 = True
    return rule1, rule2, rule3, rule4, rule5 #returns a list of all conditions

out = verification(pword) #runs method

for condition in out:
    results.append(case[condition]) #creaes a list of result strings

if False not in out:
    validity = "The password is valid"

if False in out:
    if out[0] == True:
        validity = "A suggested password is: {}".format(pword[:8]+"42"+pword[-8:]) #using slice indexes, "42" is inserted in between the two strings
    else:
        validity = "The password is not valid"


print("Rule 1 is {}\nRule 2 is {}\nRule 3 is {}\nRule 4 is {}\nRule 5 is {}".format(results[0],results[1],results[2],results[3],results[4])) #by calling the results lists earlier, this prints all the result statements
print(validity)
