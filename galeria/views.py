from django.shortcuts import render
from .models import Imagen, TagImagen

# Create your views here.
def lista_imagenes(request):
    imagenes_destacadas = Imagen.objects.filter(estado="publicar", imagen_destacada=True)
    imagenes = Imagen.objects.filter(estado="publicar")
    tags = TagImagen.objects.all()
    context = {
        'imagenes_destacadas': imagenes_destacadas,
        "imagenes": imagenes,
        'tags': tags,
    }
    return render(request, 'galeria/galeria.html', context)

def servicios(request):
    return render(request, 'galeria/servicios.html')
