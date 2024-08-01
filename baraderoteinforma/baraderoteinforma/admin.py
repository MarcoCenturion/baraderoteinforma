from django.contrib import admin
from .models import Tag, Categoria, Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'autor')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_creacion', 'categoria')

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Tag)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)

