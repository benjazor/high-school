#-*- coding:Latin-1 -*-
# PIL (Python Imaging Library) est une bibliothèque pour la manipulation des images
from PIL import Image                                    

#============================================================
def negatif(Pix,Largeur,Hauteur): 
    for n in range(Largeur*Hauteur):
        Pix[n]=255-Pix[n]     
    return Pix
#============================================================

# L'image a 3 composantes : RGB ou 1 si elle est en N&B
im = Image.open("rose.jpg")                                     
w,h=im.size

# Détermination du type d'image RGB ou N&B
bands=im.getbands()

if len(bands)==3:
    #Séparation des composantes => tuple de 3 images
    ImagePixelsRouges,ImagePixelsVerts,ImagePixelsBleus=im.split()      

    #transformation de l'image en liste de pixels
    ListePixelsRouges=list(ImagePixelsRouges.getdata())                 
    ListePixelsVerts=list(ImagePixelsVerts.getdata())
    ListePixelsBleus=list(ImagePixelsBleus.getdata())

    ListePixelsRouges=negatif(ListePixelsRouges,w,h)
    ListePixelsVerts=negatif(ListePixelsVerts,w,h)
    ListePixelsBleus=negatif(ListePixelsBleus,w,h)
    
    ImagePixelsRouges.putdata(ListePixelsRouges)
    ImagePixelsVerts.putdata(ListePixelsVerts)
    ImagePixelsBleus.putdata(ListePixelsBleus)
    
    ImagePixels = Image.merge('RGB',(ImagePixelsRouges,ImagePixelsVerts,ImagePixelsBleus))


else :
    #récupération des données de l'image
    ImagePixels=im.getdata()
    #transformation de l'image en liste de pixels
    ListePixels=list(ImagePixels)                   
    ListePixels=negatif(ListePixels,w,h)
    ImagePixels = Image.new('L',(w,h)) 
    ImagePixels.putdata(ListePixels)

ImagePixels.save("Negatif_rose.jpg")
ImagePixels.close()
im.close()
