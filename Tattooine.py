participants = ["Anakin Skywalker","Gasgano","Aldar Beedo","Ebe E. Endocott","Elan Mak","Boles Roor","Ben Quadinaros","MawhonicRatts Tyerell"]

#Le premier est "supprimé temporairement" avec pop et remis en dernier avec append
def panne_moteur(participants :list):
    premier = participants.pop(0)
    participants.append(premier)
    return participants

#le premier et le second change de position. On utilise une variable temporaire pour stocker le 1er
#on alterne les participants grâce à leur valeur.


def passe_en_tete(participants : list):
    temp = participants[0]
    participants[0] = participants[1]
    participants[1] = temp
    return participants



# On alterne les deux derniers participants en fonction de leur valeur
def sauve_honneur(participants : list):
    participants[-1], participants[-2] = participants[-2], participants[-1]
    return participants



# le 1er est touché par un tir de blaster et devient dernier
def tir_blaster(participants : list):
    return participants.pop(0)



# Le participant touché dépasse l'avant-dernier.
def retour_inattendu(participants : list, participant_touche): 
    participants.append(participant_touche)
    return participants

def affichage_course(participants: list):
    affichage = ""
    for participant in participants:
        index = participants.index(participant)
        if index == 0:
            affichage += (f"1er - {participant} ")
        else:
            affichage += (f"{index + 1}ème - {participant} ")

    print(affichage)


affichage_course(panne_moteur(participants))
affichage_course(passe_en_tete(participants))
affichage_course(sauve_honneur(participants))
participant_blasterise = tir_blaster(participants)
affichage_course(retour_inattendu(participants, participant_blasterise))
affichage_course(participants)
