import pickle

from recherche import lecture


def conversion_pdf_texte(pdf):
    document_final =[]
    for i in range(len(pdf.pages)):
        document_final.append(pdf.pages[i].extract_text())
    return document_final

def conversion_pour_envoie_tcp(pdf_a_convertir):
    data = pickle.dumps(pdf_a_convertir)
    return data

def conversion_texte_phrase(liste_pdf):

    for i in range(len(liste_pdf.pages)):
        for j in liste_pdf.pages[i].extract_text():
            print(j)

def creation_id(chaine):
    lettre = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
    valeur_mot = 0
    id_lettre = []
    mots = dict()

    for i in range(len(lettre)):
        id_lettre.append(i)
    for i in chaine:
        for j in lettre:
            if j == i and j != ' ':
                valeur_mot += id_lettre[lettre.index(i)]
    return str(valeur_mot)