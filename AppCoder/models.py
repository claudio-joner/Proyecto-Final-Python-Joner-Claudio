from pyexpat import model
from django.db import models

# Create your models here.
class Animal(models.Model):
    nombreAnimal= models.CharField(max_length=40)
    edad= models.IntegerField()
    tipo= models.CharField(max_length=40)
    motivo= models.CharField(max_length=40)
    fecha= models.DateField()
    costo= models.IntegerField()


class Persona(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    telefono= models.IntegerField()

class Veterinario(models.Model):
    veterinario = models.CharField(max_length=20)
    apellidoVet = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)