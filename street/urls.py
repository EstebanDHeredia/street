"""Street URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include(('blog.urls', "blog"), namespace="blog")),
    # path('', include('blog.urls')),
    path('galeria/', include('galeria.urls')),
    path('tienda/', include('tienda.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),#Registration Redux
    path('captcha/', include('captcha.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('turnero/', include('turnero.urls')),
    path('ordenes/', include('ordenes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)