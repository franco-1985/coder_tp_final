from django.db import models

class MomentoComida(models.Model):
    id_momento = models.IntegerField()
    nombre_momento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre_momento
