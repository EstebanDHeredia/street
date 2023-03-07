from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    """
    Un modelo de datos que representa a un autor.
    El autor puede ser el autor de un Post o de un Comentario
    
    Atributos:
        - nombre: El nombre del autor.
        - biografia: La biografía del autor.
        - direccion_web: La dirección de website del autor.
    """
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    biografia = models.TextField()
    direccion_web = models.URLField()

    def __str__(self):
        return self.autor.first_name + " " + self.autor.last_name

class Categoria(models.Model):
    """
    Un modelo de datos que representa a una categoría de una publicación de blog.
    
    Atributos:
        - nombre: El nombre de la categoría.
        - descripcion: La descripción de la categoría.
    """
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre

class Tag(models.Model):
    """
    Un modelo de datos que representa a una etiqueta de una publicación de blog.
    
    Atributos:
        - nombre: El nombre de la etiqueta.
    """
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    """
    Un modelo de datos que representa a una publicación de blog.
    
    Atributos:
        - titulo: El título de la publicación.
        - cuerpo: El contenido de la publicación.
        - creado_en: La fecha y hora en que la publicación fue creada.
        - publicado_en: La fecha y hora en que la publicación fue publicada.
        - estado: El estado de la publicación ("publicado" o "borrador").
        - slug: El slug de la publicación.
        - autor: El autor de la publicación.
        - categoria: La categoría de la publicación.
        - imagen_destacada: La imagen destacada de la publicación.
        - etiquetas: Las etiquetas de la publicación.
    """
    ESTADO = [
        ('publicado', 'Publicado'),
        ('borrador', 'Borrador'),
        ('eliminado', "Eliminado")
    ]
    titulo = models.CharField(max_length=100)
    resumen = models.CharField(max_length=255)
    cuerpo = models.TextField()
    creado_en = models.DateTimeField()
    publicado_en = models.DateTimeField()
    estado = models.CharField(max_length=255, choices=ESTADO)
    slug = models.SlugField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='blog/images')
    etiquetas = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.titulo

class Comentario(models.Model):
    """
    La clase Comentario representa los comentarios de una publicación de blog.

    Atributos:
        contenido (str): El contenido del comentario.
        publicado_en (datetime): La fecha y hora en que se publicó el comentario.
        autor (User): El usuario que publicó el comentario.
    """

    contenido = models.TextField()
    publicado_en = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.contenido

class Mensaje(models.Model):

    CONTESTADA = "Contestada"
    NOCONTESTADA = "No Contestada"
    ENPROCESO = "En Proceso"
    ESTADOS = (
        (CONTESTADA, "Contestada"),
        (NOCONTESTADA, "No Contestada"),
        (ENPROCESO, "En Proceso")
    )

    nombre = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    asunto = models.CharField(max_length=200, blank=False, null=False)
    mensaje = models.TextField(blank=False, null=False)
    estado_mensaje = models.CharField(max_length=15, blank=True, null=True, choices=ESTADOS, default=NOCONTESTADA)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

class Respuesta(models.Model):

    mensaje = models.ForeignKey(Mensaje, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

    def create_mensaje(self):
        mensaje_cambio_estado = Mensaje.objects.get(id=self.mensaje.id)
        mensaje_cambio_estado.estado_mensaje = "Contestada"    
        mensaje_cambio_estado.save()
        # Acá agregar la   lógica para el envío de un mail con la respuesta

    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super (Respuesta, self).save(force_update=force_update)