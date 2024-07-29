from django.db import models
from django.utils.text import slugify
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
        # Primero guardamos la instancia del modelo
        super().save(*args, **kwargs)
        
        # Luego leemos el contenido del archivo si existe
        if self.archivo_texto:
            try:
                with open(self.archivo_texto.path, 'r', encoding='utf-8') as file:
                    markdown_content = file.read()
                    # Convertir Markdown a HTML
                    self.contenido = markdown2.markdown(markdown_content)
                    
            except FileNotFoundError:
                print(f"Error: El archivo {self.archivo_texto.path} no se encontró.")
            except IOError:
                print(f"Error: No se pudo leer el archivo {self.archivo_texto.path}.")
            
            # Actualizamos la instancia del modelo con el contenido del archivo
            super().save(update_fields=['contenido'])

    def __str__(self):
        return self.titulo
