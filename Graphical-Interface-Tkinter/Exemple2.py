from tkinter import *

root = Tk() #Fenetre prince pricipale
W1 = Toplevel(root, bg='gold', cursor = 'X_cursor') #Définir la couleur du fond de la fenetre et le curseur affiché quand on est sur la fenetre
W2 = Toplevel(root, bg='red', cursor = 'man', pady=10) #Définir la couleur du fond de la fenetre et le curseur affiché quand on est sur la fenetre
root.geometry('400x100+100+100') #Définir la taille de l'image au lancement et sa position par rapport au coin suppérieur gauche de l'écran
W1.geometry('400x100+100+250') #Définir la taille de l'image au lancement et sa position par rapport au coin suppérieur gauche de l'écran
W2.geometry('400x200+100+400') #Définir la taille de l'image au lancement et sa position par rapport au coin suppérieur gauche de l'écran
root.title('Fenetre Principale') #Titre de la fenetre principale
W1.title('Fenetre 1') #Titre de la fenetre 1
W2.title('Fenetre 2') #Titre de la fenetre 2

B1 = Button(root, text= ' BOUTON FP').pack(pady = 10) #Définir le boutton 1
B2 = Button(W1, text= ' BOUTON W1').pack(pady = 10) #Définir le boutton 2
B3 = Button(W2, text= ' BOUTON W2').pack(pady = 10) #Définir le boutton 3
W1.maxsize(500, 400) #Définir la taille max de la fenetre
W2.minsize(150, 100) #Définir la taille min de la fenetre
root.mainloop() #Permet de fermer toutes les fenetres quand on ferme la fenetre principale