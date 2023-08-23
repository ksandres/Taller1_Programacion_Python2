print("Ingrese los valores que desea dividir y calcular su módulo o residuo:")
a = int(input())
b = int(input())

div = a // b
mod = a % b

if mod == 0:
    print("El residuo es", mod, "es exacta la división", div)
else:
    print("El residuo", mod, "no es exacta la división", div)
