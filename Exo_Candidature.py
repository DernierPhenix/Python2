age = int(input("Quel est votre âge ? : "))
salaire = int(input ("Quel salaire souhaitez-vous ?"))
experience = int(input("Combien d'années d'expérience avez-vous ?"))

profil =True
    
if age < 30 : 
    print("Votre âge ne correspond pas à nos critères")
    profil = False
if salaire > 40000 : 
    print("le montant de votre salaire ne correspond pas à nos critères")
    profil = False
if experience <=5 :
    print("Vous n'avez pas assez d'expérience")
    profil = False
if (profil) : 
    print("Vous répondez à toutes les conditions !")