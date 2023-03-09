from django.contrib import admin
from tienda.models import Categoria, Cliente, Pedido, Producto, Proveedor
from django.utils.html import format_html

# Register your models here.


class PedidoInline(admin.TabularInline):
    model = Pedido
    extra = 0


class ClienteAdmin(admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ['nombreCliente', 'cantPedidos']

    @admin.display(description='Nombre')
    def nombreCliente(self, obj):
        return obj.nombre.first_name + " " + obj.nombre.last_name

    @admin.display(description="Cant. de pedidos")
    def cantPedidos(self, obj):
        pedidos = Pedido.objects.all().filter(cliente=obj)
        pedidos.count
        return pedidos.count()


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['fecha_creacion', 'cliente', 'estadoPedido', 'monto_total']
    ordering = ['fecha_creacion', 'estado']
    list_filter = ('estado', 'cliente', 'fecha_creacion')

    @admin.display(description="Estado Pedido")
    def estadoPedido(self, obj):
        if obj.estado == 'Pendiente de envío':
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'Pedido en preparación':
            return format_html('<span style="background-color: lightgreen; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'Enviado':
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == 'Completado':
            return format_html('<span style="background-color: white; padding:7px; color:black">{}</span>', obj.estado,)
        if obj.estado == 'Cancelado':
            return format_html('<span style="background-color: white; padding:7px;color:black">{}</span>', obj.estado,)
        if obj.estado == 'Pedido aceptado':
            return format_html('<span style="background-color: blue; padding:7px;">{}</span>', obj.estado,)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre_empresa",
                    "nombre_representante", "tel_representante"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Descripcion", {"fields": ['nombre', 'descripcion', 'imagen']}),
        ("Precio - Stock", {"fields": ['estado','precio', 'en_oferta', 'porc_descuento', 'stock', 'stock_min']}),
        ("Proveedor", {"fields": ["proveedor"]}),
        ("Categoría", {"fields": ["categoria"]}),
    ]
    list_display = ["nombre", "precio", "stockProducto",
                    "categoria", "proveedor", "imagenProducto","en_oferta", "porc_descuento", "estadoProducto"]
    ordering = ['nombre']
    list_filter = ['categoria', 'proveedor', 'nombre', 'fecha_creacion']
    search_fields = ['nombre', 'proveedor', 'categoria']
    list_display_links = ['nombre', 'imagenProducto']

    @admin.display(description="Stock")
    def stockProducto(self, obj):
        '''
        me devuelve en color rojo el stock del producto si es menor al stock minimo
        me devuelve en color amarillo el stock del producto si es igual al stock minimo
        me devuelve en color verde el stock del producto si es mayor al stock minimo

        '''
        if obj.stock == obj.stock_min:
            return format_html('<span style="background-color: yellow; color:black; padding:7px;">{}</span>', obj.stock,)
        if obj.stock < obj.stock_min:
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.stock,)
        if obj.stock > obj.stock_min:
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.stock,)

    @admin.display(description="Estado")
    def estadoProducto(self, obj):
        '''
        me devuelve en color rojo si el producto está "eliminado"
        me devuelve en color amarillo el producto está "pausado"
        me devuelve en color verde el producto está "activo"

        '''
        if obj.estado == "pausado":
            return format_html('<span style="background-color: yellow; color:black; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == "eliminado":
            return format_html('<span style="background-color: red; padding:7px;">{}</span>', obj.estado,)
        if obj.estado == "activo":
            return format_html('<span style="background-color: green; padding:7px;">{}</span>', obj.estado,)

    @admin.display(description="Imagen")
    def imagenProducto(self, obj):
        '''
        ESTA FUNCION ME PERMITE MOSTRAR LA IMAGEN DEL PRODUCTO EN EL PANEL DE ADMIN
        '''
        return format_html('<img src="http://127.0.0.1:8000/media/{}" style="width:10%;"/>', obj.imagen,)


# admin.site.register(Categoria,CategoriaAdmin)
# admin.site.register(Autor)
# # admin.site.register(Comentario)
# admin.site.register(Tag)


admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Pedido)
# admin.site.register(Producto)
# admin.site.register(Proveedor)
