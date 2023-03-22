from django.urls import path
from turnero import views

urlpatterns = [
    # path('turnos/', lista_turnos, name='lista_turnos'),
    # path('turnos/nuevo/', TurnoCreateView.as_view(), name='nuevo_turno'),
    # path('turnos/<int:pk>/editar/', TurnoUpdateView.as_view(), name='editar_turno'),
    # path('turnos/<int:pk>/eliminar/', TurnoDeleteView.as_view(), name='eliminar_turno'),    
    path('turnero/<int:empleado_id>/', views.turnero_empleado, name='turnero_empleado'),
    # path('turnero/<int:empleado_id>/<int:year>/<int:month>/<int:day>/', views.turnos_empleado_fecha, name='turnos_empleado_fecha'),
]