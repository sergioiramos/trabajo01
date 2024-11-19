intervalo1 = int(input("Dime el primer numero del intervalo"))
intervalo2 = int(input("Dime el segundo numero del intervalo"))
if intervalo2 > intervalo1:
    for valor in range(intervalo1,intervalo2+1):
        if valor % 2 == 0:
            print (valor)
else:
    print("Segundo numero menor que elprimero")

