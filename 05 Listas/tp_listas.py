'''
1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja. 
'''

print("---- punto 1 ----")
notas_estudiantes = [2, 8, 8.5, 6, 9, 5, 10, 4, 6.5, 7.8]

for notas in notas_estudiantes:
    print(f"nota: ", notas)
    
promedio = sum(notas_estudiantes) / len(notas_estudiantes)
print(f"el promedio es: ", promedio)


print(f"la nota mas alta es:",max(notas_estudiantes) )
print(f"la nota mas baja es:",min(notas_estudiantes) )

'''
2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''

print("---- punto 2 ----")
productos = []
for cosas in range(5):
    producto_ingresado = input('ingrese un producto: ')
    productos.append(producto_ingresado)
lista_ordenada = sorted(productos)

print("Lista ordenada alfabeticamente:")
for cosa in lista_ordenada:
    print(cosa)
    
eliminar_producto = input('indica el producto que deseas eliminar: ')
productos.remove(eliminar_producto)

print("Producto actualizado:")
for actualizado in productos:
    print(actualizado)
    
'''
3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista. 
'''
import random
print("---- punto 3 ----")

lista_numeros = []
lista_pares = []
lista_impares = []

for numero in range(15):
    numero_aleatorio = random.randint(1, 100)
    lista_numeros.append(numero_aleatorio)

    
    if numero_aleatorio % 2 == 0:
        lista_pares.append(numero_aleatorio)
    else:
        lista_impares.append(numero_aleatorio)


print(f'----- Lista generada ({len(lista_numeros)} elementos) -----')

for elemento_lista in lista_numeros:
    print(elemento_lista, end=" ")
print("\n===================================")

print(f'----- Lista pares ({len(lista_pares)} elementos) -----')

for elemento_par in lista_pares:
    print(elemento_par, end=" ")
print("\n===================================")

print(f'----- Lista impares ({len(lista_impares)} elementos) -----')

for elemento_impar in lista_impares:
    print(elemento_impar, end=" ")
print("\n===================================")

'''
4) Dada una lista con valores repetidos: datos: [1,3,5,3,7,1,9,5,3]
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. 
'''

numeros_repetidos = [1,3,5,3,7,1,9,5,3]
lista_sin_duplicados = list(set(numeros_repetidos))

# mostramos lista con numeros duplicados

print("---- lista con duplicados ------")
for elemento_duplicado in numeros_repetidos:
    print(elemento_duplicado, end=" ")
print("\n===================================")


# mostrar lista sin duplicados
print("---- lista sin duplicados ----")
for dato in lista_sin_duplicados:
    print(dato, end=" ")
    
'''
5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada.
'''
lista_estudiantes = ["nestor", "victor", "jorge", "mario", "sergio", "gaston", "romina", "camila"]

opcion_usuario = input("elige una opcion: 'a' para agregar / 'e' eliminar 's' salir: ").lower()

while opcion_usuario != "s":
    nombre_nuevo = input("escribe el nombre a agregar: ")
    lista_estudiantes.append(nombre_nuevo)
    print(f"agregaste a: {nombre_nuevo}")
    
    for nombre_actualizado in lista_estudiantes:
        print(nombre_actualizado)
        
    opcion_usuario = input("elige una opcion: 'a' para agregar / 'e' eliminar 's' salir: ").lower()
    
    # opcion para eliminar
    if opcion_usuario == "e":
        for estudiantes in lista_estudiantes:
            print(estudiantes)
        nombre_eliminar = input(f"escribe el nombre a eliminar: ")
        if nombre_eliminar in lista_estudiantes:
            lista_estudiantes.remove(nombre_eliminar)
            print(f"eliminaste a: {nombre_eliminar}")
            opcion_usuario = input("elige una opcion: 'a' para agregar / 'e' eliminar 's' salir: ").lower()
            
        else:
            print(f"el nombre: {nombre_eliminar} no existe en la lista")
            nombre_eliminar = input(f"escribe el nombre a eliminar: ")
            
else:
    print("Gracias por usar el programa")
    
    
'''
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero). 
'''

lista_original = [10,20,30,40,50,60,70]
inicio = 0
fin = len(lista_original) -1

print("--------------- lista origunal ----------------")
for num_lista in lista_original:
    print(num_lista, end=" ")
print("\n=================================")

while inicio < fin:
    
    lista_original[inicio], lista_original[fin] = lista_original[fin], lista_original[inicio]
    
    inicio = inicio + 1
    fin = fin - 1

for lista_movida in lista_original:
    print(lista_movida, end=" ")
    
    
'''
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana.
'''

lista_temperatura =[
    [15, 25],
    [16, 27],
    [18, 30],
    [17, 28],
    [14, 26],
    [12, 24],
    [13, 25]
    ]

for temperatura in lista_temperatura:
    print(temperatura)
        
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

minima = 0
maxima = 0

maxima_amplitud = -1
dia_mayor_amplitud = ""

for fila in range(len(lista_temperatura)):
    
    minimo_dia = lista_temperatura[fila][0]
    maxima_dia = lista_temperatura[fila][1]
    
    minima = minima + minimo_dia
    maxima = maxima + maxima_dia
    
    amplitud_actual = maxima_dia - minimo_dia
    
    if amplitud_actual > maxima_amplitud:
        maxima_amplitud = amplitud_actual
        dia_mayor_amplitud = dias_semana[fila]

num_dias = len(lista_temperatura)

promedio_minima = minima / num_dias
promedio_maxima = maxima / num_dias

print("----- RESULTADOS ------")
print(f"promedio de minimas: {promedio_minima}")
print(f"promedio de maxima: {promedio_maxima}")
print(f"dia con mayor amplitud: {dia_mayor_amplitud} con {maxima_amplitud}")

'''
8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia. 
'''

materias = ["programacion", "matematicas", "fisica"]
alumnos = ["nestor", "juan", "pedro", "robert", "julian"]
notas = [[10,8,9], [5,7,3],[6,8,4], [9,7,6],[10,9,8]]

cantidad_estudiantes= len(alumnos)
cantidad_materias = len(materias)


for fila_nombres in range(len(alumnos)):
    suma_notas = 0
    for nombre_materia in range(len(materias)):
        suma_notas = suma_notas + notas[fila_nombres][nombre_materia]
        
    print()
    
    promedio_notas = suma_notas / cantidad_materias
    nombre_actual_alumno = alumnos[fila_nombres]
    print(f'Estudiante: {nombre_actual_alumno} y el promedio es: {promedio_notas}')
    
'''
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
'''

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador_actual = "X" 
turno = 0
MAX_TURNOS = 9 

print("--- Ta-Te-Ti con Límite de 9 Turnos ---")

while turno < MAX_TURNOS:
    
    
    print("\n--- Tablero Actual ---")
    for filas in tablero:
        for element in filas:
            print(element, end=" ")
        print()
    
    
    print(f"\nTurno {turno + 1}/{MAX_TURNOS} - jugador: {jugador_actual}")
    
    # NOTA: Asumimos que el usuario ingresa números válidos (0, 1, 2)
    fila_elegida = int(input("Elige una fila (0, 1, 2): "))
    columna_elegida = int(input("Elige una columna (0, 1, 2): "))

   
    tablero[fila_elegida][columna_elegida] = jugador_actual
    
    
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"
        
    turno += 1 


print("\n=== fin de juego ===")

for filas in tablero:
    for element in filas:
        print(element, end=" ")
    print()

'''
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana.
'''

ventas = [
    [10, 15, 8, 20, 12, 5, 18],
    [25, 10, 15, 5, 20, 10, 30],
    [5, 20, 10, 15, 8, 25, 12],
    [15, 5, 20, 10, 18, 12, 22]
]

nombre_producto = ["silla", "mesa", "heladera", "cocina"]
dias_semana = ["dia 1", "dia 2", "dia 3", "dia 4", "dia 5", "dia 6", "dia 7"]

print("---- total vendido ----")

# recorremos la lista ventas
for i in range(len(ventas)):
    total_product = 0
    
    for venta_dia in ventas[i]:
        total_product += venta_dia
    print(f"{nombre_producto[i]}: {total_product} unidades")
    
# dias con mayores ventas

venta_por_dia = []
dia_mayor_venta = 0

#recorremos las columnas de la lista ventas
for j in range(len(ventas[0])):
    total_dia = 0
    
    # recorremos el bucle interior es decir las filas de la lista ventas
    for i in range(len(ventas)):
        total_dia += ventas[i][j]
    venta_por_dia.append(total_dia)

print(f"ventas totales por dia: {venta_por_dia}")  
print(f"el dia con mayor venta fue: {dias_semana[dia_mayor_venta]}")




print("\n--- producto Más Vendido en la Semana ---")

max_venta_producto = -1 
producto_mas_vendido_indice = -1

# Bucle principal que recorre las filas (Productos)
for i in range(len(ventas)):
    total_producto = 0
    
    # Bucle interior: Suma de ventas del producto 'i'
    for venta_dia in ventas[i]:
        total_producto += venta_dia
        
    # Comparamos el total del producto actual con el máximo guardado
    if total_producto > max_venta_producto:
        max_venta_producto = total_producto
        producto_mas_vendido_indice = i # Guardamos el índice del producto
        
print(f"El producto más vendido fue {nombre_producto[producto_mas_vendido_indice]} (Fila {producto_mas_vendido_indice}), con un total de {max_venta_producto} unidades vendidas en la semana.")

    