min = input("Minutes ==> ")
print(min)
min = int(min)
sec = input("Seconds ==> ")
print(sec)
sec = int(sec)
mi = input("Miles ==> ")
print(mi)
mi = float(mi)
tmi = input("Target Miles ==> ")
print(tmi,"\n")
tmi = float(tmi)
print("Pace is",int(((min*60+sec)/mi)/60),"minutes and",int(60*((((min*60+sec)/mi)/60)-int(((min*60+sec)/mi)/60))),"seconds per mile.")
print("Speed is",format(round(60/(((min*60+sec)/mi)/60),2),'.2f'),"miles per hour.")
(((((min*60+sec)/mi)*tmi)/60)-int((((min*60+sec)/mi)*tmi)/60))*60
print("Time to run the target distance of",format(tmi, '.2f'),"miles is",int((((min*60+sec)/mi)*tmi)/60),"minutes and",int((((((min*60+sec)/mi)*tmi)/60)-int((((min*60+sec)/mi)*tmi)/60))*60),"seconds.")
