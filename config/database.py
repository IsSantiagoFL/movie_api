# En este archivo se harán las condifuraciones de la base de datos.

import os # Para leer el directorio actual.
from sqlalchemy import create_engine # Para crear el motor de la base de datos
from sqlalchemy.orm.session import sessionmaker # Para crear la sesion para conectarse a la base de datos.
from sqlalchemy.ext.declarative import declarative_base # Para manipular todas las tablas de la base de datos.

# Creacion de la variable que contiene a la base de datos
sqlite_file_name = "database.sqlite"

# Se indica que lea el directorio actual de este archivo "database.py"
base_dir = os.path.dirname(os.path.realpath(__file__))

# Crear la URL de la base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Crear el motor de la base de datos
engine = create_engine(database_url, echo=True)

# Crear una sesión para conectarme ala bse de datos.
Session = sessionmaker(bind = engine)

# Crear una instancia que servira para el manejo de tablas de la base de datos.
Base = declarative_base()