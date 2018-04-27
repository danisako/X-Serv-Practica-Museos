from django.db import models

# Create your models here.

class Comentario(models.Model):
	contenido = models.TextField()
	usuario = models.CharField(max_length = 16)
	def __str__(self):
		return self.contenido + "User:" + self.usuario

class Museo(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    horario = models.TextField()
    descrip = models.TextField()
    enlace = models.URLField(max_length=200)
    comentarios = models.ForeignKey(Comentario)
    accesibilidad = models.PositiveSmallIntegerField()
    equipamiento = models.TextField()
    transporte = models.TextField()
    nombrevia = models.CharField(max_length = 64)
    clasevia = models.CharField(max_length = 32)
    tiponum = models.CharField(max_length  = 1)
    numero = models.IntegerField()
    planta = models.CharField(max_length = 16)
    orientacion = models.TextField()
    localidad = models.CharField(max_length = 8)
    provincia = models.CharField(max_length = 8)
    codigopostal = models.IntegerField()
    barrio = models.CharField(max_length = 32)
    distrito = models.CharField(max_length = 16)
    coordx = models.IntegerField()
    coordy = models.IntegerField()
    latitud = models.DecimalField(max_digits =20 ,decimal_places = 18)
    longitud = models.DecimalField(max_digits =20 ,decimal_places = 18)
    telefono = models.IntegerField()
    numberpk = models.IntegerField()
	
	




    def __str__(self):
        return self.nombre
	

class Favoritos(models.Model):
	usuario = models.CharField(max_length = 32)
	museo = models.ManyToManyField(Museo) 
	




	
	
	
