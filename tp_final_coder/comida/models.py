from django.db import models

class Comida (models.Model):
    id_comida = models.IntegerField()
    nombre = models.CharField(max_length=100)
