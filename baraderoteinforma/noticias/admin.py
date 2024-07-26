from django.contrib import admin
from .models import Categoria, Noticia

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')  # Asegúrate de que 'slug' esté definido en el modelo Categoria

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'resumen')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)

