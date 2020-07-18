
from django.db import models
from persona.models import User
from dispositivo.models import Dispositivo, Sensor, Actuador


class UserDispositivo(models.Model):
    id_user_fk = models.ForeignKey(
        User, 
        models.DO_NOTHING, 
        db_column='id_user_fk',
        verbose_name='Usuario'
        )
    id_dispositivo_fk = models.ForeignKey(
        Dispositivo,
        models.DO_NOTHING,
        db_column='id_dispositivo_fk',
        verbose_name='Identificador del Controlador'
        )

    class Meta:
        db_table = 'dispositivo_user'
        verbose_name='Dispositivo del Usuario'
        verbose_name_plural='Dispositivos del Usuario'
        unique_together = (('id_user_fk', 'id_dispositivo_fk'),)
        
    def __str__(self):
        return str(self.id_dispositivo_fk.nombre)


class Tablero(models.Model):
    id_user_fk = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='id_user_fk',
        verbose_name="Usuario")

    sensor = models.ManyToManyField(
        Sensor,
        verbose_name='Sensor',
        blank=True,
    )

    actuador = models.ManyToManyField(
        Actuador,
        verbose_name='Actuador',
        blank=True,
    )

    nombre = models.CharField("Nombre del Tablero", max_length=30)

    class Meta:
        db_table = 'tablero'
        
    def __str__(self):
        return self.nombre