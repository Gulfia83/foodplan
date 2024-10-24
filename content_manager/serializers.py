from rest_framework.serializers import ModelSerializer, ListField

from recipeapp.models import Dish, RecipeItem


class RecipeItemSerializer(ModelSerializer):
    class Meta:
        model = RecipeItem
        fields = ['ingredient', 'quantity']



class DishSerializer(ModelSerializer):
    items = RecipeItemSerializer(many=True)
    class Meta:
        model = Dish
        fields = ['title','img', 'instruction', 'category', 'items']
    def create(self, validated_data):
        new_dish = Dish.objects.create(
            title=validated_data['title'],
            img=validated_data['img'],
            instruction=validated_data['instruction'],
        )
        recipe_items_from_request = validated_data.pop('items')
        for item in recipe_items_from_request:
            ingredient = item['ingredient']
            quantity = item['quantity']
            price = ingredient.price * quantity
            RecipeItem.objects.create(
                dish=new_dish,
                ingredient=ingredient,
                quantity=quantity,
                price=price
            )
        return new_dish