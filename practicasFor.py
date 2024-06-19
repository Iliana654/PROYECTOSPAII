#Suma de números pares

suma = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        suma += numero

print("La suma de los números pares del 1 al 100 es:", suma)

n = int(input("Ingresa un número entero positivo: "))

if n <= 0:
    print("El número debe ser positivo.")
else:
    # Inicializar un contador
    contador = 1
    
    # Utilizar un bucle while para imprimir los números desde 1 hasta n
    while contador <= n:
        print(contador)
        contador += 1

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar una variable para almacenar el intento del usuario
intento = 0

# Utilizar un bucle while para solicitar al usuario que adivine el número
while True:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Adivina el número (entre 1 y 100): "))
    
    # Verificar si el intento es correcto
    if intento == numero_secreto:
        print("¡Felicitaciones! ¡Has adivinado el número.")
        break  # Salir del bucle while
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    else:
        print("El número secreto es menor. Intenta nuevamente.")


