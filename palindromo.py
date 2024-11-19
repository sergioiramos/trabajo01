def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
