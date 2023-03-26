from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from tienda.models import Cliente
from ordenes.models import Empleado, Servicio
from .models import Turno




# Create your views here.
def turnero_index(request):
    return render(request, 'turnero/index.html')


# def lista_turnos(request):
#     turnos = Turno.objects.all()
#     return render(request, 'lista_turnos.html', {'turnos': turnos})

# class TurnoDeleteView(DeleteView):
#     model = Turno
#     template_name_suffix = '_confirm_delete'
#     success_url = reverse_lazy('lista_turnos')

# class TurnoUpdateView(UpdateView):
#     model = Turno
#     fields = ['cliente', 'empleado', 'fecha', 'horario', 'servicio', 'estado']
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('lista_turnos')


# def turnos_empleado(request, empleado_id):
#     empleado = Empleado.objects.get(pk=empleado_id)
#     turnos = Turno.objects.filter(empleado=empleado)
#     context = {'turnos': turnos, 'empleado': empleado}
#     return render(request, 'turnero/turnos_empleado.html', context)

# def turnos_empleado_fecha(request, empleado_id):
#     empleado = Empleado.objects.get(pk=empleado_id)
#     fecha_str = request.GET.get('fecha')
#     fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
#     turnos = Turno.objects.filter(empleado=empleado, fecha=fecha)
#     context = {'turnos': turnos, 'empleado': empleado, 'fecha': fecha}
#     return render(request, 'turnero/turnos_empleado_fecha.html', context)


# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Turno

# def turnero_empleado(request, empleado_id):
#     empleado = Empleado.objects.get(id=empleado_id)
#     turnos = Turno.objects.filter(empleado=empleado)

#     eventos = []
#     for turno in turnos:
#         evento = {
#             'title': turno.servicio.nombre,
#             'start': turno.fecha.strftime('%Y-%m-%dT') + turno.horario[1:6],
#             'end': turno.fecha.strftime('%Y-%m-%dT') + turno.horario[9:14],
#             'url': '/turnos/' + str(turno.id),
#         }
#         eventos.append(evento)

#     return JsonResponse(eventos, safe=False)

def turnero_empleado(request, empleado_id):
    # Obtendo la lista de empleados que tienen un turno asignado
    empleados = Empleado.objects.filter(turno__isnull=False).distinct()

    # Obtener los turnos del empleado pasado por parametro
    turnos = Turno.objects.filter(empleado__id=empleado_id)

    # Pasar los turnos al contexto para su uso en el template
    context = {
        'turnos': turnos,
        'empleados': empleados,
    }
    return render(request, 'turnero/turnero_empleado.html', context)

def turnero(request):
    # Obtener los turnos del empleado
    empleados = Empleado.objects.all()
    # print(empleados)
    turnos = Turno.objects.all()

    # Pasar los turnos al contexto para su uso en el template
    context = {
        'turnos': turnos,
        'empleados': empleados,
    }
    print(context)
    return render(request, 'turnero/turnero_empleado.html', context)