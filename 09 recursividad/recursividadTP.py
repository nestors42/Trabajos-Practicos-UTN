
# def factorial(n):
    
#     if n == 0 or n == 1:
#         return 1
    
#     else:
#         return n * factorial(n - 1)



# def calcular_y_mostrar_factoriales():
    
#     print("--- calculadora de factoriales ---")
#     print("El factorial se calculará desde 1 hasta el número que ingrese.")

    
#     while True:
#         limite = input("Por favor, ingrese un número entero positivo: ")
#         limite_entero = int(limite)

#         if limite_entero < 1:
#             print("El número debe ser un entero positivo mayor o igual a 1. Intente de nuevo.")
#             continue
#         break

#     print(f"\nCalculando factoriales de 1 hasta {limite_entero}:")
#     print("-------------***********-----------------------")
    
#     for i in range(1, limite_entero + 1):
#         resultado = factorial(i)
#         print(f"factorial de {i} = {resultado}")


# if __name__ == "__main__":
#     calcular_y_mostrar_factoriales()
    
'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.
'''

# def fibonacci(n):
    
#     if n < 0:
#         return 0 
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# --- Programa Principal ---

# def calcular_y_mostrar_fibonacci():
#     print("--- Calculadora Fibonacci ---")
#     print("Muestra la serie completa hasta la posición indicada.")

    
#     while True:
#         posicion_limite = input("Por favor, ingrese un número entero positivo para el límite de la posición: ")
        
        
#         limite_entero = int(posicion_limite)

        
#         if limite_entero < 0:
#             print("El número debe ser un entero positivo o cero. Intente de nuevo.")
#             continue
        
#         break

#     print(f"\nSerie de Fibonacci hasta la posición {limite_entero}:")
#     print("-------------------------------------------------")
    
#     serie = []
    
#     for i in range(limite_entero + 1):
#         valor = fibonacci(i)
#         serie.append(str(valor))

    
#     print(", ".join(serie))

#     print(f"\nEl valor de Fibonacci en la posición {limite_entero} es: {valor}")


# if __name__ == "__main__":
#     calcular_y_mostrar_fibonacci()
    
'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general. 
'''

def potencia(base, exponente):
    
    if exponente < 0:
        
        return 1 / potencia(base, -exponente)
    
    # Caso base: n^0 = 1
    elif exponente == 0:
        return 1
    
    else:
        return base * potencia(base, exponente - 1)


def probar_potencia():
    print("--- Calculadora ---")
    print("Calcula el valor de Base^Exponente.")

   
    base_str = input("Por favor, ingrese el número base: ")
    base = float(base_str)

    exponente_str = input("Por favor, ingrese el número exponente (entero): ")
    exponente = int(exponente_str)

    print("\n-----------------------------------------")
    print(f"Calculando: {base}^{exponente}")

    resultado = potencia(base, exponente)

    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")


if __name__ == "__main__":
    probar_potencia()
    
'''
4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.
'''

def decimal_a_binario(n):
    
    if n == 0:
        return "0"
    
    
    else:
        
        if n // 2 == 0:
            return str(n % 2)
        else:
           
            return decimal_a_binario(n // 2) + str(n % 2)



def probar_conversion():
    print("--- Conversor Decimal a Binario Recursivo ---")
    print("Convierte un entero positivo a su representación binaria.")

   
    while True:
        numero_decimal_str = input("Por favor, ingrese un número entero positivo en base 10: ")
        
        numero_decimal = int(numero_decimal_str)

        if numero_decimal < 0:
            print("El número debe ser un entero positivo. Intente de nuevo.")
            continue
        
        break

    print("\n-----------------------------------------")
    print(f"Número Decimal Ingresado: {numero_decimal}")

    if numero_decimal == 0:
         resultado_binario = "0"
    else:
        resultado_binario = decimal_a_binario(numero_decimal)

    print(f"Representación Binaria (recursiva): {resultado_binario}")
    

if __name__ == "__main__":
    probar_conversion()
    
    
'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed().
'''

def es_palindromo(palabra):
   
    if len(palabra) <= 1:
        return True
    
    if palabra[0].lower() != palabra[-1].lower():
        return False
    else:
        return es_palindromo(palabra[1:-1])

def probar_palindromo():
    print("--- Comprobador de Palíndromo Recursivo ---")
    print("Evalúa si una palabra (sin espacios/tildes) es un palíndromo.")
    
    palabra_ingresada = input("Por favor, ingrese una palabra para verificar: ")
    palabra_limpia = palabra_ingresada.replace(" ", "").lower()
    
    print("\n-----------------------------------------")
    print(f"Palabra a evaluar: '{palabra_ingresada}'")

    # Llamar a la función recursiva
    es_pali = es_palindromo(palabra_limpia)
    
    if es_pali:
        print("Resultado: ¡Es un palíndromo! ")
    else:
        print("Resultado: No es un palíndromo. ")


if __name__ == "__main__":
    probar_palindromo()
    
'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) 
'''
def suma_digitos(n):
    
    if n == 0:
        return 0
    
    
    else:
        
        return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    print("--- Calculadora Recursiva de Suma de Dígitos ---")
    
    
    while True:
        numero_str = input("Por favor, ingrese un número entero positivo: ")
        
        numero = int(numero_str)

        if numero < 0:
            print("El número debe ser positivo. Intente de nuevo.")
            continue
        
        break

    print("\n-----------------------------------------")
    print(f"Número ingresado: {numero}")

    resultado = suma_digitos(numero)

    print(f"La suma de los dígitos de {numero} es: {resultado}")
    
    # Ejemplos:
    print("\nEjemplos de prueba:")
    print(f"Suma de dígitos de 1234: {suma_digitos(1234)}")
    print(f"Suma de dígitos de 9: {suma_digitos(9)}")
    print(f"Suma de dígitos de 305: {suma_digitos(305)}")


if __name__ == "__main__":
    probar_suma_digitos()
    
    
'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 
'''

def contar_bloques(n):
    
    if n <= 0:
        return 0
    
   
    else:
        return n + contar_bloques(n - 1)

def probar_contar_bloques():
    print("--- Contador Recursivo de Bloques de Pirámide ---")
    
    while True:
        numero_str = input("Por favor, ingrese el número de bloques en la base (entero positivo): ")
        
        numero = int(numero_str)

        if numero < 1:
            print("El número debe ser un entero positivo (mayor o igual a 1). Intente de nuevo.")
            continue
        
        break

    print("\n-----------------------------------------")
    print(f"Base de la pirámide: {numero} bloques")

    total_bloques = contar_bloques(numero)

    # Mostrar el resultado
    print(f"El total de bloques necesarios para la pirámide es: {total_bloques}")
    
    # Ejemplos de prueba:
    print("\nEjemplos de prueba resultado:")
    print(f"contar_bloques(1) {contar_bloques(1)}")
    print(f"contar_bloques(2) {contar_bloques(2)}")
    print(f"contar_bloques(4) {contar_bloques(4)}")


if __name__ == "__main__":
    probar_contar_bloques()
    
'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0
'''

def contar_digito(numero, digito):
   
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    
    contador_actual = 1 if ultimo_digito == digito else 0
    
    return contador_actual + contar_digito(numero // 10, digito)

def probar_contador():
    print("--- Contador de Dígitos ---")
    print("Cuenta las apariciones de un dígito en un número.")
    
    numero_str = input("Por favor, ingrese el número entero positivo: ")
    numero = int(numero_str)

    # Solicitar el dígito a buscar
    digito_str = input("Por favor, ingrese el dígito (0-9) a contar: ")
    digito = int(digito_str)
    
    if not (0 <= digito <= 9):
        print("Advertencia: El dígito ingresado no está entre 0 y 9.")

    print("\n-----------------------------------------")
    print(f"Número a evaluar: {numero}")
    print(f"Dígito a buscar: {digito}")

    frecuencia = contar_digito(numero, digito)

    print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
    
    print("\nEjemplos de prueba:")
    print(f"contar_digito(12233421, 2) -> {contar_digito(12233421, 2)}")
    print(f"contar_digito(5555, 5) -> {contar_digito(5555, 5)}")
    print(f"contar_digito(123456, 7) -> {contar_digito(123456, 7)}")


if __name__ == "__main__":
    probar_contador()