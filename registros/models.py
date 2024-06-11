from django.db import models

# Create your models here.

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12) #Texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)