# Proyecto-Final-Python-Joner-Claudio.
Este proyecto es desarrollado en Python utilizando el framework Django. 
El proyecto trata de una app web sobre una Veterinaria, la cual renderiza la informacion que esta almacenadas en la base de datos y la muesta en las diferentes vistas dependiendo cual sea la solicitud.
Debajo se encuentra el link para ver la app en funcionamiento 

# Video Demostración.
https://youtu.be/-H87qxX9Zgs

_______________________________________________________________________________________________________________________________________________________________________
# DOCUMENTACIÓN.
Para poder encontrar los archivos que nombrare a posterior ingresar  en la carpeta AppCoder.
Los archivos son: models.py, forms.py, urls.py, views.py,la carpeta de templates, entre otros.

_______________________________________________________________________________________________________________________________________________________________________
# Models.py:
En este archivo podemos encontrar los modelos de datos usados por el backend.

Descripcion: modelo Animal. 
Campos: -nombreAnimal(Char, nombre de la mascota) -edad(Integer,edad de la mascota) -tipo(Char,ej:perro,gato,iguana,etc) -motivo(Char,ej:peluqueria,vacunas,etc) -fecha(Date,es la fecha de ingreso a la veterinaria) -costo(Integer, el precio de lo que lo se le haya echo al animal)

Descripcion: modelo Persona. 
Campos: -nombre(Char, nombre del dueño de la mascota) -apellido= (Char, apellido del dueño de la mascota) -telefono= (Integer, numero del dueño de la mascota)

Descripcion: modelo Veterinario. 
Campos: -veterinario(Char, nombre del veterinario) -apellidoVet= (Char, apellido del veterinario) -matricula= (Integer, numero de matricula del veterinario)
_______________________________________________________________________________________________________________________________________________________________________
# Forms.py:
En este archivo podemos encontrar los formularios usados para cargar los datos que quedan guardados en nuestra base de datos.
Son 5 los formularios, uno por cada modelo , otro para poder registrar los usuarios nuevos y el último que sirve para edirtar el perfil de un usuario.
_______________________________________________________________________________________________________________________________________________________________________
# Urls.py:
Contiene cada una de las rutas de las vistas de la app. 
_______________________________________________________________________________________________________________________________________________________________________
# Views.py:
Aparecen todas las vistas que se utilizan en la app.
Asociado a lo anterior por cada modelo se aplica el concepto de CRUD(Create, Read, Update, Delete); una vista de logueo, registro y edicion de perfil del usuario. Además tenemos la vista para buscar una mascota por su nombre.
Ejemplo de vistas (CRUD) para el Modelo Animal:

Create: vista formularioMascota

Read: vista leerMascota

Update: vista editarMascota

Delete: vista eliminarMascota

_______________________________________________________________________________________________________________________________________________________________________
# Templates:
Es una carpeta donde se encuentran todos los archivos HTML,usados por la app. Se utilza una platilla de BOOSTRAP y se aplica el concep de herencia a cada archivo.

_______________________________________________________________________________________________________________________________________________________________________
# Autor: Joner Claudio
