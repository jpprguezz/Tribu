from django.urls import path
from waves import views as wave_views

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo_list'),
    path('add/', views.add_echo, name='add_echo'),
    path('<int:pk>/', views.echo_detail, name='echo_detail'),
    path('<int:pk>/edit/', views.edit_echo, name='edit_echo'),
    path('<int:pk>/delete/', views.delete_echo, name='delete_echo'),
    path('<int:pk>/waves/', views.waves_echo, name='waves_echo'),
    path('<int:pk>/waves/add/', wave_views.add_wave, name='add_wave'),
]
