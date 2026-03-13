from rest_framework import serializers
from recipes.models import Recipe, RecipeStep
from api.v1.recipe_ingredients.serializers import (
    RecipeIngredientDisplaySerializer,
)


class RecipeStepDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ["order", "description"]


class RecipeDisplaySerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientDisplaySerializer(
        source="recipeingredient_set", many=True, read_only=True
    )
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
            "ingredients",
            "steps",
        ]


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["name", "description", "cooking_time", "meal_type"]


class RecipeUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    cooking_time = serializers.IntegerField(required=False)
    meal_type = serializers.ChoiceField(
        choices=Recipe.MealType.choices, required=False
    )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.cooking_time = validated_data.get(
            "cooking_time", instance.cooking_time
        )
        instance.meal_type = validated_data.get("meal_type", instance.meal_type)

        instance.save()
        return instance
