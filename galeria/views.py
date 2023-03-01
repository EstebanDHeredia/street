from django.shortcuts import render
from .models import Imagen, TagImagen

# Create your views here.
def lista_imagenes(request):
    imagen = Imagen.objects.all()
    tags = TagImagen.objects.all()
    context = {
        'image': imagen,
        'tags': tags,
    }
    return render(request, 'galeria/galeria.html', context)

def servicios(request):
    return render(request, 'galeria/servicios.html')
