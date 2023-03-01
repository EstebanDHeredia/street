from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        params = {}
        params['nombre_usuario'] = request.user.username
        return render(request, 'usuarios/login.html', params)
    else:
        return render(request, 'usuarios/login.html', {})