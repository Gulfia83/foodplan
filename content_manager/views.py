from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DishSerializer


@api_view(['POST'])
@csrf_exempt
@transaction.atomic
def create_dish(request):
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