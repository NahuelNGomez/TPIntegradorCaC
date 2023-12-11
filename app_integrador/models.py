from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    autor = models.CharField(max_length=50, verbose_name='Autor')
    editorial = models.CharField(max_length=50, verbose_name='Editorial')
    genero = models.CharField(max_length=50, verbose_name='Género')
    precio = models.IntegerField(verbose_name='Precio')