from django.contrib import admin

from .models import Ingredient, Recipe, RecipeItem, DishCategory


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    extra = 5


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('dish',)
    list_display = ('dish',)
    raw_id_fields = ('ingredients',)
    