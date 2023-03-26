from django.db import models
from tienda.models import Cliente
from ordenes.models import Empleado, Servicio
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import Q

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
        ('confirmado', 'Confirmado'),
        ('atendido', 'Atendido'),
        ('cancelado', 'Cancelado'),
    ]

        # opciones de horarios
    HORARIOS = (
        (0, '09:00'),
        (1, '09:30'),
        (2, '10:00'),
        (3, '10:30'),
        (4, '11:00'),
        (5, '11:30'),
        (6, '12:00'),
        (7, '12:30'),
        (8, '13:00'),
        (9, '13:30'),
        (10, '14:00'),
        (11, '14:30'),
        (12, '15:00'),
        (13, '15:30'),
        (14, '16:00'),
        (15, '16:30'),
        (16, '17:00'),
        (17, '17:30'),
        (18, '18:00'),
        (19, '18:30'),
        (20, '19:00'),
        (21, '19:30'),
        (22, '20:00'),

    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario_inicio = models.IntegerField(choices=HORARIOS)
    horario_fin = models.IntegerField(choices=HORARIOS, null=True, blank=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='confirmado')

    def __str__(self):
        return self.empleado.usuario.first_name + " " + self.empleado.usuario.last_name + "--->" + self.cliente.nombre.first_name + "----->" + str(self.fecha) + " de " + str(self.get_horario_inicio_display()) + " a " + str(self.get_horario_fin_display())
    
    
    def clean(self):
        if self.horario_fin is not None and self.horario_inicio >= self.horario_fin:
            raise ValidationError('El horario de finalizacion del turno debe ser posterior al horario de inicio.')
        
        # Chequeo si el turno se superpone con otro
        turnos_superpuestos = Turno.objects.filter(
            Q(empleado=self.empleado),
            Q(estado = "confirmado"),
            Q(fecha=self.fecha),
            (
                Q(horario_inicio__gte=self.horario_inicio, horario_inicio__lt=self.horario_fin) |
                Q(horario_fin__gt=self.horario_inicio, horario_fin__lte=self.horario_fin) |
                Q(horario_inicio__lte=self.horario_inicio, horario_fin__gte=self.horario_fin)
            )
        ).exclude(pk=self.pk)
        print(turnos_superpuestos)

        if turnos_superpuestos.exists():
            # raise ValidationError('El horario del turno se superpone con el horario de otro turno.')
            for turno in turnos_superpuestos:   
                raise ValidationError(
                    'El turno se superpone con el turno del cliente: %s' % 
                    turno.cliente + " de " + str(turno.get_horario_inicio_display()) + " a " + str(turno.get_horario_fin_display()), code="invalid"
                )           

        # if overlapping_appointments.exists():
        #     request = None
        #     try:
        #         from django.test import RequestFactory
        #         request = RequestFactory().get('/')
        #     except Exception:
        #         pass
            
        #     print(request)
        #     if request:
        #         print("Entre en el IF")
        #         message = f"El turno se superpone con otro turno ya agendado. ¿Desea continuar? (Si/No)"
        #         print(message)
        #         response = messages.warning(request, message, extra_tags='safe', fail_silently=True)
        #         if response == 'No':
        #             raise ValidationError('El turno no fue agendado.')
        #     else:
        #         raise ValidationError('El turno se superpone con otro turno ya agendado.')

    # def clean(self, request):
    #     super().clean()

    #     turnos = Turno.objects.filter(
    #         empleado=self.empleado,
    #         fecha=self.fecha,
    #         estado='confirmado'
    #     ).exclude(pk=self.pk)

    #     for turno in turnos:
    #         if self.hora_inicio < turno.hora_fin and self.hora_fin > turno.hora_inicio:
    #             # Se superpone con otro turno ya agendado
    #             message = 'El turno se superpone con otro ya agendado. ¿Desea continuar de todas maneras?'
    #             extra_tags = 'turno_superpuesto'
    #             confirm_url = f'{request.path}confirm/'
    #             cancel_url = f'{request.path}cancel/'
    #             messages.warning(request, message, extra_tags=extra_tags, 
    #                                 fail_silently=True, 
    #                                 extra={'confirm_url': confirm_url, 'cancel_url': cancel_url})
    #             return

    #     # No se superpone con ningún otro turno ya agendado
    #     self.estado = 'confirmado'

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)