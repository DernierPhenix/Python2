mon_tuple = (1,2,3,4)

print(f"Mon joli tuple : {mon_tuple}")

# Accéder à un élément
print(f"Premier élément de mon tuple : {mon_tuple[0]}")
print(f"Premier élément de mon tuple : {mon_tuple[3]}")
print(f"Premier élément de mon tuple : {mon_tuple[-1]}")

# unpacking
a, b, c, d = mon_tuple
print(f"Déballage a = {a}")
print(f"Déballage d = {d}")
print(f"Déballage b = {b}")
print(f"Déballage c = {c}")
print(f"déballage a = {a} b = {b} c = {c}") # Affiche uniquement les éléments demandés


def recuperer_nombre(nombre):
    return nombre, nombre * 2 # tuplepacking --> on utilise un tuple pour tout renvoyer

print(recuperer_nombre(3)) # Affiche le résultat entre parenthèses (= tuple)

#-----------------------------------------------------------------------------------
valeur1, valeur2 = recuperer_nombre(2)
print (f"valeur 1 : {valeur1} et valeur 2 : {valeur2}")