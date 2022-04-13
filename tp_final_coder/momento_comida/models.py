from django.db import models

class MomentoComida(models.Model):
    id_momento = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
