copie = int(input("Entrer le nombre de copies souhaitées : "))

if copie < 10 :
    print("le prix est de :",round(copie*0.5,2),"€")
elif copie >= 10 and copie <= 20 :
    print("le prix est de :",round(copie*0.4,2),"€")
else :
    print("le prix est de :",round(copie*0.3,2),"€")

