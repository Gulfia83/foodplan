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

    class Meta:
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    dish = models.CharField(
        verbose_name='Название блюда',
        max_length=100
    )
    img = models.ImageField(
        verbose_name='Изображение',
        blank=True
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe',
        verbose_name='Ингредиенты',
        through='RecipeItem'
        )
    instruction = models.TextField(
        verbose_name='Инструкция по приготовлению',
        blank=True
    )
    categoty = models.CharField(
        verbose_name='Категория',
        max_length=50,
        choices=CATEGORIES
    )

    class Meta:
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.dish


class RecipeItem(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        related_name='items',
        on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'

    def __str__(self):
        return f'{self.ingredient} - {self.quantity}'
