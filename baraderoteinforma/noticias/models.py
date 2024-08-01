from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import markdown2

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

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
    tags = models.ManyToManyField(Tag, related_name='noticias')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Asegúrate de que el usuario con ID 1 exista

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.archivo_texto:
            try:
                with open(self.archivo_texto.path, 'r', encoding='utf-8') as file:
                    self.contenido = markdown2.markdown(file.read())
            except FileNotFoundError:
                print(f"Error: El archivo {self.archivo_texto.path} no se encontró.")
            except IOError:
                print(f"Error: No se pudo leer el archivo {self.archivo_texto.path}.")
            
            super().save(update_fields=['contenido'])

    def __str__(self):
        return self.titulo

