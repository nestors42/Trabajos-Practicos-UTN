# 🌍 Sistema de Gestión de Países (CSV)

Este es un programa de consola en Python que permite gestionar una lista de países, almacenando y recuperando sus datos desde un archivo CSV.

## ✨ Características

- Carga y guardado de datos: carga automáticamente los datos al inicio y los guarda al salir.
- CRUD básico: permite agregar y actualizar países.
- Búsqueda y filtrado: buscar por nombre, filtrar por continente, población o superficie.
- Ordenamiento: ordenar la lista por cualquier campo numérico o alfabético.
- Estadísticas: muestra estadísticas clave (promedios, máximo/mínimo, conteo por continente).

## 🛠️ Requisitos

- Python 3.x

## 🚀 Uso

### 1. Preparación de datos

Asegúrate de tener un archivo llamado `paises.csv` con los siguientes encabezados:
`nombre,poblacion,superficie,continente`

### 2. Ejecución

Ejecuta el script desde la terminal:

```bash
python integrador.py
```

### 3. Menú

Al iniciar, verás el siguiente menú. Ingresa el número de la opción deseada:

===== MENÚ PRINCIPAL =====
1. Agregar país  
2. Actualizar país  
3. Buscar país  
4. Filtrar por continente  
5. Filtrar por población  
6. Filtrar por superficie  
7. Ordenar por nombre  
8. Ordenar por población  
9. Ordenar por superficie  
10. Estadísticas  
11. Guardar y salir

Nota: Selecciona la opción 11 (Guardar y salir) para que todos los cambios se guarden en `paises.csv`.

## 👨‍💻 Estructura del código

El código está organizado modularmente, con una función específica para cada operación:

| Función | Propósito principal |
| :--- | :--- |
| `cargar_datos` / `guardar_datos` | Maneja la persistencia (lectura y escritura) en CSV. |
| `agregar_pais` | Ingresa un nuevo registro con validación de datos. |
| `actualizar_pais` | Modifica la población o superficie de un país existente. |
| `buscar_pais` | Búsqueda parcial por nombre. |
| `filtrar_por_*` | Funciones para aplicar filtros por continente, población o superficie. |
| `ordenar_paises_por_clave` | Función genérica de ordenamiento ascendente o descendente. |
| `estadisticas` | Calcula y presenta resúmenes y métricas globales. |
| `menu_principal` | Bucle principal que gestiona la interacción y el flujo del programa. |