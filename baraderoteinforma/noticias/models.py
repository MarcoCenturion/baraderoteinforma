from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    archivo_markdown = models.FileField(upload_to='markdown/', null=True, blank=True)
    contenido = models.TextField(blank=True)
    texto_markdown = models.TextField(blank=True)  # Campo adicional para el contenido Markdown como texto plano
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

