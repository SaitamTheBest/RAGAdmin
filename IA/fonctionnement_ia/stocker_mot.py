import os.path
import pickle



def stockage(mots):

    if not os.path.exists('data.pkl'):
        with open("data.pkl", 'wb') as f:
            pickle.dump(mots, f)
    else:
        with open("data.pkl", 'ab') as f:
            pickle.dump(mots,f)

def affichage():
    with open("data.pkl", "rb") as f:
        obj = pickle.load(f)
        obj_l = pickle.load(f)
        print(obj)