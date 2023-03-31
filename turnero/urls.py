from django.urls import path
from turnero import views
from turnero.views import seleccionar_empleado 
from turnero.views import turnero_empleado_ajax

urlpatterns = [
    path('turnero/', seleccionar_empleado.as_view(), name="turnero"),
    path('turnero_empleado_ajax/',turnero_empleado_ajax, name='turnero_empleado_ajax'),
]