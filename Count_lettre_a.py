def compter_lettre_a(lettre_a : str):
    
    x = lettre_a.count("a")
    return x

lettre_a = str(input("Entre un mot : "))
    
print(f"Le mot contient {compter_lettre_a(lettre_a)} a")