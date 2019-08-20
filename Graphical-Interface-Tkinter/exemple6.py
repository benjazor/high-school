from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

def Ouvrir():
    Canevas.delete(ALL) # on efface la zone graphique
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('gif files','.gif'),('all files','.*')])
    photo = PhotoImage(file=filename)
    gifdict[filename] = photo  # référence
    Canevas.create_image(0,0,anchor=NW,image=photo)
    Canevas.config(height=photo.height(),width=photo.width())
    Mafenetre.title("Image "+str(photo.width())+" x "+str(photo.height()))

def Fermer():
    Canevas.delete(ALL)
    Mafenetre.title("Image")

def Apropos():
    tkinter.messagebox.showinfo("A propos","Exemple de messagebox")

def Clic(event):
    X = event.x #X = le x de la souris lors de l'evenement
    Y = event.y #Y = le y de la souris lors de l'evenement
    Balle = Canevas.create_oval(X-10,Y-10,X+10,Y+10,width=1,fill='black')#Crée un oval noir d'une taille 20x20 centré sur la souris
    Listeballe.append(Balle)#Enregistre la balle dans une liste
    
def Annuler():
    n=len(Listeballe)#définir n, tel que n soit égal à la longeur de la liste Listeball
    if n>0:
        Canevas.delete(Listeballe[n-1]) #Supprime le dernier objet de la Listeballe
        del(Listeballe[n-1]) #Supprime la dernière valeur de la Listeballe 


# Utilisation d'un dictionnaire pour conserver la référence de l'image afin qu'elle existe en dehors de la fonction ouvrir
gifdict={}

# Utilisation d'une liste pour conserver les références des items de balle
Listeballe=[]

# Création de la fenetre principale
Mafenetre = Tk()
Mafenetre.title("Image")

# Création d'un widget Menu associé à la fenetre principale
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir une image",command=Ouvrir)
menufichier.add_command(label="Fermer l'image",command=Fermer)
menufichier.add_separator()
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas dans la fenetre principale
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)

# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
Canevas.bind('<Button-1>', Clic)

# Création d'un widget Button (bouton Annuler)
BoutonAnnuler = Button(Mafenetre, text ='Annuler clic', command = Annuler)
BoutonAnnuler.pack(side = LEFT, padx = 5, pady = 5)

# On lance le gestionnaire d'évènement
Mafenetre.mainloop()
