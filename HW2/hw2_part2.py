fwdhash = [' a', 'he', 'e', 'y', 'u', 'an', 'th', 'o', '9', 'ck']
backhash = ['%4%', '7!', '9(*9(', '*%$', '@@@', '-?', '!@+3', '7654', '2', '%4']
#To whoever grades my code: the lists above were made originally to be used in a loop, but because we cant use them, now they just sit there to be indexed later.
#While technically referencing these strings directly in the replace statements results in code of lesser lines, im gonna leave them there beause theyre pretty.

def encrypt(message):
    message = str(message)
    message = message.replace(fwdhash[0],backhash[0]).replace(fwdhash[1],backhash[1]).replace(fwdhash[2],backhash[2]).replace(fwdhash[3],backhash[3]).replace(fwdhash[4],backhash[4]).replace(fwdhash[5],backhash[5]).replace(fwdhash[6],backhash[6]).replace(fwdhash[7],backhash[7]).replace(fwdhash[8],backhash[8]).replace(fwdhash[9],backhash[9])
    return message

def decrypt(message):
    message = str(message)
    message = message.replace(backhash[9], fwdhash[9]).replace(backhash[8],fwdhash[8]).replace(backhash[7],fwdhash[7]).replace(backhash[6],fwdhash[6]).replace(backhash[5],fwdhash[5]).replace(backhash[4],fwdhash[4]).replace(backhash[3],fwdhash[3]).replace(backhash[2],fwdhash[2]).replace(backhash[1],fwdhash[1]).replace(backhash[0],fwdhash[0])
    return message

msg = input("Enter a string to encode ==> ")
coded = encrypt(msg)
print(msg+"\n")
print("Encrypted as ==> ", coded)
print("Difference in length ==>", abs(len(coded)-len(msg)))
print("Deciphered as ==>", decrypt(coded))
print("Operation is reversible on the string.") if msg == decrypt(coded) else print("Operation is not reversible on the string.")
