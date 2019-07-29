## Como iniciar el Proyecto 

El proyecto esta creado con Django Rest y Nextjs

Para poder correr el proyecto de Django

Crear el virtuelenv con python 3

instalar los requerimientos del proyecto 

>> pip install -r requirements.txt

Creamos las migraciones iniciales  de Django

> ./manage.py makemigrations
> ./manage.py migrate

Creamos un super user para entrar al admin de Django 

> ./manage.py createsuperuser

>> Nota :Para el paso siguiente recuerda ejecutara mano cada funcion en el archivo de scraper.py despues esto tiene que cambiar a algo mas dinamico 

Creamos los partidos para poder relacionar los diputados y hacer la base de donde traer la lista de dipiutados por partido
activa el metodo  create_partido()

> ./manage.py runscript scraper.py 

Despues ...  

Continua la magia de traer los diputados  > version 1 (Scrapear diputados) 
activa el metodo  init_scraper()

> ./manage.py runscript scraper.py 



>Como iniciar Nexjs  

Es una web basica donde mostramos el listado de los diputados

Solo intalamos los node_modules

yarn && yarn dev 


Nota: por ahora todo lo puedes correr con sqlite , despues se puede pensar en una db como postgres para mantener los geopoint


Entrar a Django Admin

http://localhost:8000/admin