# Bonne pratique --> d'abord les fonctions et ensuite les variables
def calcul(nbre_1, nbre_2):
    somme = nbre_1 + nbre_2
    difference = nbre_1 - nbre_2
    quotient = nbre_1 / nbre_2
    produit = nbre_1 * nbre_2
    return (somme,difference,quotient, produit)

nombre_1 = float(input("Veuillez entrer le premier nombre : "))
nombre_2 = float(input("Veuillez entrer le seconde nombre : "))
    

print (calcul(nombre_1,nombre_2))

add, diff, quot, prod = calcul(nombre_1,nombre_2)
print (f"Addition : {add}, Soustraction : {diff}, Division : {quot}, Multiplication : {round(prod,2)}")