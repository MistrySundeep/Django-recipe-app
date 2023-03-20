from django.db import models


recipe_type_choices = (
    ('V', 'Vegetarian'),
    ('NV', 'Non Vegetarian'),
    ('VG', 'Vegan')
)

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_pub_date = models.DateTimeField('date published')
    ingredients_list = models.TextField('ingredients list')
    recipe_instructions = models.TextField('recipe method')
    recipe_type = models.CharField(max_length=2, choices=recipe_type_choices, default='')

    def __str__(self):
        return self.recipe_type

    def __str__(self):
        return self.recipe_name
