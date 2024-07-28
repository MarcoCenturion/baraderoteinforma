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
            return redirect('listar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/subir_noticia.html', {'form': form})

'''
def subir_noticia(request):
    if request.method == 'POST':
        noticia_form = NoticiaForm(request.POST, request.FILES)
        if noticia_form.is_valid():
            noticia = noticia_form.save()
            archivo_path = noticia.archivo_markdown.path
            if os.path.exists(archivo_path):
                try:
                    with open(archivo_path, 'r', encoding='utf-8') as file:
                        # Procesar el archivo
                        pass
                except Exception as e:
                    messages.error(request, f'Error al leer el archivo: {e}')
                    return redirect('noticias:subir_noticia')
            else:
                messages.error(request, 'El archivo markdown no se encontró.')
                return redirect('noticias:subir_noticia')
            return redirect('noticias:listar_noticias')
    else:
        noticia_form = NoticiaForm()
    return render(request, 'noticias/subir_noticia.html', {'form': noticia_form})
'''
