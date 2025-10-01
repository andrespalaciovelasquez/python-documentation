
# =================================================================================================================
# ▀▄▀▄▀▄⡷⠂ 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓𝐀𝐂𝐈𝐎́𝐍 𝐃𝐄 𝐏𝐘𝐓𝐇𝐎𝐍 ⠐⢾▀▄▀▄▀▄
# Creado por: Andrés Palacio Velásquez
# =================================================================================================================

def generate_toc():
    """Genera una tabla de contenido basada en los nombres de las funciones."""
    print("--- 📋 𝐓𝐀𝐁𝐋𝐀 𝐃𝐄 𝐂𝐎𝐍𝐓𝐄𝐍𝐈𝐃𝐎 📋 ---")
    toc_items = [
        "1. Variables",
        "2. Listas",
        "3. Tuplas",
        "4. Diccionarios",
        "5. Operadores",
        "6. Condicionales",
        "7. Bucles",
        "8. Funciones",
        "9. Clases",
        "10. Módulos",
        "11. Funciones Lambda",
        "12. Generadores",
        "13. Manejo de Excepciones",
        "14. Manejo de Archivos",
        "15. Expresiones Regulares",
        "16. Decoradores",
        "17. Context Managers",
        "18. Métodos Mágicos"
    ]
    for item in toc_items:
        print(f"- {item}")
    print("---------------------------------------")

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 1. VARIABLES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def variables():
    """
    En Python, no es necesario especificar el tipo de variable,
    ya que es un lenguaje de programación de tipado dinámico.
    """
    print("\n--- 1. Variables ---")
    
    # Declaración y tipos de variables
    # Python infiere automáticamente el tipo de dato.
    nombre = "Palacio"
    edad = 26
    altura = 1.83
    es_programador = True

    print(f"Nombre: {nombre}, Tipo: {type(nombre)}")
    print(f"Edad: {edad}, Tipo: {type(edad)}")
    print(f"Altura: {altura}, Tipo: {type(altura)}")
    print(f"¿Es programador?: {es_programador}, Tipo: {type(es_programador)}")

    # Reasignación de variables
    # Puedes cambiar el valor y el tipo de una variable en cualquier momento.
    print(f"\nValor inicial de edad: {edad}")
    edad = "veintiséis"
    print(f"Valor reasignado de edad: {edad}, Nuevo tipo: {type(edad)}")

    # Asignación múltiple
    # Asigna valores a varias variables en una sola línea.
    a, b, c = 10, 20, "Hola"
    print(f"\nAsignación múltiple: a = {a}, b = {b}, c = {c}")

    # Intercambio de valores
    # Un caso especial de asignación múltiple para intercambiar valores fácilmente.
    print(f"Valores antes del intercambio: a = {a}, b = {b}")
    a, b = b, a
    print(f"Valores después del intercambio: a = {a}, b = {b}")

# =================================================================================================================
#                           ▀▄▀▄▀▄⡷⠂ 2. LISTAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def listas():
    """
    Una lista en Python es una colección ordenada y mutable de elementos.
    Se definen entre corchetes `[]` y los elementos se separan por comas.
    """
    print("\n--- 2. Listas ---")
    mi_lista = [1, 2, "Hola", True]
    print(f"Lista inicial: {mi_lista}")

    # Acceder a elementos de la lista
    # Los índices comienzan en 0.
    print(f"Primer elemento: {mi_lista[0]}")
    print(f"Último elemento (índice negativo): {mi_lista[-1]}")

    # Slicing (división de la lista)
    # Se utiliza para obtener un subconjunto de elementos.
    sub_lista = mi_lista[1:3]
    print(f"Subconjunto de la lista (índice 1 a 2): {sub_lista}")

    # Métodos de lista
    # .append(): Añade un elemento al final de la lista.
    mi_lista.append("Python")
    print(f"Después de append(): {mi_lista}")

    # .extend(): Añade los elementos de un iterable (como otra lista) al final.
    mi_lista.extend([3, 4])
    print(f"Después de extend(): {mi_lista}")

    # .insert(): Añade un elemento en una posición específica.
    mi_lista.insert(1, 99)
    print(f"Después de insert(): {mi_lista}")

    # .remove(): Elimina la primera ocurrencia de un valor.
    mi_lista.remove("Hola")
    print(f"Después de remove(): {mi_lista}")

    # .pop(): Elimina y devuelve un elemento en una posición específica.
    elemento_removido = mi_lista.pop(2)
    print(f"Elemento removido con pop(): {elemento_removido}, Lista: {mi_lista}")

    # .index(): Devuelve el índice de la primera ocurrencia de un valor.
    posicion = mi_lista.index(3)
    print(f"El elemento '3' se encuentra en la posición: {posicion}")

    # .count(): Cuenta el número de veces que aparece un elemento.
    mi_lista.append(4) # Añadimos otro 4 para demostrar el método
    conteo = mi_lista.count(4)
    print(f"El número '4' aparece {conteo} veces.")

    # .sort(): Ordena la lista de forma ascendente.
    # Nota: No se puede ordenar si hay elementos de diferentes tipos no comparables (ej. cadenas y números).
    lista_numeros = [5, 1, 8, 3, 2]
    lista_numeros.sort()
    print(f"Lista ordenada con sort(): {lista_numeros}")

    # .reverse(): Invierte el orden de los elementos de la lista.
    mi_lista.reverse()
    print(f"Lista invertida con reverse(): {mi_lista}")

    # .clear(): Elimina todos los elementos de la lista.
    mi_lista.clear()
    print(f"Lista después de clear(): {mi_lista}")
    
    # Longitud de la lista
    # La función len() devuelve el número de elementos.
    print(f"La lista tiene {len(mi_lista)} elementos.")

# =================================================================================================================
#                           ▀▄▀▄▀▄⡷⠂ 3. TUPLAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def tuplas():
    """
    Una tupla en Python es una colección ordenada e inmutable de elementos.
    Se definen entre paréntesis `()`.
    """
    print("\n--- 3. Tuplas ---")
    mi_tupla = (1, 2, "Hola", True)
    print(f"Tupla: {mi_tupla}")

    # Acceso a elementos
    print(f"Acceso a un elemento por índice: {mi_tupla[2]}")
    print(f"Acceso con slicing: {mi_tupla[1:3]}")

    # Inmutabilidad de las tuplas
    # Una vez que se crea una tupla, no se puede modificar, añadir o eliminar elementos.
    # mi_tupla[0] = 5 # Esto generaría un error de tipo 'TypeError'.
    print("\nIntento de modificar una tupla: mi_tupla[0] = 5")
    print("Esto generaría un error de tipo (TypeError) porque las tuplas son inmutables.")

    # Empaquetado y desempaquetado de tuplas
    # Esta es una característica clave de las tuplas en Python.
    a, b, c, d = mi_tupla
    print(f"\nTupla desempaquetada: a={a}, b={b}, c={c}, d={d}")
    
    # Métodos de las tuplas
    # Las tuplas solo tienen dos métodos debido a su inmutabilidad.
    print(f"Número de veces que aparece '2': {mi_tupla.count(2)}")
    print(f"Índice del elemento 'Hola': {mi_tupla.index('Hola')}")

    # Conversión de tupla a lista (para mutabilidad)
    # A menudo se convierte una tupla en una lista para poder modificarla.
    mi_lista = list(mi_tupla)
    print(f"\nTupla convertida a lista: {mi_lista}")
    mi_lista.append("Nuevo elemento")
    mi_nueva_tupla = tuple(mi_lista)
    print(f"Lista convertida de nuevo a tupla: {mi_nueva_tupla}")

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 4. DICCIONARIOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def diccionarios():
    """
    Un diccionario en Python es una colección de pares clave-valor,
    desordenados y mutables. Se definen entre llaves `{}`.
    """
    print("\n--- 4. Diccionarios ---")
    mi_diccionario = {
        "nombre": "Palacio",
        "edad": 26,
        "ciudad": "Medellín"
    }
    print(f"Diccionario inicial: {mi_diccionario}")

    # Acceder a un valor
    # Se usa la clave entre corchetes para acceder al valor.
    print(f"Acceder a 'nombre': {mi_diccionario['nombre']}")

    # Método get(): Acceso seguro a valores
    # Si la clave no existe, get() devuelve None o un valor por defecto,
    # evitando un error de tipo KeyError.
    print(f"Usando get() para 'edad': {mi_diccionario.get('edad')}")
    print(f"Usando get() para una clave inexistente: {mi_diccionario.get('pais', 'No encontrado')}")

    # Comprobar si una clave existe
    if "ciudad" in mi_diccionario:
        print("\n'ciudad' está en el diccionario.")

    # Agregar y actualizar elementos
    # Para agregar un nuevo par clave-valor, simplemente se asigna un valor a una nueva clave.
    mi_diccionario["profesion"] = "Ingeniero"
    print(f"Después de agregar: {mi_diccionario}")

    # Para actualizar un valor, se asigna un nuevo valor a una clave existente.
    mi_diccionario["edad"] = 27
    print(f"Después de actualizar: {mi_diccionario}")

    # Eliminar elementos
    # Se puede usar la palabra clave 'del' para eliminar un par clave-valor.
    del mi_diccionario["ciudad"]
    print(f"\nDespués de eliminar con del: {mi_diccionario}")

    # Método pop(): Elimina y devuelve el valor asociado a una clave
    profesion = mi_diccionario.pop("profesion")
    print(f"Valor eliminado con pop(): {profesion}, Diccionario actual: {mi_diccionario}")

    # Vistas del diccionario (claves, valores, items)
    # Estos métodos devuelven objetos de vista dinámicos.
    print(f"\nClaves: {mi_diccionario.keys()}")
    print(f"Valores: {mi_diccionario.values()}")
    print(f"Pares clave-valor: {mi_diccionario.items()}")
    
    # Método update(): Fusionar diccionarios
    # Útil para añadir pares de clave-valor de otro diccionario o iterable.
    mi_diccionario.update({"ciudad": "Medellín", "pais": "Colombia"})
    print(f"Después de update(): {mi_diccionario}")

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 5. OPERADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def operadores():
    """
    En Python, existen diversos tipos de operadores: aritméticos,
    de asignación, de comparación, lógicos, de identidad y de pertenencia.
    """
    print("\n--- 5. Operadores ---")
    x = 10
    y = 3
    z = 10
    
    # Operadores Aritméticos
    # Se utilizan para realizar cálculos matemáticos.
    print("\n## Operadores Aritméticos")
    print(f"Suma (+): {x + y}")
    print(f"Resta (-): {x - y}")
    print(f"Multiplicación (*): {x * y}")
    print(f"División (/): {x / y} (Resultado con decimales)")
    print(f"División Entera (//): {x // y} (Parte entera del resultado)")
    print(f"Módulo (%): {x % y} (El residuo de la división)")
    print(f"Exponente (**): {x ** y} (10 elevado a la 3)")

    # Operadores de Asignación
    # Se utilizan para asignar valores a variables de forma abreviada.
    print("\n## Operadores de Asignación")
    a = 5
    print(f"Valor inicial de 'a': {a}")
    a += 3  # Equivalente a a = a + 3
    print(f"Después de 'a += 3': {a}")
    a -= 2  # Equivalente a a = a - 2
    print(f"Después de 'a -= 2': {a}")

    # Operadores de Comparación
    # Devuelven un valor booleano (True o False).
    print("\n## Operadores de Comparación")
    print(f"¿x == y? (Igualdad): {x == y}")
    print(f"¿x != y? (Desigualdad): {x != y}")
    print(f"¿x > y? (Mayor que): {x > y}")
    print(f"¿x < y? (Menor que): {x < y}")
    print(f"¿x >= z? (Mayor o igual que): {x >= z}")
    print(f"¿x <= z? (Menor o igual que): {x <= z}")

    # Operadores Lógicos
    # Combinan expresiones booleanas y devuelven True o False.
    print("\n## Operadores Lógicos")
    print(f"¿(x > y) and (x == z)?: {(x > y) and (x == z)}")  # Ambas condiciones deben ser verdaderas
    print(f"¿(x < y) or (x == z)?: {(x < y) or (x == z)}")    # Al menos una condición debe ser verdadera
    print(f"¿not(x > y)?: {not(x > y)}")                       # Invierte el resultado

    # Operadores de Identidad
    # Comparan si dos variables apuntan al mismo objeto en memoria.
    print("\n## Operadores de Identidad")
    print(f"¿x is z?: {x is z}") # Devuelve True si x y z son el mismo objeto
    print(f"¿x is y?: {x is y}") # Devuelve False

    # Operadores de Pertenencia
    # Verifican si un valor se encuentra dentro de una secuencia (lista, cadena, tupla, etc.).
    print("\n## Operadores de Pertenencia")
    mi_lista = [1, 2, 3]
    print(f"¿2 in mi_lista?: {2 in mi_lista}")
    print(f"¿4 not in mi_lista?: {4 not in mi_lista}")

# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 6. CONDICIONALES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def condicionales():
    """
    Las sentencias `if`, `elif` y `else` controlan el flujo
    de un programa basándose en condiciones lógicas.
    """
    print("\n--- 6. Condicionales ---")
    x = -5
    
    # Ejemplo básico de if/elif/else
    # El programa evalúa las condiciones de arriba a abajo y ejecuta el primer bloque que sea True.
    print("## Condicional simple")
    if x > 0:
        print("x es un número positivo")
    elif x == 0:
        print("x es cero")
    else:
        print("x es un número negativo")

    # Condicionales con operadores lógicos
    # Usa 'and' para que ambas condiciones sean True.
    # Usa 'or' para que al menos una condición sea True.
    print("\n## Condicionales con operadores lógicos")
    edad = 18
    ingresos = 25000
    
    if edad >= 18 and ingresos >= 20000:
        print("Cumples los requisitos para un préstamo.")
    else:
        print("No cumples con los requisitos del préstamo.")
        
    # Condicionales anidadas
    # Una sentencia 'if' dentro de otra.
    print("\n## Condicionales anidadas")
    calificacion = 85
    
    if calificacion >= 70:
        if calificacion >= 90:
            print("Tu calificación es A, ¡excelente!")
        else:
            print("Tu calificación es B, ¡buen trabajo!")
    else:
        print("Necesitas mejorar tu calificación.")

# =================================================================================================================
#                          ▀▄▀▄▀▄⡷⠂ 7. BUCLES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def bucles():
    """
    Los bucles (`while` y `for`) permiten repetir una sección de código.
    Son esenciales para automatizar tareas repetitivas sobre secuencias de datos.
    """
    print("\n--- 7. Bucles ---")

    # Bucle 'while'
    # Se repite mientras una condición sea verdadera. Es útil cuando no sabes
    # de antemano cuántas veces se repetirá el bucle.
    print("## Bucle `while`")
    contador = 0
    while contador < 3:
        print(f"El contador es: {contador}")
        contador += 1
    
    # Bucle 'for'
    # Itera sobre una secuencia (como una lista, tupla, cadena o rango).
    # Es ideal cuando sabes cuántos elementos hay para iterar.
    print("\n## Bucle `for`")

    # Iterando sobre un rango
    print("Iterando con `range(3)`:")
    for i in range(3):
        print(i)
    
    # Iterando sobre una lista
    nombres = ["Ana", "Luis", "Sofía"]
    print("\nIterando sobre una lista:")
    for nombre in nombres:
        print(f"Hola, {nombre}")

    # Iterando sobre una cadena de texto
    print("\nIterando sobre una cadena:")
    for letra in "Python":
        print(letra)

    # Uso de `break` y `continue`
    # `break`: sale del bucle completamente.
    # `continue`: salta a la siguiente iteración del bucle.
    print("\n## break y continue")
    for numero in range(10):
        if numero == 3:
            print("Encontré el 3, saliendo del bucle...")
            break  # El bucle se detiene
        if numero % 2 == 0:
            continue # Salta a la siguiente iteración si el número es par
        print(f"Número impar: {numero}")

    # Bucle `for` con `enumerate()`
    # `enumerate()` añade un contador a un iterable, devolviendo una tupla (índice, valor).
    print("\n## Bucle con `enumerate()`")
    frutas = ["manzana", "banana", "cereza"]
    for indice, fruta in enumerate(frutas):
        print(f"La fruta en el índice {indice} es: {fruta}")

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 8. FUNCIONES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def funciones():
    """
    Las funciones permiten dividir un programa en secciones reutilizables,
    lo que hace el código más organizado y fácil de mantener.
    Se definen con la palabra clave `def`.
    """
    print("\n--- 8. Funciones ---")
    
    # Función básica
    # La función 'sumar' acepta dos parámetros y retorna su suma.
    def sumar(a, b):
        return a + b

    resultado = sumar(5, 3)
    print("## Función básica")
    print(f"El resultado de la suma de 5 y 3 es: {resultado}")

    # Parámetros por defecto
    # Se puede asignar un valor por defecto a un parámetro. Si el usuario
    # no proporciona un valor para ese parámetro, se usará el predeterminado.
    def saludar(nombre, mensaje="Hola"):
        return f"{mensaje}, {nombre}!"

    print("\n## Parámetros por defecto")
    print(saludar("Andrés"))
    print(saludar("Andrés", "Qué tal"))

    # Argumentos de palabra clave (keyword arguments)
    # Permiten pasar argumentos en cualquier orden usando el nombre del parámetro.
    def describir_persona(nombre, edad, ciudad):
        return f"{nombre} tiene {edad} años y vive en {ciudad}."

    print("\n## Argumentos de palabra clave")
    print(describir_persona(edad=24, nombre="Tatiana", ciudad="Suiza"))

    # Número variable de argumentos (*args y **kwargs)
    # *args: Acepta un número variable de argumentos posicionales como una tupla.
    # **kwargs: Acepta un número variable de argumentos de palabra clave como un diccionario.
    def funcion_flexible(*args, **kwargs):
        print("\n## Función con *args y **kwargs")
        print(f"Argumentos posicionales (*args): {args}")
        print(f"Argumentos de palabra clave (**kwargs): {kwargs}")

    funcion_flexible(1, 2, 3, nombre="Oliver", pais="España")

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 9. CLASES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def clases():
    """
    Las clases son el pilar de la programación orientada a objetos (POO) en Python.
    Permiten crear plantillas para definir objetos, que pueden tener atributos
    (variables que almacenan datos) y métodos (funciones que operan sobre esos datos).
    """
    print("\n--- 9. Clases ---")

    # Definición de una clase
    # La clase 'Persona' sirve como un modelo para crear objetos de tipo Persona.
    class Persona:
        # Atributo de clase: un atributo compartido por todas las instancias de la clase.
        especie = "Humano"

        # Método constructor: __init__()
        # Se ejecuta automáticamente al crear una nueva instancia de la clase.
        # 'self' es una referencia a la instancia actual del objeto.
        def __init__(self, nombre, edad):
            self.nombre = nombre  # Atributo de instancia: único para cada objeto.
            self.edad = edad      # Atributo de instancia.

        # Método de instancia
        # 'self' es necesario para acceder a los atributos del objeto.
        def saludar(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
        # Método de clase: @classmethod
        # Opera sobre la clase misma, no sobre una instancia específica.
        # Usa 'cls' como primer parámetro, que se refiere a la clase.
        @classmethod
        def get_especie(cls):
            return f"Esta es una clase de la especie: {cls.especie}"

    # Creación de objetos (instancias de la clase)
    persona1 = Persona("Palacio", 26)
    persona2 = Persona("Tatiana", 24)

    # Acceder a atributos y llamar a métodos
    print("## Creando y usando instancias")
    persona1.saludar()
    print(f"El atributo de clase 'especie' es: {persona2.especie}")
    print(Persona.get_especie())

    # Herencia
    # La clase 'Estudiante' hereda de 'Persona', lo que significa que
    # obtiene todos los atributos y métodos de la clase padre.
    class Estudiante(Persona):
        def __init__(self, nombre, edad, grado):
            # Llama al constructor de la clase padre (Persona) para inicializar
            # los atributos 'nombre' y 'edad'.
            super().__init__(nombre, edad)
            self.grado = grado # Atributo de instancia propio de Estudiante.

        # Sobreescribir un método
        # Se redefine el método 'saludar' para que se adapte a la clase 'Estudiante'.
        def saludar(self):
            print(f"Hola, soy un estudiante llamado {self.nombre}, tengo {self.edad} años y estoy en el grado {self.grado}.")

    print("\n## Herencia (Clase Estudiante)")
    estudiante1 = Estudiante("Andrés", 20, "12°")
    estudiante1.saludar()

# =================================================================================================================
#                           ▀▄▀▄▀▄⡷⠂ 10. MÓDULOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def modulos():
    """
    Los módulos son archivos de Python (.py) que contienen código (funciones, clases y variables)
    que se puede reutilizar en otros programas.
    Esto ayuda a organizar y estructurar proyectos grandes.
    """
    print("\n--- 10. Módulos ---")

    # Importación completa de un módulo
    # Se importa todo el módulo 'math' y se accede a sus funciones con el prefijo 'math.'.
    print("## Importación completa del módulo")
    import math
    x = 16
    raiz_cuadrada = math.sqrt(x)
    print(f"La raíz cuadrada de {x} es: {raiz_cuadrada}")
    print(f"El valor de pi es: {math.pi}")

    # Importación de una función específica de un módulo
    # Se importa solo la función 'sin' del módulo 'math'.
    # Esto evita tener que usar el prefijo del módulo.
    print("\n## Importación de un elemento específico")
    from math import sin
    print(f"El seno de 0 es: {sin(0)}")

    # Importación con alias
    # Se le da un nombre corto (alias) al módulo para facilitar su uso.
    print("\n## Importación con alias")
    import random as rd
    numero_aleatorio = rd.randint(1, 100)
    print(f"Un número aleatorio entre 1 y 100 es: {numero_aleatorio}")

    # Creando y usando tu propio módulo
    # Para este ejemplo, imagina que tienes un archivo llamado 'mi_modulo.py' con una función 'saludar'.
    # Para importarlo, simplemente se usa el nombre del archivo (sin la extensión .py).
    print("\n## Creando tu propio módulo")
    # from mi_modulo import saludar
    # saludar("Andrés")
    print("Para este ejemplo, se importaría un archivo llamado 'mi_modulo.py'.")
    print("Si tienes un archivo con 'def saludar(nombre): ...', puedes importarlo y usarlo.")

# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 11. FUNCIONES LAMBDA ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def funciones_lambda():
    """
    Las funciones lambda son funciones anónimas, pequeñas y temporales,
    definidas con la palabra clave `lambda`. Son ideales para operaciones
    simples que no requieren una definición completa de una función.
    """
    print("\n--- 11. Funciones Lambda ---")
    
    # Sintaxis básica: lambda argumentos: expresión
    # La expresión es lo que se retorna. Solo puede haber una expresión.
    
    # 1. Ejemplo básico de suma
    # Se asigna la función lambda a una variable, y luego se llama como una función normal.
    suma = lambda a, b: a + b
    print(f"Suma con lambda: {suma(3, 5)}")

    # 2. Uso con `filter()`
    # `filter()` crea un iterable con los elementos que cumplen la condición.
    # La función lambda actúa como la condición, retornando `True` o `False`.
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"\nNúmeros pares (usando filter()): {pares}")

    # 3. Uso con `map()`
    # `map()` aplica una función a cada elemento de un iterable.
    # Aquí, la función lambda eleva cada número al cuadrado.
    cuadrados = list(map(lambda x: x * x, numeros))
    print(f"Números al cuadrado (usando map()): {cuadrados}")

    # 4. Uso en la ordenación de listas (sort/sorted)
    # Las lambdas son muy útiles como argumentos clave para ordenar colecciones.
    # Ordenar una lista de tuplas por el segundo elemento (la edad).
    personas = [("Andrés", 28), ("Tatiana", 24), ("Oliver", 7)]
    personas_ordenadas = sorted(personas, key=lambda persona: persona[1])
    print(f"\nLista de personas ordenada por edad: {personas_ordenadas}")

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 12. GENERADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def generadores():
    """
    Los generadores son una forma eficiente de crear iteradores en Python.
    A diferencia de las funciones que retornan una lista completa, los generadores
    retornan un valor a la vez usando la palabra clave `yield`.
    Esto los hace extremadamente eficientes en el manejo de grandes conjuntos de datos,
    ya que no almacenan todos los elementos en la memoria simultáneamente.
    """
    print("\n--- 12. Generadores ---")
    
    # Función generadora básica
    # `yield` pausa la ejecución de la función, retorna el valor
    # y guarda el estado local para reanudar la ejecución en la siguiente llamada.
    def even_numbers(n):
        print("El generador ha sido llamado.")
        for i in range(n):
            yield i * 2
            print(f"Generado: {i * 2}")

    print("## Ejemplo de Generador")
    print("Primeros 5 números pares:")
    
    # Almacenar el generador en una variable
    pares_generador = even_numbers(5)
    
    # Iterar sobre el generador
    # El bucle 'for' pide un nuevo valor del generador en cada iteración.
    for num in pares_generador:
        print(f"Valor recibido: {num}")

    # Demostración de la eficiencia de memoria vs. una lista
    print("\n## Generador vs. Lista (eficiencia de memoria)")
    
    # Generador (evaluación perezosa)
    def generador_grande(n):
        for i in range(n):
            yield i

    # Lista (almacenamiento en memoria)
    def lista_grande(n):
        return [i for i in range(n)]

    # Nota: No se ejecutará la función `lista_grande` con un número muy alto para no
    # consumir memoria real, pero la explicación es clave.
    print("Un generador crea los valores 'uno por uno', lo que es eficiente en memoria.")
    print("Una lista crea todos los valores a la vez, lo que puede consumir mucha memoria.")
    
    # Ejemplo de uso práctico con un bucle for
    print("\nEjemplo práctico: Imprimir los primeros 3 números de un generador de 1000.")
    generador = generador_grande(1000)
    for i in range(3):
        print(f"Valor del generador: {next(generador)}")

    print("\n## Expresión Generadora y next()")
    
    """
    La Expresión Generadora es una forma concisa (implica 'yield' automáticamente) 
    de crear un generador sin definir una función con 'def'.
    Se usa principalmente para filtros y búsquedas sencillas en línea.
    
    La función 'next(generador, valor_por_defecto)' es el método para consumir
    explícitamente un generador y obtener el siguiente valor. Es ideal para buscar
    el primer elemento coincidente en una lista.
    """
    
    data = [
        {"id": 101, "name": "A"}, 
        {"id": 102, "name": "B"}, 
        {"id": 103, "name": "C"}
    ]
    target_id = 102
    
    # 1. Creación de la Expresión Generadora (el 'yield' es implícito)
    # Crea un generador que solo producirá el cliente con el ID 102 (o nada).
    generator_expression = (client for client in data if client.get("id") == target_id)
    
    print(f"Buscando ID: {target_id}")
    # 2. Uso de next() para consumir el primer (y único) valor del generador.
    # El segundo argumento (None) es el valor por defecto si no se encuentra nada.
    found_item = next(generator_expression, None)
    
    print(f"Resultado de next(): {found_item}")
    
    # Ejemplo de no encontrado
    target_id_fail = 999
    generator_fail = (client for client in data if client.get("id") == target_id_fail)
    not_found_item = next(generator_fail, "NO ENCONTRADO")
    
    print(f"\nBuscando ID: {target_id_fail}")
    print(f"Resultado de next() (con valor por defecto): {not_found_item}")
    
    print("\n El uso de next() con una Expresión Generadora detiene la iteración en el primer match, siendo muy eficiente para búsquedas.")

# =================================================================================================================
#                    ▀▄▀▄▀▄⡷⠂ 13. MANEJO DE EXCEPCIONES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def manejo_de_excepciones():
    """
    Las sentencias `try`, `except`, `else` y `finally` permiten controlar
    y gestionar errores (excepciones) de forma elegante sin que el programa
    se detenga abruptamente.
    """
    print("\n--- 13. Manejo de Excepciones ---")

    # Ejemplo 1: Manejo de un solo tipo de excepción
    def division(a, b):
        print("\n## Ejemplo de 'try', 'except', 'else' y 'finally'")
        try:
            # El código dentro de 'try' se ejecuta primero.
            resultado = a / b
        except ZeroDivisionError:
            # Si ocurre un 'ZeroDivisionError', se ejecuta este bloque.
            print("Error: No se puede dividir por cero.")
        except TypeError:
            # Si ocurre un 'TypeError' (por ejemplo, con cadenas de texto), se ejecuta este bloque.
            print("Error: Los argumentos deben ser números.")
        except Exception as e:
            # Capturar cualquier otro tipo de excepción. 'as e' guarda el objeto del error.
            print(f"Ocurrió un error inesperado: {e}")
        else:
            # Si el bloque 'try' se ejecuta sin errores, se ejecuta 'else'.
            print(f"El resultado es: {resultado}")
        finally:
            # Este bloque se ejecuta siempre, haya o no una excepción.
            # Es útil para cerrar archivos o liberar recursos.
            print("Operación finalizada.")

    # Pruebas con diferentes escenarios
    print("\n### Caso 1: División exitosa")
    division(10, 2)
    
    print("\n### Caso 2: División por cero")
    division(10, 0)

    print("\n### Caso 3: Tipo de dato incorrecto")
    division(10, "2")
    
    # Ejemplo 2: Uso en la práctica
    # Un ejemplo más realista de cómo se usaría en una aplicación.
    print("\n## Ejemplo práctico: Convertir una entrada de usuario a un número")
    entrada = "abc"
    try:
        numero = int(entrada)
    except ValueError:
        print(f"El valor '{entrada}' no es un número válido.")
    else:
        print(f"Entrada válida: {numero}")
    
    entrada_valida = "123"
    try:
        numero = int(entrada_valida)
    except ValueError:
        print(f"El valor '{entrada_valida}' no es un número válido.")
    else:
        print(f"Entrada válida: {numero}")

# =================================================================================================================
#                     ▀▄▀▄▀▄⡷⠂ 14. MANEJO DE ARCHIVOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
import os

def manejo_de_archivos():
    """
    Python permite leer y escribir archivos de manera sencilla y segura.
    Se recomienda usar la sentencia `with open(...)` ya que asegura que el archivo
    se cierre automáticamente, incluso si ocurre un error, lo que previene fugas
    de memoria y corrupción de datos.
    """
    print("\n--- 14. Manejo de Archivos ---")
    file_path = "ejemplo_archivo.txt"

    # Modo 'w': Escribir (sobrescribe el contenido si el archivo ya existe)
    # Si el archivo no existe, lo crea.
    print("\n## Modo 'w' (Write): Escribir")
    with open(file_path, "w") as f:
        f.write("¡Hola, mundo!\n")
        f.write("Este es un archivo de prueba.")

    print(f"Archivo '{file_path}' creado y escrito (sobrescrito).")

    # Modo 'r': Leer
    # Si el archivo no existe, genera un error.
    print("\n## Modo 'r' (Read): Leer")
    with open(file_path, "r") as f:
        contenido_completo = f.read()
        print(f"Contenido completo del archivo:\n{contenido_completo}")

    # Modo 'a': Añadir (Append)
    # Si el archivo ya existe, añade el nuevo contenido al final.
    print("\n## Modo 'a' (Append): Añadir")
    with open(file_path, "a") as f:
        f.write("\n\nEsta línea se añadió al final.")

    # Volver a leer el archivo para ver el contenido añadido
    with open(file_path, "r") as f:
        contenido_actualizado = f.read()
        print(f"Contenido del archivo después de añadir:\n{contenido_actualizado}")
    
    # Leer el archivo línea por línea
    # El método .readlines() devuelve una lista de las líneas del archivo.
    print("\n## Leer línea por línea")
    with open(file_path, "r") as f:
        lineas = f.readlines()
        print("Líneas leídas (con '\\n'):")
        print(lineas)
    
    # Limpieza: Eliminar el archivo de prueba
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"\nArchivo '{file_path}' eliminado.")
    else:
        print(f"\nEl archivo '{file_path}' ya no existe.")

# =================================================================================================================
#                      ▀▄▀▄▀▄⡷⠂ 15. EXPRESIONES REGULARES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
import re

def expresiones_regulares():
    """
    Las expresiones regulares son secuencias de caracteres que forman un patrón
    de búsqueda. El módulo `re` de Python se utiliza para buscar, manipular y
    validar texto basándose en estos patrones.
    """
    print("\n--- 15. Expresiones Regulares ---")
    texto = "La lluvia en Sevilla es una maravilla."
    patron = r"lluvia"

    # re.search(): Busca el patrón en cualquier parte del texto.
    # Devuelve un objeto de coincidencia si lo encuentra, de lo contrario, devuelve None.
    print("\n## re.search() - Búsqueda de un patrón")
    resultado = re.search(patron, texto)

    if resultado:
        print(f"Se ha encontrado el patrón '{patron}' en el texto.")
        print(f"Coincidencia encontrada en la posición: {resultado.span()}")
    else:
        print(f"No se ha encontrado el patrón '{patron}'.")
        
    # re.match(): Busca el patrón al inicio del texto.
    # Solo coincide si el patrón está en el principio.
    print("\n## re.match() - Coincidencia al inicio")
    patron_inicio = r"La"
    resultado_match = re.match(patron_inicio, texto)
    if resultado_match:
        print(f"El patrón '{patron_inicio}' coincide al inicio del texto.")
    
    # re.findall(): Devuelve una lista de todas las coincidencias.
    print("\n## re.findall() - Encontrar todas las coincidencias")
    texto_numeros = "Mi número es 123-456-7890 y el otro es 987-654-3210."
    patron_telefono = r"\d{3}-\d{3}-\d{4}" # \d para dígitos, {n} para número de repeticiones
    numeros_encontrados = re.findall(patron_telefono, texto_numeros)
    print(f"Números de teléfono encontrados: {numeros_encontrados}")
    
    # re.sub(): Reemplaza las coincidencias con otro texto.
    print("\n## re.sub() - Reemplazar texto")
    texto_reemplazar = "El perro es mi animal favorito. El perro es muy leal."
    patron_reemplazo = "perro"
    nuevo_texto = re.sub(patron_reemplazo, "gato", texto_reemplazar)
    print(f"Texto original: '{texto_reemplazar}'")
    print(f"Texto modificado: '{nuevo_texto}'")

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 16. DECORADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
import time

def decoradores():
    """
    Los decoradores son funciones que toman otra función como argumento,
    le añaden nueva funcionalidad, y devuelven la función modificada.
    Permiten agregar comportamiento a una función o clase sin alterar
    su código original, siguiendo el principio de "código abierto/cerrado".
    """
    print("\n--- 16. Decoradores ---")
    
    # 1. Ejemplo de un decorador de registro (más simple)
    # Este decorador solo añade un print antes y después de la función.
    def mi_decorador(func):
        def envoltura():
            print("Algo está sucediendo antes de llamar a la función.")
            func() # Llamamos a la función original
            print("Algo está sucediendo después de llamar a la función.")
        return envoltura

    @mi_decorador
    def saludar():
        print("¡Hola a todos!")
    
    print("\n## Ejemplo de decorador simple")
    saludar()
    
    # 2. Ejemplo práctico: Decorador para medir el tiempo de ejecución
    # Este es un decorador más avanzado que usa los argumentos de la función.
    def time_it(func):
        # 'wrapper' es la función que reemplazará a la original.
        # Usa *args y **kwargs para aceptar cualquier tipo de argumento.
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"'{func.__name__}' tardó {end - start:.4f} segundos en ejecutarse.")
            return result # Es importante retornar el resultado de la función original
        return wrapper

    @time_it
    def mi_funcion_lenta():
        """Una función que simula un proceso largo."""
        time.sleep(1.5) # Pausa la ejecución por 1.5 segundos
        print("¡Función lenta terminada!")
    
    @time_it
    def sumar(a, b):
        """Una función que suma dos números."""
        print(f"Calculando la suma de {a} y {b}...")
        time.sleep(0.5)
        return a + b
    
    print("\n## Ejemplo práctico: Medir el tiempo de ejecución")
    mi_funcion_lenta()
    
    resultado_suma = sumar(5, 7)
    print(f"El resultado de la suma es: {resultado_suma}")

# =================================================================================================================
#                      ▀▄▀▄▀▄⡷⠂ 17. CONTEXT MANAGERS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
import os

def context_managers():
    """
    Los `context managers` son objetos que definen un contexto temporal para la ejecución
    de un bloque de código. Garantizan que los recursos (como archivos, conexiones
    a bases de datos o bloqueos de red) se manejen de forma segura, asegurando
    que se liberen o cierren correctamente, incluso si ocurren errores.
    """
    print("\n--- 17. Context Managers ---")
    
    # 1. Ejemplo de uso común: Manejo de archivos
    # `with` invoca el método __enter__ del objeto 'open' al inicio
    # y el método __exit__ al final, asegurando que el archivo se cierre.
    print("## Uso de un context manager integrado (archivos)")
    file_path = "temp.txt"
    try:
        with open(file_path, "w") as f:
            f.write("Este archivo se cierra automáticamente.")
        print(f"Archivo '{file_path}' escrito y cerrado.")
    except IOError as e:
        print(f"Error al manejar el archivo: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    # 2. Ejemplo de cómo crear tu propio context manager
    # Un objeto con los métodos __enter__() y __exit__().
    # __enter__(): se ejecuta al inicio del bloque `with`.
    # __exit__(): se ejecuta al final, incluso si hay una excepción.
    class Temporizador:
        def __enter__(self):
            self.inicio = time.time()
            print("\nIniciando temporizador...")
            return self

        def __exit__(self, tipo_exc, valor_exc, traceback_exc):
            fin = time.time()
            duracion = fin - self.inicio
            print(f"Deteniendo temporizador. Duración: {duracion:.4f} segundos.")
            # Si hay una excepción, __exit__ puede manejarla.
            if valor_exc:
                print(f"Se capturó una excepción: {tipo_exc}, {valor_exc}")
                return True # Retornar True suprime la excepción.

    # Usando el context manager personalizado
    print("\n## Creando tu propio context manager")
    with Temporizador():
        print("Realizando una operación que requiere un temporizador...")
        time.sleep(1.2) # Simula un proceso
        
    print("\n--- Demostración de manejo de excepciones ---")
    try:
        with Temporizador():
            print("Realizando una operación con un posible error...")
            time.sleep(0.5)
            raise ValueError("¡Algo salió mal!") # Genera una excepción
    except ValueError as e:
        print(f"Excepción capturada fuera del context manager: {e}")

# =================================================================================================================
#                      ▀▄▀▄▀▄⡷⠂ 18. MÉTODOS MÁGICOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def metodos_magicos():
    """
    Los métodos mágicos, también conocidos como "dunder methods" (por sus
    guiones bajos dobles), permiten definir un comportamiento especial para
    tus clases. Son la forma en que Python implementa la sobrecarga de
    operadores, lo que te permite usar operadores estándar como +, -,
    <, > con tus propios objetos.
    """
    print("\n--- 18. Métodos Mágicos ---")
    
    class Numero:
        def __init__(self, valor):
            """Constructor: Se llama al crear una nueva instancia del objeto."""
            self.valor = valor

        def __add__(self, otro_numero):
            """
            Método para el operador de suma (+).
            Define el comportamiento de la suma entre dos objetos 'Numero'.
            """
            return Numero(self.valor + otro_numero.valor)

        def __gt__(self, otro_numero):
            """
            Método para el operador "mayor que" (>).
            Define el comportamiento de la comparación entre dos objetos.
            """
            return self.valor > otro_numero.valor

        def __str__(self):
            """
            Método para representación de cadena (string).
            Define el comportamiento de la función `str()` y `print()`.
            Debe ser una representación legible para el usuario.
            """
            return f"Numero con valor: {self.valor}"

        def __repr__(self):
            """
            Método para representación "oficial".
            Define el comportamiento que se debe ver en la consola al
            inspeccionar el objeto. Idealmente, debería ser un string
            que permita recrear el objeto.
            """
            return f"Numero({self.valor})"

    numero_1 = Numero(10)
    numero_2 = Numero(5)
    numero_3 = Numero(10)

    print("\n## Demostración de operadores")
    
    # Uso de __add__
    suma_objetos = numero_1 + numero_2
    print(f"Suma de objetos: {suma_objetos}")
    
    # Uso de __gt__
    print(f"¿Es numero_1 > numero_2?: {numero_1 > numero_2}")
    print(f"¿Es numero_1 > numero_3?: {numero_1 > numero_3}")
    
    print("\n## Representación del objeto")
    
    # Uso de __str__ (con print)
    print(f"Uso de __str__: {numero_1}")
    
    # Uso de __repr__ (en la consola)
    print(f"Uso de __repr__: {repr(numero_1)}")

    # Nota: si __str__ no está definido, Python usará __repr__.
    # Si __repr__ no está definido, se usa una representación por defecto.
    # Es una buena práctica definir ambos.

# =================================================================================================================
# ▀▄▀▄▀▄⡷⠂ 𝐄𝐉𝐄𝐂𝐔𝐂𝐈𝐎́𝐍 𝐃𝐄 𝐋𝐀 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓𝐀𝐂𝐈𝐎́𝐍 ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def main():
    """
    Función principal que ejecuta todos los ejemplos.
    """
    print("--- 📚 INICIANDO LA DOCUMENTACIÓN DE PYTHON 📚 ---")
    generate_toc()
    variables()
    listas()
    tuplas()
    diccionarios()
    operadores()
    condicionales()
    bucles()
    funciones()
    clases()
    modulos()
    funciones_lambda()
    generadores()
    manejo_de_excepciones()
    manejo_de_archivos()
    expresiones_regulares()
    decoradores()
    context_managers()
    metodos_magicos()
    print("\n--- ✅ DOCUMENTACIÓN COMPLETADA ✅ ---")

if __name__ == "__main__":
    main()