#
#
#

import os
import glob

# Importazione moduli necessari:
from pathlib import*


#  Funzioni  del programma:

def GetPath():
    Ricerca = raw_input("Inserire una cartella da verificare: ")
    return Ricerca

def dirlist(path, c = 1):
        for i in glob.glob(os.path.join(path, "*")):
                if os.path.isfile(i):
                        filepath, filename = os.path.split(i)
                        print '----' *c + filename

                elif os.path.isdir(i):
                        dirname = os.path.basename(i)
                        print '----' *c + dirname
                        c+=1
                        dirlist(i,c)
                        c-=1



# Funzione main
def main():
   direct = GetPath()
   dirlist(direct)


#
# usage
if __name__ == '__main__':
    main()