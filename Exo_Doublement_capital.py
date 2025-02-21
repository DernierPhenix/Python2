capital = int(input("Entrer le montant de votre capital :"))
taux = float(input("Entrer le taux à appliquer : "))
cap_double = capital * 2
annee = 1 


while capital <= cap_double:

    
    capital = capital *(1+ (taux /100))
    annee += 1
print("Le nombre d'années pour doubler votre capital est : ",annee)





