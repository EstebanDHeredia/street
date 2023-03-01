from django.urls import path
from turnero import views

urlpatterns = [
    path('', views.turnero_index, name='turnero_index'),
]