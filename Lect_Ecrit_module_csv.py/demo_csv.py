import csv

# Lecture
# fichier = open("Lect_Ecrit_module_csv.py/test.csv", "rt")
# reader = csv.reader(fichier, delimiter = ";")
# for row in reader : 
#     print(row)
# fichier.close()

# Écriture
# fichier2 = open("Lect_Ecrit_module_csv.py/test.csv", "wt", newline="")
# writer_csv = csv.writer(fichier2,delimiter=";")
# writer_csv.writerow(["titi",66,"au pif"])
# writer_csv.writerow(["toto",88,"Lille"])
# writer_csv.writerow(["tata",25,"Paris"])
# fichier2.close()

with open("Lect_Ecrit_module_csv.py/test.csv",mode='a',encoding="UTF-8",newline="") as fichier:
    writer = csv.writer(fichier,delimiter=";")
    writer.writerow(["christophe",25,"Toulouse"])