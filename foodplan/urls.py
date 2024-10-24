from django.contrib import admin
from django.urls import include, path
from .views import (
    card1_view,
    card2_view,
    card3_view,
    index_view,
    order_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('card1/', card1_view, name='card1'),
    path('card2/', card2_view, name='card2'),
    path('card3/', card3_view, name='card3'),
    path('', index_view, name='index'),
    path('order/', order_view, name='order'),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
]
