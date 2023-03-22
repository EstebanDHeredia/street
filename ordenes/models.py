from django.db import models
from django.contrib.auth.models import User
from tienda.models import Cliente, Producto

# Create your models here.
class Empleado(models.Model):
    """
    Un modelo que representa a un empleado
    
    Atributos:
        telefono (str): Número de teléfono del empleado.
        direccion (str): Dirección del empleado.
        fecha_contratacion (datetime.date): Fecha en la que el empleado fue contratado.
        rol (choices): Rol del empleado en la peluquería.
        fecha_nac (datetime.date, opcional): Fecha de nacimiento del empleado.
        fecha_contratacion (datetime.date, opcional): Fecha de contratacion del empleado.
        contacto_emergencia (str, opcional): Nombre de contacto de emergencia para el empleado.
        tel_emergencia (str, opcional): Número de teléfono de contacto de emergencia para el empleado.
        valor_hora (decimal.Decimal): Valor de hora del empleado.

    """
    ROL = [
        ('peluquero', 'Peluquero'),
        ('recepcionista', 'Recepcionista'),
        ('colorista', "Colorista"),
        ('asistente', "Asistente")
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    fecha_contratacion = models.DateField()
    rol = models.CharField(max_length=255, choices=ROL, blank=True)
    fecha_nac = models.DateField(blank=True)
    contacto_emergencia = models.CharField(max_length=200, blank=True)
    tel_emergencia = models.CharField(max_length=20, blank=True)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.usuario.first_name + " " + self.usuario.last_name

class Servicio(models.Model):
    """
    Un modelo que representa un servicio prestado por la peluqueria

    Atributos:
        nombre (str): Nombre del servicio.
        direccion (str): Dirección del empleado.
        precio(decimal.Decimal): Costo del servicio.
        comisiona(boolean): indica si el servicio comisiona al empleado.
    """

    nombre = models.CharField(max_length=200, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    comisiona = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre

class Orden(models.Model):
    """
    Un modelo que representa una orden de trabajo realizada a algun cliente.
    
    Atributos:
        cliente (obj.Cliente): cliente al que se le prestó el servicio.
        fecha (datetime.date): fecha en la que se realizó el servicio.
    """

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()

class ServicioxOrden(models.Model):
    """
    un modelo que representa los servicio que contiene una orden de trabajo.
    
    Atributos:
        orden (obj.Orden): orden en la que se prestó el servicio
        empleado (obj.Empleado): empleado que realizó el servicio
        precio(decimal.Decimal): Costo del servicio.
        producto(Producto): indica el producto que se vendió si el servicio fue una venta
        cantidad_prod(int): indica la cantidad vendida del producto
    """
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    cant_prod = models.IntegerField(null=True, blank=True)


