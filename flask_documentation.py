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
    """Excepción base de la aplicación con tipado estricto."""
    status_code: int = 500
    mensaje: str = "Error interno del servidor."

    def __init__(
        self, 
        mensaje: str | None = None, 
        status_code: int | None = None, 
        detalles: list[dict[str, Any]] | dict[str, Any] | None = None
    ):
        super().__init__()
        if mensaje is not None:
            self.mensaje = mensaje
        if status_code is not None:
            self.status_code = status_code
        self.detalles = detalles

class RecursoNoEncontradoError(AppError):
    status_code = 404
    mensaje = "El recurso solicitado no fue encontrado."

class ValidacionError(AppError):
    status_code = 400
    mensaje = "La validación de los datos ha fallado."

class ConflictoError(AppError):
    status_code = 409
    mensaje = "El recurso ya existe o genera un conflicto."


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/errors/handlers.py
# ─────────────────────────────────────────────────────────────────────────────
# Los handlers interceptan las excepciones lanzadas en cualquier parte de la app.
# Incorporamos observabilidad (logging) y soporte nativo para fallas de validación de Pydantic.

from flask import Blueprint, current_app
from pydantic import ValidationError as PydanticValidationError
from app.errors.exceptions import AppError

errors_bp = Blueprint("errors", __name__)

@errors_bp.app_errorhandler(AppError)
def handle_app_error(error: AppError):
    """Captura errores de negocio controlados (herederos de AppError)."""
    response = {
        "status": "error",
        "error": error.__class__.__name__,
        "mensaje": error.mensaje
    }
    if error.detalles is not None:
        response["detalles"] = error.detalles
    return response, error.status_code


@errors_bp.app_errorhandler(PydanticValidationError)
def handle_pydantic_validation_error(error: PydanticValidationError):
    """Soluciona el choque Flask/Pydantic.
    
    Cuando la validación de un Schema de Pydantic falla, se lanza una excepción nativa
    que este handler intercepta globalmente para responder un HTTP 400 estructurado.
    """
    detalles = [
        {
            "campo": ".".join(str(loc) for loc in err["loc"]),
            "mensaje": err["msg"],
            "tipo": err["type"]
        }
        for err in error.errors()
    ]
    return {
        "status": "error",
        "error": "ValidacionError",
        "mensaje": "La validación de los datos de entrada ha fallado.",
        "detalles": detalles
    }, 400


@errors_bp.app_errorhandler(404)
def handle_not_found(error):
    """Intercepta errores 404 nativos de Flask (rutas no existentes)."""
    return {"status": "error", "mensaje": "La ruta solicitada no existe."}, 404


@errors_bp.app_errorhandler(Exception)
def handle_unhandled_exception(error: Exception):
    """Garantiza observabilidad y seguridad para excepciones no controladas (HTTP 500).
    
    Registra el traceback completo en los archivos de logs del sistema para auditoría
    y depuración, previniendo la fuga de detalles internos hacia el cliente.
    """
    current_app.logger.error("Excepción no controlada detectada: %s", error, exc_info=True)
    return {"status": "error", "mensaje": "Ha ocurrido un error interno en el servidor."}, 500


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 8: RUTAS Y CONTROLADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/modulos/usuarios/routes.py
# ─────────────────────────────────────────────────────────────────────────────
# El controlador es la capa que recibe las peticiones HTTP, orquesta la validación
# con schemas, delega la lógica a services, y responde al cliente.
# Usamos Blueprints para modularizar las rutas por dominio de negocio.

from flask import Blueprint, request, make_response, session, abort, redirect, url_for
from pydantic import TypeAdapter
from app.modulos.usuarios import services
from app.modulos.usuarios.schemas import EmpleadoCreateSchema, EmpleadoUpdateSchema, EmpleadoResponseSchema
from app.errors.exceptions import RecursoNoEncontradoError, ValidacionError

# ─── Definición del Blueprint ───
# Un Blueprint agrupa rutas de forma aislada para que cada módulo de negocio
# (ej: usuarios, productos, reportes) tenga su propio Blueprint.

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/api/v1/usuarios")


# ─── GET /api/v1/usuarios/ — Listar todos ───

@usuarios_bp.route("/")
def listar_usuarios():
    empleados = services.obtener_todos()
    # Pydantic v2 introduce TypeAdapter para validar y serializar colecciones completas
    # de forma masiva y altamente optimizada, mapeando todo a una lista de diccionarios.
    resultado = TypeAdapter(list[EmpleadoResponseSchema]).dump_python(empleados)
    return {"usuarios": resultado}


# ─── GET /api/v1/usuarios/<id> — Obtener uno ───

@usuarios_bp.route("/<int:usuario_id>")
def obtener_usuario(usuario_id):
    empleado = services.obtener_empleado(usuario_id)
    if not empleado:
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")
    return EmpleadoResponseSchema.model_validate(empleado).model_dump()


# ─── POST /api/v1/usuarios/ — Crear ───

@usuarios_bp.route("/", methods=["POST"])
def crear_usuario():
    # Instanciamos el esquema directamente desempaquetando el JSON (ya pre-parseado a dict por Flask).
    # Cualquier ValidationError de Pydantic será interceptado por el handler global.
    datos_validados = EmpleadoCreateSchema(**(request.get_json() or {}))
    
    nuevo = services.crear_empleado(**datos_validados.model_dump())
    return EmpleadoResponseSchema.model_validate(nuevo).model_dump(), 201


# ─── PUT /api/v1/usuarios/<id> — Actualizar ───

@usuarios_bp.route("/<int:usuario_id>", methods=["PUT"])
def actualizar_usuario(usuario_id):
    # La validación fluye directo al handler global ante datos inválidos
    datos_validados = EmpleadoUpdateSchema(**(request.get_json() or {}))
    
    # exclude_none=True: solo envía los campos que el cliente realmente proporcionó
    campos_a_actualizar = datos_validados.model_dump(exclude_none=True)
    if not campos_a_actualizar:
        raise ValidacionError("No se proporcionaron campos para actualizar.")

    actualizado = services.actualizar_empleado(usuario_id, campos_a_actualizar)
    if not actualizado:
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")

    return EmpleadoResponseSchema.model_validate(actualizado).model_dump()


# ─── DELETE /api/v1/usuarios/<id> — Eliminar ───

@usuarios_bp.route("/<int:usuario_id>", methods=["DELETE"])
def eliminar_usuario(usuario_id):
    eliminado = services.eliminar_empleado(usuario_id)
    if not eliminado:
        raise RecursoNoEncontradoError(f"Usuario con ID {usuario_id} no existe.")
    return "", 204


# ─── Explicación del flujo CRUD ───
# Observa cómo cada ruta sigue el mismo patrón limpio:
#   1. Extraer datos del request (request.json)
#   2. Validar con Pydantic (Schema(**data))
#   3. Delegar a services (services.crear_empleado(...))
#   4. Serializar respuesta con schema de salida (EmpleadoResponseSchema.model_validate())
#   5. Si algo falla → raise ExcepciónPersonalizada() → el handler responde automáticamente


# ─── EJEMPLOS DIDÁCTICOS DE OTROS CASOS DE USO ───

# ─── El Objeto request — Acceso a Datos de la Petición ───
# Flask provee un proxy seguro 'request' que contiene toda la información
# de la petición HTTP entrante. Estos son los atributos más usados:

@usuarios_bp.route("/ejemplo-request", methods=["GET", "POST"])
def ejemplo_request():
    if request.method == "GET":
        # Query params de la URL (ej: ?limite=10&pagina=2)
        limite = request.args.get("limite", default=20, type=int)
        pagina = request.args.get("pagina", default=1, type=int)
        return {"limite": limite, "pagina": pagina}

    elif request.method == "POST":
        # Payload JSON del body
        datos_json = request.json                        # Equivalente a request.get_json()
        # Formulario HTML (Content-Type: application/x-www-form-urlencoded)
        nombre = request.form.get("nombre")
        # Headers HTTP
        token = request.headers.get("Authorization")
        # IP del cliente
        ip = request.remote_addr

        return {"recibido": True}, 201


# ─── Construir Respuestas HTTP ───
# Flask permite responder con diferentes estructuras:

# 1. Un string simple → asume HTML con código 200
#    return "Hola Mundo"

# 2. Un diccionario directo (Flask 1.1+) → serializa automáticamente a JSON
#    return {"ok": True}, 201

# 3. Una tupla (cuerpo, código, headers)
#    return {"ok": True}, 200, {"X-Custom-Header": "valor"}

# 4. Un objeto Response completo con make_response()

@usuarios_bp.route("/descargar-csv")
def descargar_csv():
    contenido_csv = "id,nombre,email\n1,Andres,andres@correo.com"
    response = make_response(contenido_csv)
    response.headers["Content-Disposition"] = "attachment; filename=usuarios.csv"
    response.headers["Content-Type"] = "text/csv"
    return response


# ─── Ruteo Dinámico con Convertidores de Tipo ───
# Flask permite extraer parámetros tipados de la URL usando convertidores:

@usuarios_bp.route("/productos/<int:producto_id>")
def ver_producto(producto_id):
    # <int:id> valida que producto_id sea de tipo int automáticamente
    return {"producto_id": producto_id}

@usuarios_bp.route("/archivos/<path:ruta_archivo>")
def ver_archivo(ruta_archivo):
    # <path:ruta> acepta texto incluyendo barras '/'
    return {"ruta": ruta_archivo}

@usuarios_bp.route("/token/<uuid:user_token>")
def ver_por_token(user_token):
    # <uuid:token> valida que sea una cadena UUID válida
    return {"token": str(user_token)}

# Convertidores disponibles:
#   <int:id>     → Entero positivo
#   <float:val>  → Número decimal
#   <string:nom> → String sin barras (por defecto)
#   <path:ruta>  → String incluyendo barras
#   <uuid:tok>   → Cadena UUID válida


# ─── url_for y redirect — Generador de URLs ───
# url_for genera URLs dinámicamente usando el nombre del endpoint.
# Esto evita hardcodear rutas (strings fijos) en el código.

@usuarios_bp.route("/perfil")
def perfil():
    return {"pagina": "perfil"}

@usuarios_bp.route("/ir-a-perfil")
def ir_a_perfil():
    return redirect(url_for("usuarios.perfil"))
    # "usuarios" = nombre del Blueprint, "perfil" = nombre de la función


# ─── Cookies — Almacenamiento en el Cliente ───
# Las cookies se almacenan en el navegador del cliente en texto plano.

@usuarios_bp.route("/set-cookie")
def set_cookie():
    response = make_response("Cookie guardada!")
    response.set_cookie(
        "preferencia_tema",
        "oscuro",
        max_age=30 * 24 * 60 * 60,  # 30 días en segundos
        httponly=True                # Protección XSS (JavaScript no puede leerla)
    )
    return response

@usuarios_bp.route("/get-cookie")
def get_cookie():
    tema = request.cookies.get("preferencia_tema", "claro")
    return {"tema": tema}


# ─── Sessions — Sesiones Firmadas Criptográficamente ───
# Flask firma los datos de la sesión usando SECRET_KEY (definida en config.py).
# Los datos se almacenan en una cookie firmada en el cliente.
# El servidor valida su integridad (que no fue alterada).
# ⚠️ NUNCA guardes contraseñas ni tokens sensibles aquí: los datos están
# firmados pero NO encriptados (cualquiera puede leerlos, pero no modificarlos).

@usuarios_bp.route("/login")
def login():
    session["usuario_id"] = 42
    session["rol"] = "Administrador"
    return {"mensaje": "Sesión iniciada."}

@usuarios_bp.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        abort(401)  # Lanza un error 401 No Autorizado
    return {"bienvenido": f"Usuario ID: {session['usuario_id']}"}

@usuarios_bp.route("/logout")
def logout():
    session.clear()  # Limpia todos los datos de la sesión
    return {"mensaje": "Sesión cerrada."}


# =================================================================================================================
#              ▀▄▀▄▀▄⡷⠂ BLOQUE 9: INICIALIZACIÓN CENTRAL — FACTORY PATTERN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/__init__.py
# ─────────────────────────────────────────────────────────────────────────────
# En lugar de crear 'app' como variable global (como en el Hola Mundo del Bloque 1),
# usamos una función fábrica (Factory Pattern). Esto resuelve dos problemas:
#   1. Importaciones circulares: los módulos pueden importar 'db' sin importar 'app'.
#   2. Testing: podemos crear múltiples instancias con configuraciones distintas.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias de extensiones (sin inicializar — patrón de inicialización perezosa)
db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    """Application Factory Pattern optimizado para producción (2026).

    Lee dinámicamente la configuración del entorno del sistema operativo,
    inicializa las extensiones de forma perezosa y registra los componentes.
    """
    app = Flask(__name__)

    # 1. Carga dinámica de configuración (12-Factor App: Principio 3)
    # Por defecto apunta a ProductionConfig para garantizar seguridad ("fail-secure"):
    # si alguien olvida configurar la variable, la app arranca en modo estricto.
    env_config = os.getenv("FLASK_CONFIG", "app.core.config.ProductionConfig")
    app.config.from_object(env_config)

    # 2. Inicializar extensiones de forma segura
    db.init_app(app)
    migrate.init_app(app, db)  # Flask-Migrate gestiona migraciones con Alembic

    # 3. Habilitar CORS (Cross-Origin Resource Sharing)
    # Necesario cuando un frontend (React, Vue, Angular) consume la API desde otro dominio.
    # Sin esto, el navegador bloquea las peticiones por la política de mismo origen.
    from flask_cors import CORS
    CORS(app, resources={r"/api/*": {"origins": os.getenv("ALLOWED_ORIGINS", "*")}})
    # En producción, reemplaza "*" por los dominios permitidos:
    # ALLOWED_ORIGINS=https://miapp.com,https://admin.miapp.com

    # 4. Registro diferido de Blueprints (previene importaciones circulares)
    from app.modulos.usuarios.routes import usuarios_bp
    from app.errors.handlers import errors_bp

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(errors_bp)

    # ❌ SE ELIMINA: with app.app_context(): db.create_all()
    # Las tablas se gestionan profesionalmente con migraciones (Flask-Migrate/Alembic)

    return app

# ─── ¿Qué hace cada línea? ───
# Flask(__name__)                       → Crea la instancia de la app.
# os.getenv("FLASK_CONFIG", ...)        → Lee la clase de configuración de la variable de entorno.
# app.config.from_object(env_config)    → Carga la configuración del Bloque 3 dinámicamente.
# db.init_app(app)                      → Conecta SQLAlchemy a esta app específica.
# migrate.init_app(app, db)             → Conecta Flask-Migrate (Alembic) para migraciones de BD.
# CORS(app, resources={...})            → Habilita peticiones cross-origin para rutas /api/*.
# app.register_blueprint(bp)            → Registra las rutas del Bloque 8.

# ─── ⚠️ ¿Por qué NO usamos db.create_all()? ───
# Usar db.create_all() dentro del Factory es un antipatrón peligroso en producción:
#   1. No gestiona cambios incrementales: si modificas un modelo, create_all() NO altera
#      columnas existentes, solo crea tablas nuevas. Perderás cambios de esquema silenciosamente.
#   2. Condiciones de carrera: en despliegues con múltiples contenedores Docker,
#      cada instancia competiría por crear tablas simultáneamente, causando bloqueos en la BD.
#   3. Sin historial: no hay registro de qué cambios se aplicaron ni capacidad de rollback.
#
# En su lugar, Flask-Migrate (basado en Alembic) gestiona migraciones de forma segura:
#   flask db init              → Inicializa el directorio de migraciones (solo una vez).
#   flask db migrate -m "msg"  → Genera un archivo de migración con los cambios detectados.
#   flask db upgrade           → Aplica las migraciones pendientes a la base de datos.
#   flask db downgrade         → Revierte la última migración (rollback controlado).


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: run.py
# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada de la aplicación. Este archivo va en la raíz del proyecto.
# ⚠️ El servidor Werkzeug (app.run()) NO es apto para producción:
#   - Maneja un solo proceso y un solo hilo por defecto.
#   - No gestiona reinicios automáticos ante fallos.
#   - No optimiza el rendimiento para cargas concurrentes.

import os
from dotenv import load_dotenv
from app import create_app

# Carga las variables de entorno desde un archivo .env local si existe (solo desarrollo)
load_dotenv()

# Instancia global requerida por servidores WSGI como Gunicorn (ej: 'gunicorn run:app')
app = create_app()

if __name__ == "__main__":
    # Extraemos variables con valores de contingencia seguros para desarrollo local
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
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
# 💡 ¿Por qué usamos '--workers 4'? (El problema del GIL)
# Debido al GIL (Global Interpreter Lock) de Python, un proceso solo puede ejecutar un
# hilo de código a la vez. Gunicorn sortea esta limitación levantando 4 procesos
# del sistema operativo totalmente independientes (cada uno con su propio GIL).
# Esto permite que tu servidor procese 4 peticiones en paralelo real.
#
# O con Waitress (compatible con Windows):
#   waitress-serve --port=8000 --call app:create_app


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 10: LOGGING Y OBSERVABILIDAD ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/core/logging_config.py
# ─────────────────────────────────────────────────────────────────────────────
# Sin logs, estás volando a ciegas en producción. Usar print() es un antipatrón
# porque no es thread-safe, carece de niveles de severidad y no rota archivos.
# Aquí configuramos el módulo estándar 'logging' de Python para generar logs
# profesionales, rotativos y formateados.

import os
import logging
from logging.handlers import RotatingFileHandler

def configure_logging(app):
    """Configura el sistema de logging para la aplicación Flask."""
    
    # 1. Definir formato del log
    # El formato JSON estructurado es ideal para herramientas como ELK o Datadog.
    # Aquí usaremos un formato de texto robusto para legibilidad humana.
    log_format = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # 2. Handler para Archivo con Rotación
    # Evita que el archivo log llene el disco. Mantiene 10 archivos de 5MB máx.
    if not os.path.exists('logs'):
        os.mkdir('logs')
        
    file_handler = RotatingFileHandler(
        'logs/app.log', maxBytes=5242880, backupCount=10
    )
    file_handler.setFormatter(log_format)
    
    # 3. Handler para Consola (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    
    # 4. Asignar handlers y niveles
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    
    if app.config.get('DEBUG'):
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)
        
    app.logger.info('Iniciando sistema de logging de la aplicación.')

# 💡 ¿Cómo usarlo en tus servicios o rutas?
# from flask import current_app
# current_app.logger.info("Usuario creado: %s", email)
# current_app.logger.error("Error conectando a DB: %s", str(e))


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 11: TESTING PROFESIONAL CON PYTEST ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# Probar aplicaciones Flask garantiza la estabilidad del código ante futuros cambios.
# Pytest es el estándar de testing en Python gracias a su sintaxis simple basada en fixtures.

# ─── ¿Qué es una Fixture? ───
# Una fixture es una función que prepara y devuelve los recursos necesarios para un test.
# Pytest las inyecta automáticamente como argumentos de las funciones de test
# por coincidencia de nombre del parámetro.

# ─── Scope de las Fixtures ───
# scope="session"  → Se ejecuta UNA vez para toda la suite de tests.
# scope="function" → Se ejecuta una vez POR CADA función de test (por defecto).
# scope="module"   → Se ejecuta una vez por archivo de test.
# autouse=True     → Se aplica automáticamente a cada test sin necesidad de inyectarla.


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: tests/conftest.py
# ─────────────────────────────────────────────────────────────────────────────
# conftest.py es un archivo especial que Pytest escanea automáticamente.
# Las fixtures definidas aquí están disponibles para TODOS los archivos de test.

import os
import pytest
from app import create_app, db as _db
from app.modulos.usuarios.models import DepartamentoModel


# ─── Fixture: Aplicación Flask para Testing ───

@pytest.fixture(scope="session")
def app():
    """Crea la app inyectando la configuración de test mediante variable de entorno.

    Nuestro create_app() lee os.getenv("FLASK_CONFIG"). En lugar de pasarle
    un string como parámetro (lo cual rompe la firma de la función), manipulamos
    la variable de entorno ANTES de inicializar la aplicación.
    """
    os.environ["FLASK_CONFIG"] = "app.core.config.DevelopmentConfig"

    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    # db.create_all() es válido SOLO en el contexto de testing con BD en memoria.
    # En producción, las migraciones se manejan de forma estricta con Flask-Migrate.
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

    # Limpiamos la variable de entorno al finalizar la suite
    os.environ.pop("FLASK_CONFIG", None)


# ─── Fixture: Aislamiento Transaccional por Test ───

@pytest.fixture(autouse=True)
def db_session(app):
    """Orquesta una conexión transaccional externa que envuelve cada test.

    💡 ¿Por qué no usar begin_nested() directamente?
    Nuestros servicios ejecutan `with db.session.begin():` internamente.
    Si la fixture abriera una transacción con begin_nested(), el servicio intentaría
    abrir una transacción principal encima, causando un error de estado inválido.

    Este patrón conecta la sesión de SQLAlchemy a una transacción externa controlada
    por la fixture. Las transacciones internas del servicio operan como SAVEPOINTS
    anidados dentro de esta transacción padre, que se revierte al finalizar el test.
    """
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()

        # Vinculamos la sesión de SQLAlchemy a esta conexión transaccional
        _db.session.configure(bind=connection)

        yield _db.session

        # Revertimos TODA la transacción padre (incluidos los SAVEPOINTS internos)
        transaction.rollback()
        connection.close()
        _db.session.remove()


# ─── Fixture: Datos Iniciales (Seed Data) ───

@pytest.fixture()
def depto_test(db_session):
    """Crea los datos mínimos necesarios dejando que la BD asigne la Identidad.

    💡 ¿Por qué no forzar id=1?
    En motores como SQL Server forzar IDs en columnas autoincrementales falla por defecto.
    Usamos .flush() para que SQLite genere el ID identity y lo inyectamos dinámicamente.
    """
    depto = DepartamentoModel(nombre="Ingeniería")
    db_session.add(depto)
    db_session.flush()  # Persiste en la transacción actual y genera el depto.id sin hacer commit
    return depto


# ─── Fixture: Cliente HTTP Virtual ───

@pytest.fixture()
def client(app):
    """Crea el cliente virtual para simular peticiones HTTP sin levantar un servidor."""
    return app.test_client()


# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: tests/test_usuarios.py
# ─────────────────────────────────────────────────────────────────────────────
# Los tests son funciones que comienzan con 'test_'.
# Las fixtures se inyectan por coincidencia de nombre (ej: el parámetro 'client'
# corresponde a la fixture 'client' definida en conftest.py).

def test_crear_usuario_exito(client, depto_test):
    """Prueba que un usuario se crea correctamente con datos válidos."""
    payload = {
        "nombre": "Andrés",
        "email": "andres@correo.com",
        "departamento_id": depto_test.id  # Utiliza el ID dinámico generado por la semilla
    }
    response = client.post("/api/v1/usuarios/", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["nombre"] == "Andrés"
    assert data["email"] == "andres@correo.com"
    assert "id" in data
    # Verifica que el departamento anidado se serializa correctamente (joinedload + Pydantic)
    assert data["departamento"]["nombre"] == "Ingeniería"


def test_crear_usuario_email_invalido(client, depto_test):
    """Prueba que un email inválido retorna error 400 estructurado por el handler global."""
    payload = {
        "nombre": "An",
        "email": "esto-no-es-email",
        "departamento_id": depto_test.id
    }
    response = client.post("/api/v1/usuarios/", json=payload)

    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "ValidacionError"
    assert "detalles" in data


def test_crear_usuario_body_vacio(client):
    """Prueba que un body vacío retorna errores de campos obligatorios faltantes."""
    response = client.post("/api/v1/usuarios/", json={})

    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "ValidacionError"


def test_obtener_usuario_inexistente(client):
    """Prueba que buscar un ID que no existe retorna 404 con estructura de error."""
    response = client.get("/api/v1/usuarios/99999")

    assert response.status_code == 404
    data = response.get_json()
    assert data["status"] == "error"


def test_ciclo_completo_crud(client, depto_test):
    """Prueba el flujo completo en aislamiento transaccional: Crear → Leer → Actualizar → Eliminar."""
    # 1. Crear
    payload = {"nombre": "María", "email": "maria@correo.com", "departamento_id": depto_test.id}
    create_res = client.post("/api/v1/usuarios/", json=payload)
    assert create_res.status_code == 201
    usuario_id = create_res.get_json()["id"]

    # 2. Leer
    get_res = client.get(f"/api/v1/usuarios/{usuario_id}")
    assert get_res.status_code == 200
    assert get_res.get_json()["nombre"] == "María"

    # 3. Actualizar
    update_res = client.put(
        f"/api/v1/usuarios/{usuario_id}",
        json={"nombre": "María Actualizada"}
    )
    assert update_res.status_code == 200
    assert update_res.get_json()["nombre"] == "María Actualizada"

    # 4. Eliminar
    delete_res = client.delete(f"/api/v1/usuarios/{usuario_id}")
    assert delete_res.status_code == 204

    # 5. Verificar que ya no existe
    verify_res = client.get(f"/api/v1/usuarios/{usuario_id}")
    assert verify_res.status_code == 404


# ─── Tests Complementarios Didácticos (Cookies & Sessions) ───

def test_login_y_dashboard_con_sesion(client):
    """Prueba el comportamiento de las sesiones firmadas usando session_transaction()."""
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
    
    assert "preferencia_tema" in response.headers["Set-Cookie"]
    assert "oscuro" in response.headers["Set-Cookie"]
    assert "HttpOnly" in response.headers["Set-Cookie"]


# ─── 🏆 ¿Por qué nuestra aplicación es 100% Testeable? ───
# La arquitectura que hemos construido en este documento es la clave para un testing robusto:
# 1. Factory Pattern (Bloque 9): Al no tener una variable 'app' global, podemos instanciar apps aisladas.
# 2. Configuración por Entorno (Bloque 3): Permite inyectar una BD en memoria sin cambiar código.
# 3. Servicios Delgados (Bloque 5): La lógica de negocio no depende de Flask (ni request ni response).
# 4. Aislamiento Transaccional: Usar db_session con SAVEPOINTS anidados garantiza que los tests no choquen.

# ─── Ejecutar los Tests ───
# En la terminal, ejecuta pytest para correr las pruebas:
#
# pytest                    → Ejecuta todos los tests en el directorio
# pytest tests/             → Ejecuta tests de la carpeta "tests"
# pytest -v                 → Modo verboso (detalle de cada test)
# pytest -k "crear"         → Solo tests que contengan "crear" en el nombre
# pytest --tb=short         → Tracebacks reducidos (errores más cortos)


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 12: HASHING Y SEGURIDAD DE CONTRASEÑAS ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/core/security.py
# ─────────────────────────────────────────────────────────────────────────────
# NUNCA guardes contraseñas en texto plano. Si la base de datos es comprometida,
# los atacantes tendrán acceso a las cuentas de los usuarios.
# Flask provee werkzeug.security para manejar esto fácilmente, aunque en
# producción estricta se prefiere 'bcrypt' o 'argon2'.

from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """
    Convierte una contraseña en un hash irreversible usando pbkdf2:sha256.
    Incluye un 'salt' aleatorio automático para prevenir ataques de Rainbow Tables.
    """
    return generate_password_hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña ingresada coincide con el hash almacenado."""
    return check_password_hash(hashed_password, password)

# 💡 Actualización del Modelo de Usuario (Bloque 4):
# En lugar de tener un campo `password`, el modelo debe tener `password_hash`.
# 
# class UsuarioModel(db.Model):
#     ...
#     password_hash = db.Column(db.String(255), nullable=False)
#
#     def set_password(self, password):
#         self.password_hash = hash_password(password)
#
#     def check_password(self, password):
#         return verify_password(password, self.password_hash)


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 13: JWT, REFRESH TOKENS Y AUTENTICACIÓN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/auth/routes.py
# ─────────────────────────────────────────────────────────────────────────────
# Las cookies de sesión no escalan bien en arquitecturas de microservicios o apps móviles.
# La solución moderna es usar JSON Web Tokens (JWT).
# Un JWT es un token criptográficamente firmado que contiene la identidad del usuario.
# 
# Instalación: pip install Flask-JWT-Extended

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from app.core.security import verify_password
# from app.modulos.usuarios.models import UsuarioModel

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

# Lista negra en memoria (En producción: usar Redis)
BLOCKLIST = set()

@auth_bp.route("/login", methods=["POST"])
def login():
    """Autentica al usuario y emite Access y Refresh tokens."""
    datos = request.get_json()
    email = datos.get("email")
    password = datos.get("password")

    # 1. Buscar usuario (simulado)
    # usuario = UsuarioModel.query.filter_by(email=email).first()
    usuario = {"id": 1, "email": "admin@empresa.com", "rol": "admin", "password_hash": "..."}

    # 2. Verificar contraseña
    # if not usuario or not usuario.check_password(password):
    #     return jsonify({"error": "Credenciales inválidas"}), 401
    
    # 3. Crear Tokens
    # Access Token: Vida corta (ej: 15 minutos). Se envía en cada petición.
    # Refresh Token: Vida larga (ej: 30 días). Solo sirve para pedir nuevos Access Tokens.
    identity = str(usuario["id"])
    claims_adicionales = {"rol": usuario["rol"]} # Datos extra en el payload del JWT
    
    access_token = create_access_token(identity=identity, additional_claims=claims_adicionales)
    refresh_token = create_refresh_token(identity=identity)

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True) # Exige un REFRESH token válido, no un access token
def refresh():
    """Emite un nuevo Access Token usando un Refresh Token válido."""
    identity = get_jwt_identity()
    # Aquí se podría verificar en BD si el usuario sigue activo
    nuevo_access_token = create_access_token(identity=identity)
    return jsonify({"access_token": nuevo_access_token}), 200

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Invalida el token actual añadiéndolo a la Blocklist."""
    jti = get_jwt()["jti"] # Identificador único del JWT
    BLOCKLIST.add(jti)
    return jsonify({"mensaje": "Sesión cerrada exitosamente"}), 200


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 14: ROLES, PERMISOS Y DECORADORES ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/auth/decorators.py
# ─────────────────────────────────────────────────────────────────────────────
# Autenticación = ¿Quién eres? (Login)
# Autorización = ¿Qué puedes hacer? (Roles y Permisos)
#
# Construiremos un decorador personalizado para proteger rutas según el rol.

from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def roles_required(*roles_permitidos):
    """
    Decorador que verifica si el JWT tiene un rol permitido.
    Debe usarse DESPUÉS de @app.route.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # 1. Verificar que haya un JWT válido en la petición
            verify_jwt_in_request()
            
            # 2. Extraer los claims (payload) del JWT
            claims = get_jwt()
            rol_usuario = claims.get("rol", "guest")
            
            # 3. Validar autorización
            if rol_usuario not in roles_permitidos:
                return jsonify({
                    "error": "Acceso denegado", 
                    "detalle": f"Requiere uno de estos roles: {roles_permitidos}"
                }), 403
                
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# 💡 Ejemplo de Uso en routes.py:
#
# @app.route("/api/v1/usuarios/<id>", methods=["DELETE"])
# @roles_required("admin", "superadmin")
# def eliminar_usuario(id):
#     ...


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 15: MIDDLEWARE Y HOOKS DEL CICLO DE VIDA ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/middleware.py
# ─────────────────────────────────────────────────────────────────────────────
# Flask permite interceptar el ciclo de vida de una petición HTTP.
# Existen dos enfoques: Hooks (dentro de Flask) y Middleware WSGI (fuera de Flask).

# 1. Hooks Nativos de Flask
# Tienen acceso completo al contexto (request, g, current_app).
def registrar_hooks(app):
    
    @app.before_request
    def log_peticion():
        """Se ejecuta ANTES de que la petición llegue al controlador (routes.py)."""
        # Útil para: Rate limiting manual, cargar usuario en 'g', validar cabeceras.
        app.logger.debug("Nueva petición a: %s", request.path)
        
    @app.after_request
    def inyectar_headers_seguridad(response):
        """Se ejecuta DESPUÉS del controlador, antes de enviar la respuesta al cliente."""
        # Útil para: Añadir CORS, CSP, HSTS, o modificar el payload de salida.
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
        
    @app.teardown_appcontext
    def limpieza(exception):
        """Se ejecuta SIEMPRE al final, incluso si hubo un error 500 no capturado."""
        # Útil para: Cerrar conexiones a base de datos o limpiar recursos temporales.
        pass

# 2. Middleware WSGI
# Opera a un nivel más bajo. Intercepta la petición antes de que Flask siquiera despierte.
class ForzarHTTPSMiddleware:
    """Redirige tráfico HTTP a HTTPS."""
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # environ es un diccionario crudo del servidor web (Gunicorn)
        if environ.get('HTTP_X_FORWARDED_PROTO', 'http') == 'http':
            # Si es HTTP, respondemos con una redirección 301 a nivel WSGI
            url = f"https://{environ.get('HTTP_HOST', '')}{environ.get('PATH_INFO', '')}"
            start_response('301 Moved Permanently', [('Location', url)])
            return [b""]
            
        # Si es HTTPS, pasamos la petición a Flask
        return self.wsgi_app(environ, start_response)

# 💡 Integración en __init__.py:
# app.wsgi_app = ForzarHTTPSMiddleware(app.wsgi_app)


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 16: RATE LIMITING ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 INTEGRACIÓN EN FACTORY (app/__init__.py)
# ─────────────────────────────────────────────────────────────────────────────
# Protección contra ataques de Fuerza Bruta y DDoS.
# Si un bot intenta hacer 10,000 logins por segundo, tumbará la BD.
# Flask-Limiter bloquea peticiones a nivel de memoria (o Redis) antes de que
# toquen tu código de negocio.
#
# Instalación: pip install Flask-Limiter

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Inicializamos el limiter usando la IP del cliente como identificador
# En producción se recomienda usar Redis: storage_uri="redis://localhost:6379"
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"], # Límites globales
    storage_uri="memory://" 
)

# 💡 Uso en controladores (routes.py):
#
# @app.route("/login")
# @limiter.limit("5 per minute")  # Límite estricto para rutas sensibles
# def login():
#     ...


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 17: TAREAS EN SEGUNDO PLANO (CELERY) ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: app/tasks.py
# ─────────────────────────────────────────────────────────────────────────────
# ¿El Problema? Como vimos en el Bloque 9, Gunicorn usa un número limitado de workers (ej: 4).
# Si `/registro` envía un email que tarda 5 segundos, ese worker queda bloqueado.
# Si 4 usuarios se registran, los 4 workers se bloquean y tu API entera se CAE temporalmente.
#
# ¿La Solución? Celery + Redis.
# La ruta de Flask solo guarda el usuario en la BD, lanza un mensaje a Redis ("envía el email")
# y responde en 20ms. Un worker de Celery (proceso independiente) lee Redis y envía el email.
#
# Instalación: pip install celery redis

from celery import Celery

def celery_init_app(app):
    """Integra Celery con el Application Context de Flask."""
    # Configuramos Celery usando Redis como Broker (mensajería) y Backend (resultados)
    celery_app = Celery(
        app.name,
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0"
    )
    celery_app.conf.update(app.config)
    
    # Envolvemos las tareas para que se ejecuten dentro del contexto de Flask
    # (necesario si la tarea necesita acceder a la base de datos de Flask)
    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app

# 💡 Declaración de una Tarea (tasks.py):
#
# from celery import shared_task
# import time
#
# @shared_task
# def enviar_email_bienvenida(usuario_id: int):
#     time.sleep(5) # Simula envío lento de red
#     return f"Email enviado al usuario {usuario_id}"

# 💡 Uso en el controlador (routes.py):
#
# @app.route("/registro", methods=["POST"])
# def registro():
#     # ... guardar usuario en BD ...
#     enviar_email_bienvenida.delay(usuario.id) # .delay() no bloquea!
#     return jsonify({"msg": "Registrado. Email en camino."}), 201


# =================================================================================================================
#         ▀▄▀▄▀▄⡷⠂ BLOQUE 18: DOCKER Y CONTENEDORIZACIÓN ⠐⢾▀▄▀▄▀▄
# =================================================================================================================

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: Dockerfile
# ─────────────────────────────────────────────────────────────────────────────
# Un Dockerfile es la receta para crear la "imagen" de tu aplicación.
# Garantiza que tu app correrá exactamente igual en la nube que en tu laptop.
"""
# Usar imagen base ligera de Python
FROM python:3.11-slim

# Prevenir que Python escriba archivos .pyc y forzar stdout sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema operativo requeridas por pyodbc (SQL Server)
RUN apt-get update && apt-get install -y curl apt-transport-https unixodbc-dev \\
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \\
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \\
    && apt-get update \\
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \\
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copiar código fuente
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de arranque (Producción)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "run:app"]
"""

# ─────────────────────────────────────────────────────────────────────────────
# 📄 ARCHIVO: docker-compose.yml
# ─────────────────────────────────────────────────────────────────────────────
# Orquesta la infraestructura de la APLICACIÓN (API + Redis + Celery).
# ⚠️ NOTA SOBRE LA BASE DE DATOS: 
# En entornos corporativos profesionales, la base de datos SQL Server NO se incluye
# como un contenedor efímero aquí. Reside en un servidor Windows Server independiente
# (o un servicio cloud manejado como Azure SQL). Nuestra aplicación en Linux (Docker)
# se conectará a ese servidor Windows externo.
"""
version: '3.8'

services:
  # 1. Redis (Para Celery y Rate Limiting)
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  # 2. Nuestra API Flask
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FLASK_CONFIG=app.core.config.ProductionConfig
      - SECRET_KEY=clave_secreta_en_produccion
      # 💡 Nos conectamos al servidor SQL Server externo (ej: IP 192.168.1.100)
      - SQLALCHEMY_DATABASE_URI=mssql+pyodbc://sa:SuperSecretPass!123@192.168.1.100:1433/mi_basedatos?driver=ODBC+Driver+17+for+SQL+Server
    depends_on:
      - redis

  # 3. Celery Worker (El mismo código de la API, pero ejecuta otro proceso)
  celery_worker:
    build: .
    command: celery -A app.tasks.celery_app worker --loglevel=info
    environment:
      - SQLALCHEMY_DATABASE_URI=mssql+pyodbc://sa:SuperSecretPass!123@192.168.1.100:1433/mi_basedatos?driver=ODBC+Driver+17+for+SQL+Server
    depends_on:
      - redis
"""