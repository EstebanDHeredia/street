from django.urls import path
from blog import views
from blog.views import Mensaje
from blog.views import enviar_mensaje

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_post', views.lista_post, name='lista_post'),
    path('enviar_mensaje', views.enviar_mensaje, name="enviar_mensaje")
]