from django.contrib import admin
from django.urls import path
from .views import register, auth_view, lk_view



urlpatterns = [
    path('lk/', lk_view, name='auth'),
    path('registration/', register, name='registration'),
    path('auth/', auth_view, name='auth')
]