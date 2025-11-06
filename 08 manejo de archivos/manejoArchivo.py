'''
1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
'''
cabecera = "nombre,precio,cantidad"
datos_productos = [
    "Azúcar,850,150",
    "Café,1200,80",
    "Leche,900,200"
]

with open("productos.txt", "w") as archivo:
    archivo.write(cabecera + "\n")
    for linea in datos_productos:
        archivo.write(linea + "\n")
print(f"el archivo fue creado exitosamente")
print(linea)

'''
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
'''

with open("productos.txt", "r") as archivo:
    # omite la cabecera
    next(archivo)
    for linea in archivo:
        linea_limpia = linea.strip()
        
        datos = linea_limpia.split(",")
        
        nombre, precio, cantidad = datos
        
        print(f"producto: {nombre} | precio: {precio} | cantidad: {cantidad}")
    