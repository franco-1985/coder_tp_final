from django.db import models

class Comida (models.Model):
    id_comida = models.IntegerField()
    nombre_comida = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comida
