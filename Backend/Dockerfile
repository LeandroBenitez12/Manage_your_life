# Manera sencilla
# Usa la imagen oficial de Django con el mecanismo de construcción onbuild
# FROM django:onbuild

# Expone el puerto 8000 en el contenedor
# EXPOSE 8000 

FROM python:3.12.2

# carpeta donde 
WORKDIR /app_django

COPY . /app_django/

RUN pip install -r requirements.txt 
# comando que instalara todas las dependencias que hay en el proyecto 

# Expone el puerto 8000 en el contenedor
EXPOSE 8000 

# CUANDO EL CONTENEDOR ARRANQUE ES EL COMANDO QUE SE EJECUTARA
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
# PARA NO TENER PROBLEMAS DE COMUNICACION SE AGREGA 0.0.0.0:8000 

# CON ESTO YA PODEMOS CREAR IMAGEN

