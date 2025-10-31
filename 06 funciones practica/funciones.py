'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal.
'''
def imprimir_hola_mundo():
    print("hola mundo!")

imprimir_hola_mundo()

'''
 Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario.
'''


nombre_user = input("ingrese su nombre: ")

def saludar_usuario(nombre):
    return f"hola {nombre}"
    
saludo = saludar_usuario(nombre_user)
print(saludo)

'''
 3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados.
'''

nombre_usuario = input("ingrese su nombre: ")
apellido_usuario = input("ingrese su apellido: ")
edad_usuario = int(input("ingrese su edad: "))
domicilio = input("ingrese su domicilio: ")

def informacion_personal(nombre, apellido, edad, direccion):
    return f"soy {nombre} {apellido} tengo {edad} años, y vivo en {direccion}"

info_personal = informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, domicilio)
print(info_personal)

'''
 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
'''
PI = 3.14159
radio_usuario = int(input("ingrese el radio"))

def calcular_area_circulo(radio):
    area = PI * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * PI * radio
    return perimetro

area_calculada = calcular_area_circulo(radio_usuario)
perimetro_calculado = calcular_perimetro_circulo(radio_usuario)

print("------- resultados ---------")
print(f"el area del circulo es: {area_calculada}")
print(f"el perimetro es: {perimetro_calculado}")

'''
 Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función.
'''




def segundos_a_hora(cantidad_segundos):
    horas = cantidad_segundos / 3600
    return horas

segundos_usuario = float(input("ingrese los segundos"))

horas_calculadas = segundos_a_hora(segundos_usuario)

print(f"los segundos {segundos_usuario} convertidos a horas: {horas_calculadas}")

'''
 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
'''

def tabla_multiplicar(numero):
    tabla = f"tabla del {numero} --- \n"
    
    for elemento in range(1,11):
        resultado = numero * elemento
        tabla += f"{numero} x {elemento} = {resultado} \n"
    return tabla

num_usuario = int(input("ingrese un numero: "))

tabla_final = tabla_multiplicar(num_usuario)

print(tabla_final)

'''
 7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
'''



def operaciones_basicas (a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "No se puede"
        
    return (suma, division, resta, multiplicacion)

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

sumar, dividir, restar, multiplicar = operaciones_basicas(numero1, numero2)

print(f"la suma entre: {numero1} + {numero2} = {sumar}")
print(f"la resta entre: {numero1} - {numero2} = {restar}")
print(f"la multiplicacion entre: {numero1} * {numero2} = {multiplicar}")
print(f"la division entre: {numero1} / {numero2} = {dividir}")

'''
 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales
'''

def calcular_imc(peso, altura):
    
    if altura > 0:
        imc = peso / (altura **2)
    else:
        return None
    return imc


peso_usuario = float(input("ingrese peso en kilogramos (ej: 70.5): "))
altura_usuario = float(input("ingrese altura en metros (ej: 1.75): "))

resultado_imc = calcular_imc(peso_usuario, altura_usuario)
print(f"el indice de masa corporal es: {resultado_imc}")

'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función.
'''

def celsius_a_fahrenheit(celcius):
    
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

temperatura_usuario = float(input("ingrese los grados celcius"))

grados_calculados = celsius_a_fahrenheit(temperatura_usuario)

print(f"los grados celciu: {temperatura_usuario} a fahrenheit son: {grados_calculados}")

'''
 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función.
'''

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num_uno = float(input("Introduce el primer número: "))
num_dos = float(input("Introduce el segundo número: "))
num_tres = float(input("Introduce el tercer número: "))

resultado_promedio = calcular_promedio(num_uno, num_dos, num_tres)

print(resultado_promedio)