from django.contrib import admin
from django.urls import path
from .views import (
    auth_view,
    card1_view,
    card2_view,
    card3_view,
    index_view,
    order_view,
    registration_view
)


urlpatterns = [
    path('auth/', auth_view, name='auth'),
    path('card1/', card1_view, name='card1'),
    path('card2/', card2_view, name='card2'),
    path('card3/', card3_view, name='card3'),
    path('', index_view, name='index'),  # главная страница
    path('order/', order_view, name='order'),
    path('registration/', registration_view, name='registration'),
]
