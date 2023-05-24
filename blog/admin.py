from django.contrib import admin
from blog.models import Autor, Categoria,Comentario,Post,Tag
from blog.models import Mensaje, Respuesta
from django.utils.html import format_html

# Register your models here.
class PostInline(admin.TabularInline):
    model = Post
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [PostInline]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['contenido', 'autor', 'publicado_en', 'imagen_post']

    @admin.display(description="Imagen del Post")
    def imagen_post(self, obj): 
        '''
        ESTA FUNCION ME PERMITE MOSTRAR LA IMAGEN DEL POST EN EL PANEL DE ADMIN
        '''
        return format_html('<img src="http://127.0.0.1:8000/media/{}" style="width:10%;"/>', obj.post.imagen,)


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Descripción", {"fields": ["titulo", "resumen", "cuerpo", "autor", "creado_en", "slug"]}),
        ("Publicacion", {"fields": ["publicado_en", "estado"]}),
        ("Imagen / Categoria", {"fields": ["imagen", "categoria", "etiquetas"]}),
    ]
    list_display = ['titulo', 'autor', 'creado_en', "estadoPost", "imagen_post"]
    ordering = ['creado_en'] 
    list_filter = ('creado_en', 'estado', 'autor', 'categoria', 'publicado_en')
    search_fields = ('titulo', ) 
    list_display_links = ('titulo', 'imagen_post') 
    
    # @admin.display(description='Nombre-Estado') # Me permite agregar una columna customizada a la lista de productos
    # def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.producto, obj.estado)).upper()
    
    @admin.display(description="Estado")
    def estadoPost(self, obj): # ESTA FUNCION ME PERMITE DARLE UN FORMATO AL CAMPO ESTADO DE ACUERDO AL SI ESTA RETIRADO, PUBLICADO O BORRADOR EN LA LISTA DE PRODUCTOS DEL ADMIN
        if obj.estado == 'publicado':
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'borrador':
            return format_html('<span style="background-color: yellow; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'eliminado':
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.estado,)

    @admin.display(description="Imagen")
    def imagen_post(self, obj): 
        '''
        ESTA FUNCION ME PERMITE MOSTRAR LA IMAGEN DEL POST EN EL PANEL DE ADMIN
        '''
        return format_html('<img src="http://127.0.0.1:8000/media/{}" style="width:10%;"/>', obj.imagen,)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['autor','direccion_web','email']

    @admin.display(description="E-mail")
    def email(self, obj):
        '''
        funcion que devuelve el email del autor
        '''
        return obj.autor.email

class MensajeInline(admin.TabularInline):
    model = Respuesta
    extra = 0


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):

    inlines = [MensajeInline]

    list_display = ['email','fecha','asunto','estadoMensaje']
    ordering = ['fecha',] 
    list_filter = ('fecha', 'estado_mensaje', 'email')
    search_fields = ('asunto', ) 
    list_display_links = ('email', 'fecha', 'asunto', 'estadoMensaje') 

    @admin.display(description="Estado")
    def estadoMensaje(self, obj): 
        if obj.estado_mensaje == 'Contestada':
            return format_html('<span style="background-color: green; color: black; padding:7px;">{}</span>', obj.estado_mensaje,)
        if obj.estado_mensaje == 'No Contestada':
            return format_html('<span style="background-color: red; color: black; padding:7px;">{}</span>', obj.estado_mensaje,)
        if obj.estado_mensaje == 'En Proceso':
            return format_html('<span style="background-color: lightblue; color: black; padding:7px;">{}</span>', obj.estado_mensaje,)


admin.site.register(Categoria,CategoriaAdmin)
# admin.site.register(Autor)
# admin.site.register(Comentario)
admin.site.register(Tag)
# admin.site.register(Mensaje)
admin.site.register(Respuesta)