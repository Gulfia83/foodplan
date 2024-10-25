from django.urls import path

from .views import create_dish_drf, create_dish_form


app_name = 'content_manager'

urlpatterns = [
    path('create_dish_drf/', create_dish_drf, name='create_dish_drf'),
    path('create_dish_form/', create_dish_form, name='create_dish_form')
]