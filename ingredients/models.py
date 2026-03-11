from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class IngredientType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredient_type = models.ForeignKey(
        IngredientType, on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField()
