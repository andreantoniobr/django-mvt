from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/')
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo
