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

        # opciones de horarios
    HORARIOS = (
        (0, '09:00 - 09:30'),
        (1, '09:30 - 10:00'),
        (2, '10:00 - 10:30'),
        (3, '10:30 - 11:00'),
        (4, '11:00 - 11:30'),
        (5, '11:30 - 12:00'),
        (6, '12:00 - 12:30'),
        (7, '12:30 - 13:00'),
        (8, '13:00 - 13:30'),
        (9, '13:30 - 14:00'),
        (10, '14:00 - 14:30'),
        (11, '14:30 - 15:00'),
        (12, '15:00 - 15:30'),
        (13, '15:30 - 16:00'),
        (14, '16:00 - 16:30'),
        (15, '16:30 - 17:00'),
        (16, '17:00 - 17:30'),
        (17, '17:30 - 18:00'),
        (18, '18:00 - 18:30'),
        (19, '18:30 - 19:00'),
        (20, '19:00 - 19:30'),
        (21, '19:30 - 20:00'),
        (22, '20:00 - 20:30'),

    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario = models.IntegerField(choices=HORARIOS)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.empleado.usuario.first_name + " " + self.empleado.usuario.last_name + "--->" + self.cliente.nombre.first_name + "----->" + str(self.fecha) + " at " + str(self.get_horario_display())