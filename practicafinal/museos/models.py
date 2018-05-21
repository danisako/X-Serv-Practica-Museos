from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Museo(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(default = "")
    horario = models.TextField(default = "")
    descrip = models.TextField(default = "")
    enlace = models.URLField(max_length=200)
    accesibilidad = models.PositiveSmallIntegerField()
    equipamiento = models.TextField()
    transporte = models.TextField()
    nombrevia = models.CharField(max_length = 64)
    clasevia = models.CharField(max_length = 32)
    tiponum = models.CharField(max_length  = 1)
    numero = models.FloatField()
    planta = models.CharField(max_length = 16)
    orientacion = models.TextField()
    localidad = models.CharField(max_length = 8)
    provincia = models.CharField(max_length = 8)
    codigopostal = models.IntegerField()
    barrio = models.CharField(max_length = 32)
    distrito = models.CharField(max_length = 16)
    coordx = models.FloatField()
    coordy = models.FloatField()
    latitud = models.TextField(default = "")
    longitud = models.TextField(default = "")
    telefono = models.TextField()
    numberpk = models.TextField()
	
    valoracion = models.IntegerField(default = 0)
    comentarios = models.IntegerField(default = 0)
	
	
	




    def __str__(self):
        return self.nombre

class Comentario(models.Model):
	contenido = models.TextField()
	museo = models.ForeignKey('Museo')
	def __str__(self):
		return self.contenido + "User:" + self.usuario + "MUSEO: " +self.museo


	
class Cambiarcss(models.Model):
	nombre = models.ForeignKey(User)
	color = models.CharField(default="#000000", max_length=32)
	tamano = models.CharField(default="10pt",max_length = 32)

class Favoritos(models.Model):
	usuario = models.ForeignKey(User)
	museo = models.ForeignKey('Museo')
	titulo = models.CharField(max_length = 128)
	fecha = models.DateTimeField(auto_now = True)
	
