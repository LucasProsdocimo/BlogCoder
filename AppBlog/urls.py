from django.urls import path
from AppBlog import views
from django.contrib.auth import views as auth_views

import AppBlog


urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('sobreNosotros/', views.sobreNostros, name = 'sobreNosotros'),
    path('hacerPosteo/', views.hacerPosteo, name = 'hacerPosteo'),
    path('posteo/<titulo>', views.abrirPosteo, name='Posteo'),
    path('buscar/', views.buscar, name = 'Buscar'),
    path('login/', auth_views.LoginView.as_view(template_name= AppBlog/login.html ), name='login'),

]