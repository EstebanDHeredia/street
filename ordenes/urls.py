from django.urls import path
from ordenes import views

urlpatterns = [
    path('', views.ordenes_index, name='ordenes_index'),
]