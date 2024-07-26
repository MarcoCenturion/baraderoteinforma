# Generated by Django 5.0.7 on 2024-07-26 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumen', models.TextField()),
                ('contenido', models.TextField()),
                ('archivo_markdown', models.FileField(upload_to='markdown/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria')),
            ],
        ),
    ]