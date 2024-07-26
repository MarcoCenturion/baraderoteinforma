from django.db import models
from django.db import models
from django.utils.text import slugify
import os
from markdown2 import markdown

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    contenido = models.TextField()
    archivo_markdown = models.FileField(upload_to='markdown/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.archivo_markdown:
            file_path = self.archivo_markdown.path 
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    self.contenido = markdown(file.read())
            else:
                self.contenido = "No exite el archivo .md"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

