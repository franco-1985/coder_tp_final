from django.db import models

class Paciente(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()

    def __str__(self):
        return str(self.dni) + ' - ' + self.nombre + ' - ' + str(self.fecha_nacimiento)
