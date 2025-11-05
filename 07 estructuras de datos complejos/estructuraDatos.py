'''
1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 
'''

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450}

# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(precios_frutas)

'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 
'''

# precios_frutas["Banana"] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)

'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios.
'''

# lista_frutas = precios_frutas.keys()
# print(lista_frutas)

'''
4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
Ejemplo:
contactos = {"Juan": "123456", "Ana": "987654"}
'''

# contactos = {}
# NUM_CONTACTOS = 5

# ITERAMOS NUM_CONTACTO PARA QUE SOLO PUEDA LLENAR 5 NUMEROS

# for i in range(NUM_CONTACTOS):
#     # bucle while para preguntar nombre
#     while True:
#         nombre = input(f"ingrese el nombre del contacto {i + 1}: ").strip()
#         if nombre:
#             break
#         else:
#             print("el campo no puede estar vacio")
    
#     while True:
#         numero = input(f"ingrese el numero telefonico de {nombre}: ").strip()
#         if numero:
#             break
#         else:
#             print("el campo no puede estar vacio")
        

#     contactos[nombre] = numero
#     print(f"el contacto {nombre} fue cargado exitosamente")
    
# nombre_busqueda = input("ingrese el nombre a buscar").strip()

# numero_encontrado = contactos.get(nombre_busqueda)

# if numero_encontrado:
#     print(f"el numero de telefonico de {nombre_busqueda} es: {numero_encontrado}")
# else:
#     print(f"lo siento el {nombre_busqueda} no existe agenda")
    

'''
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.

entrada -> ""hola mundo"
salida:
palabras_unicas: {"hola", "mundo"}
recuento: {"hola": 2, "mundo": 1}
'''

# def ejecutar_frase_simple():
    
#     frase = input("ingrese la frase: ").lower()
    
#     frase_separada = frase.split()
    
#     palabras_unicas = set(frase_separada)
    
#     recuento = {}
    
#     for palabra in frase_separada:
        
#         recuento[palabra] = recuento.get(palabra, 0) + 1
        
#     print("----- resultado ----")
#     print(f"la palabra unica: {palabras_unicas}")
#     print(f"el recuento: {recuento}")
    
# ejecutar_frase_simple()

'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
Ejemplo:
alumnos = {
    "sofia" : (10,9,8)
    "luis" : (6,7,7) 
}
'''
# def promedio_alumnos():
#     alumnos = {}
    
#     NUM_ALUMNOS = 3
#     NUM_NOTAS = 3
    
#     for i in range(NUM_ALUMNOS):
#         nombre_alumn = input(f"ingrese el nombre de alumno {i + 1}: ").strip().capitalize()
        
#         notas_lista = []
        
#         for j in range(NUM_NOTAS):
            
#             nota = int(input(f"nota {j + 1}: "))
            
#             notas_lista.append(nota)
#         alumnos[nombre_alumn] = tuple(notas_lista)
        
#     print("---- resultados ----")
    
#     for nombre_alumnos, notas in alumnos.items():
#         promedio = sum(notas) / len(notas)
        
#         print(f"el promedio de {nombre_alumnos} (notas: ) es: {promedio}")
        
# promedio_alumnos()
    
'''
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''

# Definición de los sets de estudiantes
parcial_1 = {101, 105, 110, 115, 120, 125}
parcial_2 = {101, 115, 120, 130, 135, 140}

print(f"Estudiantes que aprobaron Parcial 1: {parcial_1}")
print(f"Estudiantes que aprobaron Parcial 2: {parcial_2}\n")

# 1. Mostrar los que aprobaron ambos parciales (Intersección)
ambos_parciales = parcial_1 & parcial_2
print(f"1. Estudiantes que aprobaron AMBOS parciales (Intersección): {ambos_parciales}")

# 2. Mostrar los que aprobaron solo uno de los dos (Diferencia Simétrica)
solo_uno = parcial_1 ^ parcial_2
print(f"2. Estudiantes que aprobaron SOLO UNO de los dos (Diferencia Simétrica): {solo_uno}")

# 3. Mostrar la lista total de estudiantes que aprobaron al menos un parcial (Unión)
al_menos_uno = parcial_1 | parcial_2
print(f"3. Lista TOTAL de estudiantes que aprobaron al menos uno (Unión): {al_menos_uno}")
