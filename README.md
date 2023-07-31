# API for movies with FastAPI Python.

Para ejecutar la aplicacion se deberan seguir los siguientes pasos:

```bash
git clone
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
Esto creara un entorno virtual donde se instalaran todos lo requerimentos para que funcione la aplicacion correctamente, seguido de esto, para ejecutar la aplicacion localmente:

```bash
uvicorn main:app --reload
```

con lo cual debera recibir un mensaje como el siguiente:
```bash
INFO:     Will watch for changes in these directories: ['/home/santiago/Documentos/Python_projects/movie_api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [26803] using StatReload
INFO:     Started server process [26805]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:34318 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:34318 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:34322 - "GET / HTTP/1.1" 200 OK
```
En el cual usted debera abrir en su navegador la siguiente dirección

http://127.0.0.1:8000

Con estos pasos podra visualizar la aplicación.

## Visualizar la documentación de la API.

Para visualizar la información que nos ofrece la documentación de la API, agregar ```/docs``` al final de la URL, de la siguiente forma:

http://127.0.0.1:8000/docs

