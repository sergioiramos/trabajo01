palabra = input("Dime una palabra: ")
#vocales = {"a", "e", "i", "o", "u"}
vocales = "aeiouAEIOU"
contador = 0

for i in palabra:
    if i in vocales:
       contador +=1
    else:
        continue

print (contador) 
