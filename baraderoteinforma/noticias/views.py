from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Noticia, Categoria, Tag
from .forms import NoticiaForm
import markdown2
import os
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def noticias_por_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    noticias = Noticia.objects.filter(tags=tag)
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    return render(request, 'noticias/listar_noticias.html', {
        'noticias': noticias,
        'categorias': categorias,
        'tags': tags,
        'current_year': timezone.now().year,
    })

def listar_noticias(request):
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    return render(request, 'noticias/listar_noticias.html', {
        'noticias': noticias,
        'categorias': categorias,
        'tags': tags,
        'current_year': timezone.now().year,
    })

def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalle.html', {'noticia': noticia})

def noticias_por_categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    noticias = Noticia.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'listar_noticias.html', {
        'noticias': noticias,
        'categorias': categorias,
        'categoria_actual': categoria
    })

@login_required
def subir_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('noticias/listar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/subir_noticia.html', {'form': form})
