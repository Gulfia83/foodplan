from random import choice
from django.shortcuts import render, get_object_or_404

from recipeapp.models import Dish


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Dish.objects.get_total_price(), pk=recipe_id)
    #recipe.total_price = 0
    #for item in recipe.items.all():
    #    item_price = item.quantity * item.ingredient.price
    #    recipe.total_price += item_price

    return render(request, 'recipe.html', context={'recipe': recipe})


def cheap_recipes_view(request):
    recipes = Dish.objects.get_total_price().filter(is_active=True,
                                                    price__lte=400)

    return render(request, 'all_recipes.html', context={'recipes': recipes, 'title': 'Недорогие рецепты'})


def all_recipes_view(request):
    recipes = Dish.objects.get_total_price().filter(is_active=True)

    return render(request, 'all_recipes.html', context={'recipes': recipes, 'title': 'Все рецепты'})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def day_menu_view(request):
    breakfast_queryset = Dish.objects.filter(category='br', is_active=True)
    lunch_queryset = Dish.objects.filter(category='l', is_active=True)
    dinner_queryset = Dish.objects.filter(category='din', is_active=True)

    if is_ajax(request):
        random_breakfast = choice(breakfast_queryset)
        random_lunch = choice(lunch_queryset)
        random_dinner = choice(dinner_queryset)

        context = {
            'breakfast': random_breakfast,
            'lunch': random_lunch,
            'dinner': random_dinner,
        }
        return render(request, 'partial_day_menu.html', context)

    # Случайное блюдо при первоначальной загрузке страницы
    random_breakfast = choice(breakfast_queryset)
    random_lunch = choice(lunch_queryset)
    random_dinner = choice(dinner_queryset)

    context = {
        'breakfast': random_breakfast,
        'lunch': random_lunch,
        'dinner': random_dinner,
    }
    return render(request, 'day_menu.html', context=context)


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')

