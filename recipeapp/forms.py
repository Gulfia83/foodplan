from django import forms
from .models import Dish, RecipeItem

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'img', 'instruction', 'category', 'is_active']

class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ['ingredient', 'quantity']