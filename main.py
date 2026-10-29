parola = input("Inserisci una parola: ")


listaParola = []

for i in range(len(parola)+1):
    temp = parola[i:] + "$" + parola[:i]
    listaParola.append(temp)

listaParola.sort()

print(listaParola)

parolaFinale = ""

for i in listaParola:
    parolaFinale = parolaFinale+i[-1]

print("Parola Algoritmo BWT: " + parolaFinale)