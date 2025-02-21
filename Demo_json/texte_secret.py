import os

path = "Demo_json/secret.txt"

def lire_secret(path): 
    file = open(path, "r", encoding="UTF-8")
    texte_fichier = file.read()
    file.closed()
    return texte_fichier

def voir_secret(path): 
    file = open(path, "r", encoding="UTF-8")
    texte_fichier = file.read()
    file.closed()
    return texte_fichier


def menu():
    secret = []
    while True:
         print("""=== MENU PRINCIPAL ===
1- Voir le secret
2- Modifier le secret
3- Quitter le programme
""")
         choix_menu = input("Votre choix : ")
         match choix_menu:
             case "1":
                voir_secret(secret)
             case "2":
                 modifier_secret(secret)
             case "3":
                 quitter(secret)
             case _:
                print("Choix invalide\n")
                
choix = input("Veuiller entrer votre choix : ")

print(menu())