from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import urllib.request
from xml.sax.handler import ContentHandler
# Create your views here.
from .models import Museo,Comentario,Favoritos,Cambiarcss
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from django.db.models.functions import Length
from museos.parse import ParsearMuseos
from django.contrib.auth import authenticate,login
from museos import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




boton = """
		Mostrar museos accesibles
		<form action = "/" method ="POST">
			<input type="hidden" name="option" value="2"><br>
			<input type="submit" value="Accesibles">
			</form>
		"""

form = """
		Cargar museos
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
		Filtrar por distrito: <input type="text" name="filtrar" value=""><br>
		<input type="hidden" name="favo" value="2"><br>
		<input type="submit" value="Enviar">
		</form>
"""

register = """
	<form action='/register/' method='post'>
	    Name: <input type= 'text' name='user'><br>
	    Correo: <input type= 'text' name='email'><br>
	    Password: <input type= 'password' name='password'<br>
	    <input type= 'submit' value='Registrar'></br></br>
</form>
"""


listamuseos = []



formulario = """
	<h3>IDENTIFICATE</h3>
	'<form action="/" method="POST">
		Nombre<br><input type="text" name="Usuario"><br>
		<input type="hidden" name="option" value="3"><br>
		Contraseña<br><input type="password" name="Password"><br>
		<input type="submit" value="Entrar">
</form>'
"""


@csrf_exempt
def barra(request):

	numero = 0
	color = ""
	tamano = ""
	
	
		

	if request.user.is_authenticated():
		logged = 'Logged in as --> ' + request.user.username + '<a href="/logout">Logout</a></br>'
		log = True


	else:
		logged = 'Not logged in. <a href = "/login">Login</a></br>'
		log = False

	if request.method == "GET":

		museos = Museo.objects.all() #devuelve una lista con todos los museos
		respuesta = "<ul>"
		###https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
		museo = Museo.objects.all().order_by('-comentarios')
		
		lista = []
		num = 0
		for lista in museo:
			if lista.comentarios != 0:
				respuesta += "Nombre Museo:  <a href="+lista.enlace+">"+lista.nombre+"</a></br> " #Muestro la información de los museos que tengo.			
				respuesta += "Dirección: " +lista.clasevia+" " + lista.nombrevia + "  "+str(lista.numero) +" Localidad:  "+ lista.localidad + "</br>"
				respuesta += "Puntuacion: " +str(lista.valoracion)+"</br>"
				respuesta += "Numero de Comentarios: " +str(lista.comentarios)+"</br>"
				respuesta+= '<li><a href="/museos/'+str(lista.id)+'"> Mas información </a></br>' #Muestro la página de información para el museo
			else:
				respuesta +=""
			num = num + 1
			if num == 5:
				break
		respuesta+= "</ul>"
		 
		

	elif request.method == "POST":
		
		if request.POST['option'] == "1":
			museos = Museo.objects.all()
			if museos.count() == 0:
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
				else:
					resp ='<head><meta http-equiv="Refresh" content="	;url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal "
			
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
		else:
		#Con ayuda de: http://www.maestrosdelweb.com/curso-django-gestion-de-usuarios/
			usuario = request.POST['Usuario']
			clave = request.POST['Password']
			acceso = authenticate(username = usuario,password = clave)
			if acceso is not None:
				respuesta = ""
				login(request,acceso)
			else:
				respuesta = "Error"
			
			
			return HttpResponseRedirect('/')
			
	
	respuesta+= "<ul>"
	list_usu = "USUARIOS"
	lista_pag = User.objects.all()
	css = Cambiarcss.objects.all()
	
	
	for i in lista_pag:
		list_usu += "<li><br>Pagina de: <a href=" + i.username + ">"
		list_usu += i.username+ "</a> " 
	 
	respuesta+= "</ul>"
	
	if request.user.is_authenticated():
		us = User.objects.get(id = request.user.id)
		print(us)
		listacss = Cambiarcss.objects.all()
		for t in listacss:
			print(t.nombre)
			if t.nombre == us:
				color = t.color
				tamano = t.tamano
				print(color)
			else:
				print("no hay color")

	else:
			respuesta += "Logeatee"

	
	
	template = get_template("plantilla/index.html")
	c = Context({'users':list_usu ,'log':log,'tamano':tamano, 'colorcss':color, 'logeado': logged , 	'content':respuesta  , 'usuario':request.user.username,'accesibles': boton,'cargar':form,'login':formulario,'comentarios':numero})
	
	return HttpResponse(template.render(c))


@csrf_exempt
def paginausuario(request,user):
	
	museos = Museo.objects.all()
	usuarios = User.objects.get(username = user)
	
		
	respuesta = "Pagina de " + user+"</br>"
	favoritos = Favoritos.objects.all().filter(usuario= usuarios.id)
	
	color = ""
	tamano =""

	if request.method == "GET":
		
		for f in favoritos:
			respuesta += "<li>Nombre: "+str(f.museo)+"</br></li>"
			respuesta += "Fecha seleccionado: "+str(f.fecha)+"</br></br></br>"
	
		respuesta += """
		<form action = "/cambiacss" method ="POST">
			<label>Color: </label>
			<input type="radio" name = "fondo" value="#fa1b09">Rojo
			<input type="radio" name = "fondo" value="#7fb3d5">Azul
			<input type="radio" name = "tamaño" value="10">Tamaño 10
			<input type="radio" name = "tamaño" value="16">Tamaño 16
			<input type="submit" value="Cambiar">
			</form>
	"""
	if request.user.is_authenticated():
		us = User.objects.get(id = request.user.id)
		print(us)
		listacss = Cambiarcss.objects.all()
		for t in listacss:
			
			if t.nombre == us:
				color = t.color
				tamano = t.tamano
				
			else:
				print("no hay color")

	else:
			respuesta += "Logeatee"

	template = get_template("plantilla/paginausuario.html")
	c = Context({ 'title': respuesta , 	'content':respuesta  , 'cambiacss':color,'tamano':tamano,'usuario':request.user.username})
	
	return HttpResponse(template.render(c))

	
	

@csrf_exempt

def usuarios(request):
	if request.method == "GET":
		respuesta = "Por favor, para registrarse rellene todos los campos: </br>"
		respuesta = register
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
	respuesta = "<h2>LISTA CON TODOS LOS MUSEOS</h2>"

	respuesta = filtro
	if request.method == "GET":
		for m in museos:
			respuesta += "<li>Nombre Museo:  "+m.nombre+"</br>" #Muestro la información de los museos que tengo.
		
			
			if request.user.is_authenticated():
				respuesta+= "Para guardar como favorito, pulsa: <a href='/favoritos/"+str(m.id)+"/"+request.user.username+"'>Favorito</a></br>"
			else:
				respuesta += "No estás logueado, haz click para entrar y poder marcar como favorito</br> <a href = '/login'>Login</a></br>"	
			respuesta += ""
			respuesta+= '<li><a href="museos/'+str(m.id)+'">Enlace</a></br></br>' #Muestro la página de información para el museo
			

	elif request.method == "POST":
		filtros = Museo.objects.filter(distrito = request.POST['filtrar'])
		for m in filtros:
			respuesta += "<li>Nombre:" +m.nombre + " Distrito: " +m.distrito + "</li></br></br>"
	color =""
	css = Cambiarcss.objects.all()
	for t in css:
				if t.nombre == request.user.username:
					color = t.color
					print(t.color)	

	template = get_template("plantilla/museos.html")
	c = Context({ 'content':respuesta,'cambiacss':color})
	return HttpResponse(template.render(c))
		
@csrf_exempt
def paginamuseo(request,identificador):

	museos = Museo.objects.get(id = identificador)
	com = Comentario.objects.all().filter(museo_id = identificador)
	respuesta = "<h3>BIENVENIDO A LA PÁGINA DEL MUSEO:</h3></br>"
	respuesta +="Nombre: "+ museos.nombre +"</br> Accesibilidad: "+ str(museos.accesibilidad) +"</br>Distrito:"+ museos.distrito +"</br>Barrio:"+museos.barrio+ "</br> Número Comentarios:" + str(museos.comentarios)+"</br>"
	respuesta += "Para puntuar el museo, click aquí: <a href='/puntuacion/"+str(museos.id)+"'>Me gusta</a></br>"
	for i in com:
		if museos.comentarios == "0":
			respuesta += "NO hay comentarios </br>"
		else:
			respuesta += "<li>Comentario:" +i.contenido +"</li></br>"
	respuesta += "<a href='/'> Volver a la pagina principal</a> "
	
	if request.method == "GET":
		if request.user.is_authenticated():
		
			respuesta += coment

		else:
			respuesta += 'Not logged in. <a href = "/login">Login</a></br>'
	

	elif request.method == "POST":
		comentario = Comentario(contenido = request.POST.get('comentario'), museo = museos)
		museos.comentarios = museos.comentarios + 1
		museos.save()
		comentario.save()

		respuesta += "Comentario añadido!"
		respuesta += '<head><meta http-equiv="Refresh" content=";url="/museos/'+str(museos.id)+'"></head>'" Redirigiendo a la pagina principal "


	template = get_template("plantilla/paginamuseo.html")
	c = Context({ 'content':respuesta})
	return HttpResponse(template.render(c))
@csrf_exempt
def redirect(request):

	resp = "<title>APP MUSEOS</title><h2>Autenticado como: " +request.user.username +"</h2></br>"
	resp += '<head><meta http-equiv="Refresh" content=";url='"http://127.0.0.1:8000"'"></head>'" Redirigiendo a la pagina principal " 
	
	template = get_template("plantilla/index.html")
	c = Context({'content':resp })

	return HttpResponse(template.render(c))

@csrf_exempt
def favoritos(request,mus,us):
	museos = Museo.objects.get(id = mus)
	usuarios = User.objects.get(username = us)
	museofavorito = Favoritos(usuario =usuarios, museo = museos)
	fav = Favoritos.objects.all().filter(usuario_id = usuarios.id)

	museofavorito.save()
	for f in fav:
		if f.museo:
			respuesta ="Museo añadido"
		else:
			respuesta = "added!!!"+str(museofavorito.museo)
			museofavorito.save()

	
	return HttpResponseRedirect("/")
@csrf_exempt
def cambiarcss(request):
	color = ""
	if request.user.is_authenticated():
		color = request.POST['fondo']
		tamano = request.POST['tamaño']
		print(color)	
		usuario = User.objects.get(username = request.user.username)
		print(usuario)
		css = Cambiarcss.objects.all()
				
		if len(css) == 0:
			cambio = Cambiarcss(nombre = usuario, color = color, tamano = tamano)
			cambio.save()
			print("añado cssuser")
			
		else:
			for t in css:
				if t.nombre == usuario:
					t.color = color
					t.tamano = tamano
					t.save()
					print(t.color)
				else:
					cambio = Cambiarcss(nombre = usuario, color = color, tamano = tamano)
					cambio.save()
					print("color añadido nuevo")
	
			
		
	template = get_template("plantilla/index.html")
	c = Context({'colorcss':color })

	return HttpResponseRedirect("/")

def about(request):
    template = get_template("plantilla/about.html")
    
    c = Context(request)
    return HttpResponse(template.render(c))
	

@csrf_exempt
def puntuacion(request,identificador):
	museos = Museo.objects.get(id = identificador)
	museos.valoracion = museos.valoracion + 1
	museos.save()

	return HttpResponseRedirect("/")

def xml(request):
    template = get_template("plantilla/index.xml")
    museo = Museo.objects.all().order_by('-comentarios')

    c = Context({'museos': museo,})
    return HttpResponse(template.render(c),content_type = "text/xml")
		



