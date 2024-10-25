from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from recipeapp.views import (
    recipe_view,
    index_view,
    order_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/<int:recipe_id>', recipe_view, name='recipe'),
    path('recipe/', recipe_view, {'recipe_id': 1}, name='recipe_default'),  
    path('', index_view, name='index'),
    path('order/', order_view, name='order'),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('content_manager.urls', 'content_manager'), namespace='content_manager')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
