import socket

ADRESSE = ''
PORT = 7000

if __name__ == "__main__":
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((ADRESSE, PORT))
    serveur.listen(1)
    print(f"Serveur en écoute sur le port {PORT}")

    client, adresse_client = serveur.accept()
    print(f"Connexion acceptée de {adresse_client}")

    client.send(b'Serveur pret')

    while True:
        reponse = client.recv(1024).decode("utf-8").strip()
        print(f"Reçu: {reponse}")

        if reponse.lower() == "stop":
            client.send(b"arret serveur")
            print("Arrêt du serveur demandé par le client.")
            break
        else:
            client.send(b"Recu")

    client.close()
    serveur.close()
    print("Le serveur est arrêté.")
