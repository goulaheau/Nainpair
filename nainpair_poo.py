from tkinter import *
from random import randint, shuffle
import csv


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
        fenetre_menu.pack(pady=50)

        bouton_jouer = Button(fenetre_menu, text='Jouer', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=MenuJeu.creer_menu_joueur)
        bouton_jouer.pack(padx=25, pady=10)

        bouton_regles = Button(fenetre_menu, text='Règles', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=MenuJeu.creer_menu_regles)
        bouton_regles.pack(padx=25, pady=10)

        bouton_score = Button(fenetre_menu, text='Scores', font=("Arial", 35), fg="#a1dbcd", bg="#383a39")
        bouton_score.pack(padx=25, pady=10)

        bouton_quitter = Button(fenetre_menu, text='Quitter', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Fenetre.destroy(fenetre))
        bouton_quitter.pack(padx=25, pady=10)

    @staticmethod
    def creer_menu_joueur():
        """
        Création du menu qui demande à combien de joueurs on va jouer
        :return:
        """
        global fenetre_menu_joueur, bouton_un_nain, bouton_deux_nains, bouton_fermer_menu_joueur

        MenuJeu.fermer_menu()

        fenetre_menu_joueur = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_menu_joueur.pack(pady=50)

        bouton_un_nain = Button(fenetre_menu_joueur, text='1 Nain', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: MenuJeu.creer_menu_difficulte(1))
        bouton_un_nain.pack(padx=25, pady=10)

        bouton_deux_nains = Button(fenetre_menu_joueur, text='2 Nains', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: MenuJeu.creer_menu_difficulte(2))
        bouton_deux_nains.pack(padx=25, pady=10)

        bouton_fermer_menu_joueur = Button(fenetre_menu_joueur, text='Retour', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=MenuJeu.fermer_menu_joueur)
        bouton_fermer_menu_joueur.pack(padx=25, pady=10)

    @staticmethod
    def creer_menu_regles(en_partie=False):
        """
        Affiche le menu contenant les règles
        :return:
        """
        global fenetre_menu_regles, bouton_fermer_menu_regles, text_regles, contenu, fichier_regles

        MenuJeu.fermer_menu()

        fichier_regles = open('regles.txt', "r")
        contenu = fichier_regles.read()
        fichier_regles.close()

        fenetre_menu_regles = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_menu_regles.pack(pady=50)

        bouton_fermer_menu_regles = Button(fenetre_menu_regles, text='Retour', font=("Arial", 23), fg="#a1dbcd", bg="#383a39", command=lambda: MenuJeu.fermer_menu_regles(en_partie))
        bouton_fermer_menu_regles.pack(padx=25, pady=10, side=BOTTOM)

        text_regles = Label(fenetre_menu_regles, text=contenu, font=("Arial", 15))
        text_regles.pack(padx=25, pady=10)

    @staticmethod
    def creer_menu_difficulte(nb_joueurs):
        """
        Crée le menu demandant la difficulte en prenant en compte le nombre de joueurs
        :param nb_joueurs: int
        :return:
        """
        global fenetre_difficulte, bouton_facile, bouton_moyen, bouton_difficile, bouton_difficulte_personnalise, slider_difficulte_personnalise

        MenuJeu.fermer_menu_joueur()
        MenuJeu.fermer_menu()

        fenetre_difficulte = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
        fenetre_difficulte.pack(pady=50)
        text_difficulte_personnalise = Label(fenetre_difficulte, text="Difficulté Personnalisé", font=("Arial", 20), fg="#383a39")
        slider_difficulte_personnalise = Scale(fenetre_difficulte, from_=1, to=10, orient=HORIZONTAL, font=("Arial", 20), fg="#383a39", length=200)

        if nb_joueurs == 1:
            bouton_facile = Button(fenetre_difficulte, text='Facile', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 4, True))
            bouton_moyen = Button(fenetre_difficulte, text='Moyen', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 6, True))
            bouton_difficile = Button(fenetre_difficulte, text='Difficile', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, 8, True))
            bouton_difficulte_personnalise = Button(fenetre_difficulte, text='Lancer', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(1, slider_difficulte_personnalise.get(), True))
        else:
            bouton_facile = Button(fenetre_difficulte, text='Facile', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 4, True))
            bouton_moyen = Button(fenetre_difficulte, text='Moyen', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 6, True))
            bouton_difficile = Button(fenetre_difficulte, text='Difficile', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, 8, True))
            bouton_difficulte_personnalise = Button(fenetre_difficulte, text='Lancer', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.creer_jeu(2, slider_difficulte_personnalise.get(), True))

        bouton_facile.pack(padx=25, pady=15)
        bouton_moyen.pack(padx=25, pady=15)
        bouton_difficile.pack(padx=25, pady=15)

        text_difficulte_personnalise.pack(padx=25, pady=0)
        slider_difficulte_personnalise.pack(padx=25, pady=0)
        bouton_difficulte_personnalise.pack(padx=25, pady=5)

        fermer_menu_difficulte = Button(fenetre_difficulte, text='Retour', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=MenuJeu.fermer_menu_difficulte)
        fermer_menu_difficulte.pack(padx=25, pady=15)

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
    def fermer_menu_regles(en_partie):
        """
        Ferme le menu menu contenant les règles
        :return:
        """
        fenetre_menu_regles.pack_forget()
        bouton_fermer_menu_regles.pack_forget()
        text_regles.pack_forget()

        fenetre_menu_regles.destroy()
        if en_partie:
            canvas.pack()
        else:
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
        bouton_difficulte_personnalise.pack_forget()
        slider_difficulte_personnalise.pack_forget()

        fenetre_difficulte.destroy()

        MenuJeu.creer_menu_joueur()


class Jeu:
    global images, cartes, cartes_jouees, nb_lignes, nb_colonnes, choix_cartes, joueur_actuel, score, fini, peut_jouer, nb_coups
    images = []
    cartes = []
    cartes_jouees = []
    nb_lignes = 4
    nb_colonnes = 4
    choix_cartes = []
    joueur_actuel = 0
    nb_coups = 0
    score = [0, 0]
    fini = False
    peut_jouer = True
    nombre_joueurs = 1

    @staticmethod
    def creer_jeu(nb_joueurs, difficulte, premiere_fois=False):
        """
        Affiche le menu permettant de choisir la difficulté pour 2 joueurs
        :param difficulte: int
        :param nb_joueurs: int
        :return:
        """
        if premiere_fois:
            MenuJeu.fermer_menu_difficulte()
            MenuJeu.fermer_menu_joueur()
            MenuJeu.fermer_menu()

        # Initilisation du jeu
        global points_un_joueur, points_joueur1, points_joueur2, canvas, nb_colonnes, top, jeu, submenu

        top = Menu(fenetre)
        fenetre.config(menu=top)

        jeu = Menu(top, tearoff=False)
        top.add_cascade(label='Jeu', menu=jeu)

        submenu = Menu(jeu, tearoff=False)
        jeu.add_cascade(label='Nouvelle Partie', menu=submenu)

        subsubmenu = Menu(submenu, tearoff=False)
        submenu.add_cascade(label='1 Nain', menu=subsubmenu)
        subsubmenu.add_command(label='Facile', command=lambda: Jeu.reinit(1, 4, True))
        subsubmenu.add_command(label='Moyen', command=lambda: Jeu.reinit(1, 6, True))
        subsubmenu.add_command(label='Difficile', command=lambda: Jeu.reinit(1, 8, True))

        subsubmenu2 = Menu(submenu, tearoff=False)
        submenu.add_cascade(label='2 Nain', menu=subsubmenu2)
        subsubmenu2.add_command(label='Facile', command=lambda: Jeu.reinit(2, 4, True))
        subsubmenu2.add_command(label='Moyen', command=lambda: Jeu.reinit(2, 6, True))
        subsubmenu2.add_command(label='Difficile', command=lambda: Jeu.reinit(2, 8, True))

        jeu.add_cascade(label='Règles', command=lambda: Jeu.afficher_regle(True))
        jeu.add_cascade(label='Menu', command=Jeu.fermer_jeu)
        jeu.add_command(label='Quitter', command=fenetre.destroy)

        # Création du canvas dont la taille dépend du nombre de cartes
        canvas = Jeu.creer_canvas(fenetre, nb_colonnes, nb_lignes)
        canvas.pack(side=TOP, padx=2, pady=2)

        points_joueur1 = Label(fenetre, text="Joueur 1 : 0", bg="orange", font="Helvetica 16")
        points_joueur2 = Label(fenetre, text="Joueur 2 : 0", font="Helvetica 16")
        points_un_joueur = Label(fenetre, text="Nombre de coups : 0", font="Helvetica 16")

        points_joueur1.pack(pady=2, side=LEFT)
        points_joueur2.pack(pady=2, side=RIGHT)
        points_un_joueur.pack(pady=2, side=LEFT)

        Jeu.charger_images()

        # Solutionne le problème d'affichage des scores
        Jeu.reinit(nb_joueurs, difficulte)

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
        global joueur_actuel, fini, peut_jouer, nb_coups, canvas, nombre_joueurs
        if cartes[cartes_jouees[0] - 1] == cartes[cartes_jouees[1] - 1]:
            # enleve les cartes identiques. Le joueur actuel reste le même
            canvas.delete(cartes_jouees[0])
            canvas.delete(cartes_jouees[1])
            score[joueur_actuel] += 1
            nb_coups += 1
        else:
            # retourne les cartes différentes. Le joueur actuel change
            canvas.itemconfig(cartes_jouees[0], image=images[0])
            canvas.itemconfig(cartes_jouees[1], image=images[0])
            joueur_actuel = (joueur_actuel + 1) % 2  # la main passe à l'autre joueur
            nb_coups += 1

        cartes_jouees = []

        text1 = 'Joueur 1 : ' + str(score[0])
        text2 = 'Joueur 2 : ' + str(score[1])
        text1joueur = 'Nombre de coups : ' + str(nb_coups)

        points_joueur1.config(text=text1)
        points_joueur2.config(text=text2)
        points_un_joueur.config(text=text1joueur)

        peut_jouer = True  # réactive l'effet du clic de la souris

        if joueur_actuel == 0:  # celui qui joue est en orange
            points_joueur1.config(bg='orange')
            points_joueur2.config(bg='white')
        else:
            points_joueur2.config(bg='orange')
            points_joueur1.config(bg='white')

        if score[0] + score[1] == (nb_colonnes * nb_lignes) // 2:
            fini = True  # afficher le résultat de la partie
            if nombre_joueurs == 1:
                with open('scores/score' + str(nb_colonnes) + '.txt', 'r') as file1:
                    valeurs = [str(row[0]) + str(row[1]) for row in csv.reader(file1)]

                top_cinq = sorted(valeurs, reverse=True, key=lambda v: v[0])[:5]

                valeurs = 0
                if valeurs < 5:
                    if nb_coups < int(top_cinq[0][valeurs]):
                        valeurs += 1
                    else:
                        place = top_cinq[0][valeurs]
                        texte = "            Vous êtes #" + str(place) + " !\n"

                texte += 'Vous avez gagné en ' + str(nb_coups) + ' coups.'

            else:
                if score[0] > score[1]:
                    texte = "Le joueur 1 a gagné !"
                elif score[0] < score[1]:
                    texte = "Le joueur 2 a gagné !"
                else:
                    texte = "Egalité !"

            canvas.pack_forget()
            canvas.destroy()
            canvas = Canvas(fenetre, width=800, height=400)
            canvas.pack(pady=50)

            texte_entrez_nom = Label(canvas, text="Entrez votre nom", font=("Arial", 15))
            zone_entrez_nom = Entry(canvas, bd=1)
            bouton_sauvegarder_score = Button(canvas, text='Sauvergarder le score', font=("Arial", 15), fg="#a1dbcd", bg="#383a39", command=lambda: Jeu.sauvegarder_score(nb_coups, zone_entrez_nom.get()))

            texte_entrez_nom.pack(pady=15)
            zone_entrez_nom.pack(pady=15)
            bouton_sauvegarder_score.pack(padx=100, pady=50)

            canvas.create_text(300, 200, text=texte, font='Calibri 24', fill='black')
            bouton_menu = Button(canvas, text='Retour au Menu', font=("Arial", 35), fg="#a1dbcd", bg="#383a39", command=Jeu.fermer_jeu)
            bouton_menu.pack(padx=100, pady=250)

    @staticmethod
    def cliquer_carte(event):
        """
        Retourne la carte sélectionnée
        :param event:
        :return:
        """
        global fini, fenetre, cartes_jouees, peut_jouer, nombre_joueurs, nb_colonnes
        if len(cartes_jouees) < 2:
            carte_selection = canvas.find_closest(event.x, event.y)
            carte_id = carte_selection[0]
            if fini:
                fini = False
                Jeu.reinit(nombre_joueurs, nb_colonnes)
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
    def creer_canvas(fen, col, lig):
        """
        Création du canvas
        :param fen:
        :param col:
        :param lig:
        :return:
        """
        return Canvas(fen, width=(125 * col), height=(164 * lig), bg='#a1dbcd', borderwidth=0)

    @staticmethod
    def reinit(nb_joueurs, difficulte, nouvelle_partie=False):
        """
        Redémarre une partie et change éventuellement la difficulté
        :return:
        """
        global canvas, joueur_actuel, score, nb_lignes, nb_colonnes, nb_coups, points_joueur1, points_joueur2, points_un_joueur, nombre_joueurs

        joueur_actuel = 0
        score = [0, 0]
        nb_coups = 0
        del cartes[:]
        del cartes_jouees[:]
        canvas.destroy()
        nb_colonnes = difficulte
        nombre_joueurs = nb_joueurs
        canvas = Jeu.creer_canvas(fenetre, nb_colonnes, nb_lignes)
        canvas.pack(pady=50)
        canvas.bind("<Button-1>", Jeu.cliquer_carte)  # permet le clic sur les cartes

        if nb_joueurs == 2:
            points_un_joueur.pack_forget()
            points_joueur1.pack(pady=2, side=LEFT)
            points_joueur2.pack(pady=2, side=RIGHT)
        else:
            points_joueur1.pack_forget()
            points_joueur2.pack_forget()
            points_un_joueur.pack(pady=2, side=LEFT)

        Jeu.melanger_cartes()

        for i in range(nb_colonnes):  # dessin des cartes retournées
            for j in range(nb_lignes):
                canvas.create_image((126 * i), (166 * j), anchor='nw', image=images[0])

        text1 = 'Joueur 1 : ' + str(score[0] * 2)
        text2 = 'Joueur 2 : ' + str(score[1] * 2)
        text1joueur = 'Nombre de coups : ' + str(nb_coups)

        points_joueur1.config(text=text1, bg='orange')
        points_joueur2.config(text=text2, bg='white')
        points_un_joueur.config(text=text1joueur, bg='white')

        if nouvelle_partie:
            Jeu.reinit(nb_joueurs, difficulte)

    @staticmethod
    def recreer_jeu(nb_joueurs, difficulte):
        """
        Ferme le menu demandant la difficulte en prenant en compte le nombre de joueurs
        :return:
        """
        global points_un_joueur, points_joueur1, points_joueur2, canvas, nb_colonnes, top, jeu, submenu
        top.pack_forget()
        jeu.pack_forget()
        submenu.pack_forget()
        canvas.pack_forget()
        points_joueur1.pack_forget()
        points_joueur2.pack_forget()
        points_un_joueur.pack_forget()

        top.destroy()

        Jeu.creer_jeu(nb_joueurs, difficulte)

    @staticmethod
    def fermer_jeu():
        """
        Ferme le menu demandant la difficulte en prenant en compte le nombre de joueurs
        :return:
        """
        top.pack_forget()
        jeu.pack_forget()
        submenu.pack_forget()
        canvas.pack_forget()
        points_joueur1.pack_forget()
        points_joueur2.pack_forget()
        points_un_joueur.pack_forget()

        top.destroy()

        MenuJeu.creer_menu()

    @staticmethod
    def afficher_regle(en_partie):
        canvas.pack_forget()
        MenuJeu.creer_menu_regles(en_partie)

    @staticmethod
    def sauvegarder_score(nb_coups, nom_joueur):




fenetre = Fenetre()
menu = MenuJeu()

fenetre.mainloop()
