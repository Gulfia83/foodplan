# Generated by Django 5.1.2 on 2024-10-25 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активное/неактивное'),
        ),
    ]
