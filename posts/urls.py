from django.urls import path
from posts import views


urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('acerca/', views.acerca, name='acerca'),
]
