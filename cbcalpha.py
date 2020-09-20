#
#


#
#
import Crypto
import time
import string
import random

#
from Crypto import *

#Esempio di utilizzo classe CBCAlpha:
   #>> alpha    = ['A', 'B', 'C', 'D', ...]
   #>> rp_alpha = ['U', 'T', 'S', 'M', ...]
   #>> cipher = list(zip(alpha, rp_alpha))
   #>> encryptor = CBCAlpha(cipher)
   #>> plaintext = 'HELLOWORLD'
   #>> iv = 'L'
   #>> ciphertext = encryptor.encrypt(iv, plaintext)
   #>> print(ciphertext)
   #'WSVYZQRVYK'
   #>> print(encryptor.decrypt(iv, ciphertext))
   #'HELLOWORLD'
#

class CBCAlpha:
    alphabet = list()
    rp_alpha = list()
    cipher = list()
    iv = " "
    def InitParameters(self):
        # Inizializza iv:
        self.iv = random.choice(string.ascii_uppercase)
        # Inizializza l'alfabeto:
        self.alphabet = list(string.ascii_uppercase)
        # Inizializza rp_alpha con shuffle:
        self.rp_alpha = list(string.ascii_uppercase)
        random.shuffle(self.rp_alpha)
        # Inizializza cipher:
        self.cipher = list(zip(self.alphabet,self.rp_alpha))
    def PrintParameters(self):
        print("Inizialization vector: "+str(self.iv))
        print("Alphabet: "+str(self.alphabet))
        print("Rp_aplha: "+str(self.rp_alpha))
        print("Cipher:   "+str(self.cipher))
    def Encrypt(IV,plaintxt):
        for c in plaintxt:
           if c in self.cipher:
             cipher += self.alphabet[(self.alphabet.index(c)+k)%(len(IV))]
    return cipher





#
def main():
   test = CBCAlpha();
   test.InitParameters()
   test.PrintParameters()

#
if __name__ == "__main__":
    main()






