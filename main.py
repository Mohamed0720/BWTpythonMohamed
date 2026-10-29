parola = input("Inserisci una parola: ")


listaParola = []

for i in range(len(parola)+1):
    temp = parola[i:] + "$" + parola[:i]
    listaParola.append(temp)

print(listaParola)