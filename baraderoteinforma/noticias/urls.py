from django.urls import path
from .views import listar_noticias, subir_noticia, detalle_noticia, noticias_por_categoria, noticias_por_tag
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', listar_noticias, name='listar_noticias'),
    path('subir_noticias/', subir_noticia, name='subir_noticia'),
    path('categoria/<slug:slug>/', noticias_por_categoria, name='categoria'),
    path('<int:id>/', views.detalle_noticia, name='detalle_noticia'),
    path('tag/<slug:slug>/', noticias_por_tag, name='tag'),
]
