"""practicafinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout,login
from django.views.static import serve
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$',  'museos.views.barra'),
	url(r'cambiacss', 'museos.views.cambiarcss' ),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^about', 'museos.views.about'),
	url(r'^puntuacion/(.+)$', 'museos.views.puntuacion'),
	url(r'static/(.*)$', serve, {'document_root': 'templates/plantilla'}),
	url(r'^login',login),
	url(r'^xml','museos.views.xml'),
	url(r'^logout',logout),
	url(r'^accounts/profile', 'museos.views.redirect'),
	url(r'^museos/(.+)$', 'museos.views.paginamuseo'),
	url(r'^museos', 'museos.views.museos'),
	url(r'^favoritos/(.+)/(.*)$','museos.views.favoritos'),
	url(r'^register', 'museos.views.usuarios', name = "Crear un usuario"),
	url(r'^(.+$)','museos.views.paginausuario'),
	
	
	
]
