from django.db import models

class Perros(models.Model):
    codigo=models.CharField(max_length=100)
    foto=models.FileField(null=True,blank=True)
    nombre=models.CharField(max_length=60)
    raza =models.CharField(max_length=60)
    descripcion=models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

class Mascota(models.Model):
    foto=models.FileField(null=True,blank=True)
    nombre=models.TextField(max_length=60)
    raza =models.TextField(max_length=60)
    descripcion=models.TextField(max_length=100)
    estadomascota = models.TextField(max_length=100)

class Adoptante(models.Model):
    email=models.EmailField()
    run = models.TextField(max_length=13)
    nombre = models.TextField(max_length=2)
    apellido = models.TextField(max_length=2)
    fechanacimiento = models.TextField(max_length=60)
    telefono= models.IntegerField()
    region=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)

class Usuario(models.Model):
    nombre=models.CharField(max_length=60)
    contraseña=models.TextField(max_length=30)

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)

class Estado(models.Model):
    descripcion=models.CharField(max_length=30)