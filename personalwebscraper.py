from bs4 import BeautifulSoup
import requests
import urllib.request
import time


# Definizione funzione di verifica del link web inserito:

def Verifica_URL(lin):
 if 'http://' in lin:
  link= requests.get(lin)
  return(link)
 else:
  return(False)

# Richiesta indirizzo da verificare:
linkerror=False
while(linkerror==False):
 lnkweb=input("Inserire un indirizzo web da filtrare:  ")
 if(Verifica_URL(lnkweb)!=False):
   linkerror=True
   continue
page = urllib.request.urlopen(lnkweb).read()
soup = BeautifulSoup (page,'html.parser')
#print (soup.get_text())
elenco=soup.findAll('form')
#elenco=soup
if elenco:
  inputs = soup.findAll('input')
  for input in inputs:
   if input.findParent('input'):
     print('Campi trovati: ')
     print('Nome campo:   '+str(input.get('name')))
     print('Tipo campo:   '+str(input.get('type')))
     print('Valore campo: '+str(input.get('value')))
 #print("Form trovato")
 #while(elenco.findAll('input')==True)
 # for a in elenco:
  # if(a.findAll('input')):
   # search=(a.find('input'))
   # print('Campi trovati: ')
   # print('Nome campo:   '+search.get('name'))
   # print('Tipo campo:   '+search.get('type'))
   # print('Valore campo: '+search.get('value'))
   # search.findnext()
   #else:
   # continue
else:
 print("Non ci sono form in questa pagina")
