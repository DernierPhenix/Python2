from math import *

rayon = float(input ("Entrer un nombre pour le rayon du cône en cm : "))
hauteur = float(input ("Entrer un nombre pour la hauteur du cône en cm : "))

#volume = round ((1/3)*hauteur*pi*(rayon**2),2)
#print("Le volume du cône droit est : ",volume, "cm3")

print("Le volume du cône droit est : ",round ((1/3)*hauteur*pi*(rayon**2),2), "cm3")