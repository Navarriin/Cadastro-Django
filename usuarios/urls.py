from django.urls import path
from . import views

app_name='usuarios'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastros/', views.cadastros, name='cadastros'),
]