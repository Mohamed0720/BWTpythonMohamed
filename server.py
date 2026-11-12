import socket
import main

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind(("127.0.0.1", 5000))

    server.listen()

    print("Socket di ascolto: ", server.getsockname())

    conn, addr = server.accept()

    with conn:
        print("Client connesso: ", addr)
        print("Socket di connessione: ", conn.getsockname())

        parola = conn.recv(1024).decode()
        print("Messaggio ricevuto: ", parola)

        parolaConvertita = main.bwt(parola)

        conn.sendall(parolaConvertita.encode())




        