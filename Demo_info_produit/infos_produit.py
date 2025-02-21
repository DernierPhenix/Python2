import csv

titre = input("Quel est le nom de votre produit ? : ")
prix = float(input("Quel est le prix du produit . : "))
stock = int(input("Quelle quantité avez vous en stock de ce produit ? : "))

with open("Demo_info_produit/produit.csv",mode='a',encoding="UTF-8",newline="") as fichier:
    writer = csv.writer(fichier,delimiter=";")
    writer.writerow([titre,prix,stock])