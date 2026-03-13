from typing import Any
from django.db import transaction
from rest_framework import serializers
from recipes.models import Recipe, RecipeStep
from ingredients.models import RecipeIngredient
from api.v1.recipe_ingredients.serializers import (
    RecipeIngredientDisplaySerializer,
    RecipeIngredientNestedCreateSerializer,
)
from api.v1.recipe_steps.serializers import (
    RecipeStepDisplaySerializer,
    RecipeStepCreateNestedSerializer,
)


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


class RecipeCreateFullInfoSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientNestedCreateSerializer(many=True)
    steps = RecipeStepCreateNestedSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            "name",
            "description",
            "cooking_time",
            "meal_type",
            "ingredients",
            "steps",
        ]

    @transaction.atomic()
    def create(self, validated_data: dict[str, Any]):
        ingredients = validated_data.pop("ingredients")
        steps = validated_data.pop("steps")

        recipe = Recipe.objects.create(**validated_data)

        recipe_ingredients = [
            RecipeIngredient(
                recipe=recipe,
                ingredient=item["ingredient"],
                ingredient_type=item["ingredient_type"],
                count=item["count"],
            )
            for item in ingredients
        ]

        RecipeIngredient.objects.bulk_create(recipe_ingredients)

        recipe_steps = [
            RecipeStep(
                recipe=recipe,
                order=item["order"],
                description=item["description"],
            )
            for item in steps
        ]
        RecipeStep.objects.bulk_create(recipe_steps)

        return recipe


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
