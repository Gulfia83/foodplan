from django.contrib import admin

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
