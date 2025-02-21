mon_dict = {"k1": 'valeur un', "k2": 25443, "k3": 3.14, "k4": {1: 'blabla'}}
print(mon_dict)
print(mon_dict['k3']) # 3.14
print(mon_dict['k4'][1]) # blabla
print(mon_dict.values()) # ['valeur un', 25443, 3.14, {&: "blabla"}]
print(mon_dict.keys()) # ["k1", "k2", "k3", "k4"]
print(mon_dict.items()) # {"k1": 'valeur un', "k2": 25443, "k3": 3.14, "k4": {1: 'blabla'}}
for key, value in mon_dict.items():
    print(f"key : {key}, value : {value}") # key : k1, value : valeur un ect..