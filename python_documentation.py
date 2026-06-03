
# =================================================================================================================
# ▀▄▀▄▀▄⡷⠂ 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓𝐀𝐂𝐈𝐎́𝐍 𝐃𝐄 𝐏𝐘𝐓𝐇𝐎𝐍 ⠐⢾▀▄▀▄▀▄
# Creado por: Andrés Palacio Velásquez
# =================================================================================================================

# ─── Imports (PEP 8: siempre al inicio del archivo, agrupados por tipo) ───
import math
import os
import random
import re
import sys
import time
from abc import ABC, abstractmethod
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass, field
from functools import wraps
from itertools import chain, islice, groupby
from typing import Optional

# Configurar stdout para soportar UTF-8 en Windows (emojis y caracteres especiales)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def generate_toc():
    """Genera una tabla de contenido basada en los nombres de las funciones."""
    print("--- 📋 𝐓𝐀𝐁𝐋𝐀 𝐃𝐄 𝐂𝐎𝐍𝐓𝐄𝐍𝐈𝐃𝐎 📋 ---")
    toc_items = [
        "",
        "  BLOQUE 1: DATOS Y TIPOS",
        "    1.  Variables y Tipos de Datos",
        "    2.  Strings",
        "    3.  Listas",
        "    4.  Tuplas",
        "    5.  Sets (Conjuntos)",
        "    6.  Diccionarios",
        "    7.  Comprehensions",
        "",
        "  BLOQUE 2: CONTROL DE FLUJO",
        "    8.  Operadores",
        "    9.  Condicionales",
        "    10. Bucles",
        "",
        "  BLOQUE 3: FUNCIONES",
        "    11. Funciones",
        "    12. Funciones Lambda",
        "    13. Closures (Cierres)",
        "    14. Decoradores",
        "    15. Generadores",
        "",
        "  BLOQUE 4: PROGRAMACIÓN ORIENTADA A OBJETOS",
        "    16. Clases",
        "    17. OOP Avanzado",
        "    18. Métodos Mágicos (Dunder Methods)",
        "    19. Dataclasses",
        "",
        "  BLOQUE 5: ROBUSTEZ Y GESTIÓN DE RECURSOS",
        "    20. Manejo de Excepciones",
        "    21. Excepciones Personalizadas",
        "    22. Context Managers",
        "    23. Manejo de Archivos",
        "",
        "  BLOQUE 6: BIBLIOTECA ESTÁNDAR Y HERRAMIENTAS",
        "    24. Módulos",
        "    25. Expresiones Regulares",
        "    26. Collections e Itertools",
        "    27. Type Hints (Tipado Estático)",
        "",
        "  BLOQUE 7: ARQUITECTURA Y RENDIMIENTO",
        "    28. Entornos Virtuales (venv)",
        "    29. Concurrencia y Async (GIL, Threads, Asyncio)",
        "    30. Rendimiento y Fugas de Memoria",
        "",
        "  BONUS",
        "    31. Próximos Pasos (Frameworks y Librerías)",
    ]
    for item in toc_items:
        print(item)
    print("───────────────────────────────────────")


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 1: DATOS Y TIPOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 1. VARIABLES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def variables():
    """
    En Python, no es necesario especificar el tipo de variable,
    ya que es un lenguaje de programación de tipado dinámico.
    """
    print("\n--- 1. Variables y Tipos de Datos ---")
    
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

    # Intercambio de valores (swap)
    # Un caso especial de asignación múltiple para intercambiar valores fácilmente.
    print(f"Valores antes del intercambio: a = {a}, b = {b}")
    a, b = b, a
    print(f"Valores después del intercambio: a = {a}, b = {b}")

    # Constantes por convención
    # Python no tiene un tipo 'constante' nativo. Se usa MAYÚSCULAS como convención.
    PI = 3.14159
    MAX_CONEXIONES = 100
    print(f"\nConstantes (por convención): PI = {PI}, MAX_CONEXIONES = {MAX_CONEXIONES}")


# =================================================================================================================
#                          ▀▄▀▄▀▄⡷⠂ 2. STRINGS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def strings():
    """
    Las cadenas de texto (strings) son secuencias inmutables de caracteres.
    Python ofrece una rica colección de métodos para manipularlas.
    """
    print("\n--- 2. Strings ---")

    texto = "  Hola, Mundo Python  "

    # Métodos de limpieza
    print("## Métodos de limpieza")
    print(f"Original:             '{texto}'")
    print(f".strip():             '{texto.strip()}'")       # Elimina espacios al inicio y final
    print(f".lstrip():            '{texto.lstrip()}'")      # Solo al inicio (left)
    print(f".rstrip():            '{texto.rstrip()}'")      # Solo al final (right)

    # Métodos de búsqueda y verificación
    print("\n## Búsqueda y verificación")
    frase = "Python es un lenguaje versátil"
    print(f"Frase: '{frase}'")
    print(f".startswith('Python'): {frase.startswith('Python')}")
    print(f".endswith('versátil'): {frase.endswith('versátil')}")
    print(f".find('lenguaje'):     {frase.find('lenguaje')}")      # Índice o -1
    print(f".count('e'):           {frase.count('e')}")
    print(f"'Python' in frase:     {'Python' in frase}")

    # Métodos de transformación
    print("\n## Transformación")
    print(f".upper():   '{frase.upper()}'")
    print(f".lower():   '{frase.lower()}'")
    print(f".title():   '{frase.title()}'")
    print(f".capitalize(): '{frase.capitalize()}'")
    print(f".swapcase(): '{frase.swapcase()}'")

    # Métodos de división y unión
    print("\n## Split y Join")
    palabras = frase.split()                   # Divide por espacios (por defecto)
    print(f".split():     {palabras}")
    csv_data = "uno,dos,tres"
    print(f".split(','):  {csv_data.split(',')}")

    # .join() — une una lista de strings con un separador
    unido = " - ".join(palabras)
    print(f"' - '.join(): '{unido}'")

    # Reemplazo
    print("\n## Reemplazo")
    print(f".replace('Python', 'Java'): '{frase.replace('Python', 'Java')}'")

    # f-strings avanzadas (Python 3.6+)
    print("\n## f-strings avanzadas")
    precio = 49.956
    cantidad = 3
    print(f"Precio formateado:   {precio:.2f}")                # 2 decimales
    print(f"Total:               {precio * cantidad:>10.2f}")   # Alineado a la derecha, 10 chars
    print(f"Binario de 42:       {42:b}")                       # En binario
    print(f"Hexadecimal de 255:  {255:#x}")                     # En hexadecimal
    print(f"Con separador miles: {1_000_000:,}")                # Con comas

    # Strings multilínea y raw strings
    print("\n## Strings multilínea y raw strings")
    multi = """Esta es
una cadena
multilínea."""
    print(f"Multilínea:\n{multi}")

    # Raw strings: no interpretan secuencias de escape (\n, \t, etc.)
    raw = r"Esto NO es un salto de línea: \n, es texto literal."
    print(f"\nRaw string: {raw}")


# =================================================================================================================
#                           ▀▄▀▄▀▄⡷⠂ 3. LISTAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def listas():
    """
    Una lista en Python es una colección ordenada y mutable de elementos.
    Se definen entre corchetes `[]` y los elementos se separan por comas.
    """
    print("\n--- 3. Listas ---")
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
#                           ▀▄▀▄▀▄⡷⠂ 4. TUPLAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def tuplas():
    """
    Una tupla en Python es una colección ordenada e inmutable de elementos.
    Se definen entre paréntesis `()`.
    """
    print("\n--- 4. Tuplas ---")
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

    # Desempaquetado extendido con el operador *
    primero, *resto = (1, 2, 3, 4, 5)
    print(f"Desempaquetado extendido: primero={primero}, resto={resto}")

    *inicio, ultimo = (10, 20, 30, 40)
    print(f"Desempaquetado extendido: inicio={inicio}, ultimo={ultimo}")
    
    # Métodos de las tuplas
    # Las tuplas solo tienen dos métodos debido a su inmutabilidad.
    print(f"\nNúmero de veces que aparece '2': {mi_tupla.count(2)}")
    print(f"Índice del elemento 'Hola': {mi_tupla.index('Hola')}")

    # Conversión de tupla a lista (para mutabilidad)
    # A menudo se convierte una tupla en una lista para poder modificarla.
    mi_lista = list(mi_tupla)
    print(f"\nTupla convertida a lista: {mi_lista}")
    mi_lista.append("Nuevo elemento")
    mi_nueva_tupla = tuple(mi_lista)
    print(f"Lista convertida de nuevo a tupla: {mi_nueva_tupla}")


# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 5. SETS (CONJUNTOS) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def sets():
    """
    Un set (conjunto) es una colección desordenada de elementos únicos.
    Se definen entre llaves `{}`. Son mutables, pero sus elementos deben ser
    inmutables (hashables). Son ideales para eliminar duplicados y realizar
    operaciones matemáticas de conjuntos.
    """
    print("\n--- 5. Sets (Conjuntos) ---")

    # Creación de sets
    mi_set = {1, 2, 3, 3, 4, 4, 5}
    print(f"Set (duplicados eliminados automáticamente): {mi_set}")

    # Set vacío — NO usar {}, eso crea un diccionario vacío
    set_vacio = set()
    print(f"Set vacío: {set_vacio}, Tipo: {type(set_vacio)}")
    print(f"Cuidado: type({{}}) es {type({})}")  # dict, no set

    # Crear un set desde una lista (para eliminar duplicados)
    lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
    sin_duplicados = set(lista_con_duplicados)
    print(f"\nLista original:       {lista_con_duplicados}")
    print(f"Set (sin duplicados): {sin_duplicados}")

    # Métodos de modificación
    print("\n## Métodos de modificación")
    mi_set.add(6)
    print(f"Después de .add(6):     {mi_set}")
    mi_set.discard(3)       # No lanza error si el elemento no existe
    print(f"Después de .discard(3): {mi_set}")
    # mi_set.remove(99)     # Lanzaría KeyError si no existe

    # Operaciones de conjuntos
    print("\n## Operaciones de conjuntos")
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(f"Set A: {a}")
    print(f"Set B: {b}")

    # Unión: todos los elementos de ambos sets
    print(f"A | B  (Unión):                {a | b}")
    print(f"A.union(B):                    {a.union(b)}")

    # Intersección: elementos comunes
    print(f"A & B  (Intersección):         {a & b}")
    print(f"A.intersection(B):             {a.intersection(b)}")

    # Diferencia: elementos en A que NO están en B
    print(f"A - B  (Diferencia):           {a - b}")
    print(f"A.difference(B):               {a.difference(b)}")

    # Diferencia simétrica: elementos que están en uno u otro, pero no en ambos
    print(f"A ^ B  (Diferencia simétrica): {a ^ b}")
    print(f"A.symmetric_difference(B):     {a.symmetric_difference(b)}")

    # Tests de pertenencia — O(1), mucho más rápido que en listas O(n)
    print(f"\n¿3 in A?: {3 in a}  (Búsqueda O(1), muy eficiente)")

    # Subconjuntos y superconjuntos
    c = {1, 2, 3}
    print(f"\n¿{c} es subconjunto de {a}?:   {c.issubset(a)}")
    print(f"¿{a} es superconjunto de {c}?: {a.issuperset(c)}")

    # Frozenset: versión inmutable del set (puede usarse como clave de diccionario)
    print("\n## Frozenset (set inmutable)")
    inmutable = frozenset([1, 2, 3])
    print(f"Frozenset: {inmutable}, Tipo: {type(inmutable)}")


# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 6. DICCIONARIOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def diccionarios():
    """
    Un diccionario en Python es una colección de pares clave-valor,
    mutables y ordenados por inserción (desde Python 3.7+).
    Se definen entre llaves `{}`.
    """
    print("\n--- 6. Diccionarios ---")
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

    # Operador de merge | (Python 3.9+)
    dict_a = {"x": 1, "y": 2}
    dict_b = {"y": 3, "z": 4}
    fusionado = dict_a | dict_b  # Las claves de dict_b prevalecen
    print(f"\nMerge con | (Python 3.9+): {fusionado}")

    # Método setdefault(): Obtiene el valor si existe, si no, lo crea con un valor por defecto
    mi_diccionario.setdefault("idioma", "Español")
    print(f"Después de setdefault('idioma', 'Español'): {mi_diccionario}")


# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 7. COMPREHENSIONS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def comprehensions():
    """
    Las comprehensions son una forma concisa y 'Pythónica' de crear
    listas, diccionarios y sets a partir de iterables existentes.
    Son más legibles y generalmente más rápidas que los bucles equivalentes.
    """
    print("\n--- 7. Comprehensions ---")

    # ─── List Comprehension ───
    # Sintaxis: [expresión for item in iterable if condición]
    print("## List Comprehension")

    # Equivalente a un bucle for con append
    cuadrados = [x**2 for x in range(10)]
    print(f"Cuadrados del 0 al 9: {cuadrados}")

    # Con condición (filtro)
    pares = [x for x in range(20) if x % 2 == 0]
    print(f"Pares del 0 al 19:    {pares}")

    # Con transformación condicional (if/else en la expresión)
    etiquetas = ["par" if x % 2 == 0 else "impar" for x in range(6)]
    print(f"Etiquetas:            {etiquetas}")

    # Comprensión anidada (equivale a bucles anidados)
    matriz = [[j for j in range(3)] for i in range(3)]
    print(f"Matriz 3x3:           {matriz}")

    # Aplanar una matriz
    plana = [elem for fila in matriz for elem in fila]
    print(f"Matriz aplanada:      {plana}")

    # ─── Dict Comprehension ───
    # Sintaxis: {clave: valor for item in iterable if condición}
    print("\n## Dict Comprehension")

    cuadrados_dict = {x: x**2 for x in range(6)}
    print(f"Dict de cuadrados: {cuadrados_dict}")

    # Invertir un diccionario (intercambiar claves y valores)
    original = {"a": 1, "b": 2, "c": 3}
    invertido = {v: k for k, v in original.items()}
    print(f"Original:  {original}")
    print(f"Invertido: {invertido}")

    # Filtrar un diccionario
    notas = {"Ana": 95, "Luis": 60, "Sofía": 85, "Pedro": 45}
    aprobados = {nombre: nota for nombre, nota in notas.items() if nota >= 70}
    print(f"Aprobados: {aprobados}")

    # ─── Set Comprehension ───
    # Sintaxis: {expresión for item in iterable if condición}
    print("\n## Set Comprehension")

    palabras = ["Hola", "HOLA", "hola", "Python", "python"]
    unicas = {p.lower() for p in palabras}
    print(f"Palabras únicas (lowercase): {unicas}")

    # ─── Expresión Generadora ───
    # Similar a una list comprehension, pero usa () en lugar de [].
    # NO crea toda la lista en memoria; genera valores bajo demanda.
    print("\n## Expresión Generadora (lazy evaluation)")
    suma_cuadrados = sum(x**2 for x in range(1000))
    print(f"Suma de cuadrados (0-999): {suma_cuadrados}")
    print("(Calculado sin crear una lista de 1000 elementos en memoria)")


# =================================================================================================================
#             ▀▄▀▄▀▄⡷⠂ BLOQUE 2: CONTROL DE FLUJO ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 8. OPERADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def operadores():
    """
    En Python, existen diversos tipos de operadores: aritméticos,
    de asignación, de comparación, lógicos, de identidad y de pertenencia.
    """
    print("\n--- 8. Operadores ---")
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
    a *= 4  # Equivalente a a = a * 4
    print(f"Después de 'a *= 4': {a}")
    a //= 3  # Equivalente a a = a // 3
    print(f"Después de 'a //= 3': {a}")

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
    # ⚠️ IMPORTANTE: `is` compara IDENTIDAD (mismo objeto en memoria), NO valor.
    #    Para comparar valores, SIEMPRE usa `==`.
    print("\n## Operadores de Identidad")
    print(f"¿x is z?: {x is z}")
    print("  ⚠️ Esto es True por el 'integer caching' de CPython (enteros -5 a 256")
    print("     se reutilizan en memoria). NO es un comportamiento garantizado del lenguaje.")
    
    # Demostración con enteros grandes (fuera del rango de caching)
    a_grande = 1000
    b_grande = 1000
    print(f"\na_grande = 1000, b_grande = 1000")
    print(f"¿a_grande == b_grande?: {a_grande == b_grande}")   # True — compara VALOR
    print(f"¿a_grande is b_grande?: {a_grande is b_grande}")   # Puede ser False
    print("  Regla: Usa `==` para valores, `is` solo para None, True, False.")

    # Operadores de Pertenencia
    # Verifican si un valor se encuentra dentro de una secuencia (lista, cadena, tupla, etc.).
    print("\n## Operadores de Pertenencia")
    mi_lista = [1, 2, 3]
    print(f"¿2 in mi_lista?: {2 in mi_lista}")
    print(f"¿4 not in mi_lista?: {4 not in mi_lista}")

    # Operador Walrus (:=) — Python 3.8+
    # Asigna un valor a una variable dentro de una expresión.
    print("\n## Operador Walrus (:=) — Python 3.8+")
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if (n := len(datos)) > 5:
        print(f"La lista tiene {n} elementos (más de 5)")


# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 9. CONDICIONALES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def condicionales():
    """
    Las sentencias `if`, `elif` y `else` controlan el flujo
    de un programa basándose en condiciones lógicas.
    """
    print("\n--- 9. Condicionales ---")
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

    # Expresión ternaria (condicional en una línea)
    print("\n## Expresión ternaria")
    estado = "aprobado" if calificacion >= 70 else "reprobado"
    print(f"Calificación {calificacion}: {estado}")

    # Match-case (Python 3.10+) — Structural Pattern Matching
    print("\n## Match-case (Python 3.10+)")
    codigo_http = 404
    match codigo_http:
        case 200:
            mensaje = "OK"
        case 301:
            mensaje = "Redirección permanente"
        case 404:
            mensaje = "No encontrado"
        case 500:
            mensaje = "Error interno del servidor"
        case _:
            mensaje = "Código desconocido"
    print(f"HTTP {codigo_http}: {mensaje}")


# =================================================================================================================
#                          ▀▄▀▄▀▄⡷⠂ 10. BUCLES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def bucles():
    """
    Los bucles (`while` y `for`) permiten repetir una sección de código.
    Son esenciales para automatizar tareas repetitivas sobre secuencias de datos.
    """
    print("\n--- 10. Bucles ---")

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

    # Bucle `for` con `zip()`
    # `zip()` combina dos o más iterables en tuplas.
    print("\n## Bucle con `zip()`")
    ciudades = ["Medellín", "Bogotá", "Cali"]
    poblaciones = [2_500_000, 7_400_000, 2_200_000]
    for ciudad, poblacion in zip(ciudades, poblaciones):
        print(f"{ciudad}: {poblacion:,} habitantes")

    # Cláusula `else` en bucles
    # Se ejecuta cuando el bucle termina normalmente (sin `break`).
    print("\n## Cláusula `else` en bucles")
    for n in range(2, 5):
        for divisor in range(2, n):
            if n % divisor == 0:
                print(f"{n} NO es primo (divisible por {divisor})")
                break
        else:
            # Este bloque se ejecuta si el `for` interno NO se interrumpió con `break`
            print(f"{n} es primo")


# =================================================================================================================
#                ▀▄▀▄▀▄⡷⠂ BLOQUE 3: FUNCIONES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 11. FUNCIONES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def funciones():
    """
    Las funciones permiten dividir un programa en secciones reutilizables,
    lo que hace el código más organizado y fácil de mantener.
    Se definen con la palabra clave `def`.
    """
    print("\n--- 11. Funciones ---")
    
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
        print(f"Argumentos posicionales (*args): {args}")
        print(f"Argumentos de palabra clave (**kwargs): {kwargs}")

    print("\n## Función con *args y **kwargs")
    funcion_flexible(1, 2, 3, nombre="Oliver", pais="España")

    # Keyword-only arguments (con *)
    # Los parámetros después de `*` solo se pueden pasar como keyword arguments.
    def crear_usuario(nombre, *, email, activo=True):
        return {"nombre": nombre, "email": email, "activo": activo}

    print("\n## Keyword-only arguments (después de *)")
    usuario = crear_usuario("Ana", email="ana@mail.com")
    print(f"Usuario: {usuario}")
    # crear_usuario("Ana", "ana@mail.com")  # TypeError — email debe ser keyword

    # Positional-only arguments (con /) — Python 3.8+
    # Los parámetros antes de `/` solo se pueden pasar como argumentos posicionales.
    def calcular_potencia(base, exponente, /):
        return base ** exponente

    print("\n## Positional-only arguments (antes de /) — Python 3.8+")
    print(f"calcular_potencia(2, 10): {calcular_potencia(2, 10)}")
    # calcular_potencia(base=2, exponente=10)  # TypeError — deben ser posicionales

    # Funciones como objetos de primera clase
    # En Python, las funciones son objetos: se pueden asignar a variables,
    # pasar como argumentos y retornar desde otras funciones.
    print("\n## Funciones como objetos de primera clase")
    
    def aplicar_operacion(func, a, b):
        """Recibe una función y la aplica a dos argumentos."""
        return func(a, b)

    def multiplicar(a, b):
        return a * b

    print(f"aplicar_operacion(sumar, 3, 4):      {aplicar_operacion(sumar, 3, 4)}")
    print(f"aplicar_operacion(multiplicar, 3, 4): {aplicar_operacion(multiplicar, 3, 4)}")

    # Funciones que retornan funciones
    mi_func = sumar  # Asignar una función a una variable
    print(f"mi_func(10, 20): {mi_func(10, 20)}")

    # Recursión
    print("\n## Recursión")
    def factorial(n):
        """Calcula el factorial de n de forma recursiva."""
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(f"factorial(5): {factorial(5)}")  # 120
    print(f"factorial(0): {factorial(0)}")  # 1


# =================================================================================================================
#                   ▀▄▀▄▀▄⡷⠂ 12. FUNCIONES LAMBDA ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def funciones_lambda():
    """
    Las funciones lambda son funciones anónimas, pequeñas y temporales,
    definidas con la palabra clave `lambda`. Son ideales para operaciones
    simples que no requieren una definición completa de una función.

    ⚠️ PEP 8 (E731): NO asignes una lambda a una variable. Si necesitas
    un nombre, usa `def`. Las lambdas son para uso inline.
    """
    print("\n--- 12. Funciones Lambda ---")
    
    # Sintaxis básica: lambda argumentos: expresión
    # La expresión es lo que se retorna. Solo puede haber una expresión.
    
    # 1. Ejemplo básico de suma
    # NOTA: En código real, esto sería una función `def`.
    # Se muestra aquí solo para ilustrar la sintaxis.
    print("## Sintaxis básica (solo ilustrativa)")
    print(f"Suma con lambda: {(lambda a, b: a + b)(3, 5)}")
    print("  ⚠️ PEP 8: No asignes lambdas a variables. Usa `def` si necesitas un nombre.")

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

    # 5. Uso con `min()` / `max()`
    # Encontrar el diccionario con el precio más alto
    productos = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 75},
    ]
    mas_caro = max(productos, key=lambda p: p["precio"])
    print(f"Producto más caro: {mas_caro}")


# =================================================================================================================
#                    ▀▄▀▄▀▄⡷⠂ 13. CLOSURES (CIERRES) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def closures():
    """
    Un closure (cierre) es una función interna que 'recuerda' las variables
    del ámbito (scope) de la función externa, incluso después de que la función
    externa haya terminado de ejecutarse.

    Los closures son el fundamento teórico de los decoradores.
    Para entenderlos, hay que conocer las reglas de scope de Python (LEGB):
      L - Local:     Variables dentro de la función actual.
      E - Enclosing: Variables de la función contenedora (función externa).
      G - Global:    Variables a nivel de módulo.
      B - Built-in:  Nombres integrados de Python (print, len, etc.).
    """
    print("\n--- 13. Closures (Cierres) ---")

    # Ejemplo 1: Closure como 'fábrica de funciones'
    print("## Fábrica de funciones")
    
    def crear_multiplicador(factor):
        """Retorna una función que multiplica por 'factor'."""
        def multiplicar(numero):
            return numero * factor  # 'factor' es una variable libre capturada del scope E (enclosing)
        return multiplicar

    doble = crear_multiplicador(2)
    triple = crear_multiplicador(3)

    print(f"doble(5):  {doble(5)}")     # 10
    print(f"triple(5): {triple(5)}")    # 15
    print(f"doble(10): {doble(10)}")    # 20

    # Verificar que es un closure
    print(f"\n¿Es un closure? Variables libres: {doble.__code__.co_freevars}")
    print(f"Valor capturado (cell): {doble.__closure__[0].cell_contents}")

    # Ejemplo 2: Closure con estado (acumulador)
    print("\n## Closure con estado")
    
    def crear_acumulador(inicio=0):
        """Crea un acumulador que mantiene un total acumulado."""
        total = [inicio]  # Lista para permitir mutación (mutable en scope enclosing)

        def acumular(valor):
            total[0] += valor
            return total[0]
        return acumular

    cuenta = crear_acumulador()
    print(f"Acumular 10: {cuenta(10)}")   # 10
    print(f"Acumular 20: {cuenta(20)}")   # 30
    print(f"Acumular 5:  {cuenta(5)}")    # 35

    # Ejemplo 3: Uso de `nonlocal` para modificar variables del scope enclosing
    print("\n## Palabra clave `nonlocal`")
    
    def crear_contador():
        """Crea un contador usando nonlocal."""
        cuenta = 0

        def incrementar():
            nonlocal cuenta  # Permite modificar 'cuenta' del scope enclosing
            cuenta += 1
            return cuenta
        return incrementar

    mi_contador = crear_contador()
    print(f"Incrementar: {mi_contador()}")   # 1
    print(f"Incrementar: {mi_contador()}")   # 2
    print(f"Incrementar: {mi_contador()}")   # 3


# =================================================================================================================
#                        ▀▄▀▄▀▄⡷⠂ 14. DECORADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def decoradores():
    """
    Los decoradores son funciones que toman otra función como argumento,
    le añaden nueva funcionalidad, y devuelven la función modificada.
    Permiten agregar comportamiento a una función o clase sin alterar
    su código original, siguiendo el principio de 'código abierto/cerrado'.

    Un decorador es esencialmente un closure que recibe una función como argumento.
    """
    print("\n--- 14. Decoradores ---")
    
    # 1. Ejemplo de un decorador simple
    # Este decorador añade un print antes y después de la función.
    # ✅ Usa @wraps para preservar los metadatos (__name__, __doc__) de la función original.
    # ✅ Acepta *args y **kwargs para funcionar con cualquier función.
    def mi_decorador(func):
        @wraps(func)
        def envoltura(*args, **kwargs):
            print("Algo está sucediendo antes de llamar a la función.")
            resultado = func(*args, **kwargs)
            print("Algo está sucediendo después de llamar a la función.")
            return resultado
        return envoltura

    @mi_decorador
    def saludar():
        """Función que saluda a todos."""
        print("¡Hola a todos!")
    
    print("## Ejemplo de decorador simple")
    saludar()
    print(f"Nombre preservado: {saludar.__name__}")  # 'saludar', NO 'envoltura'
    print(f"Docstring preservado: {saludar.__doc__}")
    
    # 2. Decorador práctico: Medir el tiempo de ejecución
    # Este decorador usa *args y **kwargs para aceptar cualquier tipo de argumento.
    def time_it(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"'{func.__name__}' tardó {end - start:.4f} segundos en ejecutarse.")
            return result
        return wrapper

    @time_it
    def mi_funcion_lenta():
        """Una función que simula un proceso largo."""
        time.sleep(0.5)  # Pausa la ejecución por 0.5 segundos
        print("¡Función lenta terminada!")
    
    @time_it
    def sumar_con_delay(a, b):
        """Una función que suma dos números con un pequeño delay."""
        time.sleep(0.2)
        return a + b
    
    print("\n## Ejemplo práctico: Medir el tiempo de ejecución")
    mi_funcion_lenta()
    
    resultado_suma = sumar_con_delay(5, 7)
    print(f"El resultado de la suma es: {resultado_suma}")

    # 3. Decorador con parámetros
    # Un decorador que acepta argumentos propios requiere un nivel extra de anidamiento.
    print("\n## Decorador con parámetros")
    
    def repetir(veces):
        """Decorador que repite la ejecución de una función N veces."""
        def decorador(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                resultado = None
                for _ in range(veces):
                    resultado = func(*args, **kwargs)
                return resultado
            return wrapper
        return decorador

    @repetir(veces=3)
    def decir_hola():
        """Dice hola."""
        print("¡Hola!")

    decir_hola()

    # 4. Apilar decoradores
    # Se pueden aplicar múltiples decoradores a una función.
    # Se ejecutan de abajo hacia arriba (el más cercano a la función se aplica primero).
    print("\n## Apilar múltiples decoradores")
    
    def negrita(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<b>{func(*args, **kwargs)}</b>"
        return wrapper

    def cursiva(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<i>{func(*args, **kwargs)}</i>"
        return wrapper

    @negrita
    @cursiva
    def formato_texto(texto):
        return texto

    print(f"Decoradores apilados: {formato_texto('Python')}")
    # Resultado: <b><i>Python</i></b>  (cursiva se aplica primero, luego negrita)


# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 15. GENERADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def generadores():
    """
    Los generadores son una forma eficiente de crear iteradores en Python.
    A diferencia de las funciones que retornan una lista completa, los generadores
    retornan un valor a la vez usando la palabra clave `yield`.
    Esto los hace extremadamente eficientes en el manejo de grandes conjuntos de datos,
    ya que no almacenan todos los elementos en la memoria simultáneamente (evaluación perezosa).
    """
    print("\n--- 15. Generadores ---")
    
    # ─── Función generadora básica ───
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

    # ─── Eficiencia de memoria ───
    print("\n## Generador vs. Lista (eficiencia de memoria)")
    
    # Generador (evaluación perezosa)
    def generador_grande(n):
        for i in range(n):
            yield i

    # Lista (almacenamiento completo en memoria)
    def lista_grande(n):
        return list(range(n))
    
    print("Un generador crea los valores 'uno por uno', lo que es eficiente en memoria.")
    print("Una lista crea todos los valores a la vez, lo que puede consumir mucha memoria.")
    
    # Ejemplo de uso práctico con next()
    print("\nEjemplo práctico: Imprimir los primeros 3 números de un generador de 1000.")
    generador = generador_grande(1000)
    for i in range(3):
        print(f"Valor del generador: {next(generador)}")

    # ─── Expresión Generadora y next() ───
    print("\n## Expresión Generadora y next()")
    
    # La Expresión Generadora es una forma concisa (implica 'yield' automáticamente) 
    # de crear un generador sin definir una función con 'def'.
    # Se usa principalmente para filtros y búsquedas sencillas en línea.
    #
    # La función 'next(generador, valor_por_defecto)' es el método para consumir
    # explícitamente un generador y obtener el siguiente valor. Es ideal para buscar
    # el primer elemento coincidente en una lista.
    
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
    
    print("\nEl uso de next() con una Expresión Generadora detiene la iteración en el primer match.")

    # ─── yield from (delegación de generadores) ───
    print("\n## `yield from` — Delegación de generadores")
    
    def numeros():
        yield from range(3)        # Delega al generador range(3)
    
    def letras():
        yield from "abc"           # Delega al iterable string
    
    def combinado():
        yield from numeros()       # Delega a otro generador
        yield from letras()        # Encadena generadores
    
    print(f"Generadores encadenados con yield from: {list(combinado())}")

    # ─── Pipeline de generadores ───
    print("\n## Pipeline de generadores")
    
    def leer_datos():
        """Simula la lectura de datos de una fuente."""
        datos = [10, -3, 25, -7, 42, 0, 15, -1]
        yield from datos
    
    def filtrar_positivos(datos):
        """Filtra solo los valores positivos."""
        for valor in datos:
            if valor > 0:
                yield valor
    
    def duplicar(datos):
        """Duplica cada valor."""
        for valor in datos:
            yield valor * 2
    
    # Pipeline: leer → filtrar → duplicar
    pipeline = duplicar(filtrar_positivos(leer_datos()))
    print(f"Pipeline (leer → filtrar positivos → duplicar): {list(pipeline)}")


# =================================================================================================================
#       ▀▄▀▄▀▄⡷⠂ BLOQUE 4: PROGRAMACIÓN ORIENTADA A OBJETOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 16. CLASES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def clases():
    """
    Las clases son el pilar de la programación orientada a objetos (POO) en Python.
    Permiten crear plantillas para definir objetos, que pueden tener atributos
    (variables que almacenan datos) y métodos (funciones que operan sobre esos datos).
    """
    print("\n--- 16. Clases ---")

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
        
        # ─── MÉTODOS DE CLASE VS ESTÁTICOS ───
        # Pregunta frecuente de entrevista: ¿Cuál es la diferencia?
        
        # 1. Método de clase: @classmethod
        # - Recibe 'cls' (la clase) como primer argumento implícito, NO 'self'.
        # - Puede modificar el estado de la clase (ej: cls.especie = "Mutante").
        # - Caso de uso principal: Constructores alternativos (Factory Methods).
        @classmethod
        def desde_anio_nacimiento(cls, nombre, anio_nacimiento):
            """Constructor alternativo usando @classmethod."""
            import datetime
            edad_calculada = datetime.date.today().year - anio_nacimiento
            return cls(nombre, edad_calculada)  # Llama al __init__ usando 'cls'

        # 2. Método estático: @staticmethod
        # - No recibe ni 'self' ni 'cls'. Es solo una función normal anidada en la clase.
        # - No puede modificar ni el estado del objeto ni de la clase.
        # - Caso de uso principal: Funciones utilitarias (Helpers) relacionadas conceptualmente.
        @staticmethod
        def es_mayor_de_edad(edad):
            return edad >= 18

    # Creación de objetos (instancias de la clase)
    persona1 = Persona("Palacio", 26)
    persona2 = Persona.desde_anio_nacimiento("Tatiana", 2002) # Usando el classmethod

    # Acceder a atributos y llamar a métodos
    print("## Instancias, @classmethod y @staticmethod")
    persona1.saludar()
    persona2.saludar()
    print(f"¿Es mayor de edad (26)? {Persona.es_mayor_de_edad(26)}") # Usando el staticmethod

    # Herencia
    # La clase 'Estudiante' hereda de 'Persona', lo que significa que
    # obtiene todos los atributos y métodos de la clase padre.
    class Estudiante(Persona):
        def __init__(self, nombre, edad, grado):
            # Llama al constructor de la clase padre (Persona) para inicializar
            # los atributos 'nombre' y 'edad'.
            super().__init__(nombre, edad)
            self.grado = grado # Atributo de instancia propio de Estudiante.

        # Sobreescribir un método (Polimorfismo)
        # Se redefine el método 'saludar' para que se adapte a la clase 'Estudiante'.
        def saludar(self):
            print(f"Hola, soy un estudiante llamado {self.nombre}, tengo {self.edad} años y estoy en el grado {self.grado}.")

    print("\n## Herencia (Clase Estudiante)")
    estudiante1 = Estudiante("Andrés", 20, "12°")
    estudiante1.saludar()
    print(f"isinstance(estudiante1, Persona): {isinstance(estudiante1, Persona)}")
    print(f"isinstance(estudiante1, Estudiante): {isinstance(estudiante1, Estudiante)}")


# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 17. OOP AVANZADO ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def oop_avanzado():
    """
    Conceptos avanzados de Programación Orientada a Objetos en Python:
    encapsulamiento, propiedades, herencia múltiple, MRO, clases abstractas y __slots__.
    """
    print("\n--- 17. OOP Avanzado ---")

    # ─── Encapsulamiento ───
    # Python no tiene modificadores de acceso (public/private/protected) como Java.
    # En su lugar, usa convenciones de nomenclatura:
    #   _atributo   → 'protegido' (convención: uso interno, pero accesible)
    #   __atributo  → 'privado' (name mangling: _Clase__atributo)
    print("## Encapsulamiento")
    
    class CuentaBancaria:
        def __init__(self, titular, saldo_inicial):
            self.titular = titular           # Público
            self._banco = "Bancolombia"      # Protegido (convención)
            self.__saldo = saldo_inicial     # Privado (name mangling)

        def depositar(self, cantidad):
            if cantidad > 0:
                self.__saldo += cantidad

        def get_saldo(self):
            return self.__saldo

    cuenta = CuentaBancaria("Andrés", 1000)
    print(f"Titular (público):     {cuenta.titular}")
    print(f"Banco (protegido):     {cuenta._banco}")
    print(f"Saldo (vía método):    {cuenta.get_saldo()}")
    # print(cuenta.__saldo)         # AttributeError — name mangling
    print(f"Saldo (name mangling): {cuenta._CuentaBancaria__saldo}")
    print("  ⚠️ Name mangling NO es seguridad, es protección contra colisiones accidentales.")

    # ─── @property: Getter/Setter Pythónico ───
    print("\n## @property (Getter/Setter Pythónico)")
    
    class Temperatura:
        def __init__(self, celsius):
            self._celsius = celsius

        @property
        def celsius(self):
            """Getter: se accede como atributo, no como método."""
            return self._celsius

        @celsius.setter
        def celsius(self, valor):
            """Setter: valida antes de asignar."""
            if valor < -273.15:
                raise ValueError("Temperatura por debajo del cero absoluto")
            self._celsius = valor

        @property
        def fahrenheit(self):
            """Propiedad calculada (solo lectura)."""
            return self._celsius * 9 / 5 + 32

    temp = Temperatura(25)
    print(f"Celsius:    {temp.celsius}")       # Usa el getter
    print(f"Fahrenheit: {temp.fahrenheit}")     # Propiedad calculada
    temp.celsius = 100                          # Usa el setter
    print(f"Nuevo Celsius:    {temp.celsius}")
    print(f"Nuevo Fahrenheit: {temp.fahrenheit}")

    # ─── Herencia Múltiple y MRO ───
    print("\n## Herencia Múltiple y MRO")
    
    class Volador:
        def mover(self):
            return "Volando"

    class Nadador:
        def mover(self):
            return "Nadando"

    class Pato(Volador, Nadador):
        pass  # Hereda de ambas clases

    pato = Pato()
    print(f"pato.mover(): '{pato.mover()}'")
    print("  (Se usa el método de 'Volador' porque está primero en la lista de herencia)")
    
    # MRO — Method Resolution Order
    # Python usa el algoritmo C3 para resolver el orden de herencia.
    print(f"\nMRO de Pato: {[cls.__name__ for cls in Pato.__mro__]}")
    
    # ─── Clases Abstractas (ABC) ───
    print("\n## Clases Abstractas (ABC)")
    
    class Figura(ABC):
        @abstractmethod
        def area(self):
            """Método abstracto: DEBE ser implementado por las subclases."""
            pass

        @abstractmethod
        def perimetro(self):
            pass

        def descripcion(self):
            """Método concreto: las subclases lo heredan tal cual."""
            return f"Soy una {self.__class__.__name__} con área {self.area():.2f}"

    class Circulo(Figura):
        def __init__(self, radio):
            self.radio = radio

        def area(self):
            return math.pi * self.radio ** 2

        def perimetro(self):
            return 2 * math.pi * self.radio

    class Rectangulo(Figura):
        def __init__(self, ancho, alto):
            self.ancho = ancho
            self.alto = alto

        def area(self):
            return self.ancho * self.alto

        def perimetro(self):
            return 2 * (self.ancho + self.alto)

    # figura = Figura()  # TypeError: Can't instantiate abstract class
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)

    print(f"Círculo:    {circulo.descripcion()}, Perímetro: {circulo.perimetro():.2f}")
    print(f"Rectángulo: {rectangulo.descripcion()}, Perímetro: {rectangulo.perimetro():.2f}")
    print("  (No se puede instanciar Figura() directamente — es abstracta)")

    # ─── __slots__ ───
    print("\n## __slots__ (Optimización de memoria)")
    
    class PuntoConSlots:
        __slots__ = ("x", "y")  # Restringe los atributos a solo estos
        def __init__(self, x, y):
            self.x = x
            self.y = y

    punto = PuntoConSlots(3, 4)
    print(f"Punto: ({punto.x}, {punto.y})")
    # punto.z = 5  # AttributeError — __slots__ impide añadir atributos dinámicos
    print("  __slots__ reduce el uso de memoria y mejora la velocidad de acceso.")
    print("  Úsalo cuando creas muchas instancias (miles/millones) de una clase simple.")


# =================================================================================================================
#                  ▀▄▀▄▀▄⡷⠂ 18. MÉTODOS MÁGICOS (DUNDER) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def metodos_magicos():
    """
    Los métodos mágicos, también conocidos como 'dunder methods' (por sus
    guiones bajos dobles: __method__), permiten definir un comportamiento especial
    para tus clases. Son la forma en que Python implementa la sobrecarga de
    operadores, lo que te permite usar operadores estándar como +, -, <, >
    con tus propios objetos.
    """
    print("\n--- 18. Métodos Mágicos (Dunder Methods) ---")
    
    class Vector:
        """Representa un vector 2D con operaciones matemáticas."""
        
        def __init__(self, x, y):
            """Constructor: Se llama al crear una nueva instancia del objeto."""
            self.x = x
            self.y = y

        # ─── Representación ───
        def __str__(self):
            """Representación legible para el usuario (print, str)."""
            return f"Vector({self.x}, {self.y})"

        def __repr__(self):
            """Representación 'oficial', debe permitir recrear el objeto."""
            return f"Vector({self.x}, {self.y})"

        # ─── Operadores aritméticos ───
        def __add__(self, otro):
            """Operador + : suma de vectores."""
            return Vector(self.x + otro.x, self.y + otro.y)

        def __sub__(self, otro):
            """Operador - : resta de vectores."""
            return Vector(self.x - otro.x, self.y - otro.y)

        def __mul__(self, escalar):
            """Operador * : multiplicación por un escalar."""
            return Vector(self.x * escalar, self.y * escalar)

        # ─── Operadores de comparación ───
        def __eq__(self, otro):
            """Operador == : igualdad."""
            return self.x == otro.x and self.y == otro.y

        def __gt__(self, otro):
            """Operador > : mayor que (comparando la magnitud)."""
            return (self.x**2 + self.y**2) > (otro.x**2 + otro.y**2)

        def __hash__(self):
            """Necesario si defines __eq__. Permite usar el objeto en sets y como clave de dict."""
            return hash((self.x, self.y))

        # ─── Protocolos de contenedor ───
        def __len__(self):
            """len(vector) — retorna la dimensión del vector."""
            return 2  # Es un vector 2D

        def __getitem__(self, index):
            """vector[index] — acceso por índice."""
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            raise IndexError(f"Índice {index} fuera de rango para un Vector 2D")

        def __contains__(self, valor):
            """valor in vector — test de pertenencia."""
            return valor in (self.x, self.y)

        # ─── Callable ───
        def __call__(self):
            """vector() — permite llamar al objeto como una función."""
            return (self.x**2 + self.y**2) ** 0.5  # Magnitud

        # ─── Bool ───
        def __bool__(self):
            """bool(vector) — un vector es True si no es el vector cero."""
            return self.x != 0 or self.y != 0

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = Vector(3, 4)
    v_cero = Vector(0, 0)

    print("## Representación")
    print(f"__str__:  {v1}")
    print(f"__repr__: {repr(v1)}")

    print("\n## Operadores aritméticos")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3  = {v1 * 3}")

    print("\n## Operadores de comparación")
    print(f"v1 == v3: {v1 == v3}")     # True — mismas coordenadas
    print(f"v1 == v2: {v1 == v2}")     # False
    print(f"v1 > v2:  {v1 > v2}")      # True — mayor magnitud

    print("\n## Hash (usar en sets/dicts)")
    vectores = {v1, v2, v3}  # v1 y v3 son iguales, el set los deduplica
    print(f"Set de vectores: {vectores}")
    print(f"Cantidad en set: {len(vectores)} (v1 y v3 se deduplicaron)")

    print("\n## Protocolos de contenedor")
    print(f"len(v1):    {len(v1)}")
    print(f"v1[0]:      {v1[0]}")
    print(f"v1[1]:      {v1[1]}")
    print(f"3 in v1:    {3 in v1}")
    print(f"5 in v1:    {5 in v1}")

    print("\n## Callable y Bool")
    print(f"v1() (magnitud): {v1()}")     # Llama a __call__
    print(f"bool(v1):        {bool(v1)}")          # True
    print(f"bool(v_cero):    {bool(v_cero)}")      # False

    # Nota: si __str__ no está definido, Python usará __repr__.
    # Si __repr__ no está definido, se usa una representación por defecto.
    # Es una buena práctica definir ambos.


# =================================================================================================================
#                       ▀▄▀▄▀▄⡷⠂ 19. DATACLASSES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def dataclasses_ejemplo():
    """
    Las dataclasses (Python 3.7+) son una forma moderna y concisa de crear
    clases que almacenan datos. El decorador @dataclass genera automáticamente
    __init__, __repr__, __eq__ y opcionalmente otros métodos dunder.
    """
    print("\n--- 19. Dataclasses ---")

    # Dataclass básica
    @dataclass
    class Producto:
        nombre: str
        precio: float
        cantidad: int = 0      # Valor por defecto

        @property
        def valor_total(self):
            return self.precio * self.cantidad

    print("## Dataclass básica")
    laptop = Producto("Laptop", 1200.00, 5)
    mouse = Producto("Mouse", 25.50)
    print(f"Producto: {laptop}")                   # __repr__ generado automáticamente
    print(f"Valor total: ${laptop.valor_total:,.2f}")
    print(f"Mouse:   {mouse}")

    # __eq__ generado automáticamente
    laptop2 = Producto("Laptop", 1200.00, 5)
    print(f"\nlaptop == laptop2: {laptop == laptop2}")  # True

    # Dataclass inmutable (frozen=True)
    @dataclass(frozen=True)
    class Coordenada:
        latitud: float
        longitud: float

    print("\n## Dataclass inmutable (frozen=True)")
    coord = Coordenada(4.60, -74.08)
    print(f"Coordenada: {coord}")
    # coord.latitud = 5.0  # FrozenInstanceError — no se puede modificar
    print("  (No se puede modificar una dataclass frozen)")

    # Dataclass con campo calculado usando field()
    @dataclass
    class Equipo:
        nombre: str
        jugadores: list = field(default_factory=list)  # ⚠️ Nunca usar [] como default
        _total: int = field(init=False, repr=False)     # Campo interno, excluido de __init__ y __repr__

        def __post_init__(self):
            """Se ejecuta después de __init__. Ideal para campos calculados."""
            self._total = len(self.jugadores)

        def agregar_jugador(self, jugador):
            self.jugadores.append(jugador)
            self._total = len(self.jugadores)

    print("\n## Dataclass con field() y __post_init__")
    equipo = Equipo("Python FC", ["Ana", "Luis"])
    print(f"Equipo: {equipo}")
    equipo.agregar_jugador("Sofía")
    print(f"Después de agregar: {equipo}")
    print(f"Total jugadores: {equipo._total}")

    # Dataclass ordenable (order=True)
    @dataclass(order=True)
    class Estudiante:
        promedio: float         # Se usa para ordenar (primer campo)
        nombre: str = ""

    print("\n## Dataclass ordenable (order=True)")
    estudiantes = [
        Estudiante(8.5, "Ana"),
        Estudiante(9.2, "Luis"),
        Estudiante(7.8, "Sofía"),
    ]
    estudiantes.sort()
    for e in estudiantes:
        print(f"  {e.nombre}: {e.promedio}")


# =================================================================================================================
#        ▀▄▀▄▀▄⡷⠂ BLOQUE 5: ROBUSTEZ Y GESTIÓN DE RECURSOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                    ▀▄▀▄▀▄⡷⠂ 20. MANEJO DE EXCEPCIONES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def manejo_de_excepciones():
    """
    Las sentencias `try`, `except`, `else` y `finally` permiten controlar
    y gestionar errores (excepciones) de forma elegante sin que el programa
    se detenga abruptamente.
    """
    print("\n--- 20. Manejo de Excepciones ---")

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
#                ▀▄▀▄▀▄⡷⠂ 21. EXCEPCIONES PERSONALIZADAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def excepciones_personalizadas():
    """
    Las excepciones personalizadas permiten crear errores específicos de tu
    dominio de negocio. La convención es heredar de Exception (o de una
    excepción base de tu aplicación).
    """
    print("\n--- 21. Excepciones Personalizadas ---")

    # Excepción base de la aplicación
    class AppError(Exception):
        """Excepción base para toda la aplicación."""
        pass

    # Excepciones específicas
    class UsuarioNoEncontrado(AppError):
        def __init__(self, user_id):
            self.user_id = user_id
            super().__init__(f"Usuario con ID {user_id} no encontrado")

    class SaldoInsuficiente(AppError):
        def __init__(self, saldo_actual, monto_solicitado):
            self.saldo_actual = saldo_actual
            self.monto_solicitado = monto_solicitado
            super().__init__(
                f"Saldo insuficiente: tienes ${saldo_actual}, "
                f"pero intentaste retirar ${monto_solicitado}"
            )

    # Uso de excepciones personalizadas
    print("## Definir y lanzar excepciones personalizadas")
    
    def buscar_usuario(user_id):
        usuarios = {1: "Ana", 2: "Luis", 3: "Sofía"}
        if user_id not in usuarios:
            raise UsuarioNoEncontrado(user_id)
        return usuarios[user_id]

    def retirar(saldo, monto):
        if monto > saldo:
            raise SaldoInsuficiente(saldo, monto)
        return saldo - monto

    # Capturando excepciones personalizadas
    try:
        usuario = buscar_usuario(99)
    except UsuarioNoEncontrado as e:
        print(f"Error capturado: {e}")
        print(f"  ID buscado: {e.user_id}")

    try:
        nuevo_saldo = retirar(100, 500)
    except SaldoInsuficiente as e:
        print(f"\nError capturado: {e}")
        print(f"  Saldo actual: ${e.saldo_actual}")
        print(f"  Monto solicitado: ${e.monto_solicitado}")

    # Capturar por la excepción base (atrapa todos los errores de la app)
    print("\n## Capturar por la excepción base")
    for user_id in [1, 99]:
        try:
            print(f"Buscando usuario {user_id}: {buscar_usuario(user_id)}")
        except AppError as e:
            print(f"Error de app: {e}")


# =================================================================================================================
#                      ▀▄▀▄▀▄⡷⠂ 22. CONTEXT MANAGERS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def context_managers():
    """
    Los `context managers` son objetos que definen un contexto temporal para la ejecución
    de un bloque de código. Garantizan que los recursos (como archivos, conexiones
    a bases de datos o bloqueos de red) se manejen de forma segura, asegurando
    que se liberen o cierren correctamente, incluso si ocurren errores.
    """
    print("\n--- 22. Context Managers ---")
    
    # 1. Ejemplo de uso común: Manejo de archivos
    # `with` invoca el método __enter__ del objeto 'open' al inicio
    # y el método __exit__ al final, asegurando que el archivo se cierre.
    print("## Uso de un context manager integrado (archivos)")
    file_path = "temp_cm.txt"
    try:
        with open(file_path, "w") as f:
            f.write("Este archivo se cierra automáticamente.")
        print(f"Archivo '{file_path}' escrito y cerrado.")
    except IOError as e:
        print(f"Error al manejar el archivo: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    # 2. Crear tu propio context manager con una clase
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
            if valor_exc:
                print(f"Se detectó una excepción: {tipo_exc.__name__}: {valor_exc}")
            # return False (o no retornar nada) → PROPAGA la excepción
            # return True → SUPRIME la excepción (úsalo con mucho cuidado)
            return False  # Propaga la excepción al bloque exterior

    # Usando el context manager personalizado
    print("\n## Creando tu propio context manager (clase)")
    with Temporizador():
        print("Realizando una operación que requiere un temporizador...")
        time.sleep(0.3)
        
    # Demostración de que la excepción se propaga correctamente
    print("\n--- Demostración de propagación de excepciones ---")
    try:
        with Temporizador():
            print("Realizando una operación con un posible error...")
            time.sleep(0.1)
            raise ValueError("¡Algo salió mal!")
    except ValueError as e:
        print(f"Excepción capturada FUERA del context manager: {e}")

    # 3. Context manager con generador (usando contextlib)
    from contextlib import contextmanager

    @contextmanager
    def manejar_archivo(ruta, modo):
        """Context manager creado con un generador."""
        print(f"\nAbriendo archivo '{ruta}' en modo '{modo}'...")
        f = open(ruta, modo)
        try:
            yield f          # El código dentro de `with` se ejecuta aquí
        finally:
            f.close()
            print(f"Archivo '{ruta}' cerrado.")
            if os.path.exists(ruta):
                os.remove(ruta)

    print("\n## Context manager con @contextmanager")
    with manejar_archivo("temp_ctx.txt", "w") as archivo:
        archivo.write("Escrito con context manager de generador.")
        print("Archivo escrito correctamente.")


# =================================================================================================================
#                     ▀▄▀▄▀▄⡷⠂ 23. MANEJO DE ARCHIVOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def manejo_de_archivos():
    """
    Python permite leer y escribir archivos de manera sencilla y segura.
    Se recomienda usar la sentencia `with open(...)` ya que asegura que el archivo
    se cierre automáticamente, incluso si ocurre un error, lo que previene fugas
    de memoria y corrupción de datos.
    """
    print("\n--- 23. Manejo de Archivos ---")
    file_path = "ejemplo_archivo.txt"

    # Modo 'w': Escribir (sobrescribe el contenido si el archivo ya existe)
    # Si el archivo no existe, lo crea.
    print("\n## Modo 'w' (Write): Escribir")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("¡Hola, mundo!\n")
        f.write("Este es un archivo de prueba.")

    print(f"Archivo '{file_path}' creado y escrito (sobrescrito).")

    # Modo 'r': Leer
    # Si el archivo no existe, genera un error.
    print("\n## Modo 'r' (Read): Leer")
    with open(file_path, "r", encoding="utf-8") as f:
        contenido_completo = f.read()
        print(f"Contenido completo del archivo:\n{contenido_completo}")

    # Modo 'a': Añadir (Append)
    # Si el archivo ya existe, añade el nuevo contenido al final.
    print("\n## Modo 'a' (Append): Añadir")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\nEsta línea se añadió al final.")

    # Volver a leer el archivo para ver el contenido añadido
    with open(file_path, "r", encoding="utf-8") as f:
        contenido_actualizado = f.read()
        print(f"Contenido del archivo después de añadir:\n{contenido_actualizado}")
    
    # Leer el archivo línea por línea
    # El método .readlines() devuelve una lista de las líneas del archivo.
    print("\n## Leer línea por línea")
    with open(file_path, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        print("Líneas leídas (con '\\n'):")
        print(lineas)

    # Forma Pythónica de leer línea por línea (más eficiente en memoria)
    print("\n## Lectura eficiente línea por línea (iterando sobre el archivo)")
    with open(file_path, "r", encoding="utf-8") as f:
        for numero_linea, linea in enumerate(f, start=1):
            print(f"Línea {numero_linea}: {linea.rstrip()}")
    
    # Limpieza: Eliminar el archivo de prueba
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"\nArchivo '{file_path}' eliminado.")
    else:
        print(f"\nEl archivo '{file_path}' ya no existe.")


# =================================================================================================================
#       ▀▄▀▄▀▄⡷⠂ BLOQUE 6: BIBLIOTECA ESTÁNDAR Y HERRAMIENTAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                           ▀▄▀▄▀▄⡷⠂ 24. MÓDULOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def modulos():
    """
    Los módulos son archivos de Python (.py) que contienen código (funciones, clases y variables)
    que se puede reutilizar en otros programas.
    Esto ayuda a organizar y estructurar proyectos grandes.

    NOTA: En código de producción, los imports siempre van al inicio del archivo (PEP 8).
    Aquí se muestran dentro de la función solo con fines didácticos.
    """
    print("\n--- 24. Módulos ---")

    # Importación completa de un módulo
    # Se importa todo el módulo 'math' y se accede a sus funciones con el prefijo 'math.'.
    # NOTA: En este archivo, `import math` ya está al inicio (PEP 8).
    # Aquí se muestra la sintaxis con fines didácticos.
    print("## Importación completa del módulo")
    print("import math")
    x = 16
    raiz_cuadrada = math.sqrt(x)
    print(f"La raíz cuadrada de {x} es: {raiz_cuadrada}")
    print(f"El valor de pi es: {math.pi}")

    # Importación de una función específica de un módulo
    # Se importa solo la función 'sin' del módulo 'math'.
    # Esto evita tener que usar el prefijo del módulo.
    print("\n## Importación de un elemento específico")
    print("from math import sin")
    print(f"El seno de 0 es: {math.sin(0)}")

    # Importación con alias
    # Se le da un nombre corto (alias) al módulo para facilitar su uso.
    print("\n## Importación con alias")
    print("import random as rd")
    numero_aleatorio = random.randint(1, 100)
    print(f"Un número aleatorio entre 1 y 100 es: {numero_aleatorio}")

    # Creando y usando tu propio módulo
    # Para este ejemplo, imagina que tienes un archivo llamado 'mi_modulo.py' con una función 'saludar'.
    # Para importarlo, simplemente se usa el nombre del archivo (sin la extensión .py).
    print("\n## Creando tu propio módulo")
    # from mi_modulo import saludar
    # saludar("Andrés")
    print("Para este ejemplo, se importaría un archivo llamado 'mi_modulo.py'.")
    print("Si tienes un archivo con 'def saludar(nombre): ...', puedes importarlo y usarlo.")

    # Módulos útiles de la biblioteca estándar
    print("\n## Módulos útiles de la biblioteca estándar")
    modulos_utiles = {
        "os":           "Interacción con el sistema operativo",
        "sys":          "Configuración del intérprete de Python",
        "json":         "Codificar/decodificar JSON",
        "datetime":     "Manejo de fechas y horas",
        "pathlib":      "Manejo moderno de rutas de archivos",
        "logging":      "Sistema de logging profesional",
        "unittest":     "Framework de testing integrado",
        "collections":  "Estructuras de datos especializadas",
        "itertools":    "Funciones para iteraciones eficientes",
        "functools":    "Herramientas para funciones de orden superior",
        "typing":       "Soporte para type hints",
    }
    for modulo, descripcion in modulos_utiles.items():
        print(f"  {modulo:15s} → {descripcion}")


# =================================================================================================================
#                   ▀▄▀▄▀▄⡷⠂ 25. EXPRESIONES REGULARES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def expresiones_regulares():
    """
    Las expresiones regulares son secuencias de caracteres que forman un patrón
    de búsqueda. El módulo `re` de Python se utiliza para buscar, manipular y
    validar texto basándose en estos patrones.
    """
    print("\n--- 25. Expresiones Regulares ---")
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

    # Grupos de captura
    print("\n## Grupos de captura")
    email_texto = "Contacto: usuario@dominio.com y admin@empresa.org"
    patron_email = r"(\w+)@(\w+)\.(\w+)"
    matches = re.finditer(patron_email, email_texto)
    for match in matches:
        print(f"Email completo: {match.group()}")
        print(f"  Usuario: {match.group(1)}, Dominio: {match.group(2)}, TLD: {match.group(3)}")


# =================================================================================================================
#                  ▀▄▀▄▀▄⡷⠂ 26. COLLECTIONS E ITERTOOLS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def collections_itertools():
    """
    Los módulos `collections` e `itertools` de la biblioteca estándar ofrecen
    estructuras de datos especializadas y funciones para iteraciones eficientes.
    Son herramientas esenciales para escribir código Python idiomático y eficiente.
    """
    print("\n--- 26. Collections e Itertools ---")

    # ═══════════════════════════════════════
    # COLLECTIONS
    # ═══════════════════════════════════════
    print("=" * 40)
    print("COLLECTIONS")
    print("=" * 40)

    # ─── Counter ───
    # Cuenta las ocurrencias de elementos en un iterable.
    print("\n## Counter")
    palabras = ["python", "java", "python", "go", "python", "java", "rust"]
    conteo = Counter(palabras)
    print(f"Conteo: {conteo}")
    print(f"Más comunes (top 2): {conteo.most_common(2)}")
    print(f"Conteo de 'python': {conteo['python']}")

    # Counter también funciona con strings
    letras = Counter("mississippi")
    print(f"Letras en 'mississippi': {letras}")

    # ─── defaultdict ───
    # Un diccionario que nunca lanza KeyError; crea un valor por defecto automáticamente.
    print("\n## defaultdict")
    
    # Agrupar datos
    estudiantes = [
        ("matemáticas", "Ana"),
        ("ciencias", "Luis"),
        ("matemáticas", "Sofía"),
        ("ciencias", "Pedro"),
        ("arte", "Ana"),
    ]
    
    por_materia = defaultdict(list)  # El valor por defecto es una lista vacía
    for materia, alumno in estudiantes:
        por_materia[materia].append(alumno)  # No necesita verificar si la clave existe
    
    print("Agrupado por materia:")
    for materia, alumnos in por_materia.items():
        print(f"  {materia}: {alumnos}")

    # Contar sin Counter
    conteo_manual = defaultdict(int)  # El valor por defecto es 0
    for palabra in palabras:
        conteo_manual[palabra] += 1
    print(f"\nConteo manual con defaultdict: {dict(conteo_manual)}")

    # ─── namedtuple ───
    # Una tupla con campos nombrados. Más legible que una tupla normal.
    print("\n## namedtuple")
    
    Punto = namedtuple("Punto", ["x", "y"])
    p1 = Punto(3, 4)
    p2 = Punto(x=1, y=2)
    
    print(f"Punto: {p1}")
    print(f"Acceso por nombre: x={p1.x}, y={p1.y}")
    print(f"Acceso por índice: p1[0]={p1[0]}, p1[1]={p1[1]}")
    print(f"Es una tupla: {isinstance(p1, tuple)}")

    # ─── deque (double-ended queue) ───
    # Cola de doble extremo: eficiente para agregar/quitar al inicio y al final.
    print("\n## deque (cola de doble extremo)")
    
    cola = deque([1, 2, 3])
    cola.append(4)           # Agregar al final — O(1)
    cola.appendleft(0)       # Agregar al inicio — O(1) (vs O(n) en listas)
    print(f"Después de append(4) y appendleft(0): {cola}")
    
    cola.pop()               # Quitar del final — O(1)
    cola.popleft()           # Quitar del inicio — O(1) (vs O(n) en listas)
    print(f"Después de pop() y popleft(): {cola}")

    # deque con tamaño máximo (descarta los más antiguos)
    ultimos_3 = deque(maxlen=3)
    for i in range(5):
        ultimos_3.append(i)
        print(f"  Agregar {i}: {list(ultimos_3)}")

    # ═══════════════════════════════════════
    # ITERTOOLS
    # ═══════════════════════════════════════
    print("\n" + "=" * 40)
    print("ITERTOOLS")
    print("=" * 40)

    # ─── chain ───
    # Encadena múltiples iterables en uno solo.
    print("\n## chain")
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    lista_c = [7, 8, 9]
    encadenado = list(chain(lista_a, lista_b, lista_c))
    print(f"chain([1,2,3], [4,5,6], [7,8,9]): {encadenado}")

    # ─── islice ───
    # Corta un iterable (como slice, pero para cualquier iterable, incluidos generadores).
    print("\n## islice")
    # Tomar los primeros 5 números pares de un generador infinito
    def numeros_pares():
        n = 0
        while True:
            yield n
            n += 2

    primeros_5_pares = list(islice(numeros_pares(), 5))
    print(f"Primeros 5 pares (de generador infinito): {primeros_5_pares}")

    # ─── groupby ───
    # Agrupa elementos consecutivos que comparten una clave.
    # ⚠️ Los datos DEBEN estar ordenados por la clave.
    print("\n## groupby")
    datos = [
        {"tipo": "fruta", "nombre": "manzana"},
        {"tipo": "fruta", "nombre": "banana"},
        {"tipo": "verdura", "nombre": "zanahoria"},
        {"tipo": "verdura", "nombre": "brócoli"},
        {"tipo": "fruta", "nombre": "cereza"},
    ]
    # Ordenar primero por la clave de agrupación
    datos_ordenados = sorted(datos, key=lambda x: x["tipo"])
    for tipo, grupo in groupby(datos_ordenados, key=lambda x: x["tipo"]):
        items = [item["nombre"] for item in grupo]
        print(f"  {tipo}: {items}")


# =================================================================================================================
#                  ▀▄▀▄▀▄⡷⠂ 27. TYPE HINTS (TIPADO ESTÁTICO) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def type_hints():
    """
    Los Type Hints (Python 3.5+) permiten anotar los tipos esperados de variables,
    parámetros y valores de retorno. No afectan la ejecución del programa
    (Python sigue siendo dinámico), pero son verificados por herramientas como
    mypy, pyright o el IDE para detectar errores antes de ejecutar.

    Son IMPRESCINDIBLES en código Python profesional moderno.
    """
    print("\n--- 27. Type Hints (Tipado Estático) ---")

    # ─── Tipos básicos ───
    print("## Tipos básicos")
    
    nombre: str = "Andrés"
    edad: int = 26
    altura: float = 1.83
    es_programador: bool = True

    print(f"nombre: str = '{nombre}'")
    print(f"edad: int = {edad}")
    print(f"altura: float = {altura}")
    print(f"es_programador: bool = {es_programador}")

    # ─── Funciones con type hints ───
    print("\n## Funciones con type hints")
    
    def saludar(nombre: str, veces: int = 1) -> str:
        """Retorna un saludo repetido N veces."""
        return (f"¡Hola, {nombre}! " * veces).strip()

    print(f"saludar('Ana'): {saludar('Ana')}")
    print(f"saludar('Ana', 3): {saludar('Ana', 3)}")

    # ─── Tipos de colecciones (Python 3.9+ usa tipos built-in) ───
    print("\n## Tipos de colecciones")
    
    # Python 3.9+ — se usa directamente list, dict, tuple, set
    edades: list[int] = [25, 30, 35]
    coordenadas: tuple[float, float] = (4.60, -74.08)
    config: dict[str, int] = {"timeout": 30, "retries": 3}
    tags: set[str] = {"python", "programming"}

    print(f"edades: list[int] = {edades}")
    print(f"coordenadas: tuple[float, float] = {coordenadas}")
    print(f"config: dict[str, int] = {config}")
    print(f"tags: set[str] = {tags}")

    # ─── Optional y Union ───
    print("\n## Optional (valor puede ser None)")
    
    def buscar_usuario(user_id: int) -> Optional[dict]:
        """Retorna un usuario o None si no existe."""
        usuarios = {1: {"nombre": "Ana"}, 2: {"nombre": "Luis"}}
        return usuarios.get(user_id)

    resultado = buscar_usuario(1)
    print(f"buscar_usuario(1): {resultado}")
    resultado_none = buscar_usuario(99)
    print(f"buscar_usuario(99): {resultado_none}")

    # Python 3.10+ — se puede usar X | Y en lugar de Union[X, Y]
    def procesar(valor: int | str) -> str:
        """Acepta int o str (Python 3.10+)."""
        return str(valor).upper()

    print(f"\nprocesar(42): '{procesar(42)}'")
    print(f"procesar('hola'): '{procesar('hola')}'")

    # ─── Type Hints con clases propias ───
    print("\n## Type Hints con clases propias")
    
    class Producto:
        def __init__(self, nombre: str, precio: float) -> None:
            self.nombre = nombre
            self.precio = precio

        def __repr__(self) -> str:
            return f"Producto('{self.nombre}', {self.precio})"

    def producto_mas_caro(productos: list["Producto"]) -> Optional["Producto"]:
        """Encuentra el producto más caro de una lista."""
        if not productos:
            return None
        return max(productos, key=lambda p: p.precio)

    catalogo = [
        Producto("Laptop", 1200),
        Producto("Mouse", 25),
        Producto("Teclado", 75),
    ]
    print(f"Catálogo: {catalogo}")
    print(f"Más caro: {producto_mas_caro(catalogo)}")

    # ─── Resumen de imports comunes del módulo typing ───
    print("\n## Imports comunes de 'typing'")
    resumen = {
        "Optional[X]":     "X o None (equivale a X | None en 3.10+)",
        "Union[X, Y]":     "X o Y (equivale a X | Y en 3.10+)",
        "Any":             "Cualquier tipo (evitar si es posible)",
        "Callable[[A], R]": "Función que acepta A y retorna R",
        "TypeVar":         "Variable de tipo genérico",
        "Protocol":        "Tipado estructural (duck typing explícito)",
        "Literal['a','b']": "Solo valores literales específicos",
    }
    for tipo, desc in resumen.items():
        print(f"  {tipo:22s} → {desc}")


# =================================================================================================================
#        ▀▄▀▄▀▄⡷⠂ BLOQUE 7: ARQUITECTURA Y RENDIMIENTO ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#                         ▀▄▀▄▀▄⡷⠂ 28. ENTORNOS VIRTUALES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def entornos_virtuales():
    """
    Los entornos virtuales resuelven el problema de "En mi máquina sí funciona".
    Permiten crear instalaciones de Python aisladas, donde cada proyecto tiene 
    sus propias dependencias sin afectar al Python global del sistema.
    """
    print("\n--- 28. Entornos Virtuales (venv) ---")
    print("\n Revisa los comentarios de esta sección en el documento .py para entender los entornos virtuales en Python.\n")

    # ============================================================
    # ¿POR QUÉ SON INDISPENSABLES?
    # ============================================================

    # Si el Proyecto A usa Django 3.0 y el Proyecto B usa Django 4.0,
    # instalarlos globalmente causará conflictos de versiones.
    #
    # Un entorno virtual encapsula:
    # - Dependencias
    # - Librerías
    # - Paquetes
    #
    # para CADA proyecto de manera independiente.
    #
    # IMPORTANTE:
    # Un venv NO crea un Python nuevo desde cero.
    # Usa el intérprete base del sistema, pero con paquetes aislados.

    # ============================================================
    # COMANDOS BÁSICOS (TERMINAL)
    # ============================================================

    # 1. Crear el entorno:       python -m venv venv
    # 2. Activar (Windows):      venv\Scripts\activate
    # 3. Activar (Mac/Linux):    source venv/bin/activate
    # 4. Instalar paquetes:      pip install requests
    # 5. Guardar dependencias:   pip freeze > requirements.txt
    # 6. Instalar dependencias:  pip install -r requirements.txt
    # 7. Desactivar:             deactivate

    # ============================================================
    # BUENAS PRÁCTICAS
    # ============================================================

    # - Nunca subas la carpeta 'venv' a GitHub (añádela a .gitignore).
    # - Sube solo el archivo 'requirements.txt'.


# =================================================================================================================
#                  ▀▄▀▄▀▄⡷⠂ 29. CONCURRENCIA Y ASYNC ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def concurrencia_y_async():
    """
    Python tiene múltiples modelos para hacer varias cosas a la vez. 
    Elegir el correcto depende de si el problema requiere mucha CPU (cálculos) 
    o mucho tiempo de espera (I/O, red, discos).
    """
    print("\n--- 29. Concurrencia y Async (GIL, Threads, Asyncio) ---")
    print("\n Revisa los comentarios de esta sección en el documento .py para entender concurrencia, paralelismo, GIL, threading, multiprocessing y asyncio en Python.\n")

    # Python tiene varios modelos para ejecutar tareas concurrentes.
    # La elección depende principalmente de si el problema es:
    #
    # - CPU Bound:
    #   Mucho cálculo matemático o procesamiento intensivo.
    #
    # - I/O Bound:
    #   Mucho tiempo esperando red, APIs, archivos o bases de datos.


    # ============================================================
    # CONCURRENCIA VS PARALELISMO
    # ============================================================

    # Concurrencia:
    # Varias tareas progresan al mismo tiempo.
    #
    # Paralelismo:
    # Varias tareas ejecutándose literalmente al mismo tiempo
    # usando múltiples núcleos del CPU.


    # ============================================================
    # EL GIL (GLOBAL INTERPRETER LOCK)
    # ============================================================

    # CPython tiene un lock interno llamado GIL.
    #
    # Este lock permite que solo un thread ejecute bytecode Python
    # a la vez dentro de un proceso.
    #
    # Por eso, los threads normalmente NO mejoran tareas
    # CPU-bound puras escritas en Python.
    #
    # Sin embargo:
    # - El GIL cambia constantemente entre threads.
    # - Operaciones I/O suelen liberar el GIL.
    # - Librerías escritas en C (NumPy, OpenCV, TensorFlow, etc.)
    #   pueden liberar el GIL y aprovechar múltiples núcleos.


    # ============================================================
    # 1. THREADING (HILOS)
    # ============================================================

    # Cuándo usar:
    # - Tareas I/O bound.
    # - APIs.
    # - Archivos.
    # - Sockets.
    # - Bases de datos.
    #
    # ¿Por qué funciona bien para I/O?
    # Mientras un hilo espera una respuesta de red o disco,
    # el GIL puede liberarse y otro hilo continuar trabajando.
    #
    # Ventajas:
    # - Fácil de implementar.
    # - Muy útil para tareas bloqueantes.
    #
    # Desventajas:
    # - No ofrece paralelismo real para CPU-bound en CPython.
    #
    # Módulos comunes:
    # - threading
    # - concurrent.futures.ThreadPoolExecutor


    # ============================================================
    # 2. MULTIPROCESSING (PROCESOS)
    # ============================================================

    # Cuándo usar:
    # - Tareas CPU bound.
    # - Machine Learning.
    # - Procesamiento de imágenes.
    # - Compresión.
    # - Cálculos matemáticos intensivos.
    #
    # ¿Por qué funciona?
    # Cada proceso tiene:
    # - Su propio intérprete.
    # - Su propia memoria.
    # - Su propio GIL.
    #
    # Esto permite paralelismo real.
    #
    # Desventajas:
    # - Más consumo de memoria.
    # - Comunicación entre procesos más costosa.
    #
    # Módulos comunes:
    # - multiprocessing
    # - concurrent.futures.ProcessPoolExecutor


    # ============================================================
    # 3. ASYNCIO (ASINCRONISMO COOPERATIVO)
    # ============================================================

    # Cuándo usar:
    # - Miles de conexiones concurrentes.
    # - APIs masivas.
    # - WebSockets.
    # - Servidores modernos.
    #
    # ¿Cómo funciona?
    # Usa un Event Loop en un solo hilo.
    #
    # Las tareas cooperan entre sí usando:
    # - async
    # - await
    #
    # Cuando una tarea hace:
    #     await algo()
    #
    # cede el control para que otra tarea pueda ejecutarse.
    #
    # Esto se llama concurrencia cooperativa.
    #
    # Ventajas:
    # - Muy eficiente en consumo de recursos.
    # - Excelente escalabilidad para I/O.
    # - Mucho más ligero que crear miles de threads.
    #
    # Desventajas:
    # - No acelera tareas CPU-bound.
    # - Requiere librerías compatibles con async.
    # - Puede ser más complejo de depurar.
    #
    # Ejemplo conceptual:
    #
    # async def obtener_datos():
    #     resultado = await peticion_http()
    #     return resultado


    # ============================================================
    # RESUMEN RÁPIDO
    # ============================================================

    # THREADING:
    # ✔ Bueno para I/O
    # ✘ Malo para CPU-bound puro
    #
    # MULTIPROCESSING:
    # ✔ Bueno para CPU-bound
    # ✔ Paralelismo real
    # ✘ Más pesado
    #
    # ASYNCIO:
    # ✔ Excelente para MUCHAS tareas I/O concurrentes
    # ✔ Muy eficiente
    # ✘ No sirve para paralelizar CPU

# =================================================================================================================
#                  ▀▄▀▄▀▄⡷⠂ 30. RENDIMIENTO Y FUGAS DE MEMORIA ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def fugas_de_memoria():
    """
    Aunque Python tiene Garbage Collector y manejo automático de memoria,
    las aplicaciones grandes o de larga duración pueden aumentar su consumo
    de memoria inesperadamente si los objetos permanecen referenciados.
    """

    print("\n--- 30. Rendimiento y Fugas de Memoria ---")
    print("\n📘 Revisa los comentarios de esta sección en el documento .py para entender el manejo de memoria en Python.\n")


    # ============================================================
    # ¿CÓMO FUNCIONA LA MEMORIA EN PYTHON?
    # ============================================================

    # Python usa principalmente:
    #
    # 1. Reference Counting
    #    Cada objeto lleva un contador de referencias.
    #
    # 2. Garbage Collector (GC)
    #    Detecta ciclos de referencia que el conteo normal no puede liberar.


    # ============================================================
    # ¿POR QUÉ PUEDE CRECER LA MEMORIA?
    # ============================================================

    # Muchas veces no son "memory leaks" reales,
    # sino objetos que siguen vivos accidentalmente.
    #
    # Ejemplos comunes:
    #
    # 1. Listas o diccionarios globales que crecen infinitamente.
    # 2. Cachés mal diseñadas.
    # 3. Variables globales reteniendo objetos grandes.
    # 4. Referencias persistentes en singletons.
    # 5. Objetos con ciclos de referencia complejos.
    # 6. Librerías externas o extensiones en C.


    # ============================================================
    # HERRAMIENTAS DE DEPURACIÓN
    # ============================================================

    # tracemalloc
    # ------------------------------------------------------------
    # Módulo estándar para rastrear dónde se asignó memoria.

    # import tracemalloc
    # tracemalloc.start()

    # snapshot = tracemalloc.take_snapshot()
    # top_stats = snapshot.statistics('lineno')


    # objgraph
    # ------------------------------------------------------------
    # Librería externa excelente para visualizar referencias
    # entre objetos y detectar quién mantiene viva la memoria.


    # memory_profiler
    # ------------------------------------------------------------
    # Permite medir consumo de memoria línea por línea.


    # ============================================================
    # WEAKREF Y CACHÉS
    # ============================================================

    # El módulo 'weakref' permite crear referencias débiles.
    #
    # Esto significa que el objeto puede ser destruido por
    # el Garbage Collector si no existen otras referencias fuertes.
    #
    # Muy útil para:
    # - cachés
    # - observers
    # - listeners
    # - estructuras temporales


    # ============================================================
    # BUENAS PRÁCTICAS
    # ============================================================

    # - Evita estructuras globales gigantes.
    # - Libera recursos grandes cuando ya no se necesiten.
    # - Usa generadores en lugar de cargar todo en memoria.
    # - Monitorea memoria en producción.
    # - Ten cuidado con cachés infinitas.
    # - Usa perfiles de memoria regularmente en sistemas grandes.


# =================================================================================================================
# ▀▄▀▄▀▄⡷⠂ 𝐄𝐉𝐄𝐂𝐔𝐂𝐈𝐎́𝐍 𝐃𝐄 𝐋𝐀 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓𝐀𝐂𝐈𝐎́𝐍 ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# =================================================================================================================
#          ▀▄▀▄▀▄⡷⠂ 31. PRÓXIMOS PASOS (FRAMEWORKS Y LIBRERÍAS) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================
def proximos_pasos():
    """
    Una guía de referencia rápida sobre los frameworks y librerías más relevantes
    del ecosistema Python, organizados por dominio. Esta sección NO cubre su uso,
    solo sirve como mapa de ruta para saber por dónde continuar una vez dominados
    los fundamentos del lenguaje.
    """
    print("\n--- 31. Próximos Pasos: Frameworks y Librerías ---")
    print("Una vez que domines los fundamentos de Python, el siguiente paso es")
    print("especializarte en un área. Aquí tienes un mapa del ecosistema:\n")

    ecosistema = {
        "Desarrollo Web": {
            "descripcion": "Construir aplicaciones y APIs web",
            "herramientas": [
                ("Django",       "Framework web 'batteries-included'. Ideal para apps complejas con ORM, auth, admin."),
                ("Flask",        "Microframework ligero y flexible. Ideal para APIs y proyectos pequeños/medianos."),
                ("FastAPI",      "Framework moderno para APIs REST. Async, type hints, docs automáticas (OpenAPI)."),
                ("Uvicorn",      "Servidor ASGI de alto rendimiento. Se usa con FastAPI y Starlette."),
                ("SQLAlchemy",   "ORM y toolkit SQL. El estándar de facto para interactuar con bases de datos."),
                ("Celery",       "Cola de tareas distribuidas. Para procesar trabajos en segundo plano."),
            ],
        },
        "Ciencia de Datos y Análisis": {
            "descripcion": "Manipulación, análisis y visualización de datos",
            "herramientas": [
                ("NumPy",        "Arrays multidimensionales y operaciones matemáticas de alto rendimiento."),
                ("Pandas",       "DataFrames para análisis y manipulación de datos tabulares."),
                ("Matplotlib",   "Librería base de visualización. Gráficos estáticos, animados e interactivos."),
                ("Seaborn",      "Visualización estadística basada en Matplotlib. Gráficos más elegantes."),
                ("Plotly",       "Gráficos interactivos y dashboards web."),
                ("Jupyter",      "Notebooks interactivos. Estándar para exploración de datos y prototipado."),
                ("Polars",       "Alternativa moderna a Pandas. Mucho más rápido para datasets grandes."),
            ],
        },
        "Machine Learning e IA": {
            "descripcion": "Modelos predictivos, deep learning e inteligencia artificial",
            "herramientas": [
                ("Scikit-learn",  "ML clásico: clasificación, regresión, clustering, preprocesamiento."),
                ("TensorFlow",   "Framework de deep learning de Google. Producción y escala."),
                ("PyTorch",      "Framework de deep learning de Meta. Preferido en investigación."),
                ("Keras",        "API de alto nivel para redes neuronales (integrada en TensorFlow)."),
                ("Hugging Face", "Transformers, LLMs y NLP. El hub central de modelos de IA."),
                ("LangChain",    "Framework para construir aplicaciones con LLMs (RAG, agentes, cadenas)."),
            ],
        },
        "Automatización y Scripting": {
            "descripcion": "Automatizar tareas repetitivas y scripting del sistema",
            "herramientas": [
                ("Requests",     "Cliente HTTP elegante. El estándar para consumir APIs REST."),
                ("httpx",        "Cliente HTTP moderno con soporte async. Alternativa a Requests."),
                ("Beautiful Soup", "Parsing de HTML/XML. Web scraping sencillo."),
                ("Scrapy",       "Framework completo de web scraping y crawling."),
                ("Selenium",     "Automatización de navegadores web. Testing y scraping dinámico."),
                ("Paramiko",     "Cliente SSH para automatización remota de servidores."),
            ],
        },
        "DevOps e Infraestructura": {
            "descripcion": "Despliegue, contenedores y gestión de infraestructura",
            "herramientas": [
                ("Docker SDK",   "Interactuar con Docker desde Python."),
                ("Fabric",       "Ejecución remota de comandos y despliegue."),
                ("Ansible",      "Automatización de configuración e infraestructura (IaC)."),
                ("Boto3",        "SDK oficial de AWS. Interactuar con todos los servicios de Amazon."),
            ],
        },
        "Testing y Calidad de Código": {
            "descripcion": "Pruebas automatizadas y herramientas de calidad",
            "herramientas": [
                ("pytest",       "Framework de testing. Más potente y flexible que unittest."),
                ("coverage",     "Medir la cobertura de código de tus tests."),
                ("mypy",         "Verificador de tipos estáticos. Valida tus type hints."),
                ("ruff",         "Linter y formateador ultrarrápido (reemplaza flake8, isort, black)."),
                ("pre-commit",   "Git hooks para ejecutar checks automáticos antes de cada commit."),
            ],
        },
        "Herramientas de Entorno y Empaquetado": {
            "descripcion": "Gestión de dependencias, entornos virtuales y distribución",
            "herramientas": [
                ("pip",          "Gestor de paquetes oficial de Python."),
                ("venv",         "Entornos virtuales (incluido en la biblioteca estándar)."),
                ("Poetry",       "Gestión moderna de dependencias y empaquetado."),
                ("uv",           "Gestor de paquetes ultrarrápido (escrito en Rust). Reemplazo moderno de pip + venv."),
                ("pyenv",        "Gestionar múltiples versiones de Python en tu sistema."),
            ],
        },
    }

    for categoria, info in ecosistema.items():
        print(f"{'=' * 60}")
        print(f"  {categoria.upper()}")
        print(f"  {info['descripcion']}")
        print(f"{'=' * 60}")
        for nombre, desc in info["herramientas"]:
            print(f"  {nombre:17s} → {desc}")
        print()

    print("─" * 60)
    print("  CONSEJO: No intentes aprender todo a la vez.")
    print("  Elige UN área que te apasione y profundiza en ella.")
    print("  Los fundamentos que has aprendido aquí te servirán")
    print("  en CUALQUIERA de estos caminos.")
    print("─" * 60)


# Mapeo de nombres de sección a funciones — permite ejecución selectiva
SECCIONES = {
    "variables": variables,
    "strings": strings,
    "listas": listas,
    "tuplas": tuplas,
    "sets": sets,
    "diccionarios": diccionarios,
    "comprehensions": comprehensions,
    "operadores": operadores,
    "condicionales": condicionales,
    "bucles": bucles,
    "funciones": funciones,
    "lambda": funciones_lambda,
    "closures": closures,
    "decoradores": decoradores,
    "generadores": generadores,
    "clases": clases,
    "oop": oop_avanzado,
    "magicos": metodos_magicos,
    "dataclasses": dataclasses_ejemplo,
    "excepciones": manejo_de_excepciones,
    "excepciones_personalizadas": excepciones_personalizadas,
    "context_managers": context_managers,
    "archivos": manejo_de_archivos,
    "modulos": modulos,
    "regex": expresiones_regulares,
    "collections": collections_itertools,
    "type_hints": type_hints,
    "entornos": entornos_virtuales,
    "concurrencia": concurrencia_y_async,
    "memoria": fugas_de_memoria,
    "proximos_pasos": proximos_pasos,
}


def main():
    """
    Función principal que ejecuta todos los ejemplos.
    Soporta ejecución selectiva: python python_documentation.py <seccion>
    """
    # Ejecución selectiva por sección
    if len(sys.argv) > 1:
        seccion = sys.argv[1].lower()
        if seccion == "help":
            print("Secciones disponibles:")
            for nombre in SECCIONES:
                print(f"  - {nombre}")
            return
        func = SECCIONES.get(seccion)
        if func:
            func()
        else:
            print(f"Sección '{seccion}' no encontrada.")
            print(f"Secciones disponibles: {', '.join(SECCIONES.keys())}")
            print("Usa 'help' para ver todas las secciones.")
        return

    # Ejecución completa
    print("--- 📚 INICIANDO LA DOCUMENTACIÓN DE PYTHON 📚 ---")
    generate_toc()

    for func in SECCIONES.values():
        func()

    print("\n--- ✅ DOCUMENTACIÓN COMPLETADA ✅ ---")


if __name__ == "__main__":
    main()