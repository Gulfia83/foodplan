from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme

from foodplan import settings
from recipeapp.models import Ingredient, Dish, RecipeItem


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    extra = 5


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'units', 'price')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    inlines = [RecipeItemInline]

    def response_post_save_change(self, request, obj):
        res = super().response_post_save_change(request, obj)
        next_url = request.GET.get('next')

        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts=settings.ALLOWED_HOSTS):
            return HttpResponseRedirect(next_url)
        else:
            return res