max_value = None

for i in range (1,7):
    #value = int(input("Entrer le chiffre n°:",i,":" ))
    value = int(input(f"Entrer le chiffre n°{i}: "))

    if (max_value ==None or max_value <= value):
        max_value = value

print("La valeur maximale est : ", max_value)