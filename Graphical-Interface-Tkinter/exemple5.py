from tkinter import *
fp =Tk() #Crée la fenetre principale
F1 = Frame(fp, bg='gold', bd=5,relief = RAISED) #Crée la Frame F1 dans la fenetre principale qui a un fond de la couleur gold, un bord de taile 5 et du relief.
F2 = LabelFrame(fp, text = 'Groupe 2', labelanchor = N) #Crée la LabelFrame dans la fenetre principale avec le label "Groupe 2"
B1 = Button(F1,text='Bouton 1 F1') #Crée le bouton B1 dans F1
B2 = Button(F2,text='Bouton 1 F2') #Crée le bouton B2 dans F2
B1.pack(padx = 10, pady = 10) #Definir le padding
B2.pack(padx = 10, pady = 10) #Definir le padding
F1.pack(padx =10, pady = 10) #Definir le padding
F2.pack(padx =10, pady = 10) #Definir le padding
fp.mainloop()