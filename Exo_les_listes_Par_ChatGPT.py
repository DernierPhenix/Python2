# Exercice
# 1. Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant à l'utilisateur
#  d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
#  - saisie avant la saisie de notes
#  - permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes.
# 2. Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant
#  d'avoir la note max, la note min ainsi que la moyenne (possible de faire un menu pour choisir)

def saisir_notes_mode_1():
    # Mode où l'utilisateur entre d'abord le nombre de notes
    try:
        nombre_notes = int(input("Combien de notes voulez-vous entrer ? "))
        notes = []
        for i in range(nombre_notes):
            note = float(input(f"Entrez la note {i + 1} : "))
            notes.append(note)
        return notes
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return []

def saisir_notes_mode_2():
    # Mode permissif où l'utilisateur entre des notes jusqu'à une note négative
    notes = []
    while True:
        try:
            note = float(input("Entrez une note (ou une note négative pour arrêter) : "))
            if note < 0:
                break
            notes.append(note)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return notes

def afficher_stats(notes):
    if notes:
        note_max = max(notes)
        note_min = min(notes)
        moyenne = sum(notes) / len(notes)
        print(f"Note maximale : {note_max}")
        print(f"Note minimale : {note_min}")
        print(f"Moyenne des notes : {moyenne}")
    else:
        print("Aucune note saisie.")

def menu():
    print("Choisissez un mode de saisie des notes :")
    print("1. Saisie avec un nombre défini de notes")
    print("2. Saisie permissive (note négative pour arrêter)")
    
    choix = input("Entrez le numéro de votre choix : ")
    
    if choix == '1':
        notes = saisir_notes_mode_1()
    elif choix == '2':
        notes = saisir_notes_mode_2()
    else:
        print("Choix invalide.")
        return
    
    afficher_stats(notes)

# Lancer le programme
menu()
