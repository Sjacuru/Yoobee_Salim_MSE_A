from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/<str:name>/', views.welcome, name='welcome'),
]

