from django.db import models

from tp_final_coder.comida.views import ComidaView
from django.core import serializers

from tp_final_coder.comida.models import Comida
from tp_final_coder.momento_comida.models import MomentoComida

class ComidaXPaciente(models.Model):
    #print('ComidaxPaciente models')
    dni = models.IntegerField()
    id_comida = models.ForeignKey(Comida, on_delete=models.CASCADE, null=True)
    id_momento = models.ForeignKey(MomentoComida, on_delete=models.CASCADE, null=True)
    descripcion = models.CharField(max_length=1000)

    def get_nombre_comida(id_comida):
        return dni

    def __str__(self):
        return 'prueba comidaxPaciente'

class PesoXPaciente(models.Model):
    dni = models.IntegerField()
    peso = models.FloatField()
    estatura = models.IntegerField()
    fecha_registro = models.DateField()

    def __str__(self):
        return 'registo de peso por paciente'
