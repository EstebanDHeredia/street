from django.shortcuts import render

# Create your views here.
def ordenes_index(request):
    return render(request, 'ordenes/index.html')