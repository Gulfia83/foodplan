from django.shortcuts import render, get_object_or_404

from recipeapp.models import Dish


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Dish, pk=recipe_id)
    recipe.total_price = 0
    for item in recipe.items.all():
        item_price = item.quantity * item.ingredient.price
        recipe.total_price += item_price

    return render(request, 'recipe.html', context={'recipe': recipe})


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')

