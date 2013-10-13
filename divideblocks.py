def blockConverter(sentence):
    encoded = []
    res = ""
    for i in range(0,len(sentence)):
        if i%4==0 and i!=0 :
            encoded.append(res)
            res = ""
        temp = bin(ord(sentence[i]))[2:]
        if len(temp) <8:
            temp = "0"*(8-len(temp)) + temp
        res = res + temp
    encoded.append(res)
    return encoded

def getBlocksInt(sentence):
    encoded = blockConverter(sentence)    
    decimalencoded = []
    for i in range(0,4):
        decimalencoded.append(int(encoded,2))
    return decimalencoded


def getBlocksBinary(sentence):
    return blockConverter(sentence)
	
sentence = "A WORD IS A WORD"
print getBlocksBinary(sentence)
