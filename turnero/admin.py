from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Turno
from django.utils.html import format_html
from django.contrib import messages
from django.utils.translation import ngettext
from django.http import HttpResponseRedirect

class TurnoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'cliente', 'fecha', 'horario_inicio', 'horario_fin', 'servicio', 'estadoTurno')
    list_filter = ('estado', 'empleado', 'fecha', 'servicio')
    search_fields = ('cliente__nombre', 'empleado__usuario__first_name', 'empleado__usuario__last_name')
    actions = ['marcar_atendido', 'marcar_cancelado', 'marcar_confirmado', 'ver_calendario']

    @admin.display(description="Estado")
    def estadoTurno(self, obj):
        if obj.estado == 'confirmado':
            return format_html('<span style="background-color: blue; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'cancelado':
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'atendido':
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.estado,)

    @admin.action(description='Marcar los turnos como Atendidos')
    def marcar_atendido(self, request, queryset):
        actualizados = queryset.update(estado='atendido')
        self.message_user(request, ngettext(
            '%d turno actualizado como Atendido.',
            '%d turnos actualizados como Atendido.',
            actualizados,
        ) % actualizados, messages.SUCCESS)

    @admin.action(description='Marcar los turnos como Cancelados')
    def marcar_cancelado(self, request, queryset):
        actualizados = queryset.update(estado='cancelado')
        self.message_user(request, ngettext(
            '%d turno actualizado como Cancelado.',
            '%d turnos actualizados como Cancelado.',
            actualizados,
        ) % actualizados, messages.SUCCESS)

    @admin.action(description='Marcar los turnos como Confirmados')
    def marcar_confirmado(self, request, queryset):
        actualizados = queryset.update(estado='confirmado')
        self.message_user(request, ngettext(
            '%d turno actualizado como Confirmado.',
            '%d turnos actualizados como Confirmado.',
            actualizados,
        ) % actualizados, messages.SUCCESS)
        
    @admin.action(description='Ver Calendario')
    def ver_calendario():
        return HttpResponseRedirect('/turnero/turnero/')

admin.site.register(Turno, TurnoAdmin)
