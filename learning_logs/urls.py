from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('entry/', views.entry, name='Entry'),
    path('user/', views.user, name='User Profile'),
    path('topic/', views.topic, name='Topics'),
]   
