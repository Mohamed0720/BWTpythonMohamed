
def ordina(lista):
    scambiato = True

    while scambiato:
        scambiato = False
        for i in range(len(lista)-1):

            if lista[i]>lista[i+1]:
                p = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = p
                scambiato = True

parola = input("Inserisci una parola: ")


listaParola = []

for i in range(len(parola)+1):
    temp = parola[i:] + "$" + parola[:i]
    listaParola.append(temp)


ordina(listaParola)    

print(listaParola)

parolaFinale = ""

for i in listaParola:
    parolaFinale = parolaFinale+i[-1]

print("Parola Algoritmo BWT: " + parolaFinale)