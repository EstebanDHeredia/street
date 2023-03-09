from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


from .models import Producto

# Create your views here.


# def tienda_index(request):
#     return render(request, 'tienda/index.html')


def tienda_producto(request):
    return render(request, 'tienda/producto.html')


# def carrito(request):
#     return render(request, 'tienda/cart.html')

######################################################
####   TIENDA INDEX ORIGINAL QUE FUNCIONA BIEN    ####
####   IMPLEMENTACION OK ANTES DE INCORPORAR EL   ####
####   CARRITO                                    ####
######################################################
# def tienda_index(request):

#     lista_productos = Producto.objects.filter(estado='activo')
#     # especifica que quiero mostrar 8 productos por página
#     paginator = Paginator(lista_productos, 8)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     for producto in page_obj:
#         producto.precio_con_descuento = producto.precio - (producto.precio * producto.porc_descuento / 100)
#     context = {'page_obj': page_obj}
#     return render(request, 'tienda/lista_productos.html', context)

# def producto_detalle(request, pk):
#     producto = get_object_or_404(Producto, pk=pk)
#     producto.precio_con_descuento = producto.precio - (producto.precio * producto.porc_descuento / 100)
#     return render(request, 'tienda/producto.html', {'producto': producto})



######################################################
####   TIENDA INDEX MODIFICADA AGREGANDO LA       ####
####   IMPLEMENTACION DEL CARRITO DE COMPRAS      ####
######################################################
def tienda_index(request):

    lista_productos = Producto.objects.filter(estado='activo')
    # especifica que quiero mostrar 8 productos por página
    paginator = Paginator(lista_productos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for producto in page_obj:
        producto.precio_con_descuento = producto.precio - (producto.precio * producto.porc_descuento / 100)
    context = {'page_obj': page_obj}

    '''
    para inicializar la variable de session carro
    '''
    try:
        request.session["carrito"]
        print("Carro en este momento: ", request.session["carrito"])
    except:
        request.session["carrito"] = {}
        print("Carro inexistente, se inicializa nuevo carro")

    return render(request, 'tienda/lista_productos.html', context)


class Carrito(View):
    template = "tienda/localstorage.html"

    def get(self, request):
        params = {}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        '''
        para inicializar la variable de session carro
        '''
        try:
            request.session["carro"]
            print("Carro en este momento: ", request.session["carro"])
        except:
            request.session["carro"] = {}
            print("Carro inexistente, se inicializa nuevo carro")
        
        return render(request, self.template, params)