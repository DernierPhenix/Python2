# chaine = str.lower(input("Veuillez entrer une chaîne d'ADN : "))
# sequence = str.lower(input("Veuillez entrer la séquence d'ADN : "))

# def verification_adn(chaine):

#     for i in chaine:
#         if i == "a" or i == "t" or i == "c" or i == "g":
#             chaine = True
#             print("la chaine est à True")
#         else:
#             chaine = False
#             print("la chaine est à false")
#         return chaine


# verification_adn(chaine)

#chaine = str(input("Veuillez entrer une chaîne d'ADN : "))
#sequence = str(input("Veuillez entrer la séquence d'ADN : "))

# 1. Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide

def verification_adn(chaine: str):
    #print(f"ma chaine testée est : {chaine}")
    for i in chaine: #pour i dans chaîne
        #print(f"Je vérifie la lettre {i}")
        if i not in "atcg": #si 'i' ne contient pas les caractères 'atcg"
           # print(f"Oups, cette lettre ne convient pas ... {i}")
            return False # retourne False
    return True #retourne True, ici on est en dehors du If et dans le For

# 2. Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
# chaîne d’ADN valide sous forme de chaîne

# def saisie_adn(question):
#     ma_chaine = input(question)
#     if verification_adn(ma_chaine):
#         print("saisie valide")
#         return ma_chaine
#     print (" Erreur de saisie !! ")

def saisie_adn(question):
    ma_chaine = input(question)
    while not verification_adn(ma_chaine): #tant que vérificaction_adn ne convient pas
        print (" Erreur de saisie !! ") # on affiche "erreur de saisie"
        ma_chaine = input(question) # on repose la question

# saisie_adn("Veuillez entrer une chaîne d'ADN contenant a, t, c, g :")

# 3. Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
# séquence d’ADN Elle renverra le nombre d’occurrences de la séquence dans la chaîne

def proportion(chaine: str,sequence: str):
    print(chaine)
    print (sequence)
    return chaine.count(sequence) # On compte le nombre de séquences présentes dans la chaîne

# print(proportion("toto", "to")) -->Exemple de print pour la proportion
# print(proportion("tata", "e")) --> Exemple de print pour la proportion
# print(verification_adn("atcgz"))
# print(verification_adn("gcta"))

# Bonus : Calcul du pourcentage
def poucentage_sequence(chaine : str, sequence: str, proportion: str):
    return round(proportion * len(sequence) * 100 / len(chaine),2)


chaine_adn = saisie_adn("Veuillez entrer une chaîne d'ADN contenant a, t, c, g : ")
sequence_adn = saisie_adn("Veuillez entrer la séquence d'ADN : ")

print (f"Il y a la séquence {sequence_adn} {proportion(chaine_adn,sequence_adn)} fois dans la chaine : {chaine_adn}")
print (f"Il y a la séquence {sequence_adn} {poucentage_sequence(chaine_adn,sequence_adn,proportion(chaine_adn, sequence_adn))} % dans la chaine : {chaine_adn}")