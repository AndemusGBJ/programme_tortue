import turtle

t = turtle.Turtle() # Création de l'objet
"""
    DPLACEMENT DE LA TORTUE
"""

def tortue():
    t.forward(200)  #On avance de 200 pixel
    t.right(90)     #On tourne à droit à 90°
    t.forward(100)  # On avance de 100 pixels
    t.left(90)      # On toure à gauche de 90°
    t.forward(100)  # On avance de 100 pixels
    t.right(90)     # On toure à doite à 90°
    t.backward(300) # On récule de 300 pixels

"""
    FAIRE UN ESCACLIER
"""
def excalier(taille, rea):
    for i in range(taille):
        t.forward(rea)
        t.left(90)
        t.forward(rea)
        t.right(90)
    t.forward(rea)

"""
    DESSINER UN CARRE
"""
def carre(taille):
    for i in range(4):
        t.forward(taille)
        t.right(90)

def plusieurs_carres(taille_depart, nb):
    for i in range (1,nb):
        taille = i*taille_depart
        carre(taille)  #Appel de la fonction carre(taille) pour dessiner les différents carrés


# tortue()
# excalier(5,30)
# carre(100)

plusieurs_carres(30,5)


turtle.done()   #Pour garder la fenêtre ouverte
