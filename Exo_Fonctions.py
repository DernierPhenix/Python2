def bonjour(prenom, nom):
    print(f"Bonjour, {prenom} {nom}")

bonjour("JPierre","FLEURY")

#Autre Solution :
def bonjour(prenom :str = "John", nom: str ="Doe"): #on a les paramètres "prenom et nom" le type "str" et une valeur par défaut
    return prenom + " " + nom
    
prenom1 = bonjour("JPierre","FLEURY")#On stocke les valeurs dans prenom1
prenom2 = bonjour()# Va appeler les valeurs par défaut

print (prenom1)
print(prenom2)

# Refactorisation de code au-dessus :
def bonjour(prenom :str = "John", nom: str ="Doe") ->str: #on a les paramètres "prenom et nom" le type "str" et une valeur par défaut - on précise le type en sortieavec '->str'
    return prenom + " " + nom
    
#prenom1 = bonjour("JPierre","FLEURY")#On stocke les valeurs dans prenom1
#prenom2 = bonjour()# Va appeler les valeurs par défaut

print (bonjour("JPierre","FLEURY"))
print(bonjour())

#--------------------------------------------------------------------------
def soustraction(nbre_a,nbre_b):
    result = nbre_a -nbre_b
    print(f"Je soustrais {nbre_a} & {nbre_b} et le résultat est {result}")

nbre_a = int(input("Entrer le premier nombre : "))
nbre_b = int(input("Entrer le deuxième nombre : "))



soustraction(nbre_a,nbre_b)

#--------------------------------------------------------------------------
#Autre Solution Soustraction
def soustraction(nb1,nb2):
    print(f"Je soustrais {nb1} & {nb2} et le résultat est {nb1-nb2}")
#    result = nb1 -nb2
    return nb1 - nb2
    
nb1 = int(input("Entrer le premier nombre : "))
nb2 = int(input("Entrer le deuxième nombre : "))

result = soustraction(nb1,nb2)
print (result)

#--------------------------------------------------------------------------
def quelle_heure(heure : str ="12h00"):
    print("il est",heure)

quelle_heure()
quelle_heure("14h00")

#--------------------------------------------------------------------------
def compter_lettre_a(lettre_a : str):
    cpt = 0
    for i in lettre_a:
        if i == "a":
            cpt += 1
    return cpt

lettre_a = str(input("Entre un mot : "))

print(f"Le mot contient {compter_lettre_a(lettre_a)} a")

#Même exercice mais avec un count -----------------------------------------

def compter_lettre_a(lettre_a : str):
    
    x = lettre_a.count("a")
    return x

lettre_a = str(input("Entre un mot : "))
    
print(f"Le mot contient {compter_lettre_a(lettre_a)} a")

#--------------------------------------------------------------------------
chaine = str(input("Veuillez entrer une chaîne d'ADN : "))
sequence = str(input("Veuillez entrer la séquence d'ADN : "))
# Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide

def verification_adn(chaine: str):
    for i in chaine: #pour i dans chaîne
        if i not in "atcg": #si 'i' ne contient pas les caractères 'atcg"
            return False # retourne False
    return True #retourne True, ici on est en dehors du If et dans le For


print(verification_adn("atcgz"))
print(verification_adn("gcta"))