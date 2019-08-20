from tkinter import *
def hello(): #Crée la commande hello
   E3.insert(INSERT, 'Bonjour '+ E1.get() + '  ' +  E2.get()+'\n') #E3.insert : la zone de text, INSERT = Insérer du text à l'aide différentes chaines de caractèrtes, E1.get() = récupérer le text dans dans la zone de text E1 et pareil pour E2
   
fp = Tk()#Créer la fenetre fp
fp.title('Widgets Button Entry Text')#Donner un titre 
L1 = Label(fp, text = 'Nom')#Affiche "Nom" au dessus de la premire zone de text
E1 = Entry(fp, width=20, bg = 'yellow')#Crée une zone d'inserssion de texte en dessus de L1
E1.insert(INSERT , 'Pain')#Remplir au démarage E1 avec Pain
L2 = Label(fp, text = '\nPrénom')#Afficher "Prénom" en sautant une ligne
# le \n permet d'espacer verticalement
E2 = Entry(fp, width=15 ,  bg ='#ffcc00')#Crée une zone d'inserssion de texte qui s'appelle E2 avec une largeur de 15 et un fond de couleur orange
E2.insert(INSERT,'Desucre')#Remplir au démarage E1 avec Desucre
B1 = Button(fp, text='Saluer', bd=5, command = hello)#Créer un boutton pour saluer qui lance la commande hello
B2 = Button(fp, text='EXIT', bd=5, command=fp.destroy)#Créer un boutton qui ferme la fenetre fp
E3 = Text(fp, width=30, height=15)#Crée une zone de texte et définir la taille
E3.pack(side=RIGHT, fill= BOTH, padx = 5, pady = 10, expand=False)#Placer E3, side=Right : allignement de E3 à droite de la fenetre. fill= BOTH : la fenetre peut s'éttendre autant qu'elle veut sur X et Y.
L1.pack()#Place les wigets par défaut dans la fenetre.
E1.pack()#Place les wigets par défaut dans la fenetre.
L2.pack()#Place les wigets par défaut dans la fenetre.
E2.pack()#Place les wigets par défaut dans la fenetre.
B1.pack(pady=20)#Place B1 avec un padding y de 20.
B2.pack(pady=5)#Place B2 avec un padding Y de 5.
fp.mainloop()#Quand fp est fermer, tout se ferme.
