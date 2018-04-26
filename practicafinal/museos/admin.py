from django.contrib import admin

# Register your models here.
from .models import Museo,Comentario,Favoritos

admin.site.register(Museo)
admin.site.register(Favoritos)
admin.site.register(Comentario)
