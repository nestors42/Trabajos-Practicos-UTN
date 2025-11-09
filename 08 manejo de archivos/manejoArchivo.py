'''
1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
'''
nombre_archivo = "productos.txt"
cabecera = "nombre,precio,cantidad"


with open(nombre_archivo, "w") as archivo:
    # creamos la lista de productos
    datos_productos = [
    "Azucar,850,150",
    "Cafe,1200,80",
    "Leche,900,200"
]
    archivo.write(cabecera +"\n")
    
    # iteramos la lista de producto y lo escribimos en el archivo
    
    for elemento_producto in datos_productos:
        archivo.write(elemento_producto + "\n")
        print(elemento_producto)


'''
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''

with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        
        datos = linea_limpia.split(",")
        
        # desempaquetamos los datos a variables
        nombre, precio, cantidad = datos
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

with open("productos.txt", "r") as archivo:
    # omite la cabecera
    next(archivo)
    for linea in archivo:
        linea_limpia = linea.strip()
        
        datos = linea_limpia.split(",")
        
        nombre, precio, cantidad = datos
        
        print(f"producto: {nombre} | precio: {precio} | cantidad: {cantidad}")


'''
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente.
'''
def leer_mostrar_productos(nombre_archivo):
    print("----- Lista de Productos -----")
    # lee el archivo ya existente
    with open(nombre_archivo, "r") as archivo:
        # omite la cabecera
        next(archivo)
        # iteramos cada linea
        for linea in archivo:
            linea_limpia = linea.strip()
        
            datos = linea_limpia.split(",")
        
        # desempaquetamos los datos a variables
            nombre, precio, cantidad = datos
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        
leer_mostrar_productos(nombre_archivo)

def agragar_producto(nombre_archivo):
    print("----- agregar nuevo producto -----")
    # pedimos al usuario los datos
    nombre_product = input("ingresa el nombre del producto: ").strip()
    precio_product = input("ingrese el precio del producto: ").strip()
    cantidad_product = input("ingrese la cantidad: ").strip()
    
    # validamos para que los campos no esten vacios
    if not nombre_product or not precio_product or not cantidad_product:
        print("error: los campos no deben estar vacios")
        return
    
    # formateamos lo ingresado a variables
    linea_nueva = f"{nombre_product},{precio_product},{cantidad_product}"
    
    # añadimos con el metodo "a"
    with open(nombre_archivo, "a") as archivo:
        archivo.write(linea_nueva + "\n")
    print(f"Producto {nombre_product.capitalize()} agregado")
    
agragar_producto(nombre_archivo)

print("---- inventario actualizado -----")
leer_mostrar_productos(nombre_archivo)

'''
 Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad.
'''

nombre_archivo = "productos.txt"
productos = []

print(f"--- Cargando datos desde '{nombre_archivo}' a la lista ---")

with open(nombre_archivo, "r") as archivo:
    cabecera = archivo.readline().strip().split(",")
    
    
    for linea in archivo:
        linea_limpia = linea.strip()
        
        if not linea_limpia:
            continue
            
        datos_valores = linea_limpia.split(",")
        
        
        if len(datos_valores) == len(cabecera):
            
            producto_dict = {
                cabecera[0]: datos_valores[0],
                cabecera[1]: float(datos_valores[1]),
                cabecera[2]: int(datos_valores[2])
            }
            
            productos.append(producto_dict)

print(f"Se cargaron {len(productos)} productos en la lista 'productos'.")


print("\n--- Estructura Final de la Lista 'productos' ---")
for p in productos:
    print(p)
    
'''
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error. 
'''




def cargar_productos(nombre_archivo):
    productos = []
    
    with open(nombre_archivo, "r") as archivo:
        # Saltamos la cabecera
        next(archivo) 
        
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia: continue
            
            datos_valores = linea_limpia.split(",")
            
            if len(datos_valores) == 3:
                nombre, precio_str, cantidad_str = datos_valores
                
                producto_dict = {
                    'nombre': nombre.strip(),
                    # Convertimos precio y cantidad a números
                    'precio': float(precio_str.strip()),
                    'cantidad': int(cantidad_str.strip())
                }
                productos.append(producto_dict)
    return productos

# --------------------------------------------------------------------------------

# --- Función para buscar producto por nombre ---
def buscar_producto_por_nombre(productos_list):
    print("\n----- Búsqueda de Producto por Nombre -----")
    
    # Pedir al usuario el nombre a buscar, convirtiéndolo a minúsculas para una búsqueda flexible
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    
    encontrado = False
    
    # Recorrer la lista de diccionarios
    for producto in productos_list:
        
        # Comparar el nombre del diccionario
        if producto['nombre'].lower() == nombre_buscado:
            
            # 3. Mostrar todos los datos si se encuentra
            print("\nProducto Encontrado:")
            print(f"  Nombre: {producto['nombre'].capitalize()}")
            print(f"  Precio: ${producto['precio']:.2f}")
            print(f"  Cantidad en stock: {producto['cantidad']}")
            
            encontrado = True
            break
            
    
    if not encontrado:
        print(f"\nError: El producto '{nombre_buscado.capitalize()}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------------

productos_cargados = cargar_productos(nombre_archivo) 

if productos_cargados:
    buscar_producto_por_nombre(productos_cargados)
else:
    print("No se pudo cargar ningún producto. La lista está vacía.")
    
'''
 Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista. 
'''

nombre_archivo = "productos.txt"
CABECERA = "nombre,precio,cantidad"


def cargar_productos(nombre_archivo):
    productos = []
    
    with open(nombre_archivo, "r") as archivo:
        archivo.readline() 
        
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia: continue
            
            datos_valores = linea_limpia.split(",")
            
            if len(datos_valores) == 3:
                nombre, precio_str, cantidad_str = datos_valores
                producto_dict = {
                    'nombre': nombre.strip(),
                    'precio': float(precio_str.strip()),
                    'cantidad': int(cantidad_str.strip())
                }
                productos.append(producto_dict)
    return productos


# Guardar Productos Actualizados ---
def guardar_productos(nombre_archivo, productos_list):
    
    
    
    with open(nombre_archivo, "w") as archivo:
        
        
        archivo.write(CABECERA + "\n")
        
        
        for producto in productos_list:
            
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}"
            archivo.write(linea + "\n")
            
    print(f"\nArchivo '{nombre_archivo}' SOBRESCRITO y productos guardados correctamente.")

# --------------------------------------------------------------------------------




productos_inventario = cargar_productos(nombre_archivo) 


productos_inventario.append({
    'nombre': 'Sal', 
    'precio': 550.0, 
    'cantidad': 80
})
print(f"Lista de productos lista para guardar ({len(productos_inventario)} items).")

guardar_productos(nombre_archivo, productos_inventario)