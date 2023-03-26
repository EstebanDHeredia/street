from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TagImagen(models.Model):
    """
    Un modelo de datos que representa a una etiqueta de una imagen.

    Atributos:
        - nombre: El nombre de la etiqueta.
    """

    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Imagen(models.Model):
    """
    Un modelo de datos que representa a una imagen.

    Atributos:
        - titulo: El título de la imagen.
        - cuerpo: breve descripcion de la imagen.
        - creado_en: La fecha y hora en que la imagen fue creada.
        - publicado_en: La fecha y hora en que la imagen fue publicada.
        - estado: El estado de la publicación de la imagen ("publicado" o "borrador").
        - imagen_destacada: Si es una imagen destacada.
        - etiquetas: Las etiquetas de la imagen.
        - imagen: fotografia.
    """
    ESTADO = [
        ('publicar', 'Publicar'),
        ('no_publicar', 'No Publicar'),
    ]
    titulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=50)
    creado_en = models.DateTimeField()
    estado = models.CharField(max_length=255, choices=ESTADO, default='publicar')
    publicado_en = models.DateTimeField()
    imagen = models.ImageField(upload_to="galeria/images")
    imagen_destacada = models.BooleanField(default=False)
    etiquetas = models.ManyToManyField(TagImagen)

    def __str__(self) -> str:
        return self.titulo
    
    # modifico el save para asegurarme que todas las imagenes tengan la misma relacion de aspecto
    def save(self, *args, **kwargs):
    # Ajustar la proporción de aspecto de la imagen
        if self.imagen:
            image = Image.open(self.imagen)
            width, height = image.size
            aspect_ratio = width / height
            target_aspect_ratio = 1.5
            if aspect_ratio != target_aspect_ratio:
                new_width = int(height * target_aspect_ratio)
                image = image.resize((new_width, height))

                # Sobreescribe el archivo de imagen original con el nuevo archivo
                output = BytesIO()
                image.save(output, format='JPEG')
                output.seek(0)
                self.imagen = InMemoryUploadedFile(output, 'ImageField', f"{self.titulo}.jpg", 'image/jpeg', output.getbuffer().nbytes, None)

        super().save(*args, **kwargs)
