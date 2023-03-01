from django.shortcuts import render
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
    posts = Post.objects.all()
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    comentarios = Comentario.objects.all()
    context = {
        'posts': posts,
        'autores': autores,
        'categorias': categorias,
        'tags': tags,
        'comentarios': comentarios
    }
    return render(request, 'blog/posts.html', context)

def index(request):
    return render(request, 'blog/index.html')



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
            return render(request,"blog/mensaje_enviado.html")
        else:
            print("El form no es valido")    
            return render(request,'blog/mensaje_no_enviado.html')

    else: # GET
        form = MensajeForm()
        params['form'] = form
        return render(request, 'blog/index.html', params)
