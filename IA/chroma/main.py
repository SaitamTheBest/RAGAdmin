
import chromadb

from conversion import conversion_pdf_texte, creation_id
from fonctionnement_ia.recherche import listage_pdf, recherche_pdf

if __name__ == "__main__":
    pdf = listage_pdf()
    pdf_a_lire = recherche_pdf("luxembourg",pdf)
    texte_pdf = conversion_pdf_texte(pdf_a_lire)
    print(texte_pdf)
    client = chromadb.Client()
    collection = client.create_collection(name="termes")
    for i in texte_pdf:
        collection.add(
            documents=[i],
            ids= creation_id(i)
        )
    print(collection)