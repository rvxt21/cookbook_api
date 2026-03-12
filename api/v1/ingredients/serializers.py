from rest_framework import serializers
from recipes.models import Recipe
from ingredients.models import Ingredient, IngredientType, RecipeIngredient


class IngredientDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class IngredientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name"]


class IngredientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = ["id", "name"]
        read_only_fields = ["id"]


class RecipeIngredientDisplaySerializer(serializers.ModelSerializer):
    ingredient = IngredientDisplaySerializer(read_only=True)
    ingredient_type = IngredientTypeSerializer(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ["id", "ingredient", "ingredient_type", "count"]


class RecipeIngredientCreateSerializer(serializers.Serializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    ingredient = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all()
    )
    ingredient_type = serializers.PrimaryKeyRelatedField(
        queryset=IngredientType.objects.all()
    )
    count = serializers.IntegerField()

    def create(self, validated_data):
        return RecipeIngredient.objects.create(**validated_data)
