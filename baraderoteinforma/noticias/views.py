from django.shortcuts import render, redirect
from .forms import NoticiaForm
from .models import Noticia, Categoria

def subir_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/subir_noticia.html', {'form': form})

def lista_noticias(request):
    categorias = Categoria.objects.all()
    return render(request, 'noticias/lista_noticias.html', {'categorias': categorias})

