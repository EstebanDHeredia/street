import json
from django.http import HttpResponse
from tienda.models import Producto

def agregar_producto(request, *args, **kwargs):
    if request.method == "GET":
        idproducto = request.GET.get("producto_id")
        valor_actual = request.GET.get("valor_actual")
        valor_a_agregar = request.GET.get("valor_a_agregar")
        carro = request.session.get("carrito")
        idproducto_rec = idproducto[16:] #obtengo el id del producto recortando "street_producto_"
        idproducto_rec = int(idproducto_rec)
        producto = Producto.objects.get(id=idproducto_rec) #obtengo el producto de la BD
        print("stock actual en BD", producto.stock, "del producto", producto.nombre)
        stock_actual = int(producto.stock)

        if int(valor_actual)+int(valor_a_agregar) > stock_actual:
            print("supero el valor en stock, no se puede agregar mas productos")
            cantidad = int(valor_actual)
        else:
            cantidad = int(valor_actual) + int(valor_a_agregar)
        
        '''
        ACTUALIZO VARIABLE DE SESION
        '''

        carro[idproducto] = cantidad
        request.session["carrito"] = carro

        '''
        FIN
        '''

        print("id del producto:", idproducto)
        print("cantidad actual en el carro:", valor_actual)
        print("nueva cantidad cantidad en el carro:", cantidad)
        print("carro (variable de session):", carro)
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantidad"] = str(cantidad)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)