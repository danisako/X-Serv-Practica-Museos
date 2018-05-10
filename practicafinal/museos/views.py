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
from django.contrib.auth import login, logout
from museos import models
from django.contrib.auth.models import User



boton = """
		<form action = "/" method ="POST">
			<input type="hidden" name="option" value="2"><br>
			<input type="submit" value="Accesibles">
			</form>
		"""

form = """
		<form action = "/" method ="POST">
			<input type="hidden" name="option" value="1"><br>
			<input type="submit" value="Cargar">
			</form>
		"""
		
coment = """
	<form action = "" method ="POST">
		Comentario: <input type="text" name="comentario" value=""><br>
		<input type="submit" value="Enviar">
		</form>
"""

filtro = """
	<form action = "" method ="POST">
		Filtrar por distrito: <input type="text" name="filtro" value=""><br>
		<input type="submit" value="Enviar">
		</form>
"""

register = """
	<form action='/register/' method='post'>"
        Name: <input type= 'text' name='user'>"
        Correo: <input type= 'text' name='email'>"
        Password: <input type= 'password' name='password'>"
        <input type= 'submit' value='Registrar'>
formulario += "</form>"
"""



@csrf_exempt

def barra(request):

	
	
	if request.method == "GET":
		
		respuesta = ""
		respuesta += "ACTUALIZA..</br>"
		
			

		if request.user.is_authenticated():
			logged = 'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a></br>'
			logged = True


		else:
			logged = 'Not logged in. <a href = "/login">Login</a></br>'

		respuesta = logged

		if logged == True:
			respuesta = form +'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a></br> Click aquí para favoritos: <a href = "/'+request.user.username+'">Favoritos</a>'
		else:
			respuesta += 'Para poder comentar logeate!  <a href = "/login">Login</a>'

		museos = Museo.objects.all() #devuelve una lista con todos los museos
		respuesta += "<ul>"
		###https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
		museo = Museo.objects.all().order_by('-comentarios')

		for m in museo:
			respuesta += "Nombre Museo:  <a href="+m.enlace+">"+m.nombre+"</a></br> Num: "+str(m.comentarios)+"</br>" #Muestro la información de los museos que tengo.
			 
			respuesta+= '<li><a href="/museos/'+str(m.id)+'"> Mas información </a></br>' #Muestro la página de información para el museo
		respuesta+= "</ul>"
		
		#favoritos = Favoritos.objects.all()
		#for f in favoritos:
			#respuesta += "Museo:  "+ str(m.nombre)+ " </br>" #Muestro la información de los museos que tengo.
			#respuesta += "usuario:  "+ f.usuario+ " </br>" 
		

	elif request.method == "POST":
		
		if request.POST['option'] == "1":
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
			
			resp = '<head><meta http-equiv="Refresh" content="	;url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal "
			return HttpResponse(resp)

		elif request.POST['option'] == "2":

			museos = Museo.objects.all()
			
			filtro = Museo.objects.filter(accesibilidad = 1)
			respuesta = "<ul>"
			respuesta += " "
			for m in filtro:
	#			respuesta = "Nombre Museo:  <a href="+">"+filtro.nombre+"</a></br>" #Muestro la información de los museos que tengo.
				respuesta+= "<li>Nombre: "+m.nombre+ "</br>Accesibilidad:  "+str(m.accesibilidad)+'</br>' #Muestro la página de información para el museo
	respuesta+= "</ul>"
	respuesta+= "<ul>"
	list_usu = "USUARIOSS"
	lista_pag = User.objects.all()
	
	for i in lista_pag:
		list_usu += "<li><br><a href=" + i.username + ">"
		list_usu += i.username+ "</a> " 
	respuesta+= "</ul>"

	template = get_template("plantilla/index.html")
	c = Context({'users':list_usu , 'title': "Pagina principal" , 	'content':respuesta  , 'usuario':request.user.username})
	
	return HttpResponse(template.render(c))


@csrf_exempt
def paginausuario(request):
	if request.method == "POST":
		name = request.POST['user']
		password = request.POST['passwd']

	usuario = authenticate(username = name, password= password)

	if usuario is not None:
		login(request,user)
		respuesta = "has entrado correctamente!"
		
		
	else:
		respuesta = "erRRor"

	return HttpResponse(respuesta)

@csrf_exempt

def usuarios(request):
	if request.method == "GET":
		respuesta = register
		respuesta += "EEEEEEEEE"
	elif request.method == "POST":
		username = request.POST['user']
		email = request.POST['email']
		password = request.POST['password']
		usuario = User.objects.create_user(username,email,password)
		usuario.save()
		respuesta = '<head><meta http-equiv="Refresh" content="1	;url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal "

	template = get_template("plantilla/register.html")
	c = Context({ 'content':respuesta  , 'url': "http://google.es" , 'algo':"Google"})
	return HttpResponse(template.render(c))
	
	
			

@csrf_exempt
def museos(request):
	museos = Museo.objects.all()
	respuesta = "<h2>LISTA CON TODOS LOS MUSEOS</h2><ul>"

	respuesta = filtro
	if request.method == "GET":
		for m in museos:
			respuesta += "Nombre Museo:  "+m.nombre+"</br>" #Muestro la información de los museos que tengo.
			respuesta+= "Para dar favorito, pulsa: <a href='/favorito/'"+str(m.id)+">Favorito</a></br>"	 
			respuesta+= '<li><a href="'+m.enlace+'">Enlace</a></br></br>' #Muestro la página de información para el museo
		respuesta+= "</ul>"

	elif request.method == "POST":
		dist = request.POST['filtro']
		filtros = Museo.objects.filter(distrito = dist)
		for m in filtros:
			respuesta += "<li>Nombre:" +m.nombre + " Distrito: " +m.distrito + "</br>"

	return HttpResponse(respuesta)
		
@csrf_exempt
def paginamuseo(request,identificador):

	museos = Museo.objects.get(id = identificador)
	com = Comentario.objects.all()
	respuesta = "<h3>BIENVENIDO A LA PÁGINA DEL MUSEO:</h3></br>"
	respuesta +="Nombre --> "+ museos.nombre +"</br> Accesibilidad -->"+ str(museos.accesibilidad) +"</br>Distrito --> "+ museos.distrito +"</br>Número Comentarios -->" + str(museos.comentarios)+"</br>"
	respuesta += "<a href='/'> Volver a la pagina principal</a> "
	
	if request.method == "GET":
		if request.user.is_authenticated():
			respuesta += 'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a></br>'
		
			respuesta += coment

		else:
			respuesta += 'Not logged in. <a href = "/login">Login</a></br>'
	

	#return HttpResponse(respuesta)

	elif request.method == "POST":
		comentario = Comentario(contenido = request.POST.get('comentario'), museo = museos)
		museos.comentarios = museos.comentarios + 1
		museos.save()
		comentario.save()

		respuesta += "Comentario añadido!"


	template = get_template("plantilla/index.html")
	c = Context({'title': "Pagina principal" , 	'content':respuesta  , 'usuario':request.user.username})
	
	return HttpResponse(template.render(c))
@csrf_exempt
def redirect(request):

	resp = "<title>CMS</title><h2>Autenticado como: " +request.user.username +"</h2></br>"
	resp += '<head><meta http-equiv="Refresh" content=";url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal " 
	
	template = get_template("plantilla/index.html")
	c = Context({'content':resp })

	return HttpResponse(template.render(c))

def favoritos(request,mus):
	museos = Museo.objects.all().filter(id = mus)
	museofavorito = Favoritos(usuario = request.user.username, museo = museos)
	print(museo)
	respuesta = "added!!!"
	return HttpResponse(respuesta)


