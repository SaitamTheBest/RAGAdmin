import socket

ADRESSE = '127.0.0.1'
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADRESSE, PORT))
print("Connecté au serveur.")



message = ""
while message != "quit":
    # Demander l'entrée à l'utilisateur
    message = input("=> ")
    if message == "recherche":
        envoie = input("recherche=>")
        message_recherche= "recherche:"+envoie
        client.send(message_recherche.encode('utf-8'))
    else:
        client.send(message.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))



# Une fois que vous quittez, fermez la connexion
client.close()
