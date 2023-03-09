from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models

class Categoria(models.Model):
    """
    Clase que representa a una categoría de productos.
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    """
    Clase que representa un proveedor de productos
    """
    nombre_empresa = models.CharField(max_length=200)
    nombre_representante = models.CharField(max_length=200)
    tel_representante = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_empresa


class Producto(models.Model):
    """
    Clase que representa a un producto.
    """
    ESTADO = [
        ('activo', 'activo'),
        ('pausado', 'pausado'),
        ('eliminado', "eliminado")
    ]

    estado = models.CharField(max_length=255, choices=ESTADO, default="activo")
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='tienda/productos/images/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    stock_min = models.PositiveIntegerField(null=True, blank=True, verbose_name="Stock mínimo")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    en_oferta = models.BooleanField(default=False)
    porc_descuento = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    """
    Clase que representa a un cliente de la tienda.

    Atributos:
    - nombre (User): usuario relacionado con el cliente.
    - direccion (str): dirección del cliente.
    - telefono (str): número de teléfono del cliente.
    - dni (int): DNI del cliente.
    - foto (ImageField): imagen del cliente.
    - fecha_creacion (date): fecha de creación del cliente.

    """
    nombre = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.IntegerField()
    foto = models.ImageField(upload_to='tienda/cliente/images/', null=True, blank=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre.first_name + " " + self.nombre.last_name

class Pedido(models.Model):
    """
    Clase que representa a un pedido realizado por un cliente.
    """
    PENDIENTE_ENVIO = 'Pendiente de envío'
    EN_PREPARACION = 'Pedido en preparación'
    ACEPTADO = 'Pedido aceptado'
    ENVIADO = 'Enviado'
    COMPLETADO = 'Completado'
    CANCELADO = 'Cancelado'
    ESTADOS_CHOICES = [
        (PENDIENTE_ENVIO, 'Pendiente de envío'),
        (EN_PREPARACION, 'Pedido en preparación'),
        (ACEPTADO, 'Pedido aceptado'),
        (ENVIADO, 'Enviado'),
        (COMPLETADO, 'Completado'),
        (CANCELADO, 'Cancelado'),
    ]
    estado = models.CharField(max_length=50, choices=ESTADOS_CHOICES, default=ACEPTADO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # productos = models.ForeignObject(ProductoPedido)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion_envio = models.TextField()
    fecha_envio = models.DateTimeField(null=True, blank=True)
    cod_seguimiento = models.CharField(max_length=50, null=True, blank=True)
    monto_total = models.DecimalField(max_digits=6, decimal_places=2)

class ProductoPedido(models.Model):
    """
    Clase que representa los productos que contiene un pedido
    junto con la cantidad de los mismo y el costo al momento de
    hacer la compra
    """
    nombreProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

