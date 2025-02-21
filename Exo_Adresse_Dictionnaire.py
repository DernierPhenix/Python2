# adresse = []
# Fonction pour ajouter une adresse
def ajouter_adresse(adresses : list):
    #print("Ajoute une nouvelle adresse en demandant les informations à l'utilisateur.")
    """Ajoute une nouvelle adresse en demandant les informations à l'utilisateur."""
    print("\n=== AJOUTER UNE ADRESSE ===")
    numero = input("Veuillez entrer le numéro de voie SVP : ")
    complement = input("Veuillez entrer le complément d'adresse SVP : ")
    voie = input("Veuillez entrer l'intitulé de voie SVP : ")
    code_postal = input("Veuillez entrer le code postal SVP : ")
    commune = input("Veuillez entrer la commune SVP : ")
    


 # Création d'un dictionnaire pour l'adresse
    adresse = {
        "Numéro de voie": numero,
        "Complément": complement,
        "Intitulé de voie": voie,
        "Code postal": code_postal,
        "Commune": commune
        
    }
    adresses.append(adresse) # On ajoute une adresse dans la variable 'adresse' en dernière position
    print("Adresse ajoutée avec succès !")
    
 # Fonction pour éditer une adresse  
def editer_adresse(adresses):
    #print("Permet d'éditer une adresse existante en modifiant un champ spécifique.")
    """Permet d'éditer une adresse existante en modifiant un champ spécifique."""
    afficher_adresses(adresses)
    index = int(input("Veuillez entrer le numéro de l'adresse à éditer : ")) - 1
    
    # Vérification que l'index est valide
    if 0 <= index < len(adresses):
        champ = input("Quel champ voulez-vous modifier ? (Numéro de voie, Complément, Intitulé de voie, Code postal, Commune) : ")
        if champ in adresses[index]:
            nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {champ} : ")
            adresses[index][champ] = nouvelle_valeur
            print("Adresse mise à jour avec succès !")
        else:
            print("Champ invalide.")
    else:
        print("Index invalide.")

# Fonction pour supprimer une adresse
def supprimer_adresse(adresses):
    #print("Permet de supprimer une adresse existante en sélectionnant son index.")
    """Permet de supprimer une adresse existante en sélectionnant son index."""
    afficher_adresses(adresses)
    index = int(input("Veuillez entrer le numéro de l'adresse à supprimer : ")) - 1
    
    # Vérification de la validité de l'index
    if 0 <= index < len(adresses):
        del adresses[index]
        print("Adresse supprimée avec succès !")
    else:
        print("Index invalide.")

# Fonction pour afficher une adresse
def afficher_adresses(adresses):
    #print("Affiche toutes les adresses enregistrées sous un format lisible.")
    """Affiche toutes les adresses enregistrées sous un format lisible."""
    print("\n=== LISTE DES ADRESSES ===")
    if not adresses:
        print("Aucune adresse enregistrée.")
        return
    
    for i, adresse in enumerate(adresses):
        print(f"Adresse {i+1} :")
        for cle, valeur in adresse.items():
            print(f"  {cle}: {valeur}")
        print("-" * 20)

def menu():
    adresse = []
    while True:
         print("""=== MENU PRINCIPAL ===
1- Voir les adresses
2- Ajouter une adresse
3- Éditer une adresse
4- Supprimer une adresse
5- Quitter le programme
""")
         choix_menu = input("Votre choix : ")
         match choix_menu:
             case "1":
                afficher_adresses(adresse)
             case "2":
                 ajouter_adresse(adresse)
             case "3":
                 editer_adresse(adresse)
             case "4":
                 supprimer_adresse(adresse)
             case "5":
                 exit()
             case _:
                 print("Choix invalide\n")

# def afficher_menu():
#     """Affiche le menu principal permettant à l'utilisateur de choisir une action."""
#     print("\n=== MENU PRINCIPAL ===")
#     print("1. Voir les adresses")
#     print("2. Ajouter une adresse")
#     print("3. Éditer une adresse")
#     print("4. Supprimer une adresse")
#     print("5. Quitter le programme")
#     return input("Votre choix : ")

adresse = menu()
