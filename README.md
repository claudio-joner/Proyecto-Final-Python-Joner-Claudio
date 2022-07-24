# Proyecto-Final-Python-Joner-Claudio.
Este proyecto es desarrollado en Python utilizando el framework Django. 
El proyecto trata de una app web sobre una Veterinaria, la cual renderiza la informacion que esta almacenadas en la base de datos y la muesta en las diferentes vistas dependiendo cual sea la solicitud.
Debajo se encuentra el link para ver la app en funcionamiento 

# Video Demostración.
https://youtu.be/-H87qxX9Zgs

#DOCUMENTACIÓN.

Para poder encontrar los archivos que nombrare a posterior ingresar  en la caperta AppCoder.

Descripcion: modelo Animal. Campos: -nombreAnimal(Char, nombre de la mascota) -edad(Integer,edad de la mascota) -tipo(Char,ej:perro,gato,iguana,etc) -motivo(Char,ej:peluqueria,vacunas,etc) -fecha(Date,es la fecha de ingreso a la veterinaria) -costo(Integer, el precio de lo que lo se le haya echo al animal)

Descripcion: modelo Persona. Campos: -nombre(Char, nombre del dueño de la mascota) -apellido= (Char, apellido del dueño de la mascota) -telefono= (Integer, numero del dueño de la mascota)

Descripcion: modelo Veterinario. Campos: -veterinario(Char, nombre del veterinario) -apellidoVet= (Char, apellido del veterinario) -matricula= (Integer, numero de matricula del veterinario)

La diposición de la página es la siguiente: -Menú: Tenemos una barra de navegación. Esta tiene los sigueientes botones: *Inicio: redirecciona template padre(inicio.html), lo demás templates heredan ccs y html de él. *Dueño/a: muestra un herencia y un lorem *Veterinario: muestra un herencia y un lorem *Formularios: abri un formulario para cargar los datos de una mascota (Modelo: Animal). *Busqueda: formulario para buscar una mascota por su nombre.

-Titulo: muestra el nombre de la veterinaria.

-Pie.

Cabe aclarar que toda la informacion se presenta entre el titulos y el pie,se aplica herencia.git 


