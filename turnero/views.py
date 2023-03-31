from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from tienda.models import Cliente
from ordenes.models import Empleado, Servicio
from .models import Turno
from django.http import Http404
from django.views.generic import View
from django.http import JsonResponse


def turnero_empleado_ajax(request, *args, **kwargs):
    print("INGRESE A LA FUNCION AJAX")
    if request.method == 'GET':
        empleado = request.GET.get('empleado_id')
        turnos = Turno.objects.filter(empleado=empleado)
        print(turnos)
        # return render(request, 'turnero/seleccionar_empleado.html', {'turnos': turnos})

    eventos = []
    for turno in turnos:
        evento = {
            'id': turno.id,
            'title': turno.servicio.nombre,
            'cliente': turno.cliente.nombre.first_name,
            'start': turno.fecha.strftime('%Y-%m-%dT') + str(turno.get_horario_inicio_display()),
            'end': turno.fecha.strftime('%Y-%m-%dT') + str(turno.get_horario_fin_display()),
            'estado': turno.estado,
            'descripcion': turno.servicio.descripcion,

            # 'url': '/turnos/' + str(turno.id),
        }
        eventos.append(evento)

    return JsonResponse(eventos, safe=False)

class seleccionar_empleado(View):
    template = "turnero/seleccionar_empleado.html"

    def get(self, request):
        params = {}
        try:
            empleados = Empleado.objects.all()
        except Empleado.DoesNotExist:
            raise Http404
        params["empleados"] = empleados
        
        return render(request, self.template, params)