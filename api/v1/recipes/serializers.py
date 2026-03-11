from rest_framework import serializers
from recipes.models import Recipe, RecipeStep


class RecipeStepDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ["order", "description"]


class RecipeDisplaySerializer(serializers.ModelSerializer):
    steps = RecipeStepDisplaySerializer(
        source="recipe_steps", many=True, read_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "description",
            "time_in_minutes",
            "meal_type",
            "steps",
        ]
