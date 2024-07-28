from django.db import models
import markdown2

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
    contenido = models.TextField(null=True, blank=True)
    archivo_texto = models.FileField(upload_to='textos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        with open(self.archivo_texto.path, 'r', encoding='utf-8') as file:
            self.contenido = file.read()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
