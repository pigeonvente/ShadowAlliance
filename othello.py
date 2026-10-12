#Tout d'abord, on importe le module tkinter et on crée la fenêtre de jeu
import tkinter as t
fenetre=t.Tk()
fenetre.title("Othello")
fenetre.geometry("1000x500")
# C'est mieux de mettre True pour que le prof puisse mettre en plein écran.
fenetre.resizable(width=True,height=True)
letter=["A","B","C","D","E","F","G","H"] #liste de lettres à afficher
#pas de liste de nombre, vu qu'ils sont générés avec la boucle for

"""
    Petit schéma pour mieux comprendre la suite :

    On découpe le plateau de jeu en 13x9 cases :
    Les 9x9 à gauche sont les cases du plateau de jeu,
    Les 4x9 à droite sont les cases pour les statistiques. On a donc :
    O A B C D E F G H [Statistiques]
    1 X X X X X X X X [Statistiques]
    2 X X X X X X X X [Statistiques]
    3 X X X X X X X X [Statistiques]
    4 X X X X X X X X [Statistiques]
    5 X X X X X X X X [Statistiques]
    6 X X X X X X X X [Statistiques]
    7 X X X X X X X X [Statistiques]
    8 X X X X X X X X [Statistiques]
    
    Pour chaque case, on crée un Canva carrés de même taille, et qui s'adaptent à la taille de la fenêtre.
    Les canvas sont crées ci dessous...

"""

cletter=[] #liste vide pour stocker les Canvas des lettres (en haut du plateau)
cnumbers=[] #liste vide pour stocker les Canvas des chiffres (à gauche du plateau)

clet_content=[] #liste vide pour stocker le CONTENU (le texte en gros) des canvas des lettres
cnum_content=[] #liste vide pour stocker le CONTENU des canvas des chiffres


wood=t.Canvas(fenetre,width=1,height=1,bg="green")
wood.grid(row=0,column=0,rowspan=9,columnspan=9,sticky="nw")

#Création des Canvas :
for i in range(8):
    clet_content.append(wood.create_text(1,1, text=letter[i], font=("Arial")))
for i in range(8):
    cnum_content.append(wood.create_text(1,1, text=str(i+1), font=("Arial")))

#Un test qui m'a servi au début, mais qui pourra servir plus tard pour le jeu
def printd():
    global c
    largeur = fenetre.winfo_width()
    hauteur = fenetre.winfo_height()
    print("Largeur de la fenêtre :", largeur)
    print("Hauteur de la fenêtre :", hauteur)
    c=round(min(largeur/14,hauteur/10))
    print(c)
    print(5*c)
    fenetre.after(2000, printd)
    
"""
Avec Tkinter, on peut pas faire une boucle parce que le fenetre.mainLoop bouffe tout du coup
obligé de créer un .after, qui lance une fonction au bout de 10 millièmes.
Comme tu le vois plus haut, cette fonction se relance toute seule au bout de 2 secondes (on mettra quelques centièmes plus tard)
"""
fenetre.after(10,printd())

def resizeall(event):
    #On récupère la taille de la fenetre :
    largeur = fenetre.winfo_width()
    hauteur = fenetre.winfo_height()
    # J'ai pris 14 et 10 au lieu de 13 et 9 pour avoir de la marge, sinon l'arrondi est un peu risqué...
    c=round(min(largeur/14,hauteur/10))
    # c08, c'est la variable pour la taille de la police. 
    # Je met 0.8 pour que ça passe bien dans le Canva.
    c08=round(0.7*c)
    wood.config(width=9*c,height=9*c)
    for i in range(8):
        wood.itemconfig(clet_content[i], font=("Arial", c08))
        wood.itemconfig(cnum_content[i], font=("Arial", c08))
        wood.coords(clet_content[i], (i+1)*c + c/2, c/2)
        wood.coords(cnum_content[i], c/2, (i+1)*c + c/2)

""" Création d'une bind : en gros, à chaque fois qu'on redimensionne la fenêtre
    (= "<Configure>"), python lance la fonction "resizeall" pour réajuster toutes
    les diensions.
"""
fenetre.bind("<Configure>", resizeall)
fenetre.mainloop()

