happy = ['laugh', 'happiness', 'love', 'excellent', 'good', 'smile']
sad = ['bad', 'sad', 'terrible', 'horrible', 'problem', 'hate']

def number_happy(sentence):
    count = 0
    count += sentence.lower().count(happy[0])
    count += sentence.lower().count(happy[1])
    count += sentence.lower().count(happy[2])
    count += sentence.lower().count(happy[3])
    count += sentence.lower().count(happy[4])
    count += sentence.lower().count(happy[5])

    return count

def number_sad(sentence):
    count = 0
    count += sentence.lower().count(sad[0])
    count += sentence.lower().count(sad[1])
    count += sentence.lower().count(sad[2])
    count += sentence.lower().count(sad[3])
    count += sentence.lower().count(sad[4])
    count += sentence.lower().count(sad[5])

    return count

statement = input("Enter a sentence => ")
print(statement)
h = int(number_happy(statement))
s = int(number_sad(statement))
print("Sentiment:", str('+'*h)+str('-'*s))
if h == s:
    print("This is a neutral sentence.")
if h < s:
    print("This is a sad sentence.")
if h > s:
    print("This is a happy sentence.")
