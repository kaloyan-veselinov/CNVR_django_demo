from django.db import models


class Cliente(models.Model):
    nombre = models.CharField("Nombre del usuario", max_length=50)
    apellidos = models.CharField("Apellidos del usuario", max_length=100)
    balance = models.IntegerField("Dinero en la cuenta")

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellidos)
