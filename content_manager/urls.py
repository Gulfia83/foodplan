from django.urls import path

from .views import create_dish_drf, create_dish_form, view_dishes, dish_edit


app_name = 'content_manager'

urlpatterns = [
    path('create_dish_drf/', create_dish_drf, name='create_dish_drf'),
    path('create_dish_form/', create_dish_form, name='create_dish_form'),
    path('dishes/', view_dishes, name='dishes'),
    path('dish/<int:pk>/edit/', dish_edit, name='dish_edit'),
]