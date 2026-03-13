from rest_framework import serializers
from recipes.models import RecipeStep, Recipe


class RecipeStepDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ["order", "description"]


class RecipeStepCreateSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = RecipeStep
        fields = ("recipe", "order", "description")


class RecipeStepCreateNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ("order", "description")
