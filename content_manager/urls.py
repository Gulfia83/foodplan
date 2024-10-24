from django.urls import path

from .views import create_dish


app_name = 'content_manager'

urlpatterns = [
    path('create_dish/', create_dish),
]