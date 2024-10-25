from django.db import models
from django.core.validators import MinValueValidator


CATEGORIES = [
    ('br', 'завтраки'),
    ('l', 'обеды'),
    ('din', 'ужины'),
    ('des', 'десерты')
]


class Ingredient(models.Model):
    title = models.CharField(
        verbose_name='Ингредиент',
        max_length=100
    )
    units = models.CharField(
        'единицы измерения',
        max_length=20,
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(
        verbose_name='Название блюда',
        max_length=100
    )
    img = models.ImageField(
        upload_to='recipes',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание блюда',
        blank=True
    )
    instruction = models.TextField(
        verbose_name='Инструкция по приготовлению',
        blank=True
    )
    category = models.CharField(
        verbose_name='Категория',
        max_length=50,
        choices=CATEGORIES
    )
    is_active = models.BooleanField(
        verbose_name='Активное/неактивное',
        default=True
    )

    class Meta:
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class RecipeItem(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        related_name='items',
        on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Dish,
        verbose_name='Рецепт',
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'

    def __str__(self):
        return f'{self.ingredient} - {self.quantity}'
