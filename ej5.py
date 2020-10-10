valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
if valor2 == pow(valor1,2):
  print("El Segundo valor es el cuadrado EXACTO del primero")
else:
  if valor2<pow(valor1,2):
    print("El Segundo valor es menor que el cuadrado del primero")
  else:
    print("El Segundo valor es mayor que el cuadrado del primero")