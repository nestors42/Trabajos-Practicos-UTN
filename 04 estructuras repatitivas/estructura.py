'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''
for numero in range(0,101):
    print(numero)

'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.
'''
numero_user = input("Introduce un número entero: ")
numero_user = str(numero_user)
print(f'el numero ingresado {numero_user} tiene {len(numero_user)} digitos')


'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. 
'''
numero1 = int(input('introduce el primer numero: '))
numero2 = int(input('introduce el segundo numero: '))
suma = 0
contador = 0
for contador in range(numero1, numero2,1):
    print(f'la suma entre {suma} + {contador} = {suma + contador}')
    suma = suma + contador
print(f'la suma total entre {numero1} y {numero2} es: {suma}')

'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 
'''


suma = 0

while True:
    numero = int(input('Introduce un número (0 para terminar): '))
    if numero == 0:
        break
    print(f'{suma} + {numero} = {suma + numero}')
    suma = suma + numero

print(f'La suma total es: {suma}')

'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''
import random
numero_aleatorio = random.randint(0,9)
intentos_usuarios = 6

numero_entrada = int(input('adivina el numero secreto, la pista es que está entre el 0 y el 9: '))
print(numero_aleatorio)

for intentos in range(intentos_usuarios):
    if numero_entrada < 0 or numero_entrada > 9:
        print('el numero que ingresas, debe ser entre el 0 y el 9')
        numero_entrada = int(input('intenta otra vez: '))
    if numero_entrada == numero_aleatorio:
        print('adivinaste el numero secreto')
        break
    elif numero_entrada < numero_aleatorio:
        print('el numero secreto es mayor')
        numero_entrada = int(input('intentalo de nuevo: '))
    elif numero_entrada > numero_aleatorio:
        print('el numero secreto es menor')
        numero_entrada = int(input('intenta otra vez: '))
else:
    print('perdiste, el numero secreto era: ', numero_aleatorio)
    
        
'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 
'''
for numeros_pares in range(101, -1, -1):
    if numeros_pares % 2 == 0:
        print(numeros_pares)

'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. 
'''
entrada_usuario1 = int(input('introduce un numero entero positivo: '))
numero_fijo = 0
suma = 0
for contador1 in range(numero_fijo, entrada_usuario1 + 1, 1):
    print(f'{suma} + {contador1} = {suma + contador1}')
    suma = suma + contador1
print(f'La suma total es: {suma}')


'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
'''

cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for contador2 in range(cantidad):
    numero_usuario2 = int(input(f'Ingresa el número: '))
    contador2 = contador2 + 1
    if numero_usuario2 % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if numero_usuario2 > 0:
        positivos = positivos + 1
    elif numero_usuario2 < 0:
        negativos = negativos + 1

print(f'Cantidad de números pares: {pares}')
print(f'Cantidad de números impares: {impares}')
print(f'Cantidad de números positivos: {positivos}')
print(f'Cantidad de números negativos: {negativos}')

'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).
'''
cantidad_a_contar = 100
suma = 0
for contador3 in range(cantidad_a_contar):
    numero_usuario4 = int(input('ingresa un numero entero: '))
    suma = suma + numero_usuario4
media = suma / cantidad_a_contar
print(f'la media de los numeros ingresados es: {media}')

'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''
numero_usuario5 = int(input('ingresa un numero entero positivo: '))
numero_usuario5 = str(numero_usuario5)
numero_invertido = numero_usuario5[::-1]
print(f'el numero invertido es: {numero_invertido}')