from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Museo,Comentario,Favoritos
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


form = """
<form action = "" method ="POST">
	Museo: <input type="text" name="nombre" value=""><br>
    <input type="submit" value="Enviar">
    </form>
"""




def barra(request):

	if request.method == "GET":
	

		if request.user.is_authenticated():
			logged = 'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a>'

			respuesta = "<h2>Hola --> " +request.user.username + "selecciona los museos favoritos: </h2></br>"
			respuesta += form 
	
		else:
			logged = 'Not logged in. <a href = "/login">Login</a>'

		respuesta += "probando...."

		museos = Museo.objects.all() #devuelve una lista con todos los museos
		respuesta += "<ul>"
		for m in museos:
			respuesta += "Nombre Museo:  "+ m.nombre+ " </br>" #Muestro la información de los museos que tengo.
			respuesta += "Comentarios:  "+ str(m.comentarios)+ " </br>" 
			respuesta+= '<li><a href="'+m.enlace+'"> Mas información </a>' #Muestro la página de información para el museo
		respuesta+= "</ul>"

	elif request.method == "POST":
		
		if request.user.is_authenticated():
			logged = 'Logged in as ' + request.user.username + '<a href="/logout">Logout</a>'

			respuesta = "<h2>Hola  " +request.user.username + "selecciona los museos favoritos: </h2></br>"
			respuesta += form 
			favorito = Favoritos(museo = request.POST['nombre'],usuario = request.user.username)
			favorito.save()
	
	
		else:
			logged = 'Not logged in. <a href = "/login">Login</a>'

		respuesta += "probando...."

		museos = Museo.objects.all() #devuelve una lista con todos los museos
		respuesta += "<ul>"

		for m in museos:
			respuesta += "Nombre Museo:  "+ m.nombre+ " </br>" #Muestro la información de los museos que tengo.
			respuesta += "Comentarios:  "+ str(m.comentarios)+ " </br>" 
			respuesta+= '<li><a href="'+m.enlace+'"> Mas información </a>' #Muestro la página de información para el museo
		respuesta+= "</ul>"

	
	return HttpResponse(respuesta + logged)



