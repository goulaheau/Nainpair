from tkinter import *
from random import randint, shuffle


class Fenetre(Tk):
    def __init__(self):
        """
        Création de la fenêtre de l'Application
        :return:
        """
        Tk.__init__(self)
        self.title("Nainpair")
        self.geometry('1200x800')
        self.configure(background="#a1dbcd")

        top = Menu(self)
        self.config(menu=top)
        jeu = Menu(top, tearoff=False)
        top.add_cascade(label='Jeu', menu=jeu)
        jeu.add_command(label='Nouvelle partie', command=Jeu.reinit)
        submenu = Menu(jeu, tearoff=False)
        jeu.add_cascade(label='Dimensions', menu=submenu)
        submenu.add_command(label='4 x 4', command=Jeu.jeu4x4)
        submenu.add_command(label='4 x 6', command=Jeu.jeu4x6)
        submenu.add_command(label='4 x 8', command=Jeu.jeu4x8)
        jeu.add_command(label='Quitter', command=self.destroy)


class MenuJeu:
    def __init__(self):
        self.creer_menu()

    @staticmethod
    def creer_menu():
        """
        Création du MenuJeu
        :return:
        """
        global fenetre_menu, bouton_jouer, bouton_regles, bouton_score, bouton_quitter
        fenetre_menu = Frame(fenetre, borderwidth=2, relief=GROOVE, width=50, height=500)
        fenetre_menu.pack()

        bouton_jouer = Button(fenetre_menu, text='Jouer', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=MenuJeu.creer_menu_joueur)
        bouton_jouer.pack(padx=50, pady=10)

        bouton_regles = Button(fenetre_menu, text='Règles', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=MenuJeu.creer_menu_regles)
        bouton_regles.pack(padx=25, pady=25)

        bouton_score = Button(fenetre_menu, text='Scores', font=("Arial", 50), fg="#a1dbcd", bg="#383a39")
        bouton_score.pack(padx=25, pady=25)

        bouton_quitter = Button(fenetre_menu, text='Quitter', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Fenetre.destroy(fenetre))
        bouton_quitter.pack(padx=25, pady=25)

    @staticmethod
    def creer_menu_joueur():
        """
        Création du menu qui demande à combien de joueurs on va jouer
        :return:
        """
        global fenetre_menu_joueur, bouton_un_nain, bouton_deux_nains, bouton_fermer_menu_joueur

        MenuJeu.fermer_menu()

        fenetre_menu_joueur = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_menu_joueur.pack(padx=50, pady=50)
        fenetre_menu_joueur.place(x=350, y=100)

        bouton_un_nain = Button(fenetre_menu_joueur, text='1 Nain', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: MenuJeu.creer_menu_difficulte(1))
        bouton_un_nain.pack(padx=50, pady=10)

        bouton_deux_nains = Button(fenetre_menu_joueur, text='2 Nains', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: MenuJeu.creer_menu_difficulte(2))
        bouton_deux_nains.pack(padx=25, pady=25)

        bouton_fermer_menu_joueur = Button(fenetre_menu_joueur, text='Retour', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=MenuJeu.fermer_menu_joueur)
        bouton_fermer_menu_joueur.pack(padx=25, pady=25)

    @staticmethod
    def creer_menu_regles():
        """
        Affiche le menu contenant les règles
        :return:
        """
        global fenetre_menu_regles, bouton_fermer_menu_regles, text_regles, contenu, fichier_regles

        MenuJeu.fermer_menu()

        fichier_regles = open('regles/regles.txt', "r")
        contenu = fichier_regles.read()
        fichier_regles.close()

        fenetre_menu_regles = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_menu_regles.pack()
        fenetre_menu_regles.place(x=150, y=100)

        bouton_fermer_menu_regles = Button(fenetre_menu_regles, text='Retour', font=("Arial", 23), fg="#a1dbcd", bg="#383a39", command=MenuJeu.fermer_menu_regles)
        bouton_fermer_menu_regles.pack(padx=25, pady=25, side=BOTTOM)

        text_regles = Label(fenetre_menu_regles, text=contenu, font=("Arial", 20))
        text_regles.pack()

    @staticmethod
    def creer_menu_difficulte(nombre_joueurs):
        """
        Crée le menu demandant la difficulte en prenant en compte le nombre de joueurs
        :param nombre_joueurs: int
        :return:
        """
        global fenetre_difficulte, bouton_facile, bouton_moyen, bouton_difficile

        MenuJeu.fermer_menu_joueur()
        MenuJeu.fermer_menu()

        fenetre_difficulte = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_difficulte.pack(padx=50, pady=50)
        fenetre_difficulte.place(x=350, y=100)

        if nombre_joueurs == 1:
            bouton_facile = Button(fenetre_difficulte, text='Facile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 4))
            bouton_moyen = Button(fenetre_difficulte, text='Moyen', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 6))
            bouton_difficile = Button(fenetre_difficulte, text='Difficile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 8))
        else:
            bouton_facile = Button(fenetre_difficulte, text='Facile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 4))
            bouton_moyen = Button(fenetre_difficulte, text='Moyen', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 6))
            bouton_difficile = Button(fenetre_difficulte, text='Difficile', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 8))

        bouton_facile.pack(padx=50, pady=10)
        bouton_moyen.pack(padx=25, pady=25)
        bouton_difficile.pack(padx=25, pady=25)

        fermer_menu_difficulte = Button(fenetre_difficulte, text='Retour', font=("Arial", 50), fg="#a1dbcd", bg="#383a39", command=MenuJeu.fermer_menu_difficulte)
        fermer_menu_difficulte.pack(padx=25, pady=25)

    @staticmethod
    def fermer_menu():
        """
        Ferme le MenuJeu
        :return:
        """
        fenetre_menu.pack_forget()
        bouton_jouer.pack_forget()
        bouton_regles.pack_forget()
        bouton_score.pack_forget()
        bouton_quitter.pack_forget()

        fenetre_menu.destroy()

    @staticmethod
    def fermer_menu_joueur():
        """
        Ferme le menu qui demande à combien de joueurs on va jouer
        :return:
        """
        fenetre_menu_joueur.pack_forget()
        bouton_un_nain.pack_forget()
        bouton_deux_nains.pack_forget()
        bouton_fermer_menu_joueur.pack_forget()

        fenetre_menu_joueur.destroy()

        MenuJeu.creer_menu()

    @staticmethod
    def fermer_menu_regles():
        """
        Ferme le menu menu contenant les règles
        :return:
        """
        fenetre_menu_regles.pack_forget()
        bouton_fermer_menu_regles.pack_forget()
        text_regles.pack_forget()

        fenetre_menu_regles.destroy()

        MenuJeu.creer_menu()

    @staticmethod
    def fermer_menu_difficulte():
        """
        Ferme le menu demandant la difficulte en prenant en compte le nombre de joueurs
        :return:
        """
        fenetre_difficulte.pack_forget()
        bouton_facile.pack_forget()
        bouton_moyen.pack_forget()
        bouton_difficile.pack_forget()

        fenetre_difficulte.destroy()

        MenuJeu.creer_menu_joueur()


class Jeu:
    global images, cartes, cartes_jouees, nb_lignes, nb_colonnes, choix_cartes, joueur_actuel, score, fini, peut_jouer
    images = []
    cartes = []
    cartes_jouees = []
    nb_lignes = 4
    nb_colonnes = 4
    choix_cartes = []
    joueur_actuel = 0
    score = [0, 0]
    fini = False
    peut_jouer = True

    @staticmethod
    def creer_jeu(nb_joueurs, difficulte):
        """
        Affiche le menu permettant de choisir la difficulté pour 2 joueurs
        :param difficulte: int
        :param nb_joueurs: int
        :return:
        """
        MenuJeu.fermer_menu_difficulte()
        MenuJeu.fermer_menu_joueur()
        MenuJeu.fermer_menu()

        # Initilisation du jeu
        global points_joueur1, points_joueur2, canvas, nb_colonnes
        # Création du canvas dont la taille dépend du nombre de cartes
        canvas = Jeu.creer_canvas(fenetre, nb_colonnes, nb_lignes)
        canvas.pack(side=TOP, padx=2, pady=2)

        points_joueur1 = Label(fenetre, text="Joueur 1 : 0", bg="orange", font="Helvetica 16")
        points_joueur2 = Label(fenetre, text="Joueur 2 : 0", font="Helvetica 16")

        if nb_joueurs == 2:
            points_joueur1.pack(pady=2, side=LEFT)
            points_joueur2.pack(pady=2, side=RIGHT)

        Jeu.charger_images()

        # Solutionne le problème d'affichage des scores
        nb_colonnes = difficulte
        Jeu.reinit()

    @staticmethod
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

    @staticmethod
    def melanger_cartes():
        """
        Mélange les cartes
        :return:
        """
        global nb_colonnes, nb_lignes, cartes
        nb_cartes = nb_colonnes * nb_lignes
        cartes = list(range(1, nb_cartes // 2 + 1)) * 2
        shuffle(cartes)

    @staticmethod
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

    @staticmethod
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
                Jeu.reinit()
            else:
                canvas.itemconfig(carte_id, image=images[cartes[carte_id - 1]])
                if len(cartes_jouees) == 0:
                    cartes_jouees.append(carte_id)  # enregistre la carte jouée
                elif carte_id != cartes_jouees[0]:  # ne pas cliquer 2x sur la même carte
                    cartes_jouees.append(carte_id)
        if peut_jouer and len(cartes_jouees) == 2:
            peut_jouer = False  # désactive l'effet du clic de la souris
            fenetre.after(1500, Jeu.gerer_tirage)  # patiente 1,5 secondes

    @staticmethod
    def jeu4x4():
        """
        Le jeu passe en 4x4
        :return:
        """
        global nb_colonnes
        nb_colonnes = 4
        Jeu.reinit()

    @staticmethod
    def jeu4x6():
        """
        Le jeu passe en 4x6
        :return:
        """
        global nb_colonnes
        nb_colonnes = 6
        Jeu.reinit()

    @staticmethod
    def jeu4x8():
        """
        Le jeu passe en 4x8
        :return:
        """
        global nb_colonnes
        nb_colonnes = 8
        Jeu.reinit()

    @staticmethod
    def creer_canvas(fen, col, lig):
        """
        Création du canvas
        :param fen:
        :param col:
        :param lig:
        :return:
        """
        return Canvas(fen, width=(155 * col) + 10, height=(205 * lig) + 10, bg='white')

    @staticmethod
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
        canvas = Jeu.creer_canvas(fenetre, nb_colonnes, nb_lignes)
        canvas.pack(side=TOP, padx=5, pady=5)
        canvas.bind("<Button-1>", Jeu.cliquer_carte)  # permet le clic sur les cartes
        Jeu.melanger_cartes()
        for i in range(nb_colonnes):  # dessin des cartes retournées
            for j in range(nb_lignes):
                canvas.create_image((155 * i) + 60, (205 * j) + 60, image=images[0])
        text1 = 'Joueur 1 : ' + str(score[0] * 2)
        text2 = 'Joueur 2 : ' + str(score[1] * 2)
        points_joueur1.config(text=text1, bg='orange')
        points_joueur2.config(text=text2, bg='white')


fenetre = Fenetre()
menu = MenuJeu()

fenetre.mainloop()
