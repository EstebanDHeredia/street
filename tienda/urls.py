from django.urls import path
from tienda import views

urlpatterns = [
    path('', views.tienda_index, name='tienda_index'),
    path('producto/', views.tienda_producto, name='tienda_producto'),
    path('carrito/', views.carrito, name='carrito'),
]
