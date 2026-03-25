from rest_framework import viewsets

from ingredients.models import IngredientType
from api.v1.ingredient_types.serializers import (
    IngredientTypeSerializer,
)


class IngredientTypeViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientTypeSerializer
    queryset = IngredientType.objects.all()
