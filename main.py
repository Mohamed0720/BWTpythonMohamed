parola = input("Inserisci una parola: ")


listaParola = []

for i in range(len(parola)+1):
    temp = parola[i:] + "$" + parola[:i]
    listaParola.append(temp)

scambiato = True

while scambiato:
    scambiato = False
    for i in range(len(listaParola)-1):

        if listaParola[i]>listaParola[i+1]:
            p = listaParola[i]
            listaParola[i] = listaParola[i+1]
            listaParola[i+1] = p
            scambiato = True
        

print(listaParola)

parolaFinale = ""

for i in listaParola:
    parolaFinale = parolaFinale+i[-1]

print("Parola Algoritmo BWT: " + parolaFinale)