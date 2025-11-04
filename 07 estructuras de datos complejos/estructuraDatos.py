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

contactos = {}
NUM_CONTACTOS = 5

# ITERAMOS NUM_CONTACTO PARA QUE SOLO PUEDA LLENAR 5 NUMEROS

for i in range(NUM_CONTACTOS):
    # bucle while para preguntar nombre
    while True:
        nombre = input(f"ingrese el nombre del contacto {i + 1}: ").strip()
        if nombre:
            break
        else:
            print("el campo no puede estar vacio")
    
    while True:
        numero = input(f"ingrese el numero telefonico de {nombre}: ").strip()
        if numero:
            break
        else:
            print("el campo no puede estar vacio")
        

    contactos[nombre] = numero
    print(f"el contacto {nombre} fue cargado exitosamente")
    
nombre_busqueda = input("ingrese el nombre a buscar").strip()

numero_encontrado = contactos.get(nombre_busqueda)

if numero_encontrado:
    print(f"el numero de telefonico de {nombre_busqueda} es: {numero_encontrado}")
else:
    print(f"lo siento el {nombre_busqueda} no existe agenda")
    

'''
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.

entrada -> ""hola mundo"
salida:
palabras_unicas: {"hola", "mundo"}
recuento: {"hola": 2, "mundo": 1}
'''
