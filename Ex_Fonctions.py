#On définit la fonction comme suit:
def hello_world():
    #print("Hello World !!!")
    return "Hello World !!!"

#on appelle la fonction
#hello_world()

# On stocke le return de ma fonction dans ma_variable
ma_variable = hello_world()
print(f"Valeur de ma_variable {ma_variable}")

#__________________________________________________________________________________

#On définit la foncction "dire_bonjour" avec deux paramètres (nom, prénom)
def dire_bonjour(nom, prenom):
    print (f"Bonjour {nom} {prenom}") 

dire_bonjour("Toto", "Tata") #On appelle la fonction avec des paramètres choisis
dire_bonjour("Tutu", "Titi")

#__________________________________________________________________________________

#On définit la foncction "dire_bonjour" avec deux paramètres (nom, prénom)
def dire_bonjour(nom: str, prenom):
    print (f"Bonjour {nom.capitalize()} {prenom}") 

dire_bonjour("toto", "tata") #On appelle la fonction avec des paramètres choisis
dire_bonjour("tutu", "titi")

#__________________________________________________________________________________

def say_hello(name = "JPierre"): # On définit la fonction avec une variable par défaut "JPierre"
    print(f"Hello {name}")

say_hello() # On affiche le résultat de la fonction avec le paramètre par défaut "JPierre"
say_hello("Antonio") # On affiche le résultat de la fonction avec un autre paramètre

#__________________________________________________________________________________

def nombre():
    a = 2
    return a

a=nombre()
print (a)

#__________________________________________________________________________________

def nombre():
    d = 2*5
    e = 3*8
    f = 4*4
    return d, e, f

lettre_d, lettre_e, lettre_f = nombre()
print(lettre_d)
print(lettre_e)
print(lettre_f)

#__________________________________________________________________________________
#Fonction qui va demander un nombre et si nombre est pair, il affiche OUI sinon il affiche NON
def affiche_oui_si_pair(nombre):
#Structure conditionnelle If
    if nombre % 2 == 0: #Si nombre est divisible par 2 sans reste alors c'est oui
        print ("Oui")
    else:
        print ("Non")

nb = int(input("Veuillez saisir un nombre :" )) # on demande à l'utilisateur de rentrer un nombre et on le stocke dans nb
affiche_oui_si_pair(nb) # On appelle la fonction avec la valeur stockée dans la dans nb et transmis à nombre

#__________________________________________________________________________________
#Fonction qui va demander un nombre et si nombre est pair, il affiche OUI sinon il affiche NON
def retourne_oui_si_pair(nombre):
#Structure conditionnelle If
    if nombre % 2 == 0: #Si nombre est divisible par 2 sans reste alors c'est oui
        return "Oui" #Return --> à ce niveau la fonction s'arrête à ce return si le nbre est pair
    else:
        return "Non"

result = retourne_oui_si_pair(nb) # on demande à l'utilisateur de rentrer un nombre et on le stocke dans result
print(f"Retourne_oui_si_pair : {result}") # On affiche la phrase entre "" et on appelle le nombre stocké dans 'result'