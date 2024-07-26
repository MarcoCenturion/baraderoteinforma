from django.urls import path
from .views import subir_noticia, lista_noticias

urlpatterns = [
    path('subir/', subir_noticia, name='subir_noticia'),
    path('', lista_noticias, name='lista_noticias'),
]

