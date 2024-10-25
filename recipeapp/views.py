from random import choice
from django.shortcuts import render, get_object_or_404

from recipeapp.models import Dish


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Dish, pk=recipe_id)
    recipe.total_price = 0
    for item in recipe.items.all():
        item_price = item.quantity * item.ingredient.price
        recipe.total_price += item_price

    return render(request, 'recipe.html', context={'recipe': recipe})


def all_recipes_view(request):
    recipes = Dish.objects.filter(is_active=True)
    return render(request, 'all_recipes.html', context={'recipes': recipes})


def day_menu_view(request):
    random_breakfast = choice(Dish.objects.filter(category='br'))
    random_lunch = choice(Dish.objects.filter(category='l'))
    random_dinner = choice(Dish.objects.filter(category='din'))

    context = {'breakfast': random_breakfast,
               'lunch': random_lunch,
               'dinner': random_dinner
               }
    return render(request, 'day_menu.html', context=context)


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')

