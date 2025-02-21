# Ecrire un programme qui demande le prénom et le nom et affiche le Message 
# "Bonjour M. ou Mme" avecles réponse dont la 1ère lettre est en majuscule.

nom = input("Quel est votre Nom ? ").capitalize()
#nom = nom.capitalize()

prenom = input("Quel est votre prénom ? ").capitalize()
#prenom = prenom.capitalize()

print("Bonjour M.ou Mme",prenom, nom)
