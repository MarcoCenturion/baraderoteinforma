from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Noticia, Categoria
from .forms import NoticiaForm
import markdown2
import os

def listar_noticias(request):
    categorias = Categoria.objects.all()
    return render(request, 'noticias/listar_noticias.html', {'categorias': categorias})

def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalle.html', {'noticia': noticia})

def subir_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            if noticia.archivo_texto:
                with open(noticia.archivo_texto.path, 'r', encoding='utf-8') as file:
                    texto = file.read()
                noticia.contenido = texto
            noticia.save()
            return render(request, 'noticias/subir_noticia.html')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/subir_noticia.html', {'form': form})
