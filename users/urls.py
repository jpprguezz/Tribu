from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('@me/', views.user_logged, name='user_logged'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('<str:username>/echos/', views.user_echos, name='user_echos'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
]
