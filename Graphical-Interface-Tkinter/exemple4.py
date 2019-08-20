from tkinter import *
Mafenetre = Tk() #Créer la fenetre Mafenetre
Mafenetre.title('France') #Met un titre à la fenetre.
photo = PhotoImage(file="image.gif") #Crée un widget image. 
Can = Canvas(Mafenetre,width = photo.width(), height = photo.height())    # Création d'un widget Canvas (zone graphique)
item = Can.create_image(0,0,anchor=NW, image=photo) # Crée l'objet image et l'insert dans le cancevas
Can.create_oval(150, 150, 200, 200, outline='black', fill='black') #Crée un rond oval noir d'un pixel à un autre
Can.pack() #Affiche le canevas
Mafenetre.mainloop() #Quand ferme