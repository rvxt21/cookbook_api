from django.db import models


class Recipe(models.Model):
    class MealType(models.TextChoices):
        BREAKFAST = "Breakfast"
        LUNCH = "Lunch"
        DINNER = "Dinner"
        SNACK = "Snack"

    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    cooking_time = models.PositiveIntegerField(
        help_text="Cooking time in seconds",
    )
    meal_type = models.CharField(
        max_length=15, choices=MealType.choices, default=MealType.SNACK
    )

    @property
    def time_in_minutes(self):
        return self.cooking_time // 60

    def __str__(self):
        return self.name


class RecipeStep(models.Model):
    order = models.PositiveIntegerField(help_text="Step number in the recipe")
    description = models.TextField()
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_steps"
    )

    def __str__(self):
        return self.description
