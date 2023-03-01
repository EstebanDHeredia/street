from django.db import models
from tienda.models import Cliente
from ordenes.models import Empleado, Servicio

# Create your models here.
class Turno(models.Model):
    """
    Clase que representa a un turno en la peluquería.

    Atributos:
    - cliente (Cliente): cliente que solicitó el turno.
    - empleado (Empleado): empleado que atenederá el turno.
    - fecha (date): fecha del turno.
    - hora (time): hora del turno.
    - servicio (Servicio): servicio solicitado en el turno.
    - estado (Choice): estado del turno.
    """

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('atendido', 'Atendido'),
        ('cancelado', 'Cancelado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)