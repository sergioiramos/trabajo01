from geometria.area import area_cuadrado, area_circulo
from geometria.perimetro import perimetro_cuadrado, perimetro_circulo

lado = int(input("Introduce el lado del cuadrado: "))
radio = int(input("Introduce el radio del circulo: "))

print(area_cuadrado(lado))
print(area_circulo(radio))
print(perimetro_cuadrado(lado))
print(perimetro_circulo(radio))


