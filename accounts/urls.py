from django.contrib import admin
from django.urls import path
from .views import register, auth_view, lk_view, upload_avatar



urlpatterns = [
    path('lk/', lk_view, name='lk'),
    path('registration/', register, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('upload-avatar/', upload_avatar, name='upload_avatar'),
]