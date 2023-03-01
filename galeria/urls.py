from django.urls import path
from galeria import views

urlpatterns = [
    path('galeria/', views.lista_imagenes, name='galeria'),
    path('servicios/', views.servicios, name='servicios'),
]