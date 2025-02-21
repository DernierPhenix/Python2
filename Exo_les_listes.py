import random
# Écrire un algorithme qui déclare et stocke dans un tableau 10
# chiffres, puis affiche le 9éme élément de ma liste.
ma_liste1 = []
for i in range (10):
    nbre = random.randint(1,100)
    ma_liste1.append(nbre)

print (ma_liste1[8])


#--------------------------------------------------------------------------

#Autre solution exercice du dessus
ma_liste = [0,1,2,3,4,5,6,7,"tutu",9 ,10, "test", "élément", True]
print(ma_liste)
print(ma_liste[8])

# Écrire un algorithme permettant de saisir 15 notes et de les afficher.
# note = input("Veuillez entrer une note : ")
note = []
for i in range(1,11):
    note.append(i) == int(input(f"Veuillez entrer la note N°{i} : "))

print(note)
print(len(ma_liste))

#--------------------------------------------------------------------------

