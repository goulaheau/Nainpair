# Role : Réaliser un jeu de mémory

# Auteur : Loic et Hugo

# ------------------------------ Déclaration ---------------------------
from random import *
from tkinter import *


def initialisation():
    global image, position, liste, bis, choix, i, j, a, clic, fin, \
        listbt
    liste = [] * 10  # Définition de la liste vide
    position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Définir aléatoirement la position des cartes dans la liste
    bis = []  # Liste empêchant de trouver 2 fois la même paire
    choix = []
    i = 0
    j = 0
    a = 0
    clic = 0
    fin = 0
    listbt = []  # Liste permettant de créer les 10 boutons
    image = []  # Liste permettant d'avoir les 5 photos de cartes


def crea_liste():  # Permet de créer une fonction "Création d'une liste"

    for i in range(5):  # Boucle permettant de créer la liste aléatoirement
        x = choice(position)
        position.remove(x)
        y = choice(position)
        position.remove(y)
        liste.insert(x, image[i])
        liste.insert(y, image[i])


def jeu(num):  # Permet d'exécuter le jeu Memory

    global a, j, clic, choix, fin, choix1, choix2

    if fin == 0:

        choix.append(num)
        print(choix)
        a += 1  # Incrémente une valeur pour tester seulement 2 cartes
        clic += 1  # Incrémente une valeur pour compter le nombre de clics totaux
        Nbclic.configure(text="Nombre de clics : " + str(clic), \
                         font=("verdana", 10, "bold"))
        listbt[num].configure(image=liste[num])

        if len(choix) == 2:  # Teste si la longueur de la liste est égale à 2

            while j < 5 and a == 2:  # Boucle permettant de jouer jusqu'à la victoire
                choix1 = choix[0]  # Choix des positions des cartes à retourner
                choix2 = choix[1]
                T10 = choix1 in bis
                T11 = choix2 in bis
                t1 = liste[choix1]  # Récupère la lettre associé à choix1
                t2 = liste[choix2]  # Récupère la lettre associée à choix 2

                if t1 == t2 and choix1 != choix2 and T10 == False \
                        and T11 == False:  # Teste si les deux lettres sont les mêmes

                    print("Bravo, vous avez trouvé une paire")
                    j = j + 1  # Incrémente la valeur de j qui augmente lorsqu'on trouve une paire
                    bis.append(choix1)  # Remplit la liste avec les cartes déjà trouvées
                    bis.append(choix2)
                    choix.pop(1)  # Supprime la première carte sélectionnée de la liste
                    choix.pop(0)  # Supprime la seconde carte sélectionnée de la liste
                    Score.config(text="Nombre de paires : " + str(j), \
                                 font=("verdana", 9, "bold"))
                    listbt[choix1].configure(state="disabled")  # Désactive la première carte de la paire de la paire trouvée
                    listbt[choix2].configure(state="disabled")  # Désactive la seconde carte de la paire trouvée

                    if j == 5:  # Teste si les cinq paires ont été trouvées

                        fin = 1
                        Win = Label(text="Bravo, vous avez " \
                                         "gagné !", font=("verdana", 9, "bold"))
                        Win.grid(row=3, column=6, padx=0, pady=10)
                        print("Bravo, vous avez gagné !")

                else:

                    listbt[choix1].configure(image=photo)
                    listbt[choix2].configure(image=photo)
                    choix.pop(1)
                    choix.pop(0)
                    print("Réessayez!")

                a = 0


def again():
    global image, position, liste, bis, choix, i, j, a, clic, fin, \
        listbt
    liste = [] * 10  # Définition de la liste vide
    position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Définir aléatoirement la position des cartes dans la liste                                                            # Liste empêchant de trouver 2 fois la même paire
    choix = []
    i = 0
    j = 0
    a = 0
    clic = 0
    fin = 0
    image = []
    listbt = []
    num = 0

    Score.config(text="Nombre de paires : 0", font=("verdana", 9, "bold"))
    Nbclic.configure(text="Nombre de clics : 0", \
                     font=("verdana", 10, "bold"))
    for i in range(5):
        image.append(PhotoImage(file="carte" + str(i) + ".gif"))
    for ligne in range(2):
        for nbc in range(5):
            num = 5 * ligne + nbc
            listbt.append(Button(fen, image=photo, width=100, height=144, \
                                 command=lambda arg=num: jeu(arg)))
            listbt[num].grid(row=ligne, column=nbc)

    crea_liste


# -------------------------------- Main --------------------------------

fen = Tk()  # Création de la fenêtre principale
fen.title("Bienvenue dans le jeu Mémory !")
fen.geometry("710x350")
fen.resizable(width=False, height=False)

initialisation()

photo = PhotoImage(file="carte5.gif")  # Permet d'afficher le dos de la carte

for i in range(5):
    image.append(PhotoImage(file="carte" + str(i) + ".gif"))  # Remplit la liste image

crea_liste()

for ligne in range(2):
    for nbc in range(5):
        num = 5 * ligne + nbc
        listbt.append(Button(fen, image=photo, width=100, height=144, \
                             command=lambda arg=num: jeu(arg)))
        listbt[num].grid(row=ligne, column=nbc)

BtQuit = Button(fen, text="Quitter", width=12, height=2, \
                font=("verdana", 8, "bold"), command=fen.destroy)
BtQuit.grid(row=1, column=6, padx=20)

Score = Label(text="Nombre de paires : 0", font=("verdana", 9, "bold"))
Score.grid(row=0, column=6, padx=15)

Nbclic = Label(text="Nombre de clic : 0", font=("verdana", 10, "bold"))
Nbclic.place(x=10, y=310)

BtAgain = Button(fen, text="Rejouer", width=12, height=2, \
                 font=("verdana", 8, "bold"), command=again)
BtAgain.place(x=565, y=150)

fen.mainloop()
