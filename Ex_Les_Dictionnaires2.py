mon_dict = {}

mon_dict ={
    "clé 1" : "valeur 1",
    2 : 1,
    True : False
}

# Pour accéder à un valeur liée à une clé
print(f"Valeur contenu à la clé 1 : {mon_dict["clé 1"]}")
print(f"Valeur contenu à la clé 2 : {mon_dict[2]}")
print(f"Valeur contenu à la clé 3 : {mon_dict[True]}")

# On ré-affecte une autre valeur à une clé
mon_dict["clé 1"] = "ToTo"
print(f"Valeur contenue dans la clé 1 : {mon_dict['clé 1']}")

# Pour ajouter un élément
print(mon_dict)
mon_dict["clé 2"] = "Casque"
print(mon_dict)

# Supprimer un élément avec 'Del' / Ne supprime que les éléments présents dans le dictionnaire
del mon_dict["clé 2"]
print(mon_dict)

mon_dict.pop(True) # Supprime la clé 'True'
print(mon_dict)

# Supprime et renvoie l'élément (sous forme de tuple)
recup = mon_dict.popitem()
print(mon_dict)
print(recup)

#--------------------------------------------------------------------------------------------------

personne = {
    "Prénom" : "Jean-Pierre",
    "Nom" : "FLEURY",
    "Âge" : None
}

# Fusion de dictionnaires
print(personne)
personne.update(mon_dict)
print(personne)

# Parcours de dictionnaire
for cle, valeur in personne.items():
    print(f"Ma clé : {cle} & la valeur qui va avec : {valeur}")

#----------------------------------------------------------------------------------------------------
personne = {
    "Prénom" : "Marianna",
    "Nom" : "FLEURY",
    "Âge" : 26
}
personne1 = {
    "Prénom" : "Antonio",
    "Nom" : "FLEURY",
    "Âge" : 23
}
personne2 = {
    "Prénom" : "Jean-Pierre",
    "Nom" : "FLEURY",
    "Âge" : 49
}

annuaire = [personne, personne1, personne2]
print(annuaire)

for personnage in annuaire:
    print((f"Personne n° {annuaire.index(personnage)}"))
    for cle, valeur in personnage.items():
        print(f"{cle} : {valeur}")