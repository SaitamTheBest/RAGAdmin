import  os as os

from pypdf import PdfReader


def listage():
    fichier_l = os.listdir("fichier")
    dossier = []
    fichier_txt = []
    temporaire = ""
    dictionnaire = dict()
    for i in fichier_l:
        if not os.path.isfile(i):
            fichier_txt.append(i)
    for i in fichier_txt:
        for j in i:
            if j != '.':
                temporaire = temporaire + j
            else:
                fichier_l.append(temporaire)
                dictionnaire[temporaire] = i
                temporaire = ""
        fichier_l.append(temporaire)
        temporaire = ""


    return dictionnaire


def listage_pdf():
    dictionnaire = dict()
    temporaire = ""
    fichier_l = os.listdir('fichier')
    fichier_pdf = []


    for i in fichier_l:
        if i.find(".pdf") != -1:
            fichier_pdf.append(i)
    for i in fichier_pdf:
        for j in i:
            if j != '.':
                temporaire += j
            else:
                dictionnaire[temporaire] = i
                temporaire = ""

    return  dictionnaire



def recherche(fichier,liste_fichier):
    for i in liste_fichier:
        if i == fichier:
            return open("fichier/"+liste_fichier[i],"r").read()

def recherche_pdf(fichier, liste_fichier):
    pdf =[]
    for i in liste_fichier:
        if i == fichier:
          pdf = PdfReader('fichier/'+liste_fichier[i])
    return  pdf


def lecture(fichier_list, recherche):
    temporaire = ""
    fichier_interessant = []
    fichier_lue = []
    for i in fichier_list:
        fichier_a_lire = open("fichier/"+fichier_list[i],'r')
        fichier_lue.append(fichier_a_lire.read());
        for j in fichier_lue:
            if j != " " or j!=".":
                temporaire += j;
            else:
                print(temporaire)
                if temporaire == recherche:

                    fichier_interessant.append(temporaire)
                    fichier_a_lire.close()
                    temporaire = ""

                else:


                    fichier_a_lire.close()
                    temporaire = ""
    print(fichier_interessant)
