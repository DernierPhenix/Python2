# Exercice
# 1. Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant à l'utilisateur
#  d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
#  - saisie avant la saisie de notes
#  - permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes.
# 2. Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant
#  d'avoir la note max, la note min ainsi que la moyenne (possible de faire un menu pour choisir)

def saisie_nb_notes() : 
    nombre = int(input("Combien de notes voulez-vous saisir ?"))
    liste_notes = []
    for i in range(0,nombre):
        note = float(input(f"Entrer la note n°{i+1} : "))
        liste_notes.append(note)
    return liste_notes

# print(saisie_nb_notes()) <-- test de la fonction 'saisie_nb_notes'

def saisie_arret_note() : 
    liste_notes =[]
    while True :
        note = float(input("Saisir une note : "))
        if note >= 0 and note <= 20:
            liste_notes.append(note)
        else:
            print("Erreur de note, on arrête la saisie.")
            break
        return liste_notes

#print(saisie_arret_note())

def menu():
    while True:
        print("Bienvenue")
        print("[1] Pour entrer un nombre de notes connues\n[2] Pour continuer la saisie jusqu'à une note négative")
        choix = input("Votre choix : ")
        match choix:
            case "1":
                return saisie_nb_notes()
            case"2":
                return saisie_arret_note()
            case _ :
                print("Choix invalide")

#print(menu())

def menu_min_max_moy(listes_notes): 
    while True : 
        print("""Faites votre choix : 
1 - Afficher la note maximale
2 - Afficher la note minimale
3 - Afficher la moyenne
4 - Quitter le programme
          """)
        choix_menu = input("Votre choix : ")
        match choix_menu:
            case "1":
                print(max(listes_notes))
            case "2":
                print(min(listes_notes))
            case "3": 
                print(sum(listes_notes)/len(listes_notes))
            case "4": 
                exit()
            case _:
                print("Choix invalide")

menu_min_max_moy(menu())