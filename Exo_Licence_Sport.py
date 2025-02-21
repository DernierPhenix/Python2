age = int(input("Entrer l'âge de votre enfant ? : "))

if age < 3 :
    print("Votre enfant est trop jeune")
elif age >= 3 and age <= 6 :
    print("La catégorie de votre enfant est Baby") 
elif age >= 7 and age <= 8 :
    print("La catégorie de votre enfant est poussin")
elif age >= 9 and age <= 10 :
    print("La catégorie de votre enfant est Pupille")
elif age >= 11 and age <= 12 :
    print("La catégorie de votre enfant est Minime")
else : 
    print('La catégorie de votre enfant est Cadet')