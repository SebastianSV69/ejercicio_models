from django.db import models

# Create your models here.
class Employee(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)

class Fruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.TextField()
    color = models.TextField()
    sabor = models.TextField()
    precio = models.PositiveIntegerField()
    oferta = models.BooleanField()
    descripcion = models.TextField(blank=True)