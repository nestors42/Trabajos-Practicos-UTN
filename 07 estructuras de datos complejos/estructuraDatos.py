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

# definimos los dos conjuntos

# parcial_1 = {"Ana", "Beto", "Carlos", "Diana", "Elias", "Flor"}
# parcial_2 = {"Ana", "Elias", "Guillermo", "Hugo", "Irene", "Julia"}

# print(f"estudiantes que aprobaron el parcial 1: {parcial_1}")
# print(f"estudiantes que aprobaron el parcial 2: {parcial_2}")

# # mostramos los alumnos que aprobaron ambos parciales
# ambos_parciales = parcial_1 & parcial_2
# print(f"los alumnos que aprobaron ambos parciales: {ambos_parciales}")

# # los que aprobaron solo uno de los examenes
# solo_uno = parcial_1 ^ parcial_2
# print(f"alumnos que aprobaron solo un examen: {solo_uno}")

# # los alumnos que aprobaron al menos un examen
# al_menos_uno = parcial_1 | parcial_2
# print(f"estudiantes que aprobaron al menos un examen: {al_menos_uno}")

'''
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.
'''

# Código corregido y completado:
# STOCK_INVENTARIO = {
#     "manzana": 50,
#     "banana": 100,
#     "pera": 60
# }
    
# def consultar_stock(stock):
#     producto = input("ingrese el nombre del producto a consultar: ").strip().lower()
#     # Usamos .get() para obtener la cantidad, o None si no existe
#     cantidad = stock.get(producto) 
    
#     if cantidad is not None:
#         # Se imprime el stock si la cantidad existe
#         print(f"El stock de {producto.capitalize()} es: {cantidad} unidades.")
#     else:
#         # Se imprime un error si el producto no existe (cantidad es None)
#         print(f"El producto '{producto.capitalize()}' no se encuentra en el inventario.")
        
        
# def modificar_stock(stock):
#     producto = input("ingrese el nombre del producto a modificar/agregar: ").strip().lower()
    
#     unidades_asumar = int(input("cuantas unidades quieres agregar: "))
    
#     if unidades_asumar <= 0:
#         print("ERROR: la opcion debe ser un numero positivo, vuelve a intentarlo")
#         return
    
#     if producto in stock:
#         stock[producto] += unidades_asumar 
#         print(f"Se agregaron {unidades_asumar} a {producto.capitalize()}. Total nuevo: {stock[producto]}")
        
#     else:
#         stock[producto] = unidades_asumar
#         print(f"Producto nuevo agregado. {producto.capitalize()} se agregó con {unidades_asumar} unidades.")
        
        
# def mostrar_inventario_salir(stock):
#     for prod, cant in STOCK_INVENTARIO.items():
#         print(f"{prod.capitalize()}: {cant}")
#     print("Saliendo del programa.")
#     return True

# # Realizamos el menú de opciones
# def gestionar_inventario():
#     while True:
#         print("\nOpciones:")
#         print("1. Consultar stock de un producto")
#         print("2. Agregar unidades / nuevo producto")
#         print("3. Mostrar todo el inventario y Salir")
        
        
#         option = input("ingrese una opcion (1 / 2 / 3): ").strip() 
        
#         if option == '1':
#             consultar_stock(STOCK_INVENTARIO)
            
#         elif option == '2':
            
#             modificar_stock(STOCK_INVENTARIO)
#             pass
        
#         elif option == '3':
#             mostrar_inventario_salir(STOCK_INVENTARIO)
            
#             break 
        
#         else:
#             print("Opción no válida. Por favor, intente de nuevo.")

# gestionar_inventario()


'''
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Ejemplo:
agenda = ("lunes", "10:00"): "reunion",
          ("martes", "15:00"): "calse de ingles"
          
Permití consultar qué actividad hay en cierto día y hora.
'''

def gestionar_agenda():
    # Diccionario de agenda con tuplas (día, hora)
    agenda = {
        ("lunes", "10:00"): "Reunión de planificación",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:30"): "Entrenamiento en el gimnasio",
        ("jueves", "18:00"): "Cita con el dentista"
    }
    
    print("--- Consulta de Agenda ---")
    
    # 1. Solicitar el día y la hora al usuario
    dia_consulta = input("Ingresa el día a consultar (ej: lunes): ").strip().lower()
    hora_consulta = input("Ingresa la hora a consultar (ej: 10:00): ").strip()
    
    
    clave_busqueda = (dia_consulta, hora_consulta)
    
    # 3. Consultar el diccionario usando .get() para evitar errores si la clave no existe
    evento = agenda.get(clave_busqueda)
    
    print("\n--- Resultado ---")
    if evento:
        print(f"La actividad para el {dia_consulta.capitalize()} a las {hora_consulta} es: {evento}")
    else:
        print(f"No hay actividades programadas para el {dia_consulta.capitalize()} a las {hora_consulta}.")

# Ejecutar el programa
gestionar_agenda()
        
        