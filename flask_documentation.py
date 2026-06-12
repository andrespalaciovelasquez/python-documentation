# =================================================================================================================
# ▀▄▀▄▀▄⡷⠂ 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓𝐀𝐂𝐈𝐎́𝐍 𝐃𝐄 𝐅𝐋𝐀𝐒𝐊 ⠐⢾▀▄▀▄▀▄
# Creado por: Andrés Palacio Velásquez
# =================================================================================================================
#
# Este documento enseña Flask construyendo una aplicación real paso a paso.
# Cada bloque genera un archivo concreto del proyecto que será utilizado
# por los bloques siguientes, creando un flujo de aprendizaje progresivo.
#
# 📖 Archivo de lectura pasiva — no está diseñado para ejecutarse.
#    El código está descomentado para aprovechar el resaltado de sintaxis del IDE.

"""
--- 📋 𝐓𝐀𝐁𝐋𝐀 𝐃𝐄 𝐂𝐎𝐍𝐓𝐄𝐍𝐈𝐃𝐎 𝐅𝐋𝐀𝐒𝐊 📋 ---

FUNDAMENTOS (La base del framework)
├── BLOQUE 1:  INTRODUCCIÓN A FLASK & WSGI          → Qué es Flask. Hola Mundo.
├── BLOQUE 2:  ARQUITECTURA DEL PROYECTO            → Estructura de carpetas.
├── BLOQUE 3:  CONFIGURACIÓN POR ENTORNOS           → config.py (secretos, DB URI)
│
CAPA DE DATOS Y NEGOCIO (Back-to-front)
├── BLOQUE 4:  MODELOS ORM                          → models.py (tablas de BD)
├── BLOQUE 5:  SERVICIOS — LÓGICA DE NEGOCIO        → services.py (CRUD)
├── BLOQUE 6:  ESQUEMAS DE VALIDACIÓN CON PYDANTIC  → schemas.py (entrada/salida)
│
CAPA DE TRANSPORTE (Cómo la API responde)
├── BLOQUE 7:  ERRORES CENTRALIZADOS                → exceptions.py + handlers.py
├── BLOQUE 8:  RUTAS Y CONTROLADORES                → routes.py (Blueprints)
│
ENSAMBLAJE Y CALIDAD (Unir todo + validar)
├── BLOQUE 9:  FACTORY PATTERN                      → __init__.py + run.py
├── BLOQUE 10: LOGGING Y OBSERVABILIDAD             → logging_config.py
├── BLOQUE 11: TESTING PROFESIONAL CON PYTEST       → conftest.py + tests
│
SEGURIDAD Y AUTENTICACIÓN (Proteger la API)
├── BLOQUE 12: HASHING Y SEGURIDAD DE CONTRASEÑAS   → security.py
├── BLOQUE 13: JWT, REFRESH TOKENS, AUTENTICACIÓN   → auth/
├── BLOQUE 14: ROLES, PERMISOS Y DECORADORES        → auth/decorators.py
│
PRODUCCIÓN AVANZADA (Escalar y desplegar)
├── BLOQUE 15: MIDDLEWARE Y HOOKS DEL CICLO DE VIDA → middleware.py
├── BLOQUE 16: RATE LIMITING                        → integración factory
├── BLOQUE 17: TAREAS EN SEGUNDO PLANO (CELERY)     → tasks.py
└── BLOQUE 18: DOCKER Y CONTENEDORIZACIÓN           → Dockerfile + compose
"""


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 1: INTRODUCCIÓN A FLASK & WSGI ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# Flask es un microframework web para Python basado en Werkzeug (librería WSGI)
# y Jinja2 (motor de plantillas). Su filosofía es ser ligero y extensible:
# no impone ORM, validador ni estructura de carpetas. Tú eliges las herramientas.

# ─── ¿Qué es WSGI? ───
# WSGI (Web Server Gateway Interface) es el estándar de Python para comunicar
# un servidor web con una aplicación Python. Flask se construye sobre este protocolo.
#
# Ciclo de vida de una petición:
#   Cliente HTTP → Servidor (Gunicorn/Nginx) → WSGI → Flask → Respuesta

# ─── Hola Mundo — La Aplicación Mínima ───
# Este es el código más simple posible para levantar una app Flask:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mundo desde Flask!"

# __name__ le dice a Flask en qué módulo estamos para localizar recursos (templates, static).

# ─── Opciones de Ejecución ───

# Opción 1 — En código (desarrollo local):
if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Opción 2 — Línea de comandos con Flask CLI:
# flask run --debug

# Opción 3 — Producción con Gunicorn:
# gunicorn 'app:create_app()' --bind 0.0.0.0:8000

# ⚠️ NUNCA uses app.run() en producción. Gunicorn o uWSGI son los estándares.

# A partir de aquí, dejaremos este Hola Mundo atrás y construiremos un proyecto
# profesional multicapa con Factory Pattern, Blueprints, ORM y Testing.


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 2: ARQUITECTURA DEL PROYECTO ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# Antes de escribir una sola línea de código, necesitamos definir la estructura
# del proyecto. Flask te da libertad total, pero en proyectos reales que crecen
# en complejidad, es vital separar responsabilidades con una arquitectura limpia.

# ─── Estructura de Directorios Recomendada ───
# La siguiente estructura es una adaptación simplificada de Clean Architecture.
# Cada archivo tiene una responsabilidad única y clara:
"""
mi_proyecto_flask/
│
├── app/
│   ├── __init__.py          ← Inicialización central (Factory Pattern) y registro de Blueprints
│   ├── middleware.py        ← Interceptores WSGI y Hooks del ciclo de vida
│   ├── tasks.py             ← Tareas asíncronas para Celery en segundo plano
│   │
│   ├── core/
│   │   ├── config.py        ← Configuraciones por entorno (Development, Production)
│   │   ├── logging_config.py← Configuración centralizada de logs
│   │   └── security.py      ← Utilidades de hashing y validación de contraseñas
│   │
│   ├── errors/
│   │   ├── exceptions.py    ← Excepciones personalizadas del dominio de negocio
│   │   └── handlers.py      ← Interceptores centralizados de errores HTTP
│   │
│   ├── auth/                ← Módulo de Autenticación
│   │   ├── routes.py        ← Endpoints de Login, Register y Refresh
│   │   └── decorators.py    ← Decoradores para roles y permisos personalizados
│   │
│   └── modulos/
│       └── usuarios/
│           ├── routes.py    ← Rutas y controladores (Blueprint)
│           ├── models.py    ← Modelos de datos del ORM (SQLAlchemy)
│           ├── services.py  ← Lógica de negocio pura (CRUD)
│           └── schemas.py   ← Esquemas de validación (Pydantic V2)
│
├── tests/
│   ├── conftest.py          ← Fixtures principales de Pytest
│   └── test_usuarios.py     ← Casos de prueba unitarios e integración
│
├── run.py                   ← Punto de entrada para ejecutar la aplicación
├── Dockerfile               ← Receta para construir la imagen del contenedor
└── docker-compose.yml       ← Orquestación de contenedores (App, BD, Redis)
"""

# ─── ¿Por qué esta estructura? ───
#
# config.py        → Centraliza secretos y parámetros. La app la lee al iniciar.
# logging_config.py→ Configura los logs para no usar print() en producción.
# security.py      → Utilidades criptográficas para hashear contraseñas.
# models.py        → Define las tablas de la BD. Es la base de todo.
# services.py      → Contiene la lógica de negocio. Usa los modelos para leer/escribir datos.
# schemas.py       → Valida lo que entra y lo que sale. Protege la API.
# exceptions.py    → Errores con significado de negocio (ej: "Usuario no encontrado").
# handlers.py      → Intercepta las excepciones y las convierte en respuestas HTTP JSON.
# auth/            → Endpoints y decoradores independientes para Login y Roles.
# routes.py        → El controlador: recibe peticiones, orquesta schemas + services + errores.
# middleware.py    → Interceptores que actúan antes de que la petición llegue a routes.py.
# tasks.py         → Tareas lentas que se ejecutan en segundo plano vía Celery.
# __init__.py      → La fábrica: crea la app, carga config, registra Blueprints y logs.
# tests/           → Valida que todo funcione ante futuros cambios.
# Dockerfile       → Empaqueta la aplicación para que corra en un servidor Linux.

# ─── Flujo Completo de una Petición HTTP (con Middleware y Auth) ───
# Cuando una petición (ej: POST /api/v1/usuarios) entra al sistema, viaja por capas:
#
# 1. middleware.py→ Intercepta a bajo nivel (ej. forzar HTTPS o registrar logs).
# 2. auth/        → Verifica si el JWT es válido y si el usuario tiene el rol necesario.
# 3. routes.py    → Recibe la petición HTTP y extrae el payload JSON.
# 4. schemas.py   → Valida la estructura del JSON con Pydantic. Si falla → 400.
# 5. services.py  → Recibe datos validados y aplica reglas de negocio. (Si es lento → tasks.py)
# 6. models.py    → Mapea la tabla. El servicio la usa para persistir datos en la BD.
# 7. routes.py    → Serializa el resultado con el schema de salida y responde.
#
# Si ocurre un error de negocio en cualquier capa:
# → Se lanza una excepción de exceptions.py
# → handlers.py la intercepta y responde con JSON estructurado.

# ─── ¿Por qué construimos de atrás hacia adelante? ───
# En esta guía NO explicamos Flask como piezas aisladas. Construimos una app real
# siguiendo el orden inverso al flujo de la petición:
#
#   config.py → models.py → services.py → schemas.py → errors/ → routes.py → __init__.py → tests/ ... hasta Docker
#
# La razón es la cadena de dependencias: cada capa necesita que la anterior ya exista.
#   - No puedes escribir un servicio sin tener un modelo definido.
#   - No puedes validar datos sin saber qué campos espera el servicio.
#   - No puedes manejar errores sin saber qué excepciones lanza el servicio.
#   - No puedes crear una ruta sin tener servicio, schema y manejador de errores.
#   - No puedes ensamblar la app sin tener rutas registrables y logs configurados.
#   - No puedes testear sin tener todo lo anterior funcionando.
#   - No puedes asegurar (Auth/JWT) sin tener la BD funcionando.
#   - No puedes empaquetar en Docker sin tener la app terminada.
#
# Este enfoque garantiza que en cada paso puedas entender, ejecutar y probar
# lo que estás construyendo, sin depender de código que "aún no existe".

# Ahora vamos a construir cada uno de estos archivos, empezando por los cimientos.


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 3: CONFIGURACIÓN POR ENTORNOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/core/config.py
# ─────────────────────────────────────────────────────────────────────────────
# Administrar la configuración de Flask es vital para no exponer secretos
# (contraseñas, claves API) y para facilitar el despliegue en múltiples entornos.
# Usamos clases de Python que heredan de una base común.
#
# 💡 Consistencia de Base de Datos (Dev/Prod):
# Es una excelente práctica (12-Factor App) usar el mismo motor de base de datos
# en desarrollo y producción (ej: SQL Server). Esto previene inconsistencias
# de comportamiento (tipos de datos, índices, transacciones y dialectos SQL).

import os
# os pertenece a la biblioteca estándar de Python, por lo que no requiere instalación adicional.
# Lo usamos para leer variables de entorno del sistema operativo en tiempo de ejecución.

# ─────────────────────────────────────────────────────────────────────────────
# HELPER DE VALIDACIÓN
# ─────────────────────────────────────────────────────────────────────────────
 
def _require_env(key: str) -> str:
    """
    Lee una variable de entorno y garantiza que existe Y no está vacía.
 
    Problema que resuelve:
      os.environ["KEY"] implementa Fail-Fast para claves AUSENTES, pero si la
      clave existe con valor vacío (DB_SERVER="") o solo espacios (DB_SERVER="  "),
      no falla: la URI se construye mal y el error aparece en la primera consulta
      real en producción — demasiado tarde.
 
    Esta función cubre los tres casos problemáticos:
      - Clave ausente       → EnvironmentError
      - Clave vacía ""      → EnvironmentError
      - Clave con espacios  → EnvironmentError  (.strip())
 
    Solo se usa en ProductionConfig. En desarrollo, os.environ.get() con
    valores por defecto es suficiente y más cómodo.
    """
    value = os.environ.get(key, "").strip()
    if not value:
        raise EnvironmentError(
            f"[PRODUCCIÓN] Variable de entorno requerida ausente o vacía: '{key}'. "
            f"El servidor no puede arrancar sin ella."
        )
    return value

# ─────────────────────────────────────────────────────────────────────────────
# BASE
# ─────────────────────────────────────────────────────────────────────────────

class ConfigBase:
    """Configuraciones compartidas en todos los entornos."""
    # Esta es la configuración base que será común y compartida entre todas las configuraciones DEV y PROD (Patrón de Herencia de Clases).
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave_desarrollo_temporal")
    # os.environ.get() lee variables del sistema operativo exclusivamente. No tiene capacidad
    # de leer un archivo .env por sí solo. Si no encuentra la variable, usa el valor por defecto,
    # permitiendo arrancar la app sin interrupciones en desarrollo.
    #
    # ¿Cómo se leen entonces las variables de un archivo .env?
    # Herramientas como python-dotenv (load_dotenv()) las "elevan" al sistema operativo antes
    # de que config.py se ejecute. Una vez en el sistema, os.environ.get() las encuentra con
    # normalidad — el mecanismo de lectura no cambia, cambia quién pobló el sistema operativo.
    # Esto se configura en el entry point (run.py o app/__init__.py), nunca aquí.
    #
    # Recomendación: .env solo en desarrollo. En producción, usar variables del propio sistema
    # de alojamiento (variables del SO, AWS Secrets Manager, Azure Key Vault, etc.), nunca
    # un archivo .env en el servidor.
    #
    # En producción esta línea es sobreescrita por _require_env() en ProductionConfig,
    # que aplica Fail-Fast real (ver más abajo).
    #
    # Recomendación para generar una SECRET_KEY segura con el módulo nativo 'secrets':
    # python -c "import secrets; print(secrets.token_hex(32))"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_TRACK_MODIFICATIONS es una función antigua que se mantiene por RETROCOMPATIBILIDAD para no romper aplicaciones viejas. 
    # Básicamente es un sistema de seguimiento de eventos para cambios en la DB que consume demasiada memoria RAM y CPU, ralentizando el servidor y perjudicando la escalabilidad. Por ello se prefiere optar por alertas propias del ORM o de la propia DB.

# ─────────────────────────────────────────────────────────────────────────────
# DESARROLLO
# ─────────────────────────────────────────────────────────────────────────────

class DevelopmentConfig(ConfigBase):
    """Entorno de desarrollo local."""
    
    DEBUG = True
    # DEBUG = True activa el debugger interactivo y la recarga automática del servidor.
    # Facilita ubicar errores (ofrece un mapa interactivo en el navegador), pero expone
    # líneas de código sensibles. NUNCA usar en producción.
    
    # Construimos la URI dinámicamente desde variables de entorno para evitar
    # credenciales o IPs hardcodeadas en el código fuente (principio 12-Factor App).
    _dev_server = os.environ.get("DB_SERVER_DEV", "localhost")
    _dev_db     = os.environ.get("DB_NAME_DEV", "MiBaseDatosDev")
    _dev_driver = os.environ.get("DB_DRIVER", "ODBC+Driver+18+for+SQL+Server")
 
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://@{_dev_server}/{_dev_db}?"
        f"driver={_dev_driver};Trusted_Connection=yes;TrustServerCertificate=yes"
    )
    # TrustServerCertificate=yes es necesario en DEV cuando el servidor local usa
    # un certificado autofirmado. En producción se omite para forzar la validación TLS.
    #
    # Autenticación Integrada (Windows Auth): el '@' sin usuario indica que se usa
    # la identidad del proceso actual. Ideal para entornos corporativos locales.
    # Ver nota al pie sobre otros métodos de autenticación.

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCCIÓN
# ─────────────────────────────────────────────────────────────────────────────

class ProductionConfig(ConfigBase):
    """Entorno de producción real."""
    
    DEBUG = False
    # DEBUG = False evita exponer código sensible en el navegador y muestra
    # un error HTTP 500 genérico al usuario final.

    # ¿Por qué _require_env() y no simplemente os.environ["SECRET_KEY"]?
    # os.environ[] con corchetes lanza KeyError si la clave no existe — eso es Fail-Fast,
    # pero incompleto. Si la variable existe pero está vacía (SECRET_KEY="") o contiene
    # solo espacios (SECRET_KEY="  "), os.environ[] NO falla: devuelve el valor vacío,
    # la URI se construye mal y el error aparece en la primera consulta real en producción.
    # _require_env() cubre los tres casos: ausente, vacía y solo espacios, garantizando
    # que el servidor no arranca a menos que todas las variables tengan valores reales.
    SECRET_KEY   = _require_env("SECRET_KEY")
    _prod_server = _require_env("DB_SERVER")
    _prod_db     = _require_env("DB_NAME")
    _prod_driver = os.environ.get("DB_DRIVER", "ODBC+Driver+18+for+SQL+Server")
    # DB_DRIVER tiene valor por defecto porque un driver incorrecto produce un error
    # claro e inmediato de pyodbc al conectar, no un fallo silencioso.
 
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://@{_prod_server}/{_prod_db}?"
        f"driver={_prod_driver};Trusted_Connection=yes"
    )
    # Sin TrustServerCertificate: en producción el servidor debe tener un certificado
    # TLS válido (emitido por una CA reconocida). El Driver 18 cifra la conexión
    # por defecto (Encrypt=yes implícito), rechazando certificados autofirmados.

# ─────────────────────────────────────────────────────────────────────────────
# SELECTOR DE CONFIGURACIÓN
# ─────────────────────────────────────────────────────────────────────────────
 
config = {
    "development": DevelopmentConfig,
    "production":  ProductionConfig,
    "default":     DevelopmentConfig,
}
# Este diccionario permite seleccionar la configuración activa desde el entry point:
#
#   from app.core.config import config
#   app.config.from_object(config[os.environ.get("FLASK_CONFIG", "default")])
#
# NOTA: No existe TestingConfig en este archivo de forma intencional.
# La configuración de tests se inyecta a nivel de fixture en conftest.py,
# manteniendo cada suite autocontenida y desacoplada de la configuración global.

# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA: Métodos de Autenticación en SQL Server
# ─────────────────────────────────────────────────────────────────────────────

# 1. Autenticación Integrada (Windows Auth / Trusted Connection)
# Ideal para entornos corporativos locales. No requiere almacenar contraseñas en texto plano.
# NOTA: En arquitecturas de contenedores (Docker/Linux), requiere configuración
# adicional de Kerberos. En esos casos se recomienda Autenticación Estándar.
#
# SQLALCHEMY_DATABASE_URI = (
#     "mssql+pyodbc://@SERVIDOR/BASE_DATOS?"
#     "driver=ODBC+Driver+18+for+SQL+Server;Trusted_Connection=yes"
# )
#
# Desglose:
#   mssql+pyodbc://        → Dialecto SQLAlchemy + driver pyodbc
#   @SERVIDOR              → '@' sin usuario indica autenticación integrada del proceso actual
#   /BASE_DATOS            → Nombre de la base de datos
#   Trusted_Connection=yes → Activa el inicio de sesión único (SSO) basado en la identidad del sistema
 
 
# 2. Autenticación Estándar (Usuario y Contraseña)
# Requerida si SQL Server está en Linux, Docker, en la nube (ej: Azure SQL)
# o en redes sin Active Directory.
#
# SQLALCHEMY_DATABASE_URI = (
#     "mssql+pyodbc://usuario:contraseña@servidor:1433/base_datos?"
#     "driver=ODBC+Driver+18+for+SQL+Server"
# )
#
# Desglose:
#   usuario:contraseña     → Credenciales SQL creadas en la instancia
#   @servidor:1433         → IP o dominio del servidor + puerto por defecto de SQL Server
#   /base_datos            → Nombre de la base de datos
#   driver=ODBC+Driver+18  → El driver instalado en el sistema operativo debe coincidir
#                            exactamente con la versión declarada aquí

# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA: Otros motores de Base de Datos
# ─────────────────────────────────────────────────────────────────────────────

# SQLAlchemy es multi-dialecto. Si deseas migrar tu aplicación a otro motor de base de datos,
# solo necesitas cambiar la URI de conexión e instalar el driver correspondiente:

# A. PostgreSQL (Usando el driver estándar de la industria 'psycopg2' o el moderno 'psycopg')
# SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost:5432/mi_base_datos'

# B. MySQL / MariaDB (Usando el driver 'pymysql' para compatibilidad nativa en Python)
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:contraseña@localhost:3306/mi_base_datos'

# C. SQLite (Excelente para pruebas de unidad ultrarrápidas y prototipos sin dependencias externas)
# SQLALCHEMY_DATABASE_URI = "sqlite:///archivo_local.db"
# SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # En memoria, sin persistencia en disco

# ─────────────────────────────────────────────────────────────────────────────
# GLOSARIO DE CLAVES
# ─────────────────────────────────────────────────────────────────────────────
# SECRET_KEY                    → Firma cookies de sesión, protección CSRF y tokens de un solo uso
#                                 (ej: enlaces temporales para recuperación de contraseña).
# SQLALCHEMY_DATABASE_URI       → URI que SQLAlchemy usa para conectarse a la base de datos.
# SQLALCHEMY_TRACK_MODIFICATIONS → False elimina overhead de memoria y CPU innecesario.
# DEBUG                         → True: debugger interactivo y recarga automática (solo DEV).
#                                 False: error HTTP 500 genérico al usuario (PROD).


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 4: MODELOS ORM (SQLAlchemy 2.0+) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/modulos/usuarios/models.py
# ─────────────────────────────────────────────────────────────────────────────
# SQLAlchemy es el ORM más potente del ecosistema Python. Mapea tablas
# relacionales como clases de Python, permitiendo operar la BD sin SQL manual.
#
# 💡 Revolución SQLAlchemy 2.0+ (Tipado Estático PEP 484):
# El sistema moderno basado en Type Hints ('Mapped' y 'mapped_column') resuelve
# el gran problema de las versiones 1.x: la falta de autocompletado en el IDE
# y la imposibilidad de hacer análisis estático de errores con herramientas como Mypy.
#
# Al heredar de 'db.Model', cada clase representa una tabla física en la BD,
# y cada atributo de clase tipado representa una columna con restricciones.

from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


# ─────────────────────────────────────────────────────────────────────────────
# MODELO: DEPARTAMENTO (Entidad Padre)
# ─────────────────────────────────────────────────────────────────────────────

class DepartamentoModel(db.Model):
    __tablename__ = "departamentos"
    # __tablename__ es obligatorio en SQLAlchemy 2.0 con el sistema declarativo.
    # Convención estándar: snake_case en plural (empleados, departamentos).
    # Si se omite, SQLAlchemy lanza un error al inicializar — no hay inferencia
    # automática del nombre de tabla a partir del nombre de la clase.

    id: Mapped[int] = mapped_column(primary_key=True)
    # Mapped[int] deduce automáticamente 'nullable=False' — ninguna clave primaria
    # puede ser NULL. Con primary_key=True, SQLAlchemy además genera la columna
    # con autoincremento usando el mecanismo nativo del motor activo:
    #   - SQL Server  → IDENTITY(1,1)
    #   - PostgreSQL  → SERIAL / IDENTITY
    #   - SQLite      → AUTOINCREMENT implícito en INTEGER PRIMARY KEY
    # SQLAlchemy abstrae la diferencia, pero el comportamiento real depende
    # del dialecto configurado en SQLALCHEMY_DATABASE_URI.

    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    # Al declarar 'Mapped[str]', SQLAlchemy deduce automáticamente 'nullable=False'.
    # 'String(100)' define el límite físico en SQL, mapeando a VARCHAR(100).
    # Para columnas que se indexarán o compararán frecuentemente, siempre preferir
    # String(n) sobre Mapped[str] sin límite, que genera VARCHAR(max) en SQL Server
    # con implicaciones de rendimiento en índices y comparaciones.

    # 🔄 Relación 1-a-Muchos (Padre → Hijos)
    empleados: Mapped[list["EmpleadoModel"]] = relationship(
        back_populates="departamento",
        cascade="all, delete-orphan"
    )
    # - Mapped[list[...]] le dice al IDE que esto retornará una colección iterable de objetos.
    #
    # - back_populates: Obliga a una declaración bidireccional explícita en ambos modelos,
    #   garantizando tipado y autocompletado perfecto en ambos extremos de la relación.
    #   Es el estándar moderno frente al antiguo 'backref', que declaraba la relación de
    #   forma "mágica" e invisible en la otra clase, rompiendo el análisis estático.
    #
    # - cascade="all, delete-orphan": Regla de integridad de negocio. Si el departamento
    #   (Padre) se elimina, todos sus empleados asociados (Hijos) se borran automáticamente
    #   de la BD. Técnicamente agrupa las siguientes operaciones:
    #     · save-update   → propaga INSERT/UPDATE del padre a los hijos en sesión.
    #     · merge         → propaga db.session.merge() del padre a los hijos.
    #     · delete        → propaga el DELETE del padre a los hijos en BD.
    #     · delete-orphan → elimina hijos que se desvinculan del padre (ej: empleado.departamento = None).
    #   El caso más crítico en producción es delete-orphan: si desvinculás un hijo
    #   de su padre, SQLAlchemy lo elimina automáticamente de la BD.
    #   Si no deseas ese comportamiento, usa solo cascade="all" sin delete-orphan.

    def __repr__(self) -> str:
        return f"<DepartamentoModel id={self.id} nombre={self.nombre!r}>"
    # __repr__ es el estándar profesional en modelos ORM. Sin él, al depurar o loguear
    # un objeto obtienes algo inútil como <DepartamentoModel object at 0x7f3a...>.
    # Con él, obtienes información accionable directamente en los logs y el debugger.
    #
    # Sobre el uso de !r:
    # !r aplica repr() al valor, añadiendo comillas en strings ('Marketing') y distinguiendo
    # None del string "None". Para tipos int y bool, !r es redundante — se representan
    # igual con o sin él — por eso se omite en id y se reserva para campos de texto.


# ─────────────────────────────────────────────────────────────────────────────
# MODELO: EMPLEADO (Entidad Hijo)
# ─────────────────────────────────────────────────────────────────────────────

class EmpleadoModel(db.Model):
    __tablename__ = "empleados"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(String(120), unique=True)

    activo: Mapped[bool] = mapped_column(default=True)
    # 'default' es una evaluación en el lado de Python (Application-side default).
    # Si al instanciar el objeto no envías este campo, el ORM le inyecta 'True'
    # en memoria justo antes de ejecutar el INSERT.
    #
    # ¿Por qué 'default' y no 'server_default'?
    #   - default (Application-side): el ORM inyecta el valor en Python ANTES del INSERT.
    #     Funciona aunque el INSERT no llegue a ejecutarse (ej: validación previa que falla).
    #     Apropiado cuando solo Flask escribe en esta tabla.
    #
    #   - server_default (Database-side): el valor lo pone el motor SQL al ejecutar el INSERT.
    #     Útil cuando múltiples aplicaciones distintas escriben en la misma BD (no solo Flask),
    #     garantizando el valor por defecto independientemente del cliente que inserte.
    #     Ejemplo: server_default=text("1") para BIT en SQL Server.
    #
    # Regla general: si solo Flask escribe en la BD → 'default'.
    # Si hay otros sistemas escribiendo en la misma tabla → 'server_default'.

    # 🔗 Clave Foránea (Foreign Key)
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id", ondelete="CASCADE"))
    # Restricción física relacional. Vincula la columna al ID de la tabla 'departamentos'.
    # El motor de BD rechazará cualquier valor que no exista en departamentos.id (IntegrityError).
    #
    # NOTA DE DISEÑO — El hijo está obligado de por vida a tener un padre:
    # Al ser Mapped[int] (NOT NULL), esta columna nunca puede ser NULL en la BD.
    # Desvincular un empleado de su departamento sin borrarlo (empleado.departamento = None)
    # provocaría que SQLAlchemy intente UPDATE SET departamento_id = NULL,
    # que la BD rechazará con un IntegrityError catastrófico en producción.
    # Las únicas salidas válidas son:
    #   1. Borrar al empleado explícitamente   → db.session.delete(empleado)
    #   2. Reasignarlo a otro departamento     → empleado.departamento = otro_departamento
    # Si el negocio requiriera empleados "flotantes" sin departamento, la sintaxis
    # correcta sería Mapped[int | None], que genera una columna NULL en la BD.
    #
    # ondelete="CASCADE" — Cascada a nivel de Base de Datos (complementaria a SQLAlchemy):
    # cascade="all, delete-orphan" en el Padre solo actúa si el borrado pasa por Flask.
    # Si un DBA borra un departamento directamente en SQL Server con un comando SQL
    # (DELETE FROM departamentos WHERE id = 1), la BD lanzará un error de clave foránea
    # porque no sabe qué hacer con los empleados huérfanos — Flask no intervino.
    # ondelete="CASCADE" instruye al propio motor SQL para que propague el borrado
    # automáticamente, independientemente de si el DELETE vino de Flask o de una
    # herramienta externa. Ambas cascadas coexisten con responsabilidades distintas:
    #   - cascade="all, delete-orphan" → gestiona objetos en la sesión SQLAlchemy (Python).
    #   - ondelete="CASCADE"           → gestiona filas directamente en el motor de BD (SQL).

    # 🔄 Relación Inversa (Hijo → Padre)
    departamento: Mapped["DepartamentoModel"] = relationship(
        back_populates="empleados"
    )
    # - Mapped["DepartamentoModel"] (sin list) indica al IDE que retorna una única instancia.
    # - NOTA DE DISEÑO: Aquí NO se usa cascade="all, delete-orphan". Las cascadas de
    #   destrucción fluyen del Padre al Hijo, nunca al revés. Si eliminas a un empleado
    #   (Hijo), no deseas bajo ningún concepto que se destruya el departamento entero
    #   (Padre) y se purgue al resto de la plantilla.

    def __repr__(self) -> str:
        return f"<EmpleadoModel id={self.id} email={self.email!r}>"
    # !r se usa en email (str) para añadir comillas y distinguir None de "None".
    # En id (int) se omite porque los enteros se representan igual con o sin él.


# ─────────────────────────────────────────────────────────────────────────────
# 📘 GLOSARIO DE LA SINTAXIS MODERNA (2.0+)
# ─────────────────────────────────────────────────────────────────────────────
# 1. Mapped[T]:
#    Anotación de tipo nativa de Python. Define el tipo de dato en memoria y la nulidad física:
#      - Mapped[str]        → VARCHAR / TEXT NOT NULL (Obligatorio)
#      - Mapped[str | None] → VARCHAR / TEXT NULL     (Opcional)
#    El error si intentas guardar un NULL se evalúa en tiempo de commit (IntegrityError).
#
# 2. mapped_column():
#    Sustituye al antiguo 'db.Column()'. Configura las restricciones directamente en el motor
#    de la base de datos (longitudes, índices, unicidad, defaults).
#    Si se deja vacío [columna: Mapped[str] = mapped_column()], SQLAlchemy infiere el tipo
#    de Python y crea una columna de texto ilimitado NOT NULL por defecto.
#
# 3. back_populates vs backref (El Estándar Actual):
#    - 'backref' (Antiguo): declaraba la relación de forma "mágica" e invisible en la otra
#      clase, rompiendo el autocompletado y el análisis estático con herramientas como Mypy.
#    - 'back_populates' (Moderno): exige que la relación esté escrita explícitamente en los
#      dos modelos, permitiendo que el IDE conozca de antemano qué tipos de datos se cruzan.


# ─────────────────────────────────────────────────────────────────────────────
# 🌐 REFERENCIA: Equivalencias de Tipado Físico según el Motor de BD
# ─────────────────────────────────────────────────────────────────────────────
# Al ejecutar db.create_all(), SQLAlchemy traduce Mapped[T] al dialecto del motor activo:
#
# | Tipo SQLAlchemy  | SQL Server (mssql)  | PostgreSQL (postgresql) | SQLite (sqlite)  |
# | :---             | :---                | :---                    | :---             |
# | Mapped[int]      | INT NOT NULL        | INTEGER NOT NULL        | INTEGER NOT NULL |
# | Mapped[str]*     | VARCHAR(max)**      | TEXT NOT NULL           | TEXT NOT NULL    |
# | String(100)      | VARCHAR(100)        | VARCHAR(100)            | VARCHAR(100)     |
# | Mapped[bool]     | BIT NOT NULL        | BOOLEAN NOT NULL        | INTEGER NOT NULL |
#
# * Mapped[str] sin String(n): para columnas que se indexarán o compararán,
#   siempre preferir String(n) explícito para controlar el tamaño físico.
#
# ** VARCHAR(max) en SQL Server permite hasta 2GB pero tiene restricciones:
#    no puede usarse en índices estándar ni en claves únicas compuestas.
#    Para columnas con unique=True o índices, es obligatorio usar String(n).

# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 5: SERVICIOS — LÓGICA DE NEGOCIO (SQLAlchemy 2.0+) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/modulos/usuarios/services.py
# ─────────────────────────────────────────────────────────────────────────────
# La capa de servicios contiene la lógica de negocio pura. NUNCA debe recibir
# objetos request ni response de Flask. Solo recibe datos validados y opera
# contra la base de datos usando los modelos del Bloque 4.
#
# 💡 Transacciones Modernas (SQLAlchemy 2.0):
# En lugar de ensuciar el código con bloques try/except/commit/rollback repetitivos,
# usamos el administrador de contexto `with db.session.begin():`.
# Este patrón autocomita la transacción si el bloque finaliza con éxito, o hace
# rollback automático si ocurre cualquier excepción, garantizando la integridad de la BD.
#
# ⚠️ TRAMPA ARQUITECTÓNICA — Transacciones Anidadas (InvalidRequestError):
# db.session.begin() intenta iniciar una transacción en la sesión actual. Si en el
# futuro compones funciones de servicio (ej: registrar_ingreso_empleado() llama a
# crear_empleado() y luego a asignar_equipo()), cada función intentará abrir su propia
# transacción. SQLAlchemy lanzará InvalidRequestError: "A transaction is already begun
# on this session" porque no permite begin() anidado sobre una sesión activa.
#
# Soluciones según el escenario:
#   - Funciones simples no compuestas (este archivo): db.session.begin() es correcto.
#   - Funciones compuestas reutilizables: usar db.session.begin_nested() (Savepoints),
#     que permite puntos de guardado parciales dentro de una transacción padre.
#   - Arquitecturas avanzadas: delegar el ciclo de vida de la transacción (Unit of Work)
#     a la capa superior (el framework/API en su ciclo de vida de la petición HTTP).

from app import db
from app.modulos.usuarios.models import EmpleadoModel, DepartamentoModel
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

# ─────────────────────────────────────────────────────────────────────────────
# ALLOWLIST DE CAMPOS ACTUALIZABLES
# ─────────────────────────────────────────────────────────────────────────────

# Columnas físicas de la BD que pueden modificarse vía API.
# Usamos __table__.columns en lugar de una lista manual porque se autoactualiza
# si el modelo cambia — no hay que recordar actualizar dos sitios.
# Esto excluye estrictamente relaciones ORM, métodos internos de SQLAlchemy
# y atributos de infraestructura (ej: _sa_instance_state, metadata).
# hasattr() NO es seguro para este propósito: devuelve True para cualquier
# propiedad del objeto, incluyendo relaciones complejas y métodos internos.
# Si el cliente envía {"departamento": "Marketing"}, hasattr() lo aprobaría
# e intentaría machacar el objeto relacional con un string, rompiendo la app.
CAMPOS_ACTUALIZABLES = {col.name for col in EmpleadoModel.__table__.columns}


# ─────────────────────────────────────────────────────────────────────────────
# CREATE
# ─────────────────────────────────────────────────────────────────────────────

def crear_empleado(nombre: str, email: str, departamento_id: int) -> EmpleadoModel:
    nuevo = EmpleadoModel(nombre=nombre, email=email, departamento_id=departamento_id)

    # El context manager begin() maneja automáticamente el ciclo de vida de la transacción.
    # No es necesario llamar a db.session.commit() ni db.session.rollback() manualmente.
    with db.session.begin():
        db.session.add(nuevo)

    # NOTA: Tras el cierre del bloque begin(), SQLAlchemy expira los atributos del objeto.
    # Si accedes a nuevo.id fuera del contexto, SQLAlchemy emitirá automáticamente un
    # SELECT para refrescarlo (lazy load). Si la sesión ya está cerrada en ese momento,
    # obtendrás un DetachedInstanceError. En Flask con scoped_session, la sesión vive
    # durante toda la petición HTTP, por lo que este acceso es seguro dentro del request.
    return nuevo


# ─────────────────────────────────────────────────────────────────────────────
# READ
# ─────────────────────────────────────────────────────────────────────────────

def obtener_empleado(empleado_id: int) -> EmpleadoModel | None:
    # db.session.get() es el método moderno y tipado para búsquedas por clave primaria.
    # Internamente revisa primero el caché de la sesión (Identity Map) antes de ir a la BD.
    return db.session.get(EmpleadoModel, empleado_id)


def obtener_empleados() -> list[EmpleadoModel]:
    # Sintaxis 2.0+: construimos una sentencia (statement) con select() y la ejecutamos.
    # db.session.scalars() retorna un cursor iterable de objetos del modelo (no tuplas).
    stmt = select(EmpleadoModel)

    # ⚠️ ADVERTENCIA DE ESCALABILIDAD: Esta función carga TODOS los registros en memoria.
    # En producción con tablas grandes, usar paginación para evitar agotar la RAM:
    #
    # def obtener_empleados(pagina: int = 1, por_pagina: int = 20) -> list[EmpleadoModel]:
    #     stmt = select(EmpleadoModel).offset((pagina - 1) * por_pagina).limit(por_pagina)
    #     return list(db.session.scalars(stmt).all())
    return list(db.session.scalars(stmt).all())


def obtener_por_departamento(dep_nombre: str) -> list[EmpleadoModel]:
    # ─── El Problema N+1 y las Estrategias de Carga ───────────────────────────
    #
    # Sin Eager Loading (Lazy Loading por defecto):
    # SQLAlchemy haría 1 consulta para traer el departamento. Luego, al iterar
    # sobre sus empleados en un bucle, dispararía 1 consulta adicional POR CADA
    # empleado (N consultas). Con 50 empleados → 51 consultas a la BD.
    # Esto destruye el rendimiento por el coste de red (Network Roundtrips).
    #
    # joinedload — Eager Loading con JOIN (usado aquí):
    # Emite 1 única consulta SQL combinando ambas tablas con LEFT OUTER JOIN.
    # Trae el padre y todos los hijos en un solo viaje a la BD.
    # Ideal para: relaciones *-a-uno, búsquedas unitarias, listas pequeñas (< ~100 registros).
    # Limitación: en relaciones 1-a-muchos masivas, el JOIN duplica los datos del padre
    # en cada fila del resultado, pudiendo saturar la memoria RAM.
    #
    # selectinload — La alternativa experta para colecciones grandes (SQLAlchemy 2.0+):
    # Emite exactamente 2 consultas SQL:
    #   1. SELECT * FROM departamentos WHERE nombre = ?
    #   2. SELECT * FROM empleados WHERE departamento_id IN (id1, id2, ...)
    # Evita la duplicación de datos del JOIN y es la recomendación oficial de
    # SQLAlchemy 2.0+ para relaciones 1-a-muchos con colecciones grandes.
    # Para usar: reemplazar joinedload(DepartamentoModel.empleados)
    #        por selectinload(DepartamentoModel.empleados)
    stmt = (
        select(DepartamentoModel)
        .where(DepartamentoModel.nombre == dep_nombre)
        .options(joinedload(DepartamentoModel.empleados))
    )

    # db.session.scalar() (singular) retorna directamente el primer resultado o None.
    # ⚠️ PRECAUCIÓN: lanza MultipleResultsFound si la consulta devuelve más de una fila.
    # Su uso es seguro aquí ÚNICAMENTE porque DepartamentoModel.nombre tiene unique=True,
    # garantizando que la BD nunca retornará más de un resultado para esta búsqueda.
    # En columnas que admitan duplicados, usar db.session.scalars(stmt).first() en su lugar,
    # que retorna el primero silenciosamente sin lanzar excepción ante múltiples resultados.
    depto = db.session.scalar(stmt)
    return depto.empleados if depto else []


# ─────────────────────────────────────────────────────────────────────────────
# UPDATE
# ─────────────────────────────────────────────────────────────────────────────

def actualizar_empleado(empleado_id: int, datos_actualizados: dict) -> EmpleadoModel | None:
    # La verificación de existencia ocurre FUERA del bloque transaccional.
    # Hacerlo dentro con un `return None` prematuro provocaría que begin() ejecute
    # un commit() vacío — un viaje innecesario al motor SQL sin nada que persistir.
    # La transacción debe abrirse solo cuando hay una escritura real que realizar.
    #
    # TRADE-OFF — Race Condition residual:
    # Existe una ventana de tiempo entre esta lectura y la escritura posterior donde
    # otro proceso podría borrar el registro. En la práctica, este escenario es
    # extremadamente improbable en APIs CRUD estándar. Si el negocio lo requiere,
    # la solución es usar SELECT ... WITH (UPDLOCK) vía with_for_update() de SQLAlchemy,
    # que bloquea la fila a nivel de BD durante la lectura.
    empleado = db.session.get(EmpleadoModel, empleado_id)
    if not empleado:
        return None

    # La transacción se abre solo si el empleado existe — limpia y sin commits vacíos.
    # Iteramos solo sobre columnas físicas de la BD (CAMPOS_ACTUALIZABLES).
    # Ver definición y justificación de la allowlist al inicio del archivo.
    #
    # ⚠️ OBJETO "SUCIO" EN RAM TRAS IntegrityError:
    # begin() garantiza rollback automático en la BD si el commit falla (ej: email duplicado).
    # Sin embargo, los atributos del objeto en la RAM de Python NO se revierten mágicamente.
    # Si capturás el IntegrityError y seguís usando el objeto empleado en la misma sesión,
    # sus atributos ya fueron mutados por setattr() con los valores nuevos.
    # Solución: refrescar el objeto desde la BD antes de reutilizarlo:
    #   db.session.refresh(empleado)  → recarga los valores reales desde la BD.
    with db.session.begin():
        for campo, valor in datos_actualizados.items():
            if campo in CAMPOS_ACTUALIZABLES:
                setattr(empleado, campo, valor)

    return empleado


# ─────────────────────────────────────────────────────────────────────────────
# DELETE
# ─────────────────────────────────────────────────────────────────────────────

def eliminar_empleado(empleado_id: int) -> bool:
    # La verificación de existencia ocurre FUERA del bloque transaccional,
    # por la misma razón que en actualizar_empleado: evitar un commit() vacío
    # cuando el registro no existe. Ver comentario completo en actualizar_empleado.
    empleado = db.session.get(EmpleadoModel, empleado_id)
    if not empleado:
        return False

    # La transacción se abre solo si hay un objeto real que borrar.
    with db.session.begin():
        db.session.delete(empleado)

    return True


# ─────────────────────────────────────────────────────────────────────────────
# 📘 ¿Por qué usar select() y db.session.scalars() en 2.0?
# ─────────────────────────────────────────────────────────────────────────────
# 1. Separación de Conceptos: separa la construcción de la query (stmt) de su ejecución física.
# 2. Eager Loading Nativo: facilita el uso de joinedload() y selectinload() de forma explícita.
# 3. Consistencia con Async: la sintaxis de select() es idéntica en SQLAlchemy síncrono y asíncrono.
# 4. Compatibilidad con Analizadores Estáticos: permite que herramientas como Mypy validen las queries.


# ─────────────────────────────────────────────────────────────────────────────
# 💡 ¿Deberían los servicios lanzar excepciones? (Patrón DDD)
# ─────────────────────────────────────────────────────────────────────────────
# En esta guía, los servicios retornan None o False cuando un recurso no existe,
# y el controlador (routes.py) decide lanzar la excepción HTTP. Esto se llama
# "Servicios Delgados" y es simple de aprender.
#
# Sin embargo, en arquitecturas de producción basadas en Domain-Driven Design (DDD),
# los servicios sí lanzan excepciones de negocio. ¿Por qué?
#
# Imagina que mañana necesitas crear una CLI, un worker de Celery o una API GraphQL
# que también llame a crear_empleado(). Esas capas NO tienen handlers HTTP.
# Si el servicio solo retorna None, el consumidor no sabe qué salió mal.
# Pero si el servicio lanza RecursoNoEncontradoError("Departamento no existe"),
# cualquier capa puede reaccionar de forma apropiada.
#
# Ejemplo de servicio con raise (patrón DDD):
#
# def crear_empleado(nombre: str, email: str, departamento_id: int) -> EmpleadoModel:
#     if not db.session.get(DepartamentoModel, departamento_id):
#         raise RecursoNoEncontradoError("El departamento especificado no existe")
#
#     existente = db.session.scalars(
#         select(EmpleadoModel).filter_by(email=email)
#     ).first()
#     if existente:
#         raise ConflictoError("El email ya está registrado")
#
#     nuevo = EmpleadoModel(nombre=nombre, email=email, departamento_id=departamento_id)
#     with db.session.begin():
#         db.session.add(nuevo)
#     return nuevo
#
# En este caso, el controlador (routes.py) se simplifica enormemente porque no necesita
# verificar si el resultado es None: si el servicio no lanza excepción, todo salió bien.
# El handler global (handlers.py) intercepta la excepción y responde con JSON estructurado.

# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 6: ESQUEMAS DE VALIDACIÓN CON PYDANTIC V2 ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/modulos/usuarios/schemas.py
# ─────────────────────────────────────────────────────────────────────────────
# Pydantic provee validación de datos con tipado estático en tiempo de ejecución.
# Definimos esquemas de ENTRADA (lo que el cliente envía) y de SALIDA
# (lo que le respondemos, ocultando datos sensibles como contraseñas).
#
# Flujo de datos:
#   Cliente → JSON → Schema de Entrada (valida estrictamente) → Service (opera) → Model ORM
#   Model ORM → Schema de Salida (serializa sin revalidar)    → JSON → Cliente
#
# Principio fundamental:
#   - Schemas de ENTRADA → estrictos: validan tipos, longitudes, formatos y campos extra.
#     Desconfiamos del cliente. Todo dato externo es potencialmente malicioso o malformado.
#   - Schemas de SALIDA  → permisivos: solo serializan. Los datos vienen de la BD,
#     ya fueron validados al entrar. Revalidarlos añade latencia sin ningún beneficio.
#     Usar tipos primitivos (str, int, bool) en lugar de tipos validadores (EmailStr, NombreEmpleado).

from typing import Annotated
from pydantic import BaseModel, Field, EmailStr, ConfigDict, model_validator


# ─────────────────────────────────────────────────────────────────────────────
# TIPOS REUTILIZABLES (Patrón DRY con Annotated)
# ─────────────────────────────────────────────────────────────────────────────
# En Pydantic v2, encapsulamos las reglas de validación en tipos personalizados
# con Annotated en lugar de duplicar Field(...) en múltiples schemas.
# Si el día de mañana cambia la longitud mínima del nombre, solo se modifica aquí.
#
# strip_whitespace=True: recorta espacios al inicio y al final automáticamente
# antes de que el dato llegue a la capa de servicios o a la BD.
# Previene bugs silenciosos de búsqueda: un nombre guardado como ' Juan '
# no aparecería en WHERE nombre = 'Juan'. Los usuarios y frontends
# siempre cometen este tipo de errores — mejor sanitizar en la entrada.
#
# Estos tipos solo se usan en schemas de ENTRADA. En schemas de SALIDA
# se usan tipos primitivos (str, int) para evitar revalidación innecesaria.
NombreEmpleado = Annotated[str, Field(min_length=3, max_length=100, strip_whitespace=True)]
IdDepartamento = Annotated[int, Field(gt=0)]


# ─────────────────────────────────────────────────────────────────────────────
# BASE DE ENTRADA (Patrón DRY para schemas de entrada)
# ─────────────────────────────────────────────────────────────────────────────

class BaseInputSchema(BaseModel):
    """Clase base para todos los schemas de entrada de la API.

    Centraliza la política de seguridad de entrada en un único lugar.
    Si en el futuro se necesita añadir una directiva global (ej: str_strip_whitespace,
    populate_by_name, o cualquier otra opción de ConfigDict), se modifica aquí
    y todos los schemas de entrada la heredan automáticamente — sin tocar 40 clases.
    """
    model_config = ConfigDict(
        extra="forbid",
        # extra="forbid": rechaza cualquier campo no declarado en el schema con un 422.
        # Patrón Fail-Fast defensivo: un campo mal escrito (departemento_id) o un intento
        # de inyectar campos no documentados (es_admin: true) falla de forma ruidosa.
        # IMPORTANTE: solo aplica a schemas de ENTRADA. En schemas de SALIDA, extra="forbid"
        # rompería la serialización si la BD tiene columnas adicionales no declaradas.
        from_attributes=True,
        # from_attributes=True incluido en la base de forma preventiva: permite construir
        # cualquier schema de entrada desde un objeto ORM si fuera necesario en tests
        # o flujos internos, sin necesidad de recordar añadirlo en cada subclase.
    )


# ─────────────────────────────────────────────────────────────────────────────
# SCHEMAS DE ENTRADA (Request Payloads)
# ─────────────────────────────────────────────────────────────────────────────

class EmpleadoCreateSchema(BaseInputSchema):
    """Valida los datos recibidos en el POST de creación."""

    nombre: NombreEmpleado
    email: EmailStr
    departamento_id: IdDepartamento


class EmpleadoUpdateSchema(BaseInputSchema):
    """Permite actualización parcial (PATCH). Todos los campos son opcionales
    sin duplicar restricciones gracias a los tipos Annotated reutilizables."""

    nombre: NombreEmpleado | None = None
    email: EmailStr | None = None
    departamento_id: IdDepartamento | None = None

    @model_validator(mode="after")
    def al_menos_un_campo(self) -> "EmpleadoUpdateSchema":
        # Sin este validador, un cliente puede enviar {} (JSON vacío) y Pydantic
        # lo acepta porque todos los campos son opcionales. El servicio no actualizaría
        # nada, haría un commit vacío y retornaría éxito — comportamiento silenciosamente
        # incorrecto que confunde al cliente y desperdicia recursos en la BD.
        #
        # ¿Por qué model_fields_set y no any()?
        # any([self.nombre, self.email, self.departamento_id]) evalúa truthiness de Python.
        # Valores como False, 0 o "" son falsy — any() los trataría como "campo no enviado"
        # y rechazaría actualizaciones perfectamente válidas. Ejemplo: si en el futuro
        # se añade activo: bool | None = None y el cliente envía {"activo": false}
        # para suspender un empleado, any() evaluaría [None, None, None, False] → False
        # y lanzaría el error rechazando una petición completamente válida.
        #
        # model_fields_set es la propiedad nativa de Pydantic v2 diseñada exactamente
        # para este caso: devuelve el conjunto de campos que el cliente envió
        # explícitamente en el JSON, sin importar si su valor es False, 0, "" o None.
        if not self.model_fields_set:
            raise ValueError("Se debe enviar al menos un campo para actualizar.")
        return self


# ─────────────────────────────────────────────────────────────────────────────
# SCHEMAS DE SALIDA (Response Payloads)
# ─────────────────────────────────────────────────────────────────────────────

class DepartamentoResponseSchema(BaseModel):
    """Esquema para serializar los datos básicos del departamento."""

    model_config = ConfigDict(from_attributes=True)
    # from_attributes=True permite a Pydantic leer directamente instancias ORM
    # de SQLAlchemy, eliminando la necesidad de métodos manuales como to_dict().

    id: int
    nombre: str
    # str en lugar de NombreEmpleado: los datos de salida provienen de la BD
    # y ya fueron validados al entrar. Revalidar longitudes en cada serialización
    # añade latencia sin beneficio. Si un dato histórico en la BD no cumpliera
    # las restricciones, Pydantic lanzaría un error de serialización inesperado.


class EmpleadoResponseSchema(BaseModel):
    """Estructura la respuesta enviada al cliente.

    Aprovecha la consulta joinedload() / selectinload() del Bloque 5 para incluir
    de forma anidada la información del departamento, evitando peticiones HTTP adicionales.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str          # str primitivo: solo serializar, sin revalidar longitud.
    email: str           # str en lugar de EmailStr: evita ejecutar regex de validación
                         # de email en cada respuesta. Con 10.000 empleados en una lista,
                         # esa regex se ejecutaría 10.000 veces añadiendo latencia innecesaria.
    activo: bool
    departamento_id: int # int primitivo: solo serializar, sin revalidar gt=0.

    # ─── ⚠️ ADVERTENCIA CRÍTICA — N+1 SILENCIOSO EN PYDANTIC ──────────────────
    # from_attributes=True hace que Pydantic acceda a los atributos del objeto ORM
    # mediante getattr(empleado, 'departamento') al serializar.
    # Si la relación 'departamento' NO fue precargada con joinedload() o selectinload()
    # en la capa de servicios, SQLAlchemy interceptará ese getattr y disparará una
    # consulta SELECT adicional por cada empleado serializado — el problema N+1
    # reaparece silenciosamente en la capa de serialización, donde nadie lo buscaría.
    #
    # CONTRATO OBLIGATORIO CON services.py:
    # Toda consulta que retorne EmpleadoResponseSchema con departamento anidado
    # DEBE usar joinedload() o selectinload() en la capa de servicios.
    # Si no se necesita el departamento anidado, usar departamento: None explícito
    # o crear un schema de respuesta simplificado sin este campo.
    departamento: DepartamentoResponseSchema | None = None


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 7: ERRORES Y OBSERVABILIDAD CENTRALIZADOS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# Una aplicación profesional no debe exponer tracebacks internos al cliente
# ni responder con páginas HTML de error en una API JSON. Centralizamos los
# errores en excepciones fuertemente tipadas y manejadores globales con registro de logs.

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/errors/exceptions.py
# ─────────────────────────────────────────────────────────────────────────────
# Creamos una jerarquía de excepciones propia para representar errores de negocio.
# Tipamos estrictamente el parámetro 'detalles' para evitar strings libres.

from typing import Any


class AppError(Exception):
    """Excepción base de la aplicación con tipado estricto.

    PRECONDICIÓN DE DISEÑO: Toda subclase de AppError debe definir 'mensaje' y
    'status_code' como atributos de clase para mantener consistencia. Si no lo hace,
    heredará los valores por defecto (500, "Error interno...") de esta clase base.
    """
    status_code: int = 500
    mensaje: str = "Error interno del servidor."

    def __init__(
        self,
        mensaje: str | None = None,
        status_code: int | None = None,
        detalles: list[dict[str, Any]] | dict[str, Any] | None = None
    ):
        if mensaje is not None:
            self.mensaje = mensaje
        if status_code is not None:
            self.status_code = status_code
        self.detalles = detalles

        # Obligatorio para que str(error) retorne texto útil en logs, Celery y pytest.
        # Sin esto, str(error) devuelve '' — inutilizable para depuración fuera del handler.
        super().__init__(self.mensaje)


class ValidacionError(AppError):
    status_code = 422
    mensaje = "La validación de la lógica de negocio ha fallado."
    # LIMITE ARQUITECTONICO (Pydantic vs ValidacionError):
    # - PydanticValidationError (automático): cuando el payload tiene tipo o formato
    #   incorrecto (campo faltante, email malformado, tipo de dato erróneo).
    #   Lo maneja handle_pydantic_validation_error() en handlers.py sin intervención manual.
    # - ValidacionError (manual en services.py): cuando los datos pasaron Pydantic
    #   pero violan reglas de negocio. Ejemplo: "El departamento_id es un entero
    #   válido, pero corresponde a un departamento que está cerrado/inactivo".


class RecursoNoEncontradoError(AppError):
    status_code = 404
    mensaje = "El recurso solicitado no fue encontrado."


class ConflictoError(AppError):
    status_code = 409
    mensaje = "El recurso ya existe o genera un conflicto de estado."


# ─── Excepciones de Seguridad (Preparadas para la capa de Autenticación) ─────
# Definidas aquí aunque se usen en los Bloques 12-14, porque la jerarquía de
# errores debe estar completa desde el principio — añadirlas después obliga
# a modificar handlers y tests ya escritos.

class NoAutenticadoError(AppError):
    status_code = 401
    mensaje = "Autenticación requerida. Token faltante o inválido."


class NoAutorizadoError(AppError):
    status_code = 403
    mensaje = "No tienes permisos suficientes para realizar esta acción."

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/errors/handlers.py
# ─────────────────────────────────────────────────────────────────────────────
# Los handlers interceptan las excepciones lanzadas en cualquier parte de la app.
# Incorporamos observabilidad (logging) y garantizamos una API JSON 100% pura.
#
# ORDEN DE REGISTRO DE HANDLERS (Crítico para la precedencia):
# Flask resuelve los handlers del MAS ESPECIFICO al MAS GENERICO.
# El orden físico de los decoradores en este archivo debe ser:
#   1. AppError                  (Específico - Errores propios de negocio)
#   2. PydanticValidationError   (Específico - Errores de schemas)
#   3. HTTPException             (Genérico   - Errores de enrutamiento de Flask/Werkzeug)
#   4. Exception                 (Genérico   - Red de seguridad final para HTTP 500)
# Invertir este registro podría causar que Exception capture errores específicos
# antes de que lleguen a su formateador adecuado.
#
# app_errorhandler() vs errorhandler():
# - errorhandler() registra el handler SOLO para las rutas de este Blueprint específico.
# - app_errorhandler() lo registra GLOBALMENTE para toda la aplicación Flask.
# Esto permite mantener los handlers separados en su propio módulo (Clean Code)
# sin acoplarlos directamente al objeto 'app' en el Factory Pattern (Bloque 9).

from flask import Blueprint, current_app, jsonify
from werkzeug.exceptions import HTTPException
from pydantic import ValidationError as PydanticValidationError
from app.errors.exceptions import AppError

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(AppError)
def handle_app_error(error: AppError):
    """Captura errores de negocio controlados (herederos de AppError)."""

    # SEVERIDAD DE LOGS DINÁMICA:
    # Distinguimos entre errores de cliente (4xx - Warning) y fallos graves del
    # servidor lanzados explícitamente vía AppError (5xx - Error con traceback).
    if error.status_code >= 500:
        current_app.logger.error(
            "AppError [%s]: %s", error.status_code, error.mensaje, exc_info=True
        )
    else:
        current_app.logger.warning("AppError [%s]: %s", error.status_code, error.mensaje)

    response = {
        "status": "error",
        "error": error.__class__.__name__,
        "mensaje": error.mensaje
    }
    if error.detalles is not None:
        response["detalles"] = error.detalles

    # jsonify() garantiza siempre el header 'Content-Type: application/json'.
    return jsonify(response), error.status_code


@errors_bp.app_errorhandler(PydanticValidationError)
def handle_pydantic_validation_error(error: PydanticValidationError):
    """Soluciona el choque Flask/Pydantic, retornando HTTP 422.

    Cuando la validación de un schema de Pydantic falla, se lanza una excepción
    nativa que este handler intercepta globalmente para responder con JSON estructurado
    en lugar de una página HTML o un traceback expuesto al cliente.
    """
    detalles = [
        {
            "campo": ".".join(str(loc) for loc in err["loc"]),
            "mensaje": err["msg"],
            "tipo": err["type"]
        }
        for err in error.errors()
    ]

    current_app.logger.warning("Pydantic ValidationError: %s", detalles)

    return jsonify({
        "status": "error",
        "error": "ValidacionError",
        "mensaje": "La validación de los datos de entrada ha fallado.",
        "detalles": detalles
    }), 422


@errors_bp.app_errorhandler(HTTPException)
def handle_http_exception(error: HTTPException):
    """Blindaje anti-HTML para errores nativos de Flask y Werkzeug.

    Captura errores de enrutamiento (404, 405, 415, etc.) y fuerza la respuesta
    en JSON, reemplazando las páginas HTML que Flask devuelve por defecto.
    Elimina la necesidad de handlers manuales individuales por cada código HTTP.
    """
    current_app.logger.warning("HTTPException [%s]: %s", error.code, error.description)

    return jsonify({
        "status": "error",
        "error": error.name,
        "mensaje": error.description
    }), error.code


@errors_bp.app_errorhandler(Exception)
def handle_unhandled_exception(error: Exception):
    """Red de seguridad final para excepciones no controladas (HTTP 500).

    Registra el traceback completo en los logs para auditoría y depuración,
    sin exponer detalles internos al cliente.
    """
    # PROGRAMACION DEFENSIVA: redirección manual de precedencias.
    # En caso de colisión en el registro de blueprints, aseguramos que el handler
    # genérico no silencie los formateadores estructurados de errores específicos.
    if isinstance(error, AppError):
        return handle_app_error(error)
    if isinstance(error, HTTPException):
        return handle_http_exception(error)
    if isinstance(error, PydanticValidationError):
        return handle_pydantic_validation_error(error)

    # Texto plano estructurado — sin emojis — para compatibilidad total con
    # parsers de observabilidad en producción (Datadog, ELK, CloudWatch).
    current_app.logger.error("Excepcion no controlada: %s", error, exc_info=True)

    return jsonify({
        "status": "error",
        "error": "InternalServerError",
        "mensaje": "Ha ocurrido un error interno en el servidor."
    }), 500

# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 8: RUTAS Y CONTROLADORES (Blueprints REST) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/modulos/usuarios/routes.py
# ─────────────────────────────────────────────────────────────────────────────
# El controlador es la capa más delgada de la arquitectura. Su ÚNICA responsabilidad
# es orquestar: recibe la petición HTTP, delega la validación a los schemas (Bloque 6),
# la lógica de negocio a los services (Bloque 5), y formatea la respuesta al cliente.
#
# 💡 Principio Clave — El controlador NO contiene lógica de negocio:
# Si mañana necesitas exponer la misma funcionalidad vía CLI, GraphQL o un worker
# de Celery, la lógica reside en services.py y es reutilizable. El controlador
# es solo un adaptador HTTP desechable.
#
# Usamos Blueprints para modularizar las rutas por dominio de negocio.
# Un Blueprint es un objeto que agrupa rutas, error handlers y hooks de forma
# aislada, permitiendo que cada módulo (usuarios, productos, reportes) se registre
# independientemente en el Factory Pattern (Bloque 9).

from flask import Blueprint, request, make_response, session, abort, redirect, url_for
from pydantic import TypeAdapter
from app.modulos.usuarios import services
from app.modulos.usuarios.schemas import EmpleadoCreateSchema, EmpleadoUpdateSchema, EmpleadoResponseSchema
from app.errors.exceptions import RecursoNoEncontradoError, ValidacionError


# ─────────────────────────────────────────────────────────────────────────────
# DEFINICIÓN DEL BLUEPRINT
# ─────────────────────────────────────────────────────────────────────────────

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/api/v1/usuarios")
# Blueprint("usuarios", __name__, url_prefix="/api/v1/usuarios"):
#   - "usuarios"    → Nombre interno del Blueprint. Se usa en url_for("usuarios.listar_usuarios").
#   - __name__      → Módulo donde reside el Blueprint (para localizar templates y static).
#   - url_prefix    → Prefijo automático para TODAS las rutas de este Blueprint.
#                     Evita repetir "/api/v1/usuarios" en cada @route. Si la versión
#                     de la API cambia a v2, solo se modifica aquí.
#
# Convención REST para el prefijo:
#   /api       → Namespace que separa la API de posibles rutas de frontend.
#   /v1        → Versionado de API. Permite mantener /v1 estable mientras /v2 evoluciona.
#   /usuarios  → Recurso en plural (convención REST universal).


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINTS CRUD — API REST
# ─────────────────────────────────────────────────────────────────────────────
# Cada endpoint sigue un flujo idéntico y predecible (Consistencia Arquitectónica):
#   1. Extraer datos del request      → request.get_json()
#   2. Validar con Pydantic           → Schema(**data) — errores capturados por handlers (Bloque 7)
#   3. Delegar a services             → services.crear_empleado(...) — lógica pura (Bloque 5)
#   4. Serializar con schema de salida → EmpleadoResponseSchema.model_validate() (Bloque 6)
#   5. Si algo falla                  → raise ExcepciónPersonalizada() → handler global responde
#
# Este patrón hace que cada nuevo endpoint sea predecible y fácil de revisar en code review.


# ─── GET /api/v1/usuarios/ — Listar todos ────────────────────────────────────

@usuarios_bp.route("/")
def listar_usuarios():
    """Retorna la lista completa de empleados con sus departamentos anidados.

    Serialización masiva: usa TypeAdapter en lugar de model_validate() individual
    porque optimiza la validación de colecciones completas en una sola pasada,
    evitando el overhead de instanciar un schema por cada elemento del iterable.
    """
    empleados = services.obtener_empleados()

    # TypeAdapter vs model_validate — Cuándo usar cada uno:
    #   - model_validate(obj)          → Un solo objeto. Retorna una instancia del schema.
    #   - TypeAdapter(list[Schema]).dump_python(lista) → Colección completa. Retorna una
    #     lista de diccionarios directamente, optimizado internamente por Pydantic v2
    #     con validación en lote (batch). Ideal para endpoints de listado.
    #
    # dump_python() serializa SIN revalidar (mode="python" por defecto).
    # Los datos provienen de la BD y ya fueron validados al entrar (principio del Bloque 6).
    resultado = TypeAdapter(list[EmpleadoResponseSchema]).dump_python(empleados)
    return {"usuarios": resultado}


# ─── GET /api/v1/usuarios/<id> — Obtener uno ─────────────────────────────────

@usuarios_bp.route("/<int:usuario_id>")
def obtener_usuario(usuario_id: int):
    """Retorna un empleado por su ID o lanza 404 si no existe.

    Usa model_validate() (objeto individual) en lugar de TypeAdapter (colección).
    model_validate() retorna una instancia del schema que luego se serializa
    a diccionario con model_dump() para la respuesta JSON.
    """
    empleado = services.obtener_empleado(usuario_id)
    if not empleado:
        # Lanzamos la excepción del Bloque 7 en lugar de usar abort(404).
        # Ventaja: el handler global (handlers.py) responde con JSON estructurado
        # consistente. abort(404) delegaría al handler de HTTPException, que tiene
        # un formato genérico sin el mensaje personalizado del recurso.
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")

    return EmpleadoResponseSchema.model_validate(empleado).model_dump()


# ─── POST /api/v1/usuarios/ — Crear ──────────────────────────────────────────

@usuarios_bp.route("/", methods=["POST"])
def crear_usuario():
    """Crea un nuevo empleado validando el payload con Pydantic.

    Flujo de datos (Bloque 6 → Bloque 5 → Bloque 4):
      JSON del cliente → EmpleadoCreateSchema (valida) → services.crear_empleado()
      → EmpleadoModel (persiste en BD) → EmpleadoResponseSchema (serializa) → JSON
    """
    # request.get_json() or {} — Patrón Defensivo:
    # Si el cliente envía un body vacío o un Content-Type incorrecto (ej: text/plain),
    # get_json() retorna None. Sin el `or {}`, desempaquetar **None lanzaría
    # TypeError("argument of type 'NoneType' is not iterable") — un error críptico
    # que no pasaría por el handler de Pydantic. Con `or {}`, Pydantic recibe un
    # diccionario vacío y lanza un ValidationError claro: "field required".
    datos_validados = EmpleadoCreateSchema(**(request.get_json() or {}))

    # model_dump() convierte el schema Pydantic a dict plano {nombre, email, departamento_id}
    # que se desempaqueta como argumentos nombrados del servicio.
    nuevo = services.crear_empleado(**datos_validados.model_dump())
    return EmpleadoResponseSchema.model_validate(nuevo).model_dump(), 201
    # HTTP 201 Created: convención REST para indicar que el recurso fue creado exitosamente.


# ─── PUT /api/v1/usuarios/<id> — Actualizar ──────────────────────────────────

@usuarios_bp.route("/<int:usuario_id>", methods=["PUT"])
def actualizar_usuario(usuario_id: int):
    """Actualiza parcialmente un empleado existente.

    NOTA DE DISEÑO — PUT vs PATCH:
    Aunque usamos PUT, el comportamiento real es de PATCH (actualización parcial)
    gracias a exclude_none=True. En REST estricto, PUT reemplaza el recurso completo
    y PATCH aplica cambios parciales. En la práctica, muchas APIs usan PUT para ambos
    casos por simplicidad. Si el equipo requiere semántica estricta, cambiar a PATCH.
    """
    datos_validados = EmpleadoUpdateSchema(**(request.get_json() or {}))

    # exclude_none=True: solo envía los campos que el cliente realmente proporcionó.
    # Si el cliente envió {"nombre": "Nuevo"}, el dict resultante es {"nombre": "Nuevo"}.
    # Los campos no enviados (None por defecto en EmpleadoUpdateSchema) se excluyen,
    # evitando sobrescribir datos existentes con NULL en la BD.
    campos_a_actualizar = datos_validados.model_dump(exclude_none=True)
    if not campos_a_actualizar:
        raise ValidacionError("No se proporcionaron campos para actualizar.")

    actualizado = services.actualizar_empleado(usuario_id, campos_a_actualizar)
    if not actualizado:
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")

    return EmpleadoResponseSchema.model_validate(actualizado).model_dump()


# ─── DELETE /api/v1/usuarios/<id> — Eliminar ─────────────────────────────────

@usuarios_bp.route("/<int:usuario_id>", methods=["DELETE"])
def eliminar_usuario(usuario_id: int):
    """Elimina un empleado por su ID. Retorna 204 No Content en caso de éxito.

    HTTP 204 No Content es la convención REST para DELETE exitoso:
    el recurso fue eliminado, no hay cuerpo en la respuesta. El string vacío ""
    es obligatorio porque Flask no permite retornar None como cuerpo.
    """
    eliminado = services.eliminar_empleado(usuario_id)
    if not eliminado:
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")
    return "", 204


# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA DIDÁCTICA: EL OBJETO REQUEST
# ─────────────────────────────────────────────────────────────────────────────
# Flask provee un proxy thread-safe 'request' que contiene toda la información
# de la petición HTTP entrante. Es un proxy porque cada hilo de ejecución
# accede a su propia petición aislada — no es una variable global compartida.
# Internamente usa el mecanismo de LocalStack de Werkzeug.

@usuarios_bp.route("/ejemplo-request", methods=["GET", "POST"])
def ejemplo_request():
    """Demuestra los atributos principales del objeto request de Flask."""
    if request.method == "GET":
        # ── Query Parameters (URL: ?limite=10&pagina=2) ──
        # request.args es un ImmutableMultiDict que parsea la query string.
        # El parámetro 'type' convierte automáticamente y retorna 'default'
        # si la conversión falla (ej: ?limite=abc → retorna 20 sin error).
        limite = request.args.get("limite", default=20, type=int)
        pagina = request.args.get("pagina", default=1, type=int)
        return {"limite": limite, "pagina": pagina}

    elif request.method == "POST":
        # ── Payload JSON (Content-Type: application/json) ──
        datos_json = request.json                        # Equivalente a request.get_json()

        # ── Formulario HTML (Content-Type: application/x-www-form-urlencoded) ──
        nombre = request.form.get("nombre")

        # ── Headers HTTP ──
        token = request.headers.get("Authorization")

        # ── IP del Cliente ──
        # ⚠️ PRECAUCIÓN: detrás de un proxy reverso (Nginx, AWS ALB), remote_addr
        # devuelve la IP del proxy, no la del cliente real. Usar request.access_route[0]
        # o el header X-Forwarded-For con precaución (puede ser falsificado).
        ip = request.remote_addr

        return {"recibido": True}, 201


# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA DIDÁCTICA: CONSTRUCCIÓN DE RESPUESTAS HTTP
# ─────────────────────────────────────────────────────────────────────────────
# Flask ofrece múltiples formas de construir respuestas. Cada una tiene un caso
# de uso específico, desde respuestas simples hasta descargas de archivos.

# 1. String simple → asume HTML con código 200
#    return "Hola Mundo"

# 2. Diccionario directo (Flask 1.1+) → serializa automáticamente a JSON
#    return {"ok": True}, 201
#    Flask internamente llama a jsonify() y establece Content-Type: application/json.

# 3. Tupla (cuerpo, código, headers) → control granular de la respuesta
#    return {"ok": True}, 200, {"X-Custom-Header": "valor"}

# 4. Objeto Response completo con make_response() → control total
#    Necesario cuando se debe manipular cookies, headers especiales o Content-Type.

@usuarios_bp.route("/descargar-csv")
def descargar_csv():
    """Genera un CSV en memoria y lo envía como archivo descargable.

    make_response() es necesario aquí porque necesitamos modificar los headers
    de la respuesta (Content-Disposition para forzar descarga, Content-Type
    para indicar que es un CSV y no HTML).
    """
    contenido_csv = "id,nombre,email\n1,Andres,andres@correo.com"
    response = make_response(contenido_csv)
    response.headers["Content-Disposition"] = "attachment; filename=usuarios.csv"
    # Content-Disposition: attachment fuerza al navegador a descargar el archivo
    # en lugar de renderizarlo en pantalla.
    response.headers["Content-Type"] = "text/csv"
    return response


# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA DIDÁCTICA: RUTEO DINÁMICO CON CONVERTIDORES DE TIPO
# ─────────────────────────────────────────────────────────────────────────────
# Flask permite extraer parámetros tipados de la URL usando convertidores.
# El convertidor valida el tipo ANTES de que la función se ejecute.
# Si la validación falla, Flask retorna automáticamente un 404 Not Found
# (no un 400), porque considera que la URL no coincide con ninguna ruta registrada.

@usuarios_bp.route("/productos/<int:producto_id>")
def ver_producto(producto_id: int):
    """<int:id> convierte y valida que producto_id sea un entero positivo."""
    return {"producto_id": producto_id}

@usuarios_bp.route("/archivos/<path:ruta_archivo>")
def ver_archivo(ruta_archivo: str):
    """<path:ruta> acepta texto incluyendo barras '/' (a diferencia de <string>)."""
    return {"ruta": ruta_archivo}

@usuarios_bp.route("/token/<uuid:user_token>")
def ver_por_token(user_token):
    """<uuid:token> valida que sea una cadena UUID válida (RFC 4122)."""
    return {"token": str(user_token)}

# ─── Convertidores Disponibles ───
#   <int:id>     → Entero positivo. Rechaza negativos y decimales.
#   <float:val>  → Número decimal (acepta punto, no coma).
#   <string:nom> → String sin barras (por defecto si no se especifica convertidor).
#   <path:ruta>  → String incluyendo barras. Útil para rutas de archivos.
#   <uuid:tok>   → Cadena UUID válida. Convierte a objeto uuid.UUID internamente.


# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA DIDÁCTICA: url_for Y redirect
# ─────────────────────────────────────────────────────────────────────────────
# url_for() genera URLs dinámicamente usando el nombre del endpoint.
# Ventaja fundamental: si el url_prefix del Blueprint cambia de /api/v1 a /api/v2,
# todas las URLs generadas con url_for() se actualizan automáticamente.
# Hardcodear strings como "/api/v1/usuarios/perfil" rompe ante cualquier cambio.

@usuarios_bp.route("/perfil")
def perfil():
    """Endpoint de ejemplo para demostrar url_for."""
    return {"pagina": "perfil"}

@usuarios_bp.route("/ir-a-perfil")
def ir_a_perfil():
    """Redirige al endpoint 'perfil' usando url_for para generar la URL."""
    return redirect(url_for("usuarios.perfil"))
    # "usuarios.perfil" → "usuarios" es el nombre del Blueprint (primer argumento),
    # "perfil" es el nombre de la función Python del endpoint.
    # Si el endpoint requiere parámetros: url_for("usuarios.obtener_usuario", usuario_id=42)


# ─────────────────────────────────────────────────────────────────────────────
# REFERENCIA DIDÁCTICA: COOKIES Y SESIONES
# ─────────────────────────────────────────────────────────────────────────────

# ─── Cookies — Almacenamiento en el Cliente (Texto Plano) ────────────────────
# Las cookies se almacenan en el navegador del cliente. Son visibles y modificables
# por el usuario. NUNCA guardes datos sensibles en cookies sin cifrado.

@usuarios_bp.route("/set-cookie")
def set_cookie():
    """Establece una cookie con directivas de seguridad."""
    response = make_response("Cookie guardada!")
    response.set_cookie(
        "preferencia_tema",
        "oscuro",
        max_age=30 * 24 * 60 * 60,  # 30 días en segundos (tiempo de expiración)
        httponly=True,               # Protección XSS: JavaScript no puede leer esta cookie
        # secure=True,              # Descomentar en producción: solo se envía por HTTPS
        # samesite="Lax",           # Protección CSRF: restringe el envío cross-site
    )
    return response

@usuarios_bp.route("/get-cookie")
def get_cookie():
    """Lee una cookie del request. Retorna valor por defecto si no existe."""
    tema = request.cookies.get("preferencia_tema", "claro")
    return {"tema": tema}


# ─── Sessions — Cookies Firmadas Criptográficamente ──────────────────────────
# Flask firma los datos de la sesión usando SECRET_KEY (definida en config.py, Bloque 3).
# Los datos se almacenan en una cookie firmada en el cliente.
# El servidor valida su integridad (que no fue alterada) en cada petición.
#
# ⚠️ ADVERTENCIA DE SEGURIDAD:
# Los datos están FIRMADOS pero NO ENCRIPTADOS. Cualquiera puede decodificar
# el contenido (es Base64), pero no puede modificarlo sin invalidar la firma.
# NUNCA guardes contraseñas, tokens ni datos sensibles en la sesión.
#
# Para sesiones server-side (datos en Redis/BD), usar Flask-Session:
#   pip install Flask-Session
#   app.config["SESSION_TYPE"] = "redis"

@usuarios_bp.route("/login")
def login():
    """Almacena datos del usuario en la sesión firmada."""
    session["usuario_id"] = 42
    session["rol"] = "Administrador"
    return {"mensaje": "Sesión iniciada."}

@usuarios_bp.route("/dashboard")
def dashboard():
    """Verifica que exista una sesión activa antes de permitir acceso."""
    if "usuario_id" not in session:
        abort(401)
        # abort(n) lanza una HTTPException que el handler del Bloque 7
        # (handle_http_exception) intercepta y responde con JSON.
        # Para APIs, se prefiere raise NoAutenticadoError() del Bloque 7
        # por consistencia semántica, pero abort() es válido para rutas didácticas.
    return {"bienvenido": f"Usuario ID: {session['usuario_id']}"}

@usuarios_bp.route("/logout")
def logout():
    """Destruye todos los datos de la sesión actual."""
    session.clear()  # Limpia todos los datos de la cookie de sesión
    return {"mensaje": "Sesión cerrada."}


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 9: INICIALIZACIÓN CENTRAL — FACTORY PATTERN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/__init__.py
# ─────────────────────────────────────────────────────────────────────────────
# En lugar de crear 'app' como variable global (como en el Hola Mundo del Bloque 1),
# usamos una función fábrica (Factory Pattern). Esto resuelve dos problemas críticos:
#
#   1. Importaciones Circulares:
#      Si 'app' fuera global, models.py necesitaría importar 'app' para obtener 'db',
#      y routes.py importaría 'app' para registrar rutas. Pero app/__init__.py también
#      importa models y routes → dependencia circular → ImportError.
#      Con Factory Pattern, los módulos importan 'db' (instancia huérfana) y la función
#      create_app() los vincula en tiempo de ejecución, rompiendo el ciclo.
#
#   2. Testing Aislado:
#      Con una variable global, todos los tests comparten la misma instancia de app.
#      Con create_app(), cada suite de tests puede crear su propia instancia con
#      configuración independiente (BD en memoria, DEBUG=True, etc.).
#
# 💡 Patrón de Inicialización Perezosa (Lazy Initialization):
# Las extensiones (SQLAlchemy, Migrate) se instancian FUERA de create_app()
# como objetos "huérfanos" sin app asociada. Esto permite que cualquier módulo
# los importe (ej: from app import db) sin depender de que la app exista.
# Dentro de create_app(), init_app() los vincula a la instancia concreta.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# ─────────────────────────────────────────────────────────────────────────────
# INSTANCIAS DE EXTENSIONES (Inicialización Perezosa)
# ─────────────────────────────────────────────────────────────────────────────

db = SQLAlchemy()
# SQLAlchemy() sin argumentos crea una instancia "huérfana". No sabe a qué app
# pertenece ni qué base de datos usar. Esta instancia es la que importan los
# modelos del Bloque 4: `from app import db` → `class MiModelo(db.Model)`.
# La conexión real se establece cuando create_app() ejecuta db.init_app(app).

migrate = Migrate()
# Flask-Migrate envuelve Alembic (herramienta de migraciones de SQLAlchemy).
# Permite gestionar cambios incrementales del esquema de BD de forma segura,
# con historial y capacidad de rollback (ver comandos al final de este bloque).


# ─────────────────────────────────────────────────────────────────────────────
# APPLICATION FACTORY
# ─────────────────────────────────────────────────────────────────────────────

def create_app() -> Flask:
    """Application Factory Pattern optimizado para producción (2026).

    Lee dinámicamente la configuración del entorno del sistema operativo,
    inicializa las extensiones de forma perezosa y registra los componentes.

    Este patrón es el estándar oficial recomendado por la documentación de Flask
    para aplicaciones que requieren testing, despliegue multi-entorno o escalabilidad.
    """
    app = Flask(__name__)
    # Flask(__name__) crea la instancia de la aplicación. __name__ le indica a Flask
    # el paquete raíz para localizar templates/ y static/ relativos al módulo.

    # ── 1. Carga Dinámica de Configuración (12-Factor App: Principio 3) ──
    # La configuración se lee del sistema operativo, no del código fuente.
    # Por defecto apunta a ProductionConfig para garantizar seguridad ("fail-secure"):
    # si alguien olvida configurar la variable, la app arranca en modo estricto
    # con _require_env() que exige todas las variables críticas (Bloque 3).
    env_config = os.getenv("FLASK_CONFIG", "app.core.config.ProductionConfig")
    app.config.from_object(env_config)
    # from_object() acepta un string con la ruta completa de la clase Python
    # (ej: "app.core.config.DevelopmentConfig"). Flask importa el módulo dinámicamente
    # y copia todos los atributos en MAYÚSCULAS al diccionario app.config.

    # ── 2. Inicializar Extensiones (Vinculación Perezosa) ──
    db.init_app(app)
    # init_app() vincula la instancia de SQLAlchemy a esta app específica.
    # Internamente, lee app.config["SQLALCHEMY_DATABASE_URI"] para saber a qué
    # motor de BD conectarse. Si la URI es inválida, el error aparece aquí.

    migrate.init_app(app, db)
    # Vincula Flask-Migrate (Alembic) a esta app y a la instancia de SQLAlchemy.
    # Habilita los comandos `flask db` para gestionar migraciones.

    # ── 3. Habilitar CORS (Cross-Origin Resource Sharing) ──
    # CORS es un mecanismo de seguridad del navegador que bloquea peticiones HTTP
    # desde un dominio distinto al del servidor (Política de Mismo Origen).
    # Si el frontend (React en localhost:3000) llama a la API (Flask en localhost:5000),
    # el navegador bloqueará la petición porque los puertos son distintos.
    # Sin CORS configurado, la API funciona desde Postman o curl (no son navegadores),
    # pero falla silenciosamente desde cualquier frontend web.
    from flask_cors import CORS
    CORS(app, resources={r"/api/*": {"origins": os.getenv("ALLOWED_ORIGINS", "*")}})
    # resources={r"/api/*": ...}: CORS solo aplica a rutas bajo /api/, no a todo el servidor.
    #
    # ⚠️ ADVERTENCIA DE SEGURIDAD:
    # origins="*" permite peticiones desde CUALQUIER dominio. Esto es aceptable en
    # desarrollo, pero en producción debe restringirse a los dominios del frontend:
    #   ALLOWED_ORIGINS=https://miapp.com,https://admin.miapp.com
    # Un atacante podría crear un sitio malicioso que haga peticiones a tu API
    # usando las cookies del usuario si CORS está abierto.

    # ── 4. Registro Diferido de Blueprints ──
    # Los imports se hacen DENTRO de create_app() (no al inicio del archivo)
    # para prevenir importaciones circulares. En el momento de estos imports,
    # 'db' ya está inicializado y los modelos pueden ser cargados sin error.
    from app.modulos.usuarios.routes import usuarios_bp
    from app.errors.handlers import errors_bp

    app.register_blueprint(usuarios_bp)
    # Registra las rutas CRUD del Bloque 8 bajo /api/v1/usuarios/.

    app.register_blueprint(errors_bp)
    # Registra los handlers globales del Bloque 7. Al usar app_errorhandler(),
    # estos capturan excepciones de CUALQUIER Blueprint, no solo del suyo.

    # ❌ SE ELIMINA: with app.app_context(): db.create_all()
    # Las tablas se gestionan profesionalmente con migraciones (Flask-Migrate/Alembic).
    # Ver justificación detallada más abajo.

    return app


# ─────────────────────────────────────────────────────────────────────────────
# ⚠️ ¿POR QUÉ NO USAMOS db.create_all()? (Antipatrón de Producción)
# ─────────────────────────────────────────────────────────────────────────────
# Usar db.create_all() dentro del Factory es un antipatrón peligroso en producción:
#
#   1. No gestiona cambios incrementales: si modificas un modelo (ej: añadir columna),
#      create_all() NO altera columnas existentes, solo crea tablas nuevas.
#      Perderás cambios de esquema silenciosamente.
#
#   2. Condiciones de carrera: en despliegues con múltiples contenedores Docker,
#      cada instancia competiría por crear tablas simultáneamente, causando
#      bloqueos y deadlocks en la BD.
#
#   3. Sin historial: no hay registro de qué cambios se aplicaron ni capacidad
#      de rollback. Si una migración rompe la BD, no hay vuelta atrás.
#
# Flask-Migrate (basado en Alembic) gestiona migraciones de forma segura:
#   flask db init              → Inicializa el directorio de migraciones (solo una vez).
#   flask db migrate -m "msg"  → Genera un archivo de migración con los cambios detectados.
#   flask db upgrade           → Aplica las migraciones pendientes a la base de datos.
#   flask db downgrade         → Revierte la última migración (rollback controlado).


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: run.py
# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada de la aplicación. Este archivo va en la raíz del proyecto.
# Su única responsabilidad es instanciar la app y, en desarrollo local,
# levantar el servidor Werkzeug.
#
# ⚠️ El servidor Werkzeug (app.run()) NO es apto para producción:
#   - Maneja un solo proceso y un solo hilo por defecto.
#   - No gestiona reinicios automáticos ante fallos.
#   - No optimiza el rendimiento para cargas concurrentes.

import os
from dotenv import load_dotenv
from app import create_app

# ─── Carga de Variables de Entorno ───
load_dotenv()
# load_dotenv() lee el archivo .env del directorio raíz del proyecto y "eleva"
# sus variables al sistema operativo ANTES de que create_app() se ejecute.
# Una vez en el sistema, os.environ.get() (usado en config.py, Bloque 3) las encuentra.
#
# ⚠️ IMPORTANTE: load_dotenv() NO sobrescribe variables del sistema operativo que
# ya existen. Si DB_SERVER ya está definida en el SO, el archivo .env la ignora.
# Esto garantiza que las variables de producción (inyectadas por Docker, Kubernetes
# o el proveedor cloud) siempre tienen prioridad sobre el .env de desarrollo.
#
# Recomendación: .env solo en desarrollo. En producción, usar variables del propio
# sistema de alojamiento (AWS Secrets Manager, Azure Key Vault, Docker secrets).

# ─── Instancia Global ───
app = create_app()
# Esta variable global 'app' es requerida por servidores WSGI como Gunicorn.
# Gunicorn busca el objeto app en el módulo especificado:
#   gunicorn "run:app" --workers 4 --bind 0.0.0.0:8000
# El string "run:app" significa: "importa 'run.py' y usa su atributo 'app'".

if __name__ == "__main__":
    # Este bloque solo se ejecuta con `python run.py`, NO con Gunicorn.
    # Extraemos variables con valores de contingencia seguros para desarrollo local.
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    # 127.0.0.1 (localhost): solo acepta conexiones locales. Usar 0.0.0.0 para
    # aceptar conexiones externas (ej: desde otro dispositivo en la red).
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "t")

    app.run(host=host, port=port, debug=debug)

# ─── Ejecución en Desarrollo ───
# python run.py
# flask --app app run --debug

# ─── Ejecución en Producción (Servidor WSGI) ───
# En producción, se delega a servidores WSGI robustos como Gunicorn (Linux/Docker):
#   gunicorn "run:app" --workers 4 --bind 0.0.0.0:8000
#
# 💡 ¿Por qué '--workers 4'? (El problema del GIL)
# Debido al GIL (Global Interpreter Lock) de Python, un proceso solo puede ejecutar
# un hilo de código Python a la vez. Gunicorn sortea esta limitación levantando
# 4 procesos del sistema operativo totalmente independientes (cada uno con su propio
# GIL y su propia copia del intérprete Python).
# Esto permite que tu servidor procese 4 peticiones en paralelo real.
# Fórmula recomendada: workers = (2 × núcleos_CPU) + 1
#
# O con Waitress (compatible con Windows — no requiere compilación C):
#   waitress-serve --port=8000 --call app:create_app


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 10: LOGGING Y OBSERVABILIDAD ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/core/logging_config.py
# ─────────────────────────────────────────────────────────────────────────────
# Sin logs, estás volando a ciegas en producción. Un bug que no deja rastro
# es un bug que no se puede diagnosticar.
#
# 💡 ¿Por qué print() es un antipatrón en producción?
#   1. No es thread-safe: en un servidor multi-hilo (Gunicorn con threads),
#      múltiples print() concurrentes pueden intercalar líneas, produciendo
#      logs ilegibles e imposibles de parsear.
#   2. Sin niveles de severidad: no puedes distinguir un mensaje informativo
#      de un error crítico. En producción, necesitas filtrar por severidad
#      para alertas automáticas (ej: solo enviar alerta Slack si nivel >= ERROR).
#   3. Sin rotación: print() escribe a stdout sin límite. Si rediriges a un
#      archivo, crecerá indefinidamente hasta llenar el disco del servidor.
#   4. Sin formato estandarizado: herramientas de observabilidad (Datadog, ELK,
#      CloudWatch) necesitan logs con formato parseable (timestamp, nivel, módulo).
#
# El módulo estándar 'logging' de Python resuelve todos estos problemas.

import os
import logging
from logging.handlers import RotatingFileHandler


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN CENTRALIZADA DE LOGGING
# ─────────────────────────────────────────────────────────────────────────────

def configure_logging(app) -> None:
    """Configura el sistema de logging para la aplicación Flask.

    Se invoca dentro de create_app() (Bloque 9) para que los logs estén
    disponibles desde el primer momento de vida de la aplicación.

    Integración con el Factory Pattern:
      def create_app() -> Flask:
          app = Flask(__name__)
          ...
          configure_logging(app)   # ← Se llama aquí
          return app
    """

    # ── 1. Formato del Log ──
    # Cada línea de log incluye: timestamp, severidad, módulo origen y mensaje.
    # Este formato de texto es legible para humanos y parseable por herramientas
    # de observabilidad básicas. Para producción avanzada, considerar JSON
    # estructurado (ver referencia al final del bloque).
    log_format = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    # Componentes del formato:
    #   %(asctime)s   → Timestamp ISO 8601 (ej: 2026-06-12 14:30:05,123)
    #   %(levelname)s → Nivel de severidad (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    #   %(module)s    → Nombre del módulo Python que emitió el log
    #   %(message)s   → El mensaje de log en sí

    # ── 2. Handler para Archivo con Rotación Automática ──
    # RotatingFileHandler evita que el archivo de log llene el disco del servidor.
    # Cuando el archivo alcanza maxBytes, se renombra a app.log.1 y se crea uno nuevo.
    # Los archivos más antiguos se eliminan cuando se supera backupCount.
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=5_242_880,  # 5 MB por archivo (5 × 1024 × 1024 bytes)
        backupCount=10       # Mantiene hasta 10 archivos rotados (50 MB total máximo)
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    # El handler de archivo filtra DEBUG para no saturar el disco con mensajes
    # de bajo nivel. Solo INFO y superiores se persisten en el archivo.

    # ── 3. Handler para Consola (stdout) ──
    # Los logs en consola son esenciales para desarrollo local y para contenedores
    # Docker, donde stdout es el mecanismo estándar de recolección de logs
    # (Docker logs, Kubernetes pod logs, CloudWatch Logs).
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # ── 4. Asignar Handlers y Nivel Global ──
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    # El nivel global determina el umbral mínimo de severidad que se procesa.
    # Mensajes por debajo del nivel configurado se descartan silenciosamente.
    if app.config.get('DEBUG'):
        app.logger.setLevel(logging.DEBUG)
        # DEBUG: todos los mensajes pasan. Ideal para desarrollo.
    else:
        app.logger.setLevel(logging.INFO)
        # INFO: filtra DEBUG. Reduce el volumen de logs en producción.

    app.logger.info('Sistema de logging inicializado correctamente.')


# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: NIVELES DE SEVERIDAD DE LOGGING
# ─────────────────────────────────────────────────────────────────────────────
# | Nivel    | Valor | Cuándo usarlo                                         |
# | :---     | :---  | :---                                                  |
# | DEBUG    | 10    | Detalles internos para diagnóstico durante desarrollo  |
# | INFO     | 20    | Eventos normales del sistema (inicio, usuario creado)  |
# | WARNING  | 30    | Situación inesperada que NO detiene la operación       |
# | ERROR    | 40    | Fallo que impide completar una operación específica    |
# | CRITICAL | 50    | Fallo total del sistema (BD caída, sin memoria)        |
#
# Ejemplos de uso en servicios y rutas:
#   from flask import current_app
#
#   current_app.logger.debug("Consultando empleado ID=%s", empleado_id)
#   current_app.logger.info("Usuario creado exitosamente: %s", email)
#   current_app.logger.warning("Intento de acceso sin token desde IP: %s", ip)
#   current_app.logger.error("Error conectando a BD: %s", str(e))
#   current_app.logger.critical("Sin memoria disponible para procesar la petición")
#
# ⚠️ NOTA SOBRE FORMATO:
# Usamos logger.info("mensaje: %s", variable) en lugar de f-strings
# (logger.info(f"mensaje: {variable}")) porque el módulo logging evalúa
# el formato SOLO si el nivel está activo. Con f-strings, Python construye
# el string SIEMPRE, incluso si el nivel está desactivado — desperdiciando CPU.

# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: current_app.logger VS logging.getLogger()
# ─────────────────────────────────────────────────────────────────────────────
# - current_app.logger: el logger oficial de Flask. Hereda los handlers y el
#   nivel configurados en configure_logging(). Disponible solo dentro de un
#   request context o app context activo. Es el recomendado para código Flask.
#
# - logging.getLogger(__name__): el logger estándar de Python. Útil para módulos
#   que se ejecutan fuera del contexto de Flask (ej: tareas de Celery, scripts
#   de migración, utilidades standalone). Requiere configuración manual de handlers.
#
# Regla general: dentro de Flask → current_app.logger.
#               fuera de Flask  → logging.getLogger(__name__).


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 11: TESTING PROFESIONAL CON PYTEST ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: tests/conftest.py + tests/test_usuarios.py
# ─────────────────────────────────────────────────────────────────────────────
# Probar aplicaciones Flask garantiza la estabilidad del código ante futuros
# cambios. Sin tests, cada deploy es una apuesta. Pytest es el estándar de
# testing en Python gracias a su sintaxis simple basada en fixtures.
#
# 💡 Pirámide de Testing (Concepto Clave):
# La proporción ideal de tests en una aplicación profesional es:
#   Base:  Tests unitarios    (muchos, rápidos, aislados — testean funciones/services)
#   Medio: Tests integración  (moderados — testean la API completa con BD)
#   Punta: Tests E2E          (pocos, lentos — testean el flujo completo con frontend)
#
# En este bloque nos enfocamos en tests de INTEGRACIÓN: simulamos peticiones HTTP
# reales contra la API con una BD en memoria (SQLite), verificando que todos los
# componentes (routes → schemas → services → models) funcionen coordinados.
#
# ─── ¿Qué es una Fixture? ───
# Una fixture es una función decorada con @pytest.fixture que prepara y devuelve
# los recursos necesarios para un test. Pytest las inyecta automáticamente como
# argumentos de las funciones de test por coincidencia de nombre del parámetro.
#
# ─── Scope de las Fixtures (Ciclo de Vida) ───
# scope="session"  → Se ejecuta UNA vez para toda la suite de tests. Compartida.
# scope="module"   → Se ejecuta una vez por archivo de test.
# scope="function" → Se ejecuta una vez POR CADA función de test (por defecto).
# autouse=True     → Se aplica automáticamente a cada test sin necesidad de inyectarla.


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: tests/conftest.py
# ─────────────────────────────────────────────────────────────────────────────
# conftest.py es un archivo especial que Pytest escanea automáticamente al inicio.
# Las fixtures definidas aquí están disponibles para TODOS los archivos de test
# del mismo directorio y subdirectorios, sin necesidad de importarlas.

import os
import pytest
from app import create_app, db as _db
from app.modulos.usuarios.models import DepartamentoModel


# ─────────────────────────────────────────────────────────────────────────────
# FIXTURE: APLICACIÓN FLASK PARA TESTING
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def app():
    """Crea una instancia de la app con configuración de testing.

    scope='session': la app se crea una sola vez para toda la suite de tests.
    Crear la app es costoso (importar módulos, configurar extensiones), así que
    reutilizamos la misma instancia. La BD se crea aquí y se destruye al final.

    Inyección de configuración:
    Nuestro create_app() (Bloque 9) lee os.getenv("FLASK_CONFIG"). En lugar de
    modificar la firma de la función (lo cual acoplaría el código de producción
    al de testing), manipulamos la variable de entorno ANTES de inicializar.
    """
    # Forzamos DevelopmentConfig para evitar que _require_env() de ProductionConfig
    # (Bloque 3) exija variables de producción que no existen en el entorno de tests.
    os.environ["FLASK_CONFIG"] = "app.core.config.DevelopmentConfig"

    app = create_app()
    app.config["TESTING"] = True
    # TESTING=True modifica el comportamiento de Flask:
    #   - Propaga excepciones al test en lugar de retornar HTTP 500.
    #   - Desactiva el manejo de errores para facilitar la depuración.

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    # BD en memoria: ultra rápida, sin archivos en disco, desaparece al cerrar.
    # Ideal para tests porque cada suite arranca con una BD limpia.

    # db.create_all() es válido SOLO en el contexto de testing con BD en memoria.
    # En producción, las migraciones se manejan estrictamente con Flask-Migrate (Bloque 9).
    with app.app_context():
        _db.create_all()
        yield app
        # yield convierte la fixture en un generador: todo lo anterior a yield es SETUP,
        # todo lo posterior es TEARDOWN. Pytest garantiza que el teardown se ejecuta
        # incluso si los tests fallan con excepciones.
        _db.drop_all()

    # Limpiamos la variable de entorno al finalizar la suite
    os.environ.pop("FLASK_CONFIG", None)


# ─────────────────────────────────────────────────────────────────────────────
# FIXTURE: AISLAMIENTO TRANSACCIONAL POR TEST
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def db_session(app):
    """Orquesta una conexión transaccional externa que envuelve cada test.

    autouse=True: se aplica automáticamente a CADA test sin necesidad de
    declarar 'db_session' como parámetro. Garantiza que todos los tests
    están aislados transaccionalmente sin excepción.

    💡 ¿Por qué no usar simplemente db.session.rollback() al final?
    Nuestros servicios (Bloque 5) ejecutan `with db.session.begin():` internamente,
    que hace COMMIT real. Un rollback() posterior no deshace un commit ya ejecutado.

    💡 ¿Por qué no usar begin_nested() directamente?
    Si la fixture abriera una transacción con begin_nested(), el servicio intentaría
    abrir una transacción principal encima, causando InvalidRequestError.

    Este patrón conecta la sesión de SQLAlchemy a una transacción externa controlada
    por la fixture. Las transacciones internas del servicio operan como SAVEPOINTS
    anidados dentro de esta transacción padre, que se revierte al finalizar el test.

    Resultado: cada test ve datos limpios, como si la BD se recreara cada vez,
    pero sin el coste de recrear tablas (que es lento).
    """
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()

        # Vinculamos la sesión de SQLAlchemy a esta conexión transaccional.
        # Todas las operaciones ORM pasan por esta conexión controlada.
        _db.session.configure(bind=connection)

        yield _db.session

        # TEARDOWN: revertimos TODA la transacción padre.
        # Esto deshace todos los INSERT, UPDATE y DELETE realizados durante el test,
        # incluidos los que pasaron por db.session.begin() (convertidos en SAVEPOINTS).
        transaction.rollback()
        connection.close()
        _db.session.remove()


# ─────────────────────────────────────────────────────────────────────────────
# FIXTURE: DATOS INICIALES (Seed Data)
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture()
def depto_test(db_session):
    """Crea un departamento de prueba dejando que la BD asigne el ID.

    💡 ¿Por qué no forzar id=1?
    En motores como SQL Server, forzar IDs en columnas IDENTITY falla por defecto
    (requiere SET IDENTITY_INSERT ON). Usamos .flush() para que el motor genere
    el ID identity y lo inyectamos dinámicamente en los tests.

    flush() vs commit():
      - flush(): ejecuta el INSERT en la BD (genera el ID) pero NO cierra la
        transacción. Los datos son visibles dentro de la sesión actual.
      - commit(): ejecuta flush() + cierra la transacción. Aquí no lo usamos
        porque la transacción la controla la fixture db_session.
    """
    depto = DepartamentoModel(nombre="Ingeniería")
    db_session.add(depto)
    db_session.flush()  # Persiste y genera depto.id sin hacer commit
    return depto


# ─────────────────────────────────────────────────────────────────────────────
# FIXTURE: CLIENTE HTTP VIRTUAL
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture()
def client(app):
    """Crea el cliente virtual para simular peticiones HTTP sin levantar un servidor.

    app.test_client() retorna un objeto que simula un navegador:
    soporta .get(), .post(), .put(), .delete() con JSON, headers y cookies.
    Las peticiones se procesan internamente por Flask sin socket TCP real.
    """
    return app.test_client()


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: tests/test_usuarios.py
# ─────────────────────────────────────────────────────────────────────────────
# Los tests son funciones que comienzan con 'test_'.
# Las fixtures se inyectan por coincidencia de nombre: el parámetro 'client'
# corresponde a la fixture 'client' definida en conftest.py.
#
# Cada test sigue el patrón AAA (Arrange-Act-Assert):
#   Arrange → Preparar datos de entrada (payload, fixtures)
#   Act     → Ejecutar la acción (petición HTTP)
#   Assert  → Verificar el resultado esperado


# ─────────────────────────────────────────────────────────────────────────────
# TESTS: CREACIÓN DE USUARIOS
# ─────────────────────────────────────────────────────────────────────────────

def test_crear_usuario_exito(client, depto_test):
    """Prueba que un usuario se crea correctamente con datos válidos."""
    # Arrange
    payload = {
        "nombre": "Andrés",
        "email": "andres@correo.com",
        "departamento_id": depto_test.id  # ID dinámico generado por la fixture
    }

    # Act
    response = client.post("/api/v1/usuarios/", json=payload)

    # Assert
    assert response.status_code == 201
    data = response.get_json()
    assert data["nombre"] == "Andrés"
    assert data["email"] == "andres@correo.com"
    assert "id" in data
    # Verifica que el departamento anidado se serializa correctamente
    # (requiere joinedload en services.py, Bloque 5 + schema anidado, Bloque 6)
    assert data["departamento"]["nombre"] == "Ingeniería"


def test_crear_usuario_email_invalido(client, depto_test):
    """Prueba que un email inválido retorna error 422 estructurado por el handler global."""
    # Arrange
    payload = {
        "nombre": "An",               # Demasiado corto (min_length=3 en NombreEmpleado, Bloque 6)
        "email": "esto-no-es-email",   # Formato inválido (EmailStr de Pydantic)
        "departamento_id": depto_test.id
    }

    # Act
    response = client.post("/api/v1/usuarios/", json=payload)

    # Assert — HTTP 422: el handler de PydanticValidationError (Bloque 7) retorna 422
    assert response.status_code == 422
    data = response.get_json()
    assert data["error"] == "ValidacionError"
    assert "detalles" in data


def test_crear_usuario_body_vacio(client):
    """Prueba que un body vacío retorna errores de campos obligatorios faltantes."""
    # Act
    response = client.post("/api/v1/usuarios/", json={})

    # Assert — Los campos nombre, email y departamento_id son obligatorios (Bloque 6)
    assert response.status_code == 422
    data = response.get_json()
    assert data["error"] == "ValidacionError"


# ─────────────────────────────────────────────────────────────────────────────
# TESTS: CONSULTA Y ERRORES
# ─────────────────────────────────────────────────────────────────────────────

def test_obtener_usuario_inexistente(client):
    """Prueba que buscar un ID inexistente retorna 404 con estructura de error."""
    # Act
    response = client.get("/api/v1/usuarios/99999")

    # Assert — RecursoNoEncontradoError del Bloque 7 retorna 404
    assert response.status_code == 404
    data = response.get_json()
    assert data["status"] == "error"


# ─────────────────────────────────────────────────────────────────────────────
# TESTS: CICLO CRUD COMPLETO
# ─────────────────────────────────────────────────────────────────────────────

def test_ciclo_completo_crud(client, depto_test):
    """Prueba el flujo completo en aislamiento transaccional: Crear → Leer → Actualizar → Eliminar.

    Gracias a la fixture db_session (autouse=True), todos los datos creados en este
    test se revierten al finalizar — no afectan a los demás tests.
    """
    # ── 1. Crear (POST) ──
    payload = {"nombre": "María", "email": "maria@correo.com", "departamento_id": depto_test.id}
    create_res = client.post("/api/v1/usuarios/", json=payload)
    assert create_res.status_code == 201
    usuario_id = create_res.get_json()["id"]

    # ── 2. Leer (GET) ──
    get_res = client.get(f"/api/v1/usuarios/{usuario_id}")
    assert get_res.status_code == 200
    assert get_res.get_json()["nombre"] == "María"

    # ── 3. Actualizar (PUT) ──
    update_res = client.put(
        f"/api/v1/usuarios/{usuario_id}",
        json={"nombre": "María Actualizada"}
    )
    assert update_res.status_code == 200
    assert update_res.get_json()["nombre"] == "María Actualizada"

    # ── 4. Eliminar (DELETE) ──
    delete_res = client.delete(f"/api/v1/usuarios/{usuario_id}")
    assert delete_res.status_code == 204

    # ── 5. Verificar que ya no existe ──
    verify_res = client.get(f"/api/v1/usuarios/{usuario_id}")
    assert verify_res.status_code == 404


# ─────────────────────────────────────────────────────────────────────────────
# TESTS COMPLEMENTARIOS: COOKIES Y SESIONES
# ─────────────────────────────────────────────────────────────────────────────

def test_login_y_dashboard_con_sesion(client):
    """Prueba el comportamiento de las sesiones firmadas usando session_transaction().

    session_transaction() permite manipular la cookie de sesión directamente
    desde el test, sin necesidad de pasar por el endpoint /login. Esto aísla
    el test: si /login tiene un bug, este test no se ve afectado.
    """
    # Intentar acceder al dashboard sin sesión activa debe lanzar 401
    res_bloqueado = client.get("/api/v1/usuarios/dashboard")
    assert res_bloqueado.status_code == 401

    # Inyectamos de forma segura datos dentro de la cookie cifrada de la sesión virtual
    with client.session_transaction() as sess:
        sess["usuario_id"] = 42
        sess["rol"] = "Administrador"

    # Verificamos la lectura exitosa del estado simulado
    res_permitido = client.get("/api/v1/usuarios/dashboard")
    assert res_permitido.status_code == 200
    assert "Usuario ID: 42" in res_permitido.get_json()["bienvenido"]


def test_verificar_guardado_de_cookies(client):
    """Prueba que las cookies de respuesta incluyan las directivas de seguridad (HttpOnly)."""
    response = client.get("/api/v1/usuarios/set-cookie")

    # Verificamos que la cookie se estableció con los valores y flags correctos
    assert "preferencia_tema" in response.headers["Set-Cookie"]
    assert "oscuro" in response.headers["Set-Cookie"]
    assert "HttpOnly" in response.headers["Set-Cookie"]


# ─────────────────────────────────────────────────────────────────────────────
# 📘 ¿POR QUÉ NUESTRA APLICACIÓN ES 100% TESTEABLE?
# ─────────────────────────────────────────────────────────────────────────────
# La arquitectura construida a lo largo de este documento es la clave:
#
#   1. Factory Pattern (Bloque 9): al no tener una variable 'app' global, podemos
#      instanciar apps aisladas con configuraciones distintas para cada suite.
#
#   2. Configuración por Entorno (Bloque 3): permite inyectar una BD en memoria
#      (SQLite) sin cambiar una línea del código de producción.
#
#   3. Servicios Delgados (Bloque 5): la lógica de negocio no depende de Flask
#      (ni request ni response). Se puede testear unitariamente sin HTTP.
#
#   4. Aislamiento Transaccional: la fixture db_session con SAVEPOINTS anidados
#      garantiza que los tests no choquen entre sí ni contaminen la BD.

# ─── Ejecutar los Tests ───
# pytest                    → Ejecuta todos los tests del directorio
# pytest tests/             → Ejecuta tests de la carpeta "tests"
# pytest -v                 → Modo verboso (detalle de cada test)
# pytest -k "crear"         → Solo tests que contengan "crear" en el nombre
# pytest --tb=short         → Tracebacks reducidos (errores más compactos)
# pytest -x                 → Se detiene en el primer test que falle


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 12: HASHING Y SEGURIDAD DE CONTRASEÑAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/core/security.py
# ─────────────────────────────────────────────────────────────────────────────
# NUNCA guardes contraseñas en texto plano. Si la base de datos es comprometida,
# los atacantes tendrán acceso a las cuentas de los usuarios en segundos.
#
# 💡 ¿Qué es el Hashing? (Irreversibilidad)
# Un hash es una función matemática de un solo sentido: convierte un texto
# (ej: "MiContraseña123") en una cadena de caracteres de longitud fija
# (ej: "pbkdf2:sha256:600000$salt$abc123..."). El proceso es IRREVERSIBLE:
# no existe operación matemática para recuperar la contraseña original a partir
# del hash. La única forma de "verificar" es hashear el intento del usuario
# y comparar ambos hashes.
#
# 💡 ¿Qué es un Salt? (Protección contra Rainbow Tables)
# Un salt es una cadena aleatoria única que se genera para cada contraseña
# ANTES de hashearla. Dos usuarios con la misma contraseña ("123456")
# producirán hashes DIFERENTES porque cada uno tiene su propio salt.
# Sin salt, un atacante podría usar tablas pre-calculadas (Rainbow Tables)
# para buscar el hash y encontrar la contraseña original en segundos.
# Con salt, las tablas pre-calculadas son inútiles porque cada hash es único.
#
# Werkzeug genera el salt automáticamente — no necesitas gestionarlo manualmente.

from werkzeug.security import generate_password_hash, check_password_hash


# ─────────────────────────────────────────────────────────────────────────────
# FUNCIONES DE HASHING
# ─────────────────────────────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    """Convierte una contraseña en un hash irreversible con salt aleatorio.

    Internamente usa PBKDF2-SHA256 (Password-Based Key Derivation Function 2)
    con 600,000 iteraciones (valor por defecto de Werkzeug 2023+).
    Las iteraciones ralentizan intencionalmente el cómputo para que un ataque
    de fuerza bruta sea computacionalmente inviable (~0.3s por intento vs ~0.000001s
    para un hash simple como MD5).

    El resultado tiene el formato: 'method$salt$hash'
    Ejemplo: 'pbkdf2:sha256:600000$abc123$def456...'
    """
    return generate_password_hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña ingresada coincide con el hash almacenado.

    Internamente extrae el salt del hash almacenado, aplica el mismo algoritmo
    a la contraseña candidata y compara de forma segura contra timing attacks.

    NOTA DE SEGURIDAD — Timing Attacks:
    check_password_hash() usa internamente hmac.compare_digest() para comparar
    los hashes en tiempo constante. Una comparación con '==' revelaría información
    al atacante: si el primer byte no coincide, '==' retorna False inmediatamente
    (más rápido). El atacante podría medir la diferencia de tiempo y deducir
    cuántos bytes del hash son correctos, reduciendo el espacio de búsqueda.
    hmac.compare_digest() siempre tarda lo mismo, independientemente de cuántos
    bytes coincidan.
    """
    return check_password_hash(hashed_password, password)


# ─────────────────────────────────────────────────────────────────────────────
# 📘 INTEGRACIÓN CON EL MODELO ORM (Bloque 4)
# ─────────────────────────────────────────────────────────────────────────────
# En lugar de un campo 'password' en texto plano, el modelo debe almacenar
# 'password_hash'. Los métodos de instancia encapsulan la lógica de seguridad:
#
# class UsuarioModel(db.Model):
#     __tablename__ = "usuarios"
#     ...
#     password_hash: Mapped[str] = mapped_column(String(255))
#     # String(255) porque los hashes PBKDF2 de Werkzeug ocupan ~160 caracteres.
#     # 255 deja margen si se migra a bcrypt o argon2 (hashes más largos).
#
#     def set_password(self, password: str) -> None:
#         """Hashea y almacena la contraseña. NUNCA almacena texto plano."""
#         self.password_hash = hash_password(password)
#
#     def check_password(self, password: str) -> bool:
#         """Compara una contraseña candidata contra el hash almacenado."""
#         return verify_password(password, self.password_hash)

# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: ALGORITMOS DE HASHING (PBKDF2 vs bcrypt vs argon2)
# ─────────────────────────────────────────────────────────────────────────────
# | Algoritmo     | Ventaja                          | Cuándo usarlo               |
# | :---          | :---                             | :---                        |
# | PBKDF2-SHA256 | Incluido en Werkzeug (0 deps)    | Apps Flask estándar         |
# | bcrypt        | Resistente a GPU (memory-hard)   | Producción con alto riesgo  |
# | argon2id      | Ganador de PHC (2015), óptimo    | Máxima seguridad disponible |
#
# PBKDF2 es suficiente para la mayoría de aplicaciones. Para producción con
# requisitos de seguridad elevados (fintech, salud), considerar bcrypt o argon2:
#   pip install bcrypt
#   generate_password_hash(password, method="bcrypt")


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 13: JWT, REFRESH TOKENS Y AUTENTICACIÓN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/auth/routes.py
# ─────────────────────────────────────────────────────────────────────────────
# Las cookies de sesión del Bloque 8 no escalan bien en arquitecturas modernas:
#   - Microservicios: cada servicio necesitaría acceso al almacén de sesiones.
#   - Apps móviles: las cookies nativas son limitadas y frágiles en iOS/Android.
#   - SPAs (React/Vue): las cookies cross-origin requieren configuración compleja.
#
# La solución moderna es JSON Web Tokens (JWT): tokens firmados criptográficamente
# que contienen la identidad del usuario y viajan en el header Authorization.
#
# 💡 Estructura de un JWT (tres partes separadas por puntos):
#   Header.Payload.Signature
#
#   - Header:    {"alg": "HS256", "typ": "JWT"} → Algoritmo de firma usado.
#   - Payload:   {"sub": "1", "rol": "admin", "exp": 1718200000} → Datos del usuario.
#                No guardar datos sensibles aquí: el Payload es Base64, NO cifrado.
#   - Signature: HMAC-SHA256(Header + Payload, SECRET_KEY) → Firma de integridad.
#                El servidor usa SECRET_KEY (Bloque 3) para verificar que el token
#                no fue alterado. Si alguien modifica el Payload, la firma no coincide.
#
# Instalación: pip install Flask-JWT-Extended
#
# 💡 Integración con el Factory Pattern (Bloque 9):
# Flask-JWT-Extended se inicializa en create_app():
#   from flask_jwt_extended import JWTManager
#   jwt = JWTManager()
#   jwt.init_app(app)
#   app.config["JWT_SECRET_KEY"] = app.config["SECRET_KEY"]
#   app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
#   app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from app.core.security import verify_password
from app.errors.exceptions import NoAutenticadoError
# from app.modulos.usuarios.models import UsuarioModel


# ─────────────────────────────────────────────────────────────────────────────
# DEFINICIÓN DEL BLUEPRINT DE AUTENTICACIÓN
# ─────────────────────────────────────────────────────────────────────────────

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


# ─────────────────────────────────────────────────────────────────────────────
# BLOCKLIST — INVALIDACIÓN DE TOKENS
# ─────────────────────────────────────────────────────────────────────────────
# Los JWT son stateless: una vez emitidos, son válidos hasta que expiran.
# Para implementar logout (invalidación anticipada), necesitamos una lista
# negra (blocklist) donde registramos los tokens invalidados.
#
# ⚠️ ADVERTENCIA DE PRODUCCIÓN:
# Esta implementación usa un set() en memoria. Si el servidor se reinicia,
# la blocklist se pierde y los tokens "invalidados" vuelven a ser válidos.
# En producción, usar Redis con TTL (Time To Live) automático:
#   import redis
#   blocklist_store = redis.Redis(host="localhost", port=6379, db=1)
#   blocklist_store.setex(jti, timedelta(minutes=15), "revoked")

BLOCKLIST = set()


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINT: LOGIN — Emisión de Tokens
# ─────────────────────────────────────────────────────────────────────────────

@auth_bp.route("/login", methods=["POST"])
def login():
    """Autentica al usuario y emite un par Access Token + Refresh Token.

    Flujo de autenticación:
      1. El cliente envía email + contraseña en el body JSON.
      2. El servidor busca al usuario en la BD por email.
      3. Verifica la contraseña contra el hash almacenado (Bloque 12).
      4. Si es válido, emite dos tokens:
         - Access Token  (vida corta: ~15 min): se envía en cada petición protegida.
         - Refresh Token (vida larga: ~30 días): solo sirve para obtener nuevos Access Tokens.
      5. El cliente almacena ambos tokens y usa el Access en el header Authorization.

    El par Access/Refresh evita que el usuario tenga que re-ingresar su contraseña
    cada 15 minutos, mientras minimiza el riesgo si el Access Token es robado
    (expira rápidamente).
    """
    datos = request.get_json()
    email = datos.get("email")
    password = datos.get("password")

    # 1. Buscar usuario en la BD (simulado para esta documentación)
    # En producción, descomentar:
    # usuario = db.session.scalars(
    #     select(UsuarioModel).filter_by(email=email)
    # ).first()
    usuario = {"id": 1, "email": "admin@empresa.com", "rol": "admin", "password_hash": "..."}

    # 2. Verificar credenciales
    # if not usuario or not usuario.check_password(password):
    #     raise NoAutenticadoError("Credenciales inválidas.")
    # Usamos NoAutenticadoError (Bloque 7) para que el handler global responda
    # con JSON estructurado consistente, en lugar de jsonify() manual.

    # 3. Crear Tokens
    identity = str(usuario["id"])
    # identity es el identificador único del usuario dentro del JWT.
    # Usamos str() porque JWT serializa a JSON, donde los tipos deben ser homogéneos.

    claims_adicionales = {"rol": usuario["rol"]}
    # additional_claims inyecta datos extra en el Payload del JWT.
    # Estos claims son accesibles con get_jwt() en cualquier endpoint protegido.
    # ⚠️ No guardar datos sensibles: el Payload es Base64 (legible por cualquiera).

    access_token = create_access_token(identity=identity, additional_claims=claims_adicionales)
    refresh_token = create_refresh_token(identity=identity)

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINT: REFRESH — Renovación de Access Token
# ─────────────────────────────────────────────────────────────────────────────

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Emite un nuevo Access Token usando un Refresh Token válido.

    @jwt_required(refresh=True): exige un REFRESH token (no un access token).
    Si el cliente envía un access token aquí, Flask-JWT-Extended lo rechaza
    con un error 422 (tipo de token incorrecto).

    Caso de uso: el frontend detecta que el Access Token expiró (error 401),
    automáticamente envía el Refresh Token a este endpoint, obtiene un nuevo
    Access Token y reintenta la petición original — transparente para el usuario.
    """
    identity = get_jwt_identity()
    # get_jwt_identity() extrae el 'sub' (subject) del JWT decodificado,
    # que corresponde al identity que pasamos en create_access_token().

    # Aquí se podría verificar en la BD si el usuario sigue activo:
    # usuario = db.session.get(UsuarioModel, int(identity))
    # if not usuario or not usuario.activo:
    #     raise NoAutenticadoError("La cuenta ha sido desactivada.")

    nuevo_access_token = create_access_token(identity=identity)
    return jsonify({"access_token": nuevo_access_token}), 200


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINT: LOGOUT — Invalidación de Token
# ─────────────────────────────────────────────────────────────────────────────

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Invalida el Access Token actual añadiéndolo a la Blocklist.

    get_jwt()["jti"] obtiene el JTI (JWT ID): un identificador único UUID
    generado automáticamente por Flask-JWT-Extended para cada token emitido.
    Al añadirlo a la blocklist, el callback @jwt.token_in_blocklist_loader
    lo rechazará en futuras peticiones.
    """
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    return jsonify({"mensaje": "Sesión cerrada exitosamente."}), 200


# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: CONFIGURACIÓN DEL CALLBACK DE BLOCKLIST
# ─────────────────────────────────────────────────────────────────────────────
# Este callback se registra en create_app() (Bloque 9) para que Flask-JWT-Extended
# verifique la blocklist en cada petición protegida:
#
# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload):
#     jti = jwt_payload["jti"]
#     return jti in BLOCKLIST  # True = token revocado → acceso denegado
#
# Con Redis en producción:
#     return blocklist_store.get(jti) is not None

# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: ALMACENAMIENTO SEGURO DE TOKENS EN EL FRONTEND
# ─────────────────────────────────────────────────────────────────────────────
# | Almacenamiento     | Riesgo         | Recomendación                        |
# | :---               | :---           | :---                                 |
# | localStorage       | Vulnerable XSS | ❌ No recomendado para tokens        |
# | sessionStorage     | Vulnerable XSS | ❌ No recomendado para tokens        |
# | Cookie HttpOnly    | Seguro XSS     | ✅ Recomendado (CSRF requiere CORS)  |
# | Memoria (variable) | Seguro XSS     | ✅ Ideal para SPAs (se pierde al cerrar) |
#
# El enfoque más seguro es almacenar el token en una cookie HttpOnly+Secure+SameSite,
# que JavaScript no puede leer (protección XSS). Flask-JWT-Extended soporta esto:
#   app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
#   app.config["JWT_COOKIE_SECURE"] = True    # Solo HTTPS
#   app.config["JWT_COOKIE_SAMESITE"] = "Lax" # Protección CSRF


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 14: ROLES, PERMISOS Y DECORADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/auth/decorators.py
# ─────────────────────────────────────────────────────────────────────────────
# Autenticación = ¿Quién eres? (Login → Bloque 13)
# Autorización  = ¿Qué puedes hacer? (Roles y Permisos → este bloque)
#
# Construiremos un decorador personalizado que protege rutas según el rol
# del usuario almacenado en los claims del JWT.
#
# 💡 ¿Qué es un Decorador? (Contexto Técnico)
# Un decorador es una función que envuelve a otra función para añadir
# comportamiento antes o después de su ejecución, sin modificar su código.
# En este caso, verificamos el rol del usuario ANTES de ejecutar el endpoint.
# Si el rol no es válido, la petición se rechaza sin llegar al controlador.
#
# 💡 ¿Por qué functools.wraps?
# Sin @wraps(fn), la función decorada pierde su nombre (__name__) y docstring
# (__doc__) originales, reemplazados por los del wrapper interno. Esto rompe:
#   - Flask: url_for() usa __name__ para resolver endpoints. Sin @wraps,
#     dos endpoints decorados tendrían el mismo __name__ ("decorator") → conflicto.
#   - Debugging: los tracebacks mostrarían "decorator" en lugar del nombre real.
#   - Documentación automática (Swagger/OpenAPI): perdería los docstrings originales.

from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from app.errors.exceptions import NoAutorizadoError


# ─────────────────────────────────────────────────────────────────────────────
# DECORADOR DE AUTORIZACIÓN POR ROLES
# ─────────────────────────────────────────────────────────────────────────────

def roles_required(*roles_permitidos):
    """Decorador que verifica si el JWT tiene un rol permitido.

    Patrón de tres funciones anidadas (Closure):
      roles_required("admin", "superadmin")  ← Recibe los roles (configuración)
      └── wrapper(fn)                        ← Recibe la función a decorar
          └── decorator(*args, **kwargs)     ← Se ejecuta en cada petición

    Debe usarse DESPUÉS de @app.route (los decoradores se aplican de abajo hacia arriba):
      @app.route("/ruta")          ← Se registra primero (más externo)
      @roles_required("admin")     ← Se ejecuta antes del endpoint (más interno)
      def mi_endpoint(): ...
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # 1. Verificar que haya un JWT válido en la petición
            # verify_jwt_in_request() busca el token en el header Authorization
            # (formato: "Bearer eyJ..."). Si no existe o está expirado, lanza
            # una excepción que Flask-JWT-Extended maneja automáticamente (401).
            verify_jwt_in_request()

            # 2. Extraer los claims (payload) del JWT
            claims = get_jwt()
            rol_usuario = claims.get("rol", "guest")
            # Si el JWT no contiene claim "rol", asumimos "guest" (mínimos privilegios).

            # 3. Validar autorización
            if rol_usuario not in roles_permitidos:
                # Usamos NoAutorizadoError del Bloque 7 para mantener consistencia
                # con el sistema centralizado de errores. El handler global
                # (handle_app_error) responde con JSON estructurado y código 403.
                raise NoAutorizadoError(
                    f"Acceso denegado. Se requiere uno de estos roles: "
                    f"{', '.join(roles_permitidos)}. Rol actual: '{rol_usuario}'."
                )

            return fn(*args, **kwargs)
        return decorator
    return wrapper


# ─────────────────────────────────────────────────────────────────────────────
# 📘 EJEMPLO DE USO EN routes.py (Bloque 8)
# ─────────────────────────────────────────────────────────────────────────────
# Los decoradores se apilan: primero @route registra la URL, luego
# @roles_required verifica permisos antes de ejecutar la función.
#
# @usuarios_bp.route("/<int:usuario_id>", methods=["DELETE"])
# @roles_required("admin", "superadmin")
# def eliminar_usuario(usuario_id: int):
#     """Solo administradores pueden eliminar usuarios."""
#     ...
#
# @usuarios_bp.route("/reportes/financiero")
# @roles_required("admin", "contador")
# def reporte_financiero():
#     """Accesible solo para roles administrativos y contables."""
#     ...
#
# @usuarios_bp.route("/mi-perfil")
# @roles_required("admin", "usuario", "guest")
# def mi_perfil():
#     """Cualquier rol autenticado puede ver su propio perfil."""
#     ...

# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: RBAC vs ABAC (Modelos de Autorización)
# ─────────────────────────────────────────────────────────────────────────────
# RBAC (Role-Based Access Control) — Usado en este bloque:
#   Los permisos se asignan por ROL ("admin puede borrar, usuario puede leer").
#   Simple, escalable y suficiente para la mayoría de aplicaciones CRUD.
#
# ABAC (Attribute-Based Access Control) — Para reglas complejas:
#   Los permisos se evalúan por ATRIBUTOS del contexto ("un usuario puede editar
#   solo sus propios recursos" o "solo si la petición viene de la red interna").
#   Requiere un motor de políticas (ej: Casbin, OPA) y es más costoso de mantener.
#
# Recomendación: empezar con RBAC. Migrar a ABAC solo si las reglas de negocio
# requieren granularidad que los roles no pueden expresar.


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 15: MIDDLEWARE Y HOOKS DEL CICLO DE VIDA ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/middleware.py
# ─────────────────────────────────────────────────────────────────────────────
# Flask permite interceptar el ciclo de vida de una petición HTTP en dos niveles:
#   1. Hooks Nativos de Flask: funciones que se ejecutan antes/después de cada
#      request. Tienen acceso completo al contexto de Flask (request, g, current_app).
#   2. Middleware WSGI: clases que envuelven la app a nivel de protocolo WSGI,
#      ANTES de que Flask procese la petición. No tienen acceso al contexto de Flask.
#
# 💡 Ciclo de Vida Completo de una Petición (con Hooks):
#   Cliente → Servidor WSGI (Gunicorn) → Middleware WSGI → Flask
#     → before_request (Hook) → Route/Controller → after_request (Hook) → Respuesta
#     → teardown_appcontext (Hook — SIEMPRE, incluso si hubo error)
#
# ⚠️ CUÁNDO USAR CADA ENFOQUE:
#   - Hooks Flask: cuando necesitas acceder a request, session, current_app o g.
#     Ejemplos: logging, inyección de usuario en 'g', headers de seguridad.
#   - Middleware WSGI: cuando la operación debe ocurrir ANTES de que Flask exista.
#     Ejemplos: redirección HTTP→HTTPS, filtrado de IPs, compresión gzip.
#
# Integración con el Factory Pattern (Bloque 9):
#   def create_app() -> Flask:
#       app = Flask(__name__)
#       ...
#       registrar_hooks(app)                                    # ← Hooks Flask
#       app.wsgi_app = ForzarHTTPSMiddleware(app.wsgi_app)     # ← Middleware WSGI
#       return app

from flask import request


# ─────────────────────────────────────────────────────────────────────────────
# 1. HOOKS NATIVOS DE FLASK
# ─────────────────────────────────────────────────────────────────────────────

def registrar_hooks(app) -> None:
    """Registra los hooks del ciclo de vida de la petición HTTP.

    Se invoca dentro de create_app() para vincular los hooks a la app específica.
    """

    @app.before_request
    def log_peticion():
        """Se ejecuta ANTES de que la petición llegue al controlador (routes.py).

        Casos de uso reales:
          - Registrar logs de acceso para auditoría.
          - Cargar datos del usuario autenticado en el objeto 'g'.
          - Rate limiting manual (aunque se recomienda Flask-Limiter, Bloque 16).
          - Validar headers obligatorios (ej: API keys, Content-Type).

        Si esta función retorna una respuesta (ej: return jsonify({...}), 403),
        la petición se ABORTA y el controlador NUNCA se ejecuta.
        Si retorna None (implícito), la petición continúa al controlador.
        """
        app.logger.debug("Petición entrante: %s %s", request.method, request.path)
        # El objeto 'g' (flask.g) es un almacén temporal por petición.
        # Útil para compartir datos entre before_request y el controlador:
        #   from flask import g
        #   g.usuario_actual = obtener_usuario_del_token()
        #   # En el controlador: current_user = g.usuario_actual

    @app.after_request
    def inyectar_headers_seguridad(response):
        """Se ejecuta DESPUÉS del controlador, antes de enviar la respuesta al cliente.

        Casos de uso reales:
          - Inyectar headers de seguridad (HSTS, CSP, X-Content-Type-Options).
          - Añadir headers CORS personalizados.
          - Modificar o filtrar el cuerpo de la respuesta.
          - Registrar métricas de tiempo de respuesta.

        IMPORTANTE: DEBE retornar el objeto response. Si no lo retorna,
        Flask lanza un error interno y el cliente recibe un 500.
        """
        # ── Headers de Seguridad Recomendados ──
        response.headers['X-Content-Type-Options'] = 'nosniff'
        # Previene que el navegador "adivine" el Content-Type del archivo.
        # Sin esto, un archivo malicioso subido como .txt podría ser ejecutado como .html.

        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        # HSTS (HTTP Strict Transport Security): indica al navegador que SIEMPRE
        # use HTTPS para este dominio durante los próximos 365 días (31536000 segundos).
        # includeSubDomains extiende la política a todos los subdominios.

        # response.headers['Content-Security-Policy'] = "default-src 'self'"
        # CSP: restringe los orígenes desde los cuales el navegador puede cargar recursos.
        # Descomentar y configurar según los recursos externos que use tu frontend.

        return response

    @app.teardown_appcontext
    def limpieza(exception):
        """Se ejecuta SIEMPRE al final, incluso si hubo un error 500 no capturado.

        Parámetro 'exception': contiene la excepción si hubo un error, None si no.
        Es el lugar seguro para liberar recursos que DEBEN cerrarse sin importar qué:
          - Cerrar conexiones a servicios externos (APIs, caches).
          - Limpiar archivos temporales generados durante la petición.
          - Registrar métricas finales de rendimiento.

        NOTA: la conexión a la BD de SQLAlchemy se cierra automáticamente por
        Flask-SQLAlchemy al final de cada request. No es necesario hacerlo aquí.
        """
        pass


# ─────────────────────────────────────────────────────────────────────────────
# 2. MIDDLEWARE WSGI — INTERCEPTOR DE BAJO NIVEL
# ─────────────────────────────────────────────────────────────────────────────
# Opera a un nivel más bajo que Flask. Intercepta la petición antes de que
# Flask siquiera despierte. Útil para operaciones que no necesitan el contexto
# de Flask (request, session, g no existen aquí).

class ForzarHTTPSMiddleware:
    """Redirige tráfico HTTP a HTTPS a nivel WSGI.

    ¿Por qué no usar before_request?
    Un hook before_request ya está dentro de Flask, lo que significa que la
    petición HTTP insegura ya llegó al framework. Con middleware WSGI,
    la redirección ocurre ANTES de que Flask procese absolutamente nada —
    máxima eficiencia y mínima superficie de ataque.
    """

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app
        # Almacenamos la app WSGI original para delegarle las peticiones HTTPS válidas.

    def __call__(self, environ: dict, start_response):
        """Punto de entrada WSGI. Se ejecuta en cada petición al servidor.

        Parámetros WSGI (estándar PEP 3333):
          environ: diccionario crudo con TODA la información de la petición HTTP.
                   Contiene headers, método, path, query string, etc.
                   No es un objeto Flask — es un dict estándar Python.
          start_response: callback para enviar el status y los headers de respuesta.
        """
        # HTTP_X_FORWARDED_PROTO: header inyectado por proxies reversos (Nginx, ALB, CloudFront).
        # Indica el protocolo ORIGINAL que usó el cliente. Necesario porque la conexión
        # entre el proxy y la app suele ser HTTP interno (el proxy termina el TLS).
        # Sin este header, la app no sabría si el cliente original usó HTTPS o HTTP.
        if environ.get('HTTP_X_FORWARDED_PROTO', 'http') == 'http':
            url = f"https://{environ.get('HTTP_HOST', '')}{environ.get('PATH_INFO', '')}"
            start_response('301 Moved Permanently', [('Location', url)])
            return [b""]
            # Retornamos body vacío (bytes) porque el navegador seguirá
            # automáticamente la redirección 301 a la URL HTTPS.

        # Si es HTTPS, delegamos la petición completa a Flask sin modificarla.
        return self.wsgi_app(environ, start_response)


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 16: RATE LIMITING ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 INTEGRACIÓN EN FACTORY (app/__init__.py)
# ─────────────────────────────────────────────────────────────────────────────
# Rate Limiting es una protección esencial contra abusos en la API:
#   - Fuerza Bruta: un bot intenta miles de combinaciones de contraseña por segundo.
#   - DDoS: un atacante satura el servidor con peticiones masivas.
#   - Scraping: un competidor extrae datos de tu API de forma abusiva.
#
# Sin Rate Limiting, un solo atacante puede tumbar tu BD con 10,000 consultas
# por segundo. Flask-Limiter bloquea las peticiones excesivas a nivel de
# memoria (o Redis) ANTES de que toquen tu código de negocio.
#
# Instalación: pip install Flask-Limiter
#
# 💡 Integración con el Factory Pattern (Bloque 9):
#   def create_app() -> Flask:
#       app = Flask(__name__)
#       ...
#       limiter.init_app(app)  # ← Vincular a la app
#       return app

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL LIMITER
# ─────────────────────────────────────────────────────────────────────────────

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)
# key_func=get_remote_address: identifica al cliente por su dirección IP.
# Cada IP tiene su propio contador independiente de peticiones.
#
# ⚠️ PRECAUCIÓN DETRÁS DE PROXIES:
# Si la app está detrás de un proxy reverso (Nginx, AWS ALB, CloudFlare),
# get_remote_address retorna la IP del PROXY, no la del cliente real.
# Esto haría que TODOS los clientes compartan el mismo límite.
# Solución: usar el header X-Forwarded-For con precaución:
#   key_func=lambda: request.headers.get("X-Forwarded-For", request.remote_addr)
# ⚠️ X-Forwarded-For puede ser falsificado. En producción, configurar
# el proxy para sobrescribir este header de forma confiable.
#
# default_limits: límites que aplican a TODAS las rutas por defecto.
# Se expresan en formato legible: "200 per day", "50 per hour", "5 per minute".
#
# storage_uri="memory://": almacena los contadores en memoria del proceso.
# ⚠️ LIMITACIÓN: si usas múltiples workers de Gunicorn, cada worker tiene
# su propia memoria. Un cliente podría hacer 200 peticiones × 4 workers = 800.
# En producción con múltiples workers, usar Redis:
#   storage_uri="redis://localhost:6379/2"
# Redis comparte el estado entre todos los workers y persiste entre reinicios.


# ─────────────────────────────────────────────────────────────────────────────
# 📘 USO EN CONTROLADORES (routes.py, Bloque 8)
# ─────────────────────────────────────────────────────────────────────────────
# Rutas sensibles deben tener límites más estrictos que los globales:
#
# @usuarios_bp.route("/login", methods=["POST"])
# @limiter.limit("5 per minute")
# def login():
#     """Login con protección anti-fuerza bruta: máximo 5 intentos por minuto."""
#     ...
#
# @usuarios_bp.route("/registro", methods=["POST"])
# @limiter.limit("3 per hour")
# def registro():
#     """Registro con protección anti-spam: máximo 3 cuentas por hora por IP."""
#     ...
#
# @limiter.exempt
# @usuarios_bp.route("/health")
# def health_check():
#     """Los health checks de infraestructura NO deben tener límite."""
#     return {"status": "ok"}

# ─────────────────────────────────────────────────────────────────────────────
# 📘 REFERENCIA: HEADERS DE RATE LIMITING EN LA RESPUESTA
# ─────────────────────────────────────────────────────────────────────────────
# Flask-Limiter inyecta automáticamente headers informativos en cada respuesta:
#
# | Header                  | Descripción                                       |
# | :---                    | :---                                              |
# | X-RateLimit-Limit       | Límite máximo configurado para esta ruta          |
# | X-RateLimit-Remaining   | Peticiones restantes en la ventana actual          |
# | X-RateLimit-Reset       | Timestamp Unix cuando el contador se reinicia      |
# | Retry-After             | Segundos que el cliente debe esperar (solo en 429) |
#
# Cuando se excede el límite, Flask-Limiter retorna automáticamente HTTP 429
# (Too Many Requests) con el header Retry-After indicando cuándo puede reintentar.


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 17: TAREAS EN SEGUNDO PLANO (CELERY) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/tasks.py
# ─────────────────────────────────────────────────────────────────────────────
# ¿El Problema? Como vimos en el Bloque 9, Gunicorn usa un número limitado de
# workers (ej: 4). Cada worker puede procesar UNA petición a la vez.
# Si el endpoint /registro envía un email que tarda 5 segundos, ese worker queda
# bloqueado durante esos 5 segundos sin poder atender otras peticiones.
# Si 4 usuarios se registran simultáneamente, los 4 workers se bloquean
# y tu API entera se CAE temporalmente — 100% de capacidad ocupada.
#
# ¿La Solución? Celery + Redis (Arquitectura de Colas de Mensajes).
# En lugar de ejecutar la tarea lenta dentro del request HTTP:
#   1. La ruta de Flask guarda el usuario en la BD (rápido: ~20ms).
#   2. Flask publica un MENSAJE en Redis: "envía el email al usuario X".
#   3. Flask responde al cliente inmediatamente (total: ~50ms).
#   4. Un WORKER de Celery (proceso independiente, fuera de Flask) lee el
#      mensaje de Redis y envía el email (tarda 5s, pero no bloquea Flask).
#
# Componentes de la Arquitectura:
#   - Broker (Redis):  Cola de mensajes. Recibe y almacena las tareas pendientes.
#   - Worker (Celery): Proceso independiente que consume mensajes del Broker.
#   - Backend (Redis): Almacena los RESULTADOS de las tareas (opcional).
#                      Útil si necesitas consultar el estado de una tarea.
#
# Instalación: pip install celery redis

from celery import Celery


# ─────────────────────────────────────────────────────────────────────────────
# INTEGRACIÓN DE CELERY CON FLASK
# ─────────────────────────────────────────────────────────────────────────────

def celery_init_app(app) -> Celery:
    """Integra Celery con el Application Context de Flask.

    ¿Por qué es necesaria esta integración?
    Los workers de Celery son procesos INDEPENDIENTES de Flask. No tienen
    acceso al contexto de la app (current_app, db, config) por defecto.
    Si una tarea necesita acceder a la base de datos (ej: marcar un email
    como enviado), necesita que el app_context esté activo.

    Esta función crea una subclase de Task que envuelve cada ejecución
    dentro de `with app.app_context():`, haciendo que db, current_app y
    el resto del contexto de Flask estén disponibles automáticamente.

    Integración en create_app() (Bloque 9):
      def create_app() -> Flask:
          app = Flask(__name__)
          ...
          celery_app = celery_init_app(app)
          return app
    """
    celery_app = Celery(
        app.name,
        broker="redis://localhost:6379/0",
        # Broker: Redis en el puerto por defecto. La base de datos /0 se usa
        # para la cola de mensajes. Usar una BD distinta (/1, /2) para no
        # mezclar con otros usos de Redis (sesiones, caché, blocklist JWT).
        backend="redis://localhost:6379/0"
        # Backend: donde Celery almacena los RESULTADOS de las tareas.
        # Si no necesitas consultar resultados, puedes omitir el backend.
    )
    celery_app.conf.update(app.config)
    # Sincroniza la configuración de Flask con Celery. Permite definir
    # configuraciones de Celery en config.py (Bloque 3) usando el prefijo CELERY_*.

    # ── ContextTask: Envolver Tareas en el App Context de Flask ──
    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
            # with app.app_context(): establece el contexto de Flask para que
            # dentro de la tarea se pueda acceder a db, current_app, config, etc.
            # Sin esto, cualquier acceso a la BD lanzaría RuntimeError:
            # "Working outside of application context."

    celery_app.Task = ContextTask
    return celery_app


# ─────────────────────────────────────────────────────────────────────────────
# 📘 DECLARACIÓN DE TAREAS
# ─────────────────────────────────────────────────────────────────────────────
# Las tareas se definen con @shared_task (en lugar de @celery_app.task)
# para desacoplarlas de la instancia concreta de Celery. shared_task permite
# que la tarea se vincule automáticamente a cualquier instancia de Celery
# activa, facilitando el testing y la reutilización entre proyectos.
#
# from celery import shared_task
# import time
#
# @shared_task(
#     bind=True,                       # Pasa 'self' como primer argumento (acceso a metadatos)
#     autoretry_for=(ConnectionError,), # Reintenta automáticamente ante errores de red
#     max_retries=3,                    # Máximo 3 reintentos antes de fallar definitivamente
#     retry_backoff=True                # Espera exponencial entre reintentos (2s, 4s, 8s)
# )
# def enviar_email_bienvenida(self, usuario_id: int) -> str:
#     """Envía un email de bienvenida al usuario recién registrado.
#
#     Esta tarea se ejecuta en un proceso Celery independiente, no en Flask.
#     El parámetro 'self' (gracias a bind=True) permite acceder a metadatos:
#       self.request.id       → ID único de esta ejecución de la tarea
#       self.request.retries  → Número de reintentos realizados hasta ahora
#     """
#     time.sleep(5)  # Simula envío lento de red (SMTP, API externa)
#     return f"Email enviado al usuario {usuario_id}"

# ─────────────────────────────────────────────────────────────────────────────
# 📘 USO EN EL CONTROLADOR (routes.py, Bloque 8)
# ─────────────────────────────────────────────────────────────────────────────
# @usuarios_bp.route("/registro", methods=["POST"])
# def registro():
#     # ... validar y guardar usuario en BD (rápido: ~50ms) ...
#     enviar_email_bienvenida.delay(usuario.id)
#     # .delay() envía la tarea a Redis y retorna INMEDIATAMENTE.
#     # El worker de Celery la ejecutará en segundo plano.
#     # .delay(args) es azúcar sintáctico de .apply_async(args=(args,))
#     return jsonify({"msg": "Registrado. Email en camino."}), 201

# ─────────────────────────────────────────────────────────────────────────────
# 📘 EJECUCIÓN Y MONITOREO
# ─────────────────────────────────────────────────────────────────────────────
# Arrancar el worker de Celery (en una terminal separada):
#   celery -A app.tasks.celery_app worker --loglevel=info
#
# Monitoreo en tiempo real con Flower (dashboard web):
#   pip install flower
#   celery -A app.tasks.celery_app flower --port=5555
#   # Abre http://localhost:5555 para ver tareas activas, completadas y fallidas.


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 18: DOCKER Y CONTENEDORIZACIÓN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: Dockerfile
# ─────────────────────────────────────────────────────────────────────────────
# Un Dockerfile es la receta para crear la "imagen" de tu aplicación.
# Una imagen es un paquete inmutable que contiene tu código, dependencias,
# sistema operativo base y configuración — garantiza que tu app correrá
# exactamente igual en la nube que en tu laptop (reproducibilidad total).
#
# 💡 Flujo de Docker:
#   Dockerfile → (docker build) → Imagen → (docker run) → Contenedor
#   - Imagen:      Plantilla inmutable (como un .iso de un sistema operativo).
#   - Contenedor:  Instancia en ejecución de una imagen (como una VM ligera).
#
# 💡 ¿Por qué python:3.11-slim? (Elección de Imagen Base)
#   - python:3.11       → Imagen completa (~900 MB). Incluye compiladores C y herramientas
#                          de desarrollo. Solo necesaria si compilas extensiones C.
#   - python:3.11-slim  → Imagen reducida (~150 MB). Incluye Python + mínimas dependencias
#                          del SO. Balance ideal entre tamaño y compatibilidad.
#   - python:3.11-alpine → Imagen ultraligera (~50 MB). Usa musl libc en lugar de glibc,
#                          lo que causa incompatibilidades con paquetes como numpy, pandas,
#                          y pyodbc. NO RECOMENDADA para aplicaciones con dependencias nativas.
"""
# Usar imagen base ligera de Python
FROM python:3.11-slim

# Prevenir que Python escriba archivos .pyc y forzar stdout sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
# PYTHONDONTWRITEBYTECODE=1: Python no genera archivos .pyc (bytecode compilado).
# En un contenedor, los .pyc son innecesarios porque la imagen es inmutable —
# el bytecode se recompila igual en cada build. Ahorra espacio en disco.

ENV PYTHONUNBUFFERED=1
# PYTHONUNBUFFERED=1: fuerza a Python a enviar stdout/stderr directamente al
# terminal sin almacenarlos en un buffer intermedio. Sin esto, los logs de la
# app podrían retrasarse o perderse si el contenedor se detiene abruptamente.
# Crítico para que `docker logs` y sistemas de observabilidad reciban logs en tiempo real.

# Directorio de trabajo en el contenedor
WORKDIR /app
# WORKDIR establece el directorio base para todos los comandos siguientes.
# Si /app no existe, Docker lo crea automáticamente.
# Equivalente a `cd /app` pero persistente para todas las capas posteriores.

# Instalar dependencias del sistema operativo requeridas por pyodbc (SQL Server)
RUN apt-get update && apt-get install -y curl apt-transport-https unixodbc-dev \\
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \\
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \\
    && apt-get update \\
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \\
    && rm -rf /var/lib/apt/lists/*
# Se encadena todo en un solo RUN para minimizar las capas de la imagen Docker.
# Cada instrucción RUN crea una capa. Menos capas = imagen más pequeña y rápida.
# rm -rf /var/lib/apt/lists/* limpia la caché de apt para reducir el tamaño final.

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn
# COPY requirements.txt primero (antes del código): Docker cachea cada capa.
# Si el código cambia pero requirements.txt no, Docker reutiliza la capa de
# pip install (que es la más lenta, ~30-60s) y solo recopia el código fuente.
# --no-cache-dir: no almacena la caché de pip (ahorra ~50-100 MB en la imagen).

# Copiar código fuente
COPY . .
# Copia TODO el directorio del proyecto al contenedor.
# ⚠️ Usar un archivo .dockerignore para excluir archivos innecesarios:
#   .git, __pycache__, .env, node_modules, tests/, *.pyc

# Exponer puerto
EXPOSE 8000
# EXPOSE es declarativo: documenta que el contenedor escucha en el puerto 8000.
# NO abre el puerto. Para exponer el puerto al host, usar:
#   docker run -p 8000:8000 mi_imagen

# Comando de arranque (Producción)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "run:app"]
# CMD define el comando por defecto cuando el contenedor se ejecuta.
# Se puede sobrescribir en docker run: docker run mi_imagen flask db upgrade
"""

# ─────────────────────────────────────────────────────────────────────────────
# 📘 MEJORA DE SEGURIDAD: USUARIO NO-ROOT
# ─────────────────────────────────────────────────────────────────────────────
# Por defecto, los procesos dentro de Docker se ejecutan como root.
# Si un atacante explota una vulnerabilidad en la app, obtiene permisos root
# dentro del contenedor (y potencialmente en el host si hay escape de contenedor).
# Crear un usuario sin privilegios mitiga este riesgo:
#
#   RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
#   USER appuser
#   # A partir de aquí, todos los comandos se ejecutan como 'appuser' (sin root)

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: docker-compose.yml
# ─────────────────────────────────────────────────────────────────────────────
# docker-compose orquesta múltiples contenedores como una unidad.
# Con un solo comando (docker compose up), levanta toda la infraestructura:
# API + Redis + Celery Worker.
#
# ⚠️ NOTA SOBRE LA BASE DE DATOS:
# En entornos corporativos profesionales, la base de datos SQL Server NO se incluye
# como un contenedor efímero aquí. Reside en un servidor Windows Server independiente
# (o un servicio cloud manejado como Azure SQL). Nuestra aplicación en Linux (Docker)
# se conecta a ese servidor Windows externo vía red.
"""
version: '3.8'

services:
  # ── 1. Redis (Broker para Celery + Storage para Rate Limiting) ──
  redis:
    image: redis:7-alpine
    # redis:7-alpine: imagen ultra ligera (~30 MB) de Redis 7.
    # Alpine Linux es seguro para Redis porque Redis es C puro (no depende de glibc).
    ports:
      - "6379:6379"
    # Mapea el puerto 6379 del contenedor al puerto 6379 del host.
    # Formato: "puerto_host:puerto_contenedor"

  # ── 2. API Flask (Nuestra Aplicación) ──
  api:
    build: .
    # build: . indica a Docker que construya la imagen usando el Dockerfile
    # del directorio actual (.).
    ports:
      - "8000:8000"
    environment:
      - FLASK_CONFIG=app.core.config.ProductionConfig
      - SECRET_KEY=clave_secreta_en_produccion
      # ⚠️ En producción real, NUNCA hardcodear secretos en docker-compose.
      # Usar Docker secrets o un gestor de secretos externo:
      #   SECRET_KEY_FILE=/run/secrets/flask_secret
      - DB_SERVER=192.168.1.100
      - DB_NAME=mi_basedatos
      # Nos conectamos al servidor SQL Server EXTERNO (fuera de Docker).
    depends_on:
      - redis
    # depends_on: garantiza que Redis se levante ANTES que la API.
    # ⚠️ Solo garantiza el ORDEN de arranque, no que Redis esté LISTO.
    # Para esperar a que Redis esté operativo, usar healthchecks o wait-for-it.

  # ── 3. Celery Worker (Mismo código, otro proceso) ──
  celery_worker:
    build: .
    command: celery -A app.tasks.celery_app worker --loglevel=info
    # command: sobrescribe el CMD del Dockerfile. En lugar de levantar Gunicorn,
    # este contenedor ejecuta un worker de Celery que consume tareas de Redis.
    # Usa la MISMA imagen Docker que la API (build: .) — mismo código,
    # diferente punto de entrada.
    environment:
      - DB_SERVER=192.168.1.100
      - DB_NAME=mi_basedatos
    depends_on:
      - redis
"""

# ─────────────────────────────────────────────────────────────────────────────
# 📘 COMANDOS ESENCIALES DE DOCKER
# ─────────────────────────────────────────────────────────────────────────────
# docker build -t mi_app .                → Construir la imagen desde el Dockerfile
# docker run -p 8000:8000 mi_app          → Ejecutar un contenedor desde la imagen
# docker compose up -d                    → Levantar toda la infraestructura (background)
# docker compose down                     → Detener y eliminar todos los contenedores
# docker compose logs -f api              → Ver logs en tiempo real del servicio 'api'
# docker compose exec api flask db upgrade → Ejecutar migraciones dentro del contenedor
# docker system prune -a                  → Limpiar imágenes y contenedores no utilizados
