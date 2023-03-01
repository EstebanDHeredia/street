from django.contrib import admin
from galeria.models import Imagen, TagImagen
from django.utils.html import format_html

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    # fields = ['categoria', 'fecha_publicacion', 'producto', 'imagen']
    fieldsets = [ # GRUPOS Y ORDEN EN QUE SE MOSTRARAN LOS CAMPOS DE 'IMAGEN' AL AGREGAR/MODIFICAR ALGUNA
        ("Descripción", {"fields": ["titulo","cuerpo","creado_en"]}),
        ("Imagen", {"fields": ["imagen", "imagen_destacada"]}),
        ("Estado", {"fields": ["estado", "publicado_en"]}),
        ("Etiquetas", {"fields": ["etiquetas"]}),
    ]
    list_display = ['titulo', 'estadoImagen','imagen_destacada', 'foto', 'publicado_en'] #LISTADO DE CAMPOS A MOSTRAR EN LA PANTALLA DE LISTADO DE IMAGENES
    ordering = ['-publicado_en']  # '-' SIGNIFICA ASCENDENTE
    list_filter = ('estado', 'etiquetas', 'imagen_destacada') # LISTADO DE CAMPOS POR LOS CUALES PUEDO FILTRAR EL LISTADO DE IMAGENES
    search_fields = ('titulo', 'cuerpo', 'creado_en', 'publicado_en', 'estado') # CAMPOS POR LOS CUALES VOY A PODER BUSCAR UNA IMAGEN EN EL LISTADO DE IMAGENES
    list_display_links = ('titulo', 'foto') # CAMPOS QUE ME VAN A SER LINK PARA SELECCIONAR UN PRODUCTO DE LA LISTA DE PRODUCTO
    
    # @admin.display(description='Nombre-Estado') # Me permite agregar una columna customizada a la lista de imagenes
    # def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.producto, obj.estado)).upper()
    
    @admin.display(description="Estado")
    def estadoImagen(self, obj): # ESTA FUNCION ME PERMITE DARLE UN FORMATO AL CAMPO ESTADO EN LA LISTA DE IMAGENES DEL ADMIN
        if obj.estado == 'publicar':
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'no_publicar':
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.estado,)

    @admin.display(description="Imagen")
    def foto(self, obj): 
        '''
        ESTA FUNCION ME PERMITE MOSTRAR LA IMAGEN EN EL PANEL DE ADMIN
        '''
        return format_html('<img src="http://127.0.0.1:8000/media/{}" style="width:10%;"/>', obj.imagen,)

admin.site.register(TagImagen)


