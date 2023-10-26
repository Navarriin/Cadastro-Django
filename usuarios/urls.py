from django.urls import path
from . import views

app_name='usuarios'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastros/', views.cadastros, name='cadastros'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/<int:usuarios_id>', views.deletar, name='deletar'),
    path('usuario/<int:usuario_id>', views.atualizar, name='atualizar'),
]