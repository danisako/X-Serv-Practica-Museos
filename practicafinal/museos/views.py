from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import urllib.request
# Create your views here.
from .models import Museo,Comentario,Favoritos
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from django.db.models.functions import Length
from museos.parse import ParsearMuseos


boton = """
		<form action = "/" method ="POST">
			<input type="hidden" name="option" value="2"><br>
			<input type="submit" value="Accesibles">
			</form>
		"""





@csrf_exempt

def barra(request):


	if request.method == "GET":
		
		respuesta = ""
		respuesta += "ACTUALIZA..</br>"
		form = """
		<form action = "/" method ="POST">
			<input type="hidden" name="option" value="1"><br>
			<input type="submit" value="Cargar">
			</form>
		"""
		
			

		if request.user.is_authenticated():
			logged = 'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a></br>'
			logged = True


		else:
			logged = 'Not logged in. <a href = "/login">Login</a></br>'

		respuesta = logged

		if logged == True:
			respuesta += 'Click aquí para favoritos: <a href = "/'+request.user.username+'">Favoritos</a>'
		else:
			respuesta += 'Para poder comentar logeate!  <a href = "/login">Login</a>'

		museos = Museo.objects.all() #devuelve una lista con todos los museos
		respuesta += "<ul>"

		for m in museos:
			respuesta += "Nombre Museo:  <a href="+m.enlace+">"+m.nombre+"</a></br>" #Muestro la información de los museos que tengo.
			 
			respuesta+= '<li><a href="'+m.enlace+'"> Mas información </a></br>' #Muestro la página de información para el museo
		respuesta+= "</ul>"
		#print(m.nombre)



		favoritos = Favoritos.objects.all()
		for f in favoritos:
			respuesta += "Museo:  "+ str(m.nombre)+ " </br>" #Muestro la información de los museos que tengo.
			respuesta += "usuario:  "+ f.usuario+ " </br>" 


	elif request.method == "POST":
		listamuseos = []
		museos = Museo.objects.all()
		listamuseos = ParsearMuseos()	
		for museos in listamuseos:
	# En cada campo del models metemos lo que hemos parseado
		
			museo_new = Museo(nombre=museos["NOMBRE"],
								accesibilidad=museos["ACCESIBILIDAD"],
								enlace=museos["CONTENT-URL"],
								nombrevia=museos["NOMBRE-VIA"],
								clasevia=museos["CLASE-VIAL"],
								tiponum=museos["TIPO-NUM"],
								numero=museos["NUM"],
								localidad=museos["LOCALIDAD"],
								provincia=museos["PROVINCIA"],
								codigopostal=museos["CODIGO-POSTAL"],
								barrio=museos["BARRIO"],
								distrito=museos["DISTRITO"],
								coordx=museos["COORDENADA-X"],
								coordy=museos["COORDENADA-Y"],)
			

			museo_new.save()

		Listado = []
		print(listamuseos)
		resp = '<head><meta http-equiv="Refresh" content="1	;url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal "
		return HttpResponse(resp)
	return HttpResponse(respuesta+form + boton)


@csrf_exempt
def usuario(request,nombre):
	respuesta = "Bienvenido a tu página  " +nombre
	favoritos = Favoritos.objects.all()
	respuesta += "<ul>"

	for f in favoritos:
		respuesta += "Museo:  "+ str(m.nombre)+ " </br>" #Muestro la información de los museos que tengo.
		respuesta += "usuario:  "+ f.usuario+ " </br>" 
	respuesta+= "</ul>"


	return HttpResponse(respuesta)







