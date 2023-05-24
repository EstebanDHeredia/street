from django.urls import path
from tienda import views
# from tienda.views import Carrito
from tienda import views_agregar 

urlpatterns = [
    path('', views.tienda_index, name='tienda_index'),
    path('producto/', views.tienda_producto, name='tienda_producto'),
    path('carrito/', views.carrito, name='carrito'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('checkout/', views.checkout, name='checkout'),
    path('agregar/', views_agregar.agregar_producto, name="agregar_producto"),

]
