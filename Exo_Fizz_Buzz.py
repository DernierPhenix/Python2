nb = int(input("Entrez un nombre pour definir la taille du FizzBuzz : "))
#Structure itérative For
for i in range(0,nb+1):
    #Structure Conditionnelle If
    if (i%3==0 and i%5==0 ):
        print ("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)