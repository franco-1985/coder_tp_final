from django.db import models

class ComidaXPaciente(models.Model):
    dni = models.IntegerField()
    id_comida = models.IntegerField()
    id_momento = models.IntegerField()
    descripcion = models.CharField(max_length=1000)


class PesoXPaciente(models.Model):
    dni = models.IntegerField()
    peso = models.FloatField()
    estatura = models.IntegerField()
    fecha_registro = models.DateField()

    def __str__(self):
        return 'registo de peso por paciente'
