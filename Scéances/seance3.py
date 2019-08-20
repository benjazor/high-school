##################
#   EXERCICE 1   #
##################

#mot=input("Entrez un mot: ")
#l=input("Entrez une lettre: ")
#compter = 0
#for letter in mot:
#    if letter == l:
#        compter=compter + 1
#print("Il y a",compter,l,"dans",mot)

##################
#   EXERCICE 2   #
##################

#t=(12.3,78,True,"Toto")
#t[0]=12
#t[0]
#for e in t:
#    print(e)

#u=["B",5,"dans l'eau"]
#u[0]
#for e in u:
#    print(e)

#nbr=[]
#nbrcarré=[]
#for loop in range(10):
#    nbr.append(loop)
#    nbrcarré.append(loop*loop)
#print("Nombres:",nbr[0:10])
#print("Carrés:",nbrcarré[0:10])
#
#c=[]
#for e in nbr:
#    c.append(e*e*e)
#print(c)
#
#q=[e**4 for e in nbr]
#print(q)

nbr=[]
nbrcarré=[]
for loop in range(200):
    nbr.append(loop)
    p=[e**loop for e in nbr]
    print("Puiisance de",loop,p)
