from django.urls import path
from tienda import views
from tienda.views import Carrito

urlpatterns = [
    path('', views.tienda_index, name='tienda_index'),
    path('producto/', views.tienda_producto, name='tienda_producto'),
    # path('carrito/', views.carrito, name='carrito'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('carrito/', Carrito.as_view(), name="carrito"),
]
