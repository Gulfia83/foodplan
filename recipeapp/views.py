from random import choice
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Case, When

from recipeapp.models import Dish, Menu
from accounts.models import Like


def liked_recipes_view(request):
    liked_dishes = Like.objects.filter(user=request.user).select_related('dish').filter(dish__is_active=True)
    
    return render(request, 'liked_recipes.html', {'liked_dishes': liked_dishes})


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Dish.objects.get_total_price(), pk=recipe_id)

    return render(request, 'recipe.html', context={'recipe': recipe})


def cheap_recipes_view(request):
    dishes = Dish.objects.get_total_price().filter(is_active=True,
                                                    price__lte=400)
    liked_dishes = Like.objects.filter(user=request.user).values_list('dish_id', flat=True)
    
    return render(request, 'all_recipes.html', context={'dishes': dishes,
                                                        'liked_dishes': liked_dishes,
                                                        'user': request.user})
    

def all_recipes_view(request):
    dishes = Dish.objects.get_total_price()\
        .get_likes_count()\
        .filter(is_active=True)
    liked_dishes = Like.objects.filter(user=request.user).values_list('dish_id', flat=True)
    dishes = dishes.annotate(
        is_liked=Case(
            When(id__in=liked_dishes, then=1),
            default=0
        )
    ).order_by('-is_liked', '-likes_count')
    return render(request, 'all_recipes.html', context={'dishes': dishes,
                                                        'liked_dishes': liked_dishes,
                                                        'user': request.user})


def day_menu_view(request):
    current_day = datetime.now().strftime('%A')

    menus = Menu.objects.filter(day_of_week=current_day)
 
    return render(request, 'day_menu.html', context={'menus': menus})


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')

