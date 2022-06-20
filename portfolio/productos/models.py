from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    disponible = models.BooleanField()
    fechaIncorporacion = models.DateField()
    correoProveedor = models.EmailField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fechaIncorporacion = models.DateField()
    correoCliente = models.EmailField()

class Boletas(models.Model):
    monto = models.IntegerField()
    descripcion = models.CharField(max_length=30)
    fecha = models.DateField()
 