from conversion import conversion_texte_phrase
from recherche import listage, recherche, lecture, listage_pdf, recherche_pdf

if __name__ == "__main__":
    entre = ""
    fichier_r = ""
    dossier = []
    fichier = []
    print("______________________________")
    print("recherche de fichier")
    print("______________________________")
    fichier = listage_pdf()
    conversion_texte_phrase(fichier)