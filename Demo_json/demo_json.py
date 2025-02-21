import json, os

path = "Demo_json/data.json"

if os.path.exists(path):
    with open(path,'r',encoding="UTF-8") as fichier:
        # Pour charger un fichier, il nous faut la méthode .load()
        data = json.load(fichier)
        print(data)
else:
    with open(path,'w',encoding="UTF-8") as fichier:
        json.dump({"Prénom ": "JPierre","Nom ": "FLEURY"},fichier, indent=4,ensure_ascii=False)
        
mon_dict_str = json.dumps(data,indent=4,ensure_ascii=False)
print("Je récupère mes datas avec DUMPS, j'obtiens une chaîne de caractères")
print(type(mon_dict_str))
print(mon_dict_str)

data_dict = json.loads(mon_dict_str)
print("À partir de cette chaîne de caractères, j'obtiens un dictionnaire avec LOADS")
print(type(data_dict))
print(data_dict)