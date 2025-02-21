import os

path = "Demo_fichier/fichier.txt"

# Vérifier si le fichier existe.

# if not os.path.exists(path):
#     fichier = open(path, "w")
#     fichier.write ("Test")
#     fichier.close()
# else:
#     fichier = open(path, "r")
#     contenu = fichier.read()
#     print (f"Contenu du fichier : {contenu}")
#     fichier.close()

if not os.path.exists(path):
    with open(path,"w") as fichier:
        fichier.write("2nd Test")
else:
    with open(path, "r") as fichier:
        contenu = fichier.read()
        print (f"Contenu du fichier : {contenu}")
        