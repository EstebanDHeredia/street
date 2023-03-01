from django.contrib import admin
from ordenes.models import Empleado, Orden, Servicio, ServicioxOrden
from django.utils.html import format_html

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Orden)
admin.site.register(Servicio)
admin.site.register(ServicioxOrden)