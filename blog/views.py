from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import View
from django.views.generic import FormView
from .models import Post, Autor, Categoria, Tag, Comentario
from .models import Mensaje
from .forms import MensajeForm

# Create your views here.

def lista_post(request):

    params = {}

    # Busco la cantidad de post publicados eliminando el ultimo ya que este se muestra como blog principal
    post_list = Post.objects.filter(estado="publicado").order_by('-publicado_en')[1:]
    paginador = Paginator(post_list, 2) # Mostramos 2 post por pagina
    nro_pagina = request.GET.get('page')
    page_obj = paginador.get_page(nro_pagina) # Obtengo los post de esa pagína para pasarlos al template
    params["page_obj"] = page_obj

    # Busco el post Publicado mas reciente para enviarlo como Post Principal de la pagina
    post_principal = Post.objects.filter(estado="publicado").order_by('-publicado_en').first()
    params["post_principal"] = post_principal

    # Busco los otros dos post para poner en la pagina
    # post_secundarios = Post.objects.filter(estado="publicado").order_by('-publicado_en')[1:3]
    # params["post_secundarios"] = post_secundarios
    # print(params["post_secundarios"])

    return render(request, 'blog/posts.html', params)

def index(request):
    return render(request, 'blog/index.html')

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})



# class Mensaje(FormView):
#     template_name = "blog/index.html"
#     from_class = MensajeForm
#     success_url = "mensaje_enviado"

#     def form_valid(self, form):
#         form.save()
#         form.send_email()
#         return super().form_valid(form)

# class MensajeEnviado(View):
#     template = "blog/mensaje_enviado.html"

#     def get(self, request):
#         params = {}
#         params['mensaje'] = "Aqui va un mensaje"
#         return render(request, self.template, params)

def enviar_mensaje(request):
    params = {}

    print("entre al enviar_mensaje")
    if request.method == "POST":
        print("entre al POST")
        form = MensajeForm(request.POST) 
        params['form'] = form
        if form.is_valid(): #Controla que lo que trae el formulario sea valido, contrastado con lo que yo declaré en el modelo de datos
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']


            nuevo_mensaje = Mensaje(mensaje=mensaje, nombre=nombre, email=email, asunto=asunto)
            print("guardo el msj")
            nuevo_mensaje.save()

            # return redirect('blog:index')
            mensaje_enviado = True
            return render(request, 'blog/index.html', {'mensaje_enviado': mensaje_enviado})
            # return render(request,"blog/mensaje_enviado.html")
        else:
            print("El form no es valido")    
            return render(request,'blog/mensaje_no_enviado.html')

    else: # GET
        form = MensajeForm()
        params['form'] = form
        return render(request, 'blog/index.html', params)
