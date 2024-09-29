import random
from tkinter import *
import tkinter as tk
import webbrowser


# 1 : Création de la fenêtre Tkinter
color="#8F8F8F"
fenetre = Tk()
fenetre.title("Générateur - Mot de passe")
fenetre.config(background=color)
fenetre.minsize(500, 300)

def callback(url):
    webbrowser.open_new(url)

# 2 : Titre
titre = Label(fenetre, text="Combien de caractères voulez-vous dans votre mot de passe ?",font=("Arial",12,"bold"),background=color)
titre.pack(pady=20)

# 3 : Champ pour entrer la longueur du mot de passe
expression = StringVar()
entree = Entry(fenetre, textvariable=expression, width=30)
entree.pack(pady=10)

# 4 : Le label pour afficher le mot de passe généré
resultat = StringVar()
sortie = Entry(fenetre, textvariable=resultat, width=40)
sortie.pack()

# 5 : Fonction pour générer le mot de passe utilisant la première version du générateur
def generer_mot_de_passe():
    try:
        longueur = int(expression.get())
        
        lettres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nombres = '0123456789'
        symboles = '!#$%&()*+'
        
        ensemble_des_caracteres = lettres + nombres + symboles
        
        mot_de_passe = [
            random.choice(lettres),
            random.choice(nombres),
            random.choice(symboles)
        ]

        for _ in range(longueur - 3):
            mot_de_passe.append(random.choice(ensemble_des_caracteres))

        random.shuffle(mot_de_passe)

        mot_de_passe_final = ''.join(mot_de_passe)
        resultat.set(mot_de_passe_final)
    except ValueError:
        resultat.set("Veuillez entrer un nombre valide.")

bouton = Button(fenetre, text="Générer", command=generer_mot_de_passe, cursor="hand2")
bouton.pack(pady=10)


link1 = Label(fenetre, text="Github", fg="blue", cursor="hand2", background=color)
link1.pack(pady=100)
link1.bind("<Button-1>", lambda e: callback("https://github.com/Rroq1"))

fenetre.mainloop()
