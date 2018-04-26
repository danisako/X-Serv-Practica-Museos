from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Museo,Comentario,Favoritos
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

def barra(request):

	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + '<a href="/logout">Logout</a>'
	else:
		logged = 'Not logged in. <a href = "/login">Login</a>'

	resp = "probando...."

	museos = Museo.objects.all() #devuelve una lista con todos los museos
	respuesta = "<ul>"
	for m in museos:
		respuesta += "Nombre Museo:  "+ m.nombre+ " </br>" #Muestro la información de los museos que tengo.
		respuesta+= '<li><a href="'+m.enlace+'"> Mas información </a>' #Muestro la página de información para el museo
	respuesta+= "</ul>"


	
	return HttpResponse(resp + logged)
