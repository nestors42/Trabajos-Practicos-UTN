'''
1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
'''
nombre_archivo = "productos.txt"
cabecera = "nombre,precio,cantidad"


# with open(nombre_archivo, "w") as archivo:
#     # creamos la lista de productos
#     datos_productos = [
#     "Azucar,850,150",
#     "Cafe,1200,80",
#     "Leche,900,200"
# ]
#     archivo.write(cabecera +"\n")
    
#     # iteramos la lista de producto y lo escribimos en el archivo
    
#     for elemento_producto in datos_productos:
#         archivo.write(elemento_producto + "\n")
#         print(elemento_producto)


'''
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''

# with open(nombre_archivo, "r") as archivo:
#     for linea in archivo:
#         linea_limpia = linea.strip()
        
#         datos = linea_limpia.split(",")
        
#         # desempaquetamos los datos a variables
#         nombre, precio, cantidad = datos
#         print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# with open("productos.txt", "r") as archivo:
#     # omite la cabecera
#     next(archivo)
#     for linea in archivo:
#         linea_limpia = linea.strip()
        
#         datos = linea_limpia.split(",")
        
#         nombre, precio, cantidad = datos
        
#         print(f"producto: {nombre} | precio: {precio} | cantidad: {cantidad}")


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
    print(f"Producto {nombre_product.capitalize()} agregado ✅")
    
agragar_producto(nombre_archivo)

print("---- inventario actualizado -----")
leer_mostrar_productos(nombre_archivo)
    