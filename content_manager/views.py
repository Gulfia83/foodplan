from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DishSerializer


from recipeapp.forms import DishForm, RecipeItemForm
from recipeapp.models import Dish, RecipeItem


#TODO: придумать как пихнуть в drf  картинку 
@api_view(['POST'])
@csrf_exempt
@transaction.atomic
def create_dish_drf(request):
    '''
    Данные для тестирования:
    {"items": [{"ingredient": 1, "quantity": 1}],
    "title": "намберван",
    "img": "http://localhost:8000/media/dishes/beconizer.jpg",
    "instruction": "нельзя так просто взять и ...",
    "category": "br"}
    '''
    dish_serializer = DishSerializer(data=request.data)
    dish_serializer.is_valid(raise_exception=True)
    dish_serializer.save()


    return Response(dish_serializer.data, status=201)


@staff_member_required
def create_dish_form(request):
    RecipeItemFormSet = modelformset_factory(
        RecipeItem,
        form=RecipeItemForm,
        extra=10
)
    if request.method == 'POST':
        dish_form = DishForm(request.POST, request.FILES)
        items_formset = RecipeItemFormSet(request.POST)

        if dish_form.is_valid() and items_formset.is_valid():
            dish = dish_form.save()
            recipe_items = items_formset.save(commit=False)
            for item in recipe_items:
                item.recipe = dish
                item.save()
            dish_form = DishForm()
            items_formset = RecipeItemFormSet(queryset=RecipeItem.objects.none())
    else:
        dish_form = DishForm()
        items_formset = RecipeItemFormSet(queryset=RecipeItem.objects.none())

    return render(request, 'create_dish.html', {
        'dish_form': dish_form,
        'items_formset': items_formset,
    })


@staff_member_required
def view_dishes(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, template_name='dishes.html', context=context)


@staff_member_required
def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    RecipeItemFormSet = modelformset_factory(
        RecipeItem,
        form=RecipeItemForm,
        extra=1,
        can_delete=True
    )
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        items_formset = RecipeItemFormSet(request.POST, queryset=RecipeItem.objects.filter(recipe=dish))

        if form.is_valid() and items_formset.is_valid():
            form.save()

            recipe_items = items_formset.save(commit=False)
            for item in recipe_items:
                item.recipe = dish
                item.save()
            for deleted_item in items_formset.deleted_objects:
                item.delete()

            return redirect('content_manager:dishes')
    else:
        form = DishForm(instance=dish)
        items_formset = RecipeItemFormSet(queryset=RecipeItem.objects.filter(recipe=dish))

    return render(request, 'dish_edit.html', {'form': form, 'dish': dish, 'items_formset': items_formset})
    