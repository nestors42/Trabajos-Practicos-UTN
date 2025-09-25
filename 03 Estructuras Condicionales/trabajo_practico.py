'''
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
'''
edad = int(input('Ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad')

'''
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. 
'''
nota = float(input('Ingrese su nota: '))
if nota >= 6 :
    print('Aprobado')
else:
    print('desaprobado')

'''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. 
'''
edad_usuario = int(input('Ingrese su edad: '))
if edad_usuario <= 12:
    print('Niño/a')
elif edad_usuario >= 12 and edad_usuario < 18:
    print('Adolecente')
elif edad_usuario >= 18 and edad_usuario < 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')

'''
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.
'''
contraseña = input('Ingrese una contraseña (entre 8 y 14 caracteres): ')
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')
'''
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
'''
from statistics import mode, median, mean;
import random;
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f'Moda: {moda}, Mediana: {mediana}, Media: {media}')
if media > mediana and mediana > moda:
    print('Sesgo positivo o a la derecha') 
elif media < mediana and mediana < moda:
    print('Sesgo negativo o a la izquierda')   
elif media == mediana and mediana == moda:
    print('Sin sesgo')

'''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. 
'''
frase = input ('Ungrese una palabra o frase: ')
if frase[-1].lower() in 'a' or frase[-1].lower() in 'e' or frase[-1].lower() in 'i' or frase[-1].lower() in 'o' or frase[-1].lower() in 'u':
    print(frase + '!')
else:
    print(frase)

'''
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''
nombre_usuario = input('Ingrese su nombre: ')
opcion = int(input('ingrese 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: '))
if opcion == 1:
    print(nombre_usuario.upper())
elif opcion == 2:
    print(nombre_usuario.lower())
elif opcion == 3:
    print(nombre_usuario.title())
else:
    print('Elije una opcion valida')

'''
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
'''
terremoto = float(input('Ingrese la magnitud del terremoto: '))
if terremoto < 3:
    print('Muy leve (imperceptible)')
elif terremoto >= 3 and terremoto < 4:
    print('Leve (Ligeramente perceptible)')
elif terremoto >= 4 and terremoto < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif terremoto >= 5 and terremoto < 6:
    print('Fuerte (puede causar daños en estructuras debiles)')
elif terremoto >= 6 and terremoto < 7:
    print('Muy Fuerte (puede causar daños significativos)')
elif terremoto >= 7:
    print('Extremo (puede causar graves daños a gran escala)')

'''
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
Desde el 21 de diciembre hasta el 20 de marzo (incluidos): emisferio norte invierno, emisferio sur verano.
Desde el 21 de marzo hasta el 20 de junio (incluidos) emisferio norte primavera, emisferio sur otoño.
Desde el 21 de junio hasta el 20 de septiembre (incluidos): emisferio norte verano, emisferio sur invierno.
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) emisferio norte otoño, emisferio sur primavera.
'''
dia = int(input('ingrese el dia: '))
mes = int(input('ingrese el mes (en numero): '))
emisferio = input('ingrese su emisferio (Norte/Sur): ').lower()
if emisferio == 'norte':
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print('La estacion es: Invierno')
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print('La estacion es: Primavera')
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print('La estacion es: Verano')
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
        print('La estacion es: Otoño')
elif emisferio == 'sur':
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print('La estacion es: Verano')
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print('Otoño')
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print('La estacion es: Invierno')
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
        print('La estacion es: Primavera')
        