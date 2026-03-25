from rest_framework import serializers
from ingredients.models import IngredientType


class IngredientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = ["id", "name"]
        read_only_fields = ["id"]
