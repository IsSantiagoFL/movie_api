from fastapi import FastAPI

app = FastAPI() # Creando una instancia de FastAPI, se esta creando una aplicación de nombre "app"

# Modificando información de la documentación
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"


@app.get('/')
def message():
    return "Hello World!"