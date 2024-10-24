from django.shortcuts import render, get_object_or_404

from recipeapp.models import Dish


def recipe_view(request, recipe_id):
    dish = get_object_or_404(Dish, pk=recipe_id)

    return render(request, 'recipe.html', context={'recipe': dish})


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')

