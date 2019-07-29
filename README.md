## Como iniciar el Proyecto 

El proyecto esta creado con Django y Nextjs

Como correr el proyecto de Django y el Scraper

Crear el virtuelenv con python 3
     instalar los requerimientos del proyecto 


Creamos las migraciones iniciales 

> ./manage.py makemigrations
> ./manage.py migrate

Creamos un super user para entrar al admin de Django 

> ./manage.py createsuperuser

>> Nota :Para el paso siguiente recuerda ejecutar cada funcion en el archivo de scraper.py

Creamos los partidos para poder relacionar los diputados y hacer la base de donde traer la lista de dipiutados por partido

> ./manage.py runscript scraper.py active create_partido()

Despues ...  Continua la magia de traer los diputados  > version 1
active init_scraper()
> ./manage.py runscript scraper.py 


Entrar a Django Admin

http://localhost:8000/admin



>Como iniciar Nexjs  && es una view basica donde mostramos el listado de los diputados

Solo intalamos los node modules  y listo 

yarn && yarn dev 


Nota: por ahora todo lo puedes correr con sqlite , despues se puede pensar en una db como posgrest para mantener los geopoint