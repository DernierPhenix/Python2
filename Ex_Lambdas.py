def add(a,b):
    return a + b
print("Avec la fonction")
print(add(2,3))

#Ligne du dessus en Lambda
add_lambda = lambda a,b: a+ b

print("avec la lambda")
print(add_lambda(3,3))

#map
nums = [1,2,3,4]
result =list(map(lambda x: x*2,nums)) # On multiplie par 2 chaque élément de la variable 'nums'

print (result)

#filter --> Filtrer des éléments
num = [1,2,3,4,5,6]
results = list(filter(lambda x: x % 2 ==0, num)) # on affiche les nombres divisibles par 2, les pairs
results2 =  list(filter(lambda x: x  == 5, num)) # on affiche le nombre égale à 5 

print(results)
print(results2)