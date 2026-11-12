import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect(("127.0.0.1", 5000))

    parola = input("Inserisci una parola: ")
    client.sendall(parola.encode())

    risposta = client.recv(1024)
    print("Algoritmo BWT applicato: ", risposta.decode())