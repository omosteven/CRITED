#This is python program that detect and tells you the hashing algorithm used to hash a plain text to cipher text
import enchant
import math
import cmath
import cmd
#import pyAesCrypt
english = enchant.Dict("en_US")
#french  = enchant.Dict("fr_FR")
def Filter():
    #CipherText = open(input("drag file or put in file here:")).read()
    #if (CipherText == False):
    #    print (CipherText)
        #print(english.check(l))

    CipherText = input("Type in the cipher text to detect")
    l = Ceaser(CipherText)

    def testceaser(CipherText):
        Plain = {}
        for Cipher in Ceaser(CipherText).keys():
            if (english.check(Ceaser(CipherText)[Cipher])):
                Plain.update({Cipher: Ceaser(CipherText)[Cipher]})
        print ('CEASER POSIBLE BRUTEFORCED TEXTS AND KEYS:',Plain)
    testceaser(CipherText)

def Ceaser(CipherText):
 #Hashing Algorithm to Decipher Ceaser Cipher Text
 #Symmetric Cruptography, Substitutional Cipher
 CipherText= CipherText.upper()
 letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #on no(hi) os us on
 PlainText ={}
 Plain = []
 for key in range(len(letter)):
    translated=''
    for symbol in CipherText:
        if symbol in letter:
            joy=letter.find(symbol)
            joy = joy - key
            if (joy < 0):
                joy = joy + len(letter)
            translated = translated + letter[joy]
            PlainText.update({key:translated})
        else:
              translated= translated+symbol
              PlainText.update({key:translated})
 return PlainText
Filter()

#Hashing algorithm for bruteforcing AES Cipher
def RSA(): #Assymetric Cryptography
    #Ron Rivest, Adi Shamir and Leonard Adleman
    #CipherText = CipherText.upper()
    E = int(input("Enter The Encryption Number,Public key1"))
    n = int(input("Enter n,Public/Private key2"))
    d = int(input("Enter d,Private key1"))
    D = (E ** d) % n
    print ('Decrypted Number:',D)
    alpha = input("Will You like to convert to Alphabets?,Y/N")
    alpha = alpha.upper()
    DE = []
    if (alpha == 'Y'):
        letter = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
        for number in str(D):
            number = int(number)
            if number in letter.keys():
                DE.append (letter[number])
def bruteforce(n,e):
        #Euler totient function
        #nt = (p -1)(q - 1) where p,q are co prime of n
        #primality testing and primality algorithm goes below
        #n = p.q
        primes = []
        for i in range(1,n+1): #for all factors of n
            if n % i == 0:
                if i % 3 != 0 or i == 3: #for prime function of 3
                   if i % 2 != 0 or i ==2: #for prime function of 2
                      primes.append(i)
        pq = []
        for j in primes: #pick two co primes p and q
            if n/j in primes and j != n and n/j != n:
                pq.append(j)
        p , q = pq[0], pq[1]
        nt = (p -1) * (q -1)
        #landaN = lcm(p-1,q-1)
        if((p - 1) > (q - 1)):
          lower = p-1
        else:
            lower = q-1
        while(1):
            if(lower % (p-1) == 0 and lower % (q-1) == 0):
              landaN = lower
              break
            lower = lower + 1
        d = (e**-1)%landaN
        print (pq)
        n = p*q
        t = (p-1)*(q-1)
        #print(math.(1,120)) cmath.

def AES(inputfile,outputfile,key):
    buffer = []
    pyAesCrypt.decryptFile(inputfile,outputfile,key,buffer)
bruteforce(3233,17)
