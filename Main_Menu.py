__author__ = 'vincs'

from tkinter import *
from tkinter.filedialog import *

#Main Frame
fenetre = Tk()
fenetre.title("NainPair")
fenetre.geometry('1200x800')

#set the window icon
#window.wm_iconbitmap('Icon.ico')

#set the window background to hex code '#a1dbcd'
fenetre.configure(background="#a1dbcd")

#Frame Menu Buttons
frame_Menu = Frame(fenetre,borderwidth=2, relief=GROOVE, width=50, height=500)
frame_Menu.pack()




#Create new frame for Number of players
def new_frame():
    global frame_players, one_player, two_players, back_menu

    frame_players = Frame(fenetre, borderwidth=4, relief=GROOVE, width=500, height=250)
    one_player= Button(frame_players, text ='1 Nain',font=("Arial",50),fg="#a1dbcd", bg="#383a39", command=new_frame)
    two_players= Button(frame_players, text='2 Nains',font=("Arial",50),fg="#a1dbcd", bg="#383a39")
    back_menu= Button(frame_players, text='Back to menu',font=("Arial",50),fg="#a1dbcd", bg="#383a39",command=fermer)
    #Basics

    frame_players.pack(padx= 50, pady=50)

 #Place of frames
    frame_players.place(x=350, y=100)

 #Buttons 1Player 2Player Quit

    one_player.pack( padx = 50, pady = 10,)
    two_players.pack(padx = 25, pady = 25)
    back_menu.pack(padx = 25, pady = 25,)

# opening text file
global rulestext, content, regles

regles = open('regles/regles.txt', "r")
content = regles.read()

regles.close()



def rules():
    global frame_rules, back_menu_rules, text_rules


    frame_rules = Frame(fenetre,borderwidth=4, relief=GROOVE, width=500, height=250)
    frame_rules.pack()
    back_menu_rules = Button(frame_rules, text='Back to menu', font=("Arial",23),fg="#a1dbcd", bg="#383a39", command=fermer_rules)
    back_menu_rules.pack(padx = 25, pady = 25, side=BOTTOM)
    text_rules = Label(frame_rules, text = content, font=("Arial", 35))
    text_rules.pack()
    frame_rules.place(x=350,y=100)




def fermer():
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

def Quit():
    fenetre.destroy()

#test boutton pack_forget
#def fermerbutton ():
    #one_player.pack_forget()




#Frame Nain Pict
frame_Nain = Frame(fenetre, width=100, height=300)
frame_Nain.pack(side= LEFT, padx = 100, pady = 100)

#Menu's Buttons
play= Button(frame_Menu, text ='Play',font=("Arial",50),fg="#a1dbcd", bg="#383a39", command=new_frame)
play.pack( padx = 50, pady = 10,)

rules= Button(frame_Menu, text='Rules',font=("Arial",50),fg="#a1dbcd", bg="#383a39", command=rules)
rules.pack(padx = 25, pady = 25)

scores= Button(frame_Menu, text='Scores',font=("Arial",50),fg="#a1dbcd", bg="#383a39")
scores.pack(padx = 25, pady = 25,)

quit= Button(frame_Menu, text='Quit',font=("Arial",50),fg="#a1dbcd", bg="#383a39",command=Quit)
quit.pack(padx = 25, pady = 25,)





fenetre.mainloop()
#
# image ain
#
# root = tk.Tk()
# img = ImageTk.PhotoImage(Image.open(path))
# panel = tk.Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()

#Frame on click
#Widget window?
