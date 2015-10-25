from tkinter import *
from random import randint, shuffle

# Programme principal
fenetre = Tk()
fenetre.title("Nainpair")
fenetre.geometry('1200x800')
fenetre.configure(background="#a1dbcd")


# Menu
def new_frame():
    global frame_players, one_player, two_players, back_menu

    frame_players = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
    one_player = Button(frame_players, text='1 Nain', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=deux_joueurs)
    two_players = Button(frame_players, text='2 Nains', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=deux_joueurs)
    back_menu = Button(frame_players, text='Back to menu', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=fermer_play)

    frame_players.pack(padx=50, pady=50)
    frame_players.place(x=350, y=100)
    one_player.pack(padx=50, pady=10)
    two_players.pack(padx=25, pady=25)
    back_menu.pack(padx=25, pady=25)


def rules():
    global frame_rules, back_menu_rules, text_rules, content, regles

    regles = open('regles/regles.txt', "r")
    content = regles.read()
    regles.close()

    frame_rules = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
    frame_rules.pack()
    frame_rules.place(x=150, y=100)

    back_menu_rules = Button(frame_rules, text='Back to menu', font=("Arial", 23), fg="#a1dbcd", bg="#383a39", command=fermer_rules)
    back_menu_rules.pack(padx=25, pady=25, side=BOTTOM)

    text_rules = Label(frame_rules, text=content, font=("Arial", 20))
    text_rules.pack()


def fermer_play():
    frame_players.pack_forget()
    one_player.pack_forget()
    two_players.pack_forget()
    back_menu.pack_forget()
    frame_players.destroy()


def fermer_rules():
    frame_rules.pack_forget()
    back_menu_rules.pack_forget()
    text_rules.pack_forget()
    frame_rules.destroy()


def fermer_difficulte():
    frame_difficulty.pack_forget()
    facile.pack_forget()
    moyen.pack_forget()
    difficile.pack_forget()
    frame_difficulty.destroy()


def fermer_menu():
    frame_Menu.pack_forget()
    frame_Nain.pack_forget()
    play.pack_forget()
    rules.pack_forget()
    scores.pack_forget()
    quitter.pack_forget()
    frame_Menu.destroy()


def quitter():
    fenetre.destroy()


# Jeu

# Variables Globales
images = []  # contient les liens aux fichiers images
cartes = []  # contient le lien vers l'image des différentes cartes
cartes_jouees = []  # contient les cartes jouées
nb_lignes, nb_colonnes = 4, 4
choix_cartes = []
joueur_actuel = 0
score = [0, 0]
fini = False
peut_jouer = True


def deux_joueurs():
    global frame_difficulty, facile, moyen, difficile

    # Fermeture du menu d'avant
    fermer_play()
    # Ouverture du menu de difficulté
    frame_difficulty = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
    facile = Button(frame_difficulty, text='Facile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: difficulte(4))
    moyen = Button(frame_difficulty, text='Moyen', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: difficulte(6))
    difficile = Button(frame_difficulty, text='Difficile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: difficulte(8))

    frame_difficulty.pack(padx=50, pady=50)
    frame_difficulty.place(x=350, y=100)
    facile.pack(padx=50, pady=10)
    moyen.pack(padx=25, pady=25)
    difficile.pack(padx=25, pady=25)


def difficulte(nb_colonnes):
    fermer_menu()

    # Initilisation du jeu
    global points_joueur1, points_joueur2, canvas
    # Création du canvas dont la taille dépend du nombre de cartes
    canvas = creer_canevas(fenetre, nb_colonnes, nb_lignes)
    canvas.pack(side=TOP, padx=2, pady=2)
    points_joueur1 = Label(fenetre, text="Joueur 1 : 0", bg="orange", font="Helvetica 16")
    points_joueur1.pack(pady=2, side=LEFT)
    points_joueur2 = Label(fenetre, text="Joueur 2 : 0", font="Helvetica 16")
    points_joueur2.pack(pady=2, side=RIGHT)

    charger_images()
    melanger_cartes()

    for i in range(nb_colonnes):  # dessin des cartes retournées
        for j in range(nb_lignes):
            canvas.create_image((155 * i) + 60, (205 * j) + 60, image=images[0])

    canvas.bind("<Button-1>", cliquer_carte)  # permet le clic sur les cartes

    # Solutionne le problème d'affichage des scores
    reinit()
    if nb_colonnes == 4:
        jeu4x4()
    if nb_colonnes == 6:
        jeu4x6()
    if nb_colonnes == 8:
        jeu4x8()

    fermer_difficulte()


def charger_images():
    """
    Charge les images
    :return:
    """
    del images[:]  # vide la liste
    nb_images = 21  # l'image no 0 est le dos des cartes
    choix_cartes = [0]
    i = 0
    while i < nb_images - 1:  # tirage au sort des cartes à utiliser
        x = randint(1, nb_images - 1)
        if x not in choix_cartes:
            choix_cartes.append(x)
            i += 1
    for i in range(nb_images):  # importation des images
        nom = 'img\image' + str(choix_cartes[i]) + '.png'
        image = PhotoImage(file=nom)
        images.append(image)


def melanger_cartes():
    """
    Mélange les cartes
    :return:
    """
    global nb_colonnes, nb_lignes, cartes
    nb_cartes = nb_colonnes * nb_lignes
    cartes = list(range(1, nb_cartes // 2 + 1)) * 2
    shuffle(cartes)


def gerer_tirage():
    """
    Retourne les deux cartes à la fin de la sélection
    :return:
    """
    global nb_colonnes, nb_lignes, cartes_jouees
    global joueur_actuel, fini, peut_jouer
    if cartes[cartes_jouees[0] - 1] == cartes[cartes_jouees[1] - 1]:
        # enleve les cartes identiques. Le joueur actuel reste le même
        canvas.delete(cartes_jouees[0])
        canvas.delete(cartes_jouees[1])
        score[joueur_actuel] += 1
    else:
        # retourne les cartes différentes. Le joueur actuel change
        canvas.itemconfig(cartes_jouees[0], image=images[0])
        canvas.itemconfig(cartes_jouees[1], image=images[0])
        joueur_actuel = (joueur_actuel + 1) % 2  # la main passe à l'autre joueur
    cartes_jouees = []
    text1 = 'Joueur 1 : ' + str(score[0])
    text2 = 'Joueur 2 : ' + str(score[1])
    points_joueur1.config(text=text1)
    points_joueur2.config(text=text2)
    peut_jouer = True  # réactive l'effet du clic de la souris
    if joueur_actuel == 0:  # celui qui joue est en orange
        points_joueur1.config(bg='orange')
        points_joueur2.config(bg='white')
    else:
        points_joueur2.config(bg='orange')
        points_joueur1.config(bg='white')
    if score[0] + score[1] == (nb_colonnes * nb_lignes) // 2:
        fini = True  # afficher le résultat de la partie
        if score[0] > score[1]:
            texte = "Le joueur 1 a gagné !"
        elif score[0] < score[1]:
            texte = "Le joueur 2 a gagné !"
        else:
            texte = "Egalité !"
        canvas.create_rectangle(0, 0, (155 * nb_colonnes) + 20, (205 * nb_lignes) + 20, fill='white')
        canvas.create_text((55 * nb_colonnes) + 10, (55 * nb_lignes) + 10, text=texte, font='Calibri 24', fill='black')


def cliquer_carte(event):
    """
    Retourne la carte sélectionnée
    :param event:
    :return:
    """
    global fini, fenetre, cartes_jouees, peut_jouer
    if len(cartes_jouees) < 2:
        carte_selection = canvas.find_closest(event.x, event.y)
        carte_id = carte_selection[0]
        if fini:
            fini = False
            reinit()
        else:
            canvas.itemconfig(carte_id, image=images[cartes[carte_id - 1]])
            if len(cartes_jouees) == 0:
                cartes_jouees.append(carte_id)  # enregistre la carte jouée
            elif carte_id != cartes_jouees[0]:  # ne pas cliquer 2x sur la même carte
                cartes_jouees.append(carte_id)
    if peut_jouer and len(cartes_jouees) == 2:
        peut_jouer = False  # désactive l'effet du clic de la souris
        fenetre.after(1500, gerer_tirage)  # patiente 1,5 secondes


def jeu4x4():
    """
    Le jeu passe en 4x4
    :return:
    """
    global nb_colonnes
    nb_colonnes = 4
    reinit()


def jeu4x6():
    """
    Le jeu passe en 4x6
    :return:
    """
    global nb_colonnes
    nb_colonnes = 6
    reinit()


def jeu4x8():
    """
    Le jeu passe en 4x8
    :return:
    """
    global nb_colonnes
    nb_colonnes = 8
    reinit()


def creer_menus(fenetre):
    """
    Création des menus et sous-menus
    :param fenetre:
    :return:
    """
    top = Menu(fenetre)
    fenetre.config(menu=top)
    jeu = Menu(top, tearoff=False)
    top.add_cascade(label='Jeu', menu=jeu)
    jeu.add_command(label='Nouvelle partie', command=reinit)
    submenu = Menu(jeu, tearoff=False)
    jeu.add_cascade(label='Dimensions', menu=submenu)
    submenu.add_command(label='4 x 4', command=jeu4x4)
    submenu.add_command(label='4 x 6', command=jeu4x6)
    submenu.add_command(label='4 x 8', command=jeu4x8)
    jeu.add_command(label='Quitter', command=fenetre.destroy)


def creer_canevas(fen, col, lig):
    """
    Création du canvas
    :param fen:
    :param col:
    :param lig:
    :return:
    """
    return Canvas(fen, width=(155 * col) + 10, height=(205 * lig) + 10, bg='white')


def reinit():
    """
    Redémarre une partie et change éventuellement la difficulté
    :return:
    """
    global canvas, joueur_actuel, score, nb_lignes, nb_colonnes
    joueur_actuel = 0
    score = [0, 0]
    del cartes[:]
    del cartes_jouees[:]
    canvas.destroy()
    canvas = creer_canevas(fenetre, nb_colonnes, nb_lignes)
    canvas.pack(side=TOP, padx=5, pady=5)
    canvas.bind("<Button-1>", cliquer_carte)  # permet le clic sur les cartes
    melanger_cartes()
    for i in range(nb_colonnes):  # dessin des cartes retournées
        for j in range(nb_lignes):
            canvas.create_image((155 * i) + 60, (205 * j) + 60, image=images[0])
    text1 = 'Joueur 1 : ' + str(score[0] * 2)
    text2 = 'Joueur 2 : ' + str(score[1] * 2)
    points_joueur1.config(text=text1, bg='orange')
    points_joueur2.config(text=text2, bg='white')


# Frame Menu Buttons
frame_Menu = Frame(fenetre, borderwidth=2, relief=GROOVE, width=50, height=500)
frame_Menu.pack()

frame_Nain = Frame(fenetre, width=100, height=300)
frame_Nain.pack(side=LEFT, padx=100, pady=100)

# Menu's Buttons
play = Button(frame_Menu, text='Play', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=new_frame)
play.pack(padx=50, pady=10, )

rules = Button(frame_Menu, text='Rules', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=rules)
rules.pack(padx=25, pady=25)

scores = Button(frame_Menu, text='Scores', font=("Arial", 50), fg="#a1dbcd", bg="#383a39")
scores.pack(padx=25, pady=25, )

quitter = Button(frame_Menu, text='Quit', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=quitter)
quitter.pack(padx=25, pady=25, )

creer_menus(fenetre)

fenetre.mainloop()
