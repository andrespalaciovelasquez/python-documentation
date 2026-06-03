# 📚 Documentación de Conceptos de Python y Flask

Autor: **Andrés Palacio Velásquez**

Este proyecto es una biblioteca completa y autodidacta de documentación de conceptos fundamentales del lenguaje de programación **Python** y patrones avanzados de desarrollo y arquitectura con el framework **Flask**. Ha sido diseñado como una guía didáctica de referencia de alto nivel, ideal tanto para repasar pilares clave como para diseñar arquitecturas listas para producción.

Cada sección incluye **explicaciones detalladas, análisis conceptuales y ejemplos prácticos de código comentados paso a paso**.

---

## 📋 Tabla de Contenido: Módulo Python

### Bloque 1: Datos y Tipos
| # | Tema | Descripción |
|---|------|-------------|
| 1 | **Variables** | Tipado dinámico, asignación múltiple, intercambio, constantes |
| 2 | **Strings** | Métodos de cadena, f-strings avanzadas, raw strings |
| 3 | **Listas** | Colecciones mutables, slicing, métodos principales |
| 4 | **Tuplas** | Colecciones inmutables, empaquetado/desempaquetado |
| 5 | **Sets** | Conjuntos, operaciones matemáticas, frozenset |
| 6 | **Diccionarios** | Pares clave-valor, métodos, merge operator |
| 7 | **Comprehensions** | List, dict, set comprehensions, expresiones generadoras |

### Bloque 2: Control de Flujo
| # | Tema | Descripción |
|---|------|-------------|
| 8 | **Operadores** | Aritméticos, comparación, lógicos, identidad, walrus |
| 9 | **Condicionales** | if/elif/else, ternario, match-case (3.10+) |
| 10 | **Bucles** | for, while, enumerate, zip, break/continue, else |

### Bloque 3: Funciones
| # | Tema | Descripción |
|---|------|-------------|
| 11 | **Funciones** | *args/**kwargs, keyword-only, positional-only, recursión |
| 12 | **Funciones Lambda** | Funciones anónimas, uso con filter/map/sorted |
| 13 | **Closures** | Cierres, nonlocal, fábricas de funciones |
| 14 | **Decoradores** | @wraps, decoradores con parámetros, apilamiento |
| 15 | **Generadores** | yield, yield from, pipelines, expresiones generadoras |

### Bloque 4: Programación Orientada a Objetos
| # | Tema | Descripción |
|---|------|-------------|
| 16 | **Clases** | OOP básica, herencia, @classmethod, @staticmethod |
| 17 | **OOP Avanzado** | Encapsulamiento, @property, herencia múltiple, MRO, ABC, __slots__ |
| 18 | **Métodos Mágicos** | Dunder methods: __add__, __eq__, __hash__, __getitem__, __call__ |
| 19 | **Dataclasses** | @dataclass, frozen, field(), order, __post_init__ |

### Bloque 5: Robustez y Gestión de Recursos
| # | Tema | Descripción |
|---|------|-------------|
| 20 | **Excepciones** | try/except/else/finally, manejo de errores |
| 21 | **Excepciones Personalizadas** | Jerarquía de errores de dominio |
| 22 | **Context Managers** | with, __enter__/__exit__, @contextmanager |
| 23 | **Manejo de Archivos** | Lectura, escritura, modos, encoding |

### Bloque 6: Biblioteca Estándar y Herramientas
| # | Tema | Descripción |
|---|------|-------------|
| 24 | **Módulos** | import, alias, módulos propios, estándar |
| 25 | **Expresiones Regulares** | re.search, findall, sub, grupos de captura |
| 26 | **Collections e Itertools** | Counter, defaultdict, namedtuple, deque, chain, groupby |
| 27 | **Type Hints** | Tipado estático, Optional, Union, clases propias |

### Bloque 7: Arquitectura y Rendimiento
| # | Tema | Descripción |
|---|------|-------------|
| 28 | **Entornos Virtuales** | venv, aislamiento de dependencias, pip freeze |
| 29 | **Concurrencia y Async** | GIL, threading vs multiprocessing, asyncio |
| 30 | **Fugas de Memoria** | Reference counting, Garbage Collector, weakref, optimizaciones |

### Bonus
| # | Tema | Descripción |
|---|------|-------------|
| 31 | **Próximos Pasos** | Mapa del ecosistema: frameworks y librerías por dominio |

---

## 📋 Tabla de Contenido: Módulo Flask — Construyendo una App Real

> El documento enseña Flask construyendo una aplicación real paso a paso. Cada bloque genera un archivo concreto del proyecto que será utilizado por los bloques siguientes.

| Bloque | Archivo Generado | Descripción |
|--------|------------------|-------------|
| 1 | — | **Introducción a Flask & WSGI** — Qué es Flask, ciclo de vida de peticiones, Hola Mundo canónico |
| 2 | — | **Arquitectura del Proyecto** — Estructura de directorios, responsabilidad de cada archivo, flujo HTTP |
| 3 | `config.py` | **Configuración por Entornos** — Clases de config (Dev/Prod), variables de entorno, conexión SQL Server |
| 4 | `models.py` | **Modelos ORM** — Tablas con `db.Model`, columnas, relaciones 1-a-muchos, cascade |
| 5 | `services.py` | **Servicios — Lógica de Negocio** — CRUD completo, transacciones seguras con rollback |
| 6 | `schemas.py` | **Esquemas de Validación (Pydantic V2)** — Esquemas In/Out, `from_attributes`, `model_validate()` |
| 7 | `exceptions.py` + `handlers.py` | **Errores Centralizados** — Jerarquía de excepciones, interceptores automáticos |
| 8 | `routes.py` | **Rutas y Controladores** — Blueprint, CRUD completo, request/response, cookies, sessions |
| 9 | `__init__.py` + `run.py` | **Factory Pattern** — `create_app()`, registro de Blueprints, punto de entrada |
| 10 | `logging_config.py` | **Logging y Observabilidad** — Formatters, RotatingFileHandler, niveles de log |
| 11 | `conftest.py` + `tests/` | **Testing con Pytest** — Fixtures, scopes, test_client, aislamiento transaccional |
| 12 | `security.py` | **Hashing y Seguridad** — Protección de contraseñas con PBKDF2:SHA256 y Salting |
| 13 | `auth/routes.py` | **JWT y Autenticación** — Access Tokens, Refresh Tokens y Blocklist stateless |
| 14 | `auth/decorators.py` | **Roles y Permisos** — Decoradores custom (`@roles_required`) inspeccionando JWT |
| 15 | `middleware.py` | **Middleware y Hooks** — `@app.before_request`, headers de seguridad y WSGI puro |
| 16 | `__init__.py` | **Rate Limiting** — Prevención de Fuerza Bruta / DDoS con `Flask-Limiter` y Redis |
| 17 | `tasks.py` | **Tareas en Segundo Plano** — Configuración de `Celery`, Workers y encolamiento |
| 18 | `Dockerfile` + `compose` | **Docker y Contenedorización** — Multi-stage, Drivers SQL Server, docker-compose |

---

## 🚀 Cómo Usar

### 🐍 Módulo Python (Práctico y Ejecutable)
Para ejecutar ejemplos prácticos del manual de Python:

```bash
# Ejecutar toda la documentación de Python
python python_documentation.py

# Ver las secciones de Python disponibles
python python_documentation.py help

# Ejecutar una sección de Python específica
python python_documentation.py decoradores
python python_documentation.py type_hints
```

### 🌶️ Módulo Flask (Lectura Pasiva en IDE)
El manual de Flask ha sido diseñado como un documento de estudio directamente en el IDE. A diferencia del módulo de Python, este archivo **no se ejecuta por consola**, sino que guía al lector a través de la construcción progresiva de una aplicación real:

- Ábrelo directamente en tu editor de código (VSCode, PyCharm, etc.).
- Todo el código se presenta sin comentar para aprovechar el resaltado de sintaxis nativo.
- Cada bloque genera un archivo real del proyecto y referencia los archivos construidos previamente.

---

## 🌟 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un error, tienes una sugerencia para mejorar la documentación o quieres añadir un nuevo concepto, no dudes en abrir un *issue* o enviar un *pull request*.

---

## 📧 Contacto

Para cualquier pregunta o comentario, puedes contactarme:

**Andrés Palacio Velásquez**
* **Email:** andrespalaciovelasquez@outlook.com
* **LinkedIn:** [Andrés Palacio Velásquez](https://www.linkedin.com/in/andrespalaciovelasquez/)
* **GitHub:** [andrespalaciovelasquez](https://github.com/andrespalaciovelasquez)