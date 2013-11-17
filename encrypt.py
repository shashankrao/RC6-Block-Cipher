from helpers import *

def encrypt(sentence,s):
    encoded = blockConverter(sentence)
    enlength = len(encoded)
    A = long(encoded[0],2)
    B = long(encoded[1],2)
    C = long(encoded[2],2)
    D = long(encoded[3],2)
    orgi = []
    orgi.append(A)
    orgi.append(B)
    orgi.append(C)
    orgi.append(D)
    r=12
    w=32
    modulo = 2**32
    lgw = 5
    B = (B + s[0])%modulo
    D = (D + s[1])%modulo 
    for i in range(1,r+1):
        t_temp = (B*(2*B + 1))%modulo 
        t = ROL(t_temp,lgw,32)
        u_temp = (D*(2*D + 1))%modulo
        u = ROL(u_temp,lgw,32)
        tmod=t%32
        umod=u%32
        A = (ROL(A^t,umod,32) + s[2*i])%modulo 
        C = (ROL(C^u,tmod,32) + s[2*i+ 1])%modulo
        (A, B, C, D)  =  (B, C, D, A)
    A = (A + s[2*r + 2])%modulo 
    C = (C + s[2*r + 3])%modulo
    cipher = []
    cipher.append(A)
    cipher.append(B)
    cipher.append(C)
    cipher.append(D)
    return orgi,cipher


def main():
    print "ENCRYPTION: "
    #key='A WORD IS A WORD'
    key =raw_input("Enter Key(0-16 characters): ")
    if len(key) <16:
        key = key + " "*(16-len(key))
    key = key[:16]
                         
    print "UserKey: "+key 
    s = generateKey(key)
    #sentence = 'I WORD IS A WORD'
    sentence =raw_input("Enter Sentence(0-16 characters): ")
    if len(sentence) <16:
        sentence = sentence + " "*(16-len(sentence))
    sentence = sentence[:16]
    
    orgi,cipher = encrypt(sentence,s)
    esentence = deBlocker(cipher)
    
    print "\nInput String: "+sentence 
    print "Original String list: ",orgi
    print "Length of Input String: ",len(sentence)
    
    print "\nEncrypted String list: ",cipher
    print "Encrypted String: " + esentence
    print "Length of Encrypted String: ",len(esentence)
    f = open("encrypted.txt","w")
    f.write(esentence);
    f.close()

if __name__ == "__main__":
    main()
