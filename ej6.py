from decimal import *


def ej6(dig):
    getcontext().prec = dig
    # se especifica los digitos requeridos
    return sum(1 / Decimal(16) ** k *
               # Se usa ** para indicar potencia
               (Decimal(4) / (8 * k + 1) -
                Decimal(2) / (8 * k + 4) -
                Decimal(1) / (8 * k + 5) -
                Decimal(1) / (8 * k + 6)) for k in range(dig))
    # Desde k=0 hasta k=dig con paso de 1


decCalc = int((input("Cuantos decimales de pi desea calcular: ")))
print(ej6(decCalc + 1))
# Si especifico 2 decimales la formula itera hasta 1 elemento menos,
# por lo que se le suma 1 digito extra a los decimales
