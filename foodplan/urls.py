from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from recipeapp.views import (
    recipe_view,
    index_view,
    order_view,
    all_recipes_view,
    day_menu_view,
    cheap_recipes_view,
    liked_recipes_view
)


Dish = apps.get_model('recipeapp', 'Dish')
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('recipe/<int:recipe_id>', recipe_view, name='recipe'),
    path('recipe/', recipe_view, {'recipe_id': Dish.objects.first().id}, name='recipe_default'),  
    path('', index_view, name='index'),
    path('order/', order_view, name='order'),
    path('all_recipes/', all_recipes_view, name='all_recipes'),
    path('cheap_recipes/', cheap_recipes_view, name='cheap_recipes'),
    path('liked_recipes/', liked_recipes_view, name='liked_recipes'),
    path('day_menu/', day_menu_view, name='day_menu'),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('content_manager.urls', 'content_manager'), namespace='content_manager')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
