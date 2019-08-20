
# PIL (Python Imaging Library) est une bibliothèque pour la manipulation des images
from PIL import Image                                   

#============================================================
def seuillage(Pix,n,inf,sup): 
  for i in range(n):
    if Pix[i]>sup or Pix[i]<inf:
      Pix[i]=0
    else:
      Pix[i]=255
  return Pix
#============================================================

# Définitions des valeurs de seuils
s1,s2=125,250

# L'image a 3 composantes :RGB
im = Image.open("rose.jpg")
w,h=im.size

bands=im.getbands()

if len(bands)==3:
    #Séparation des composantes => tuple de 3 images
    ImagePixelsRouges,ImagePixelsVerts,ImagePixelsBleus=im.split()      

    #transformation de l'image en liste de pixels
    ListePixelsRouges=list(ImagePixelsRouges.getdata())                 
    ListePixelsVerts=list(ImagePixelsVerts.getdata())
    ListePixelsBleus=list(ImagePixelsBleus.getdata())

    ListePixelsRouges=seuillage(ListePixelsRouges,w*h,s1,s2)
    ListePixelsVerts=seuillage(ListePixelsVerts,w*h,s1,s2)
    ListePixelsBleus=seuillage(ListePixelsBleus,w*h,s1,s2)
    
    ImagePixelsRouges.putdata(ListePixelsRouges)
    ImagePixelsVerts.putdata(ListePixelsVerts)
    ImagePixelsBleus.putdata(ListePixelsBleus)
    
    ImagePixels = Image.merge('RGB',(ImagePixelsRouges,ImagePixelsVerts,ImagePixelsBleus))


else :
    #récupération des données de l'image
    ImagePixels=im.getdata()
    #transformation de l'image en liste de pixels
    ListePixels=list(ImagePixels)                   
    ListePixels=seuillage(ListePixels,w*h,s1,s2)
    ImagePixels = Image.new('L',(w,h)) 
    ImagePixels.putdata(ListePixels)

ImagePixels.save("seuillage_rose.jpg")
ImagePixels.close()
im.close()
