f = open('/home/nicola/ words.txt ', 'r')

data = f.read()

lines = data.splitlines()

#random.choice(lista)

intero = input('Inserire un numero da 1-8:')

interoN = int(intero)

if interoN > 0 and interoN < 8:

	while True:

		parola =lines[interoN]

		parolaLista = list(parola) 

		lettera =input("Inserire una lettera:") 

		#listaLettera = list(lettera)

		i =listaLettera.count(listaLettera)

#		generatore = [* for i in range(len(parolaLista))]

		lista=[]

		for i in range(len(parolaLista)):

			lista.append('*')

		print('Lista *',lista)

		#print('Generatore', generatore)

		for l in range(len(parolaLista)):

			if lettera in parolaLista:



				#print('Parola', parolaLista)

				lista[l]= lettera

				print('',lista)

#			break

			else:

				pass

				#print('Lettera non presente')

#			break

else:

	print('Errore numero non compreso tra 0 e 8')