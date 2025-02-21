pop_init =int(input("Entrer le nombre de la population initiale : "))
taux = float(input("Entrer le taux d'accroissement souhaité :"))
pop_vis = float(input("Entrer le nombre de la population visée : "))
#pop_vis = pop_init + (pop_init* (taux/100))

annee = 0

while pop_init <= pop_vis :

    pop_init = pop_init + (pop_init* (taux/100))
    annee += 1
print("Le nombre d'années pour atteindre la population cible est de : ",annee, "ans")

#demande à l'itilisateur la population initiale, le taux d'accroissement, la population visé
#Combien detemps (en années) pour atteindre la population visée.
