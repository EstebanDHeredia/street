from django.shortcuts import render

# Create your views here.
def tienda_index(request):
    return render(request, 'tienda/index.html')

def tienda_producto(request):
    return render(request, 'tienda/producto.html')

def carrito(request):
    return render(request, 'tienda/cart.html')