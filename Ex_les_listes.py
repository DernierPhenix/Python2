ma_liste = []
print(ma_liste) # []
ma_liste = [1, 2, 3]
print(ma_liste) # [1, 2, 3]
ma_liste = [2, 1, 3]
print(ma_liste) # [2, 1, 3]
ma_liste.sort()
print(ma_liste) # [1, 2, 3]
ma_liste.append(4)
print(ma_liste) # [1, 2, 3, 4]
ma_liste.extend([5, 6])
print(ma_liste) # [1, 2, 3, 4, 5, 6]
ma_liste.remove(4)
print(ma_liste) # [1, 2, 3, 5, 6]
ma_liste.pop(2)
print(ma_liste) # [1, 2, 5, 6]

#----------------------------------------------------------

ma_liste = [1, 2, 3, 4, 5]
print(ma_liste) # [1, 2, 3, 4, 5]
for item in ma_liste:
    print(item)

ma_liste = [1,2,3,"toto", True,["a",False,25]]
print(ma_liste)
print(ma_liste[0])
print(ma_liste[5][1])
print(ma_liste[-1][1])
print(ma_liste[-1][-1])

# Modifier un élément
ma_liste[4] = "titi"
print(ma_liste)

# Trier une liste
ma_liste2 = [9,5,7,4,3,8,6,2,1]
print(ma_liste2) # on affiche la liste comme elle est définie
ma_liste2.sort()
print(ma_liste2) # on affiche la liste comme elle est définie
ma_liste2.sort(reverse=True) #on demande un tri décroissant
print(ma_liste2)

# Ajout d'un élément à la fin de la liste
ma_liste = [5,6,4,8,9,1]
print(ma_liste)
ma_liste.append(30)
print(ma_liste)

# Ajouter un élément à un index précis
ma_liste = [1,2,3,"toto", True,["a",False,25]]
print(ma_liste)
ma_liste.insert(2,"tutu") # on note l'index puis l'élément à rajouter
print(ma_liste)

# Ajouter une liste à la suite d'une autre
ma_liste.extend(ma_liste2)
print(ma_liste)

# Retirer un élément à une liste
ma_liste.remove(2) # Supprime le 1er élément demandé entre parenthèses. Si plusieurs éléments identiques, il n'enlève que le 1er
print(ma_liste)
ma_liste.pop(4) # Supprime un élément par rapport à son Index (ici le True)
print(ma_liste)

ma_liste[4].pop(1) # Supprime l'element à l'index 1 dans la liste à l'élément à l'index 4
print(ma_liste)

# pour parcourir une liste
for element in ma_liste:
    print(element)

# Vérifier le type d'une variable
ma_variable = "42"
print(type(ma_variable))
print(type(ma_liste))