from django.urls import path
from usuarios import views

urlpatterns = [
    path('login/', views.login, name='login-view'),
]