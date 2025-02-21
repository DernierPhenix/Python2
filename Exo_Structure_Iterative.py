for _ in range(0, 10):
    print("je me répète ! ")

for var in range(0, 10):
    print(var,"je me répète ! ")

for element in [0, 1, 2, 3, 4, 5] : 
    print (element)

for item in range (1, 11):
    print("Je suis l'itération n°: ", item)

while True:
   valeur = input("Saisir STOP pour arrêter le programme : ")
if valeur == "STOP":
    break
elif valeur.upper =="Stop":
    print("EN UPPERCASE")
    continue
else: 
    pass # ce bloc est inutile, masse ne fait rien

cpt = 0 
while cpt < 6 :
    print("Mon compteur est à : ",cpt)
    cpt += 1

entry = None
while entry!= "ok":
    entry = input("Entrez ok : ")