import math

radio = float(input("Ingrese el radio de la base del cono: "))
altura = float(input("Ingrese la altura cono: "))
g = math.sqrt(pow(radio, 2) + pow(altura, 2))
print("La generatriz es:", g)
area_lateral = math.pi * radio * g
print("El Area Lateral del cono es:", area_lateral)