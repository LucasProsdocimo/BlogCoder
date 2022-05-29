from django.urls import path
from AppBlog import views


urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('sobreNosotros/', views.sobreNostros, name = 'sobreNosotros'),
    path('hacerPosteo/', views.hacerPosteo, name = 'hacerPosteo'),
    path('posteo/<titulo>', views.abrirPosteo, name='Posteo'),
    path('buscar/', views.buscar, name = 'Buscar'),
]