from django.urls import path
from .views import listar_noticias, subir_noticia, detalle_noticia, noticias_por_categoria

app_name = 'noticias'

urlpatterns = [
    path('', listar_noticias, name='listar_noticias'),
    path('subir_noticias/', subir_noticia, name='subir_noticia'),
    path('categoria/<slug:slug>/', noticias_por_categoria, name='categoria'),
    path('<int:id>/', detalle_noticia, name='detalle_noticia'),
]
