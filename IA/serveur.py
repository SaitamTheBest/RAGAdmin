import  socket as socket
import threading
import  pypdf

from conversion import conversion_pdf_texte, conversion_pour_envoie_tcp
from recherche import listage, recherche, listage_pdf, recherche_pdf

ADRESSE =  ''
PORT = 7000
def serveur_client():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #fichier = listage()
    fichier_pdf = listage_pdf()



    serveur.bind((ADRESSE, PORT))
    serveur.listen(1)

    client, adresseClient = serveur.accept()


    reponse = ""

    while True:

        reponse = client.recv(1024).decode("utf-8")


        if reponse == "stop":
            break
        if reponse.find("recherche") != -1:
            mots = ""
            for i in range(len(reponse)):
                if i > reponse.find(':'):
                    mots+=reponse[i]

            reponse_fichier = recherche_pdf(mots, fichier_pdf)
            reponse_final = conversion_pdf_texte(reponse_fichier)
            client.send(conversion_pour_envoie_tcp(reponse_final))
        if reponse == "fichier":
            client.send()
    client.send(b'arret serveur')
    serveur.close()



if __name__ == "__main__":
    thread = threading.Thread(target=serveur_client)
    thread.start()
