'''Схемы url для приложения learning_app'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index')
]





