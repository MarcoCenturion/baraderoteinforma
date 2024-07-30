from django.urls import path
from .views import listar_noticias, subir_noticia, detalle_noticia

app_name = 'noticias'

urlpatterns = [
    path('', listar_noticias, name='listar_noticias'),
    path('subir_noticias/', subir_noticia, name='subir_noticia'),
    path('<int:id>/', detalle_noticia, name='detalle_noticia'),
]
