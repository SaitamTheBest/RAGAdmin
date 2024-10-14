from fonctionnement_ia.stocker_mot import stockage, affichage
import chromadb

if __name__ == "__main__":

    lettre = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']

    id_lettre = []
    mots = dict()

    for i in range(len(lettre)):
        id_lettre.append(i)
    continuer = 1
    print(id_lettre)
    while(continuer == 1):
        continuer = int(input("->"))
        mot = input("=>")

        valeur_mot = 0
        for i in mot:
            for j in lettre:
                if j == i and j != ' ':
                    valeur_mot += id_lettre[lettre.index(i)]
        print(valeur_mot)
        mots[valeur_mot] = mot


    stockage(mots)
    affichage()