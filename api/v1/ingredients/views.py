from rest_framework.generics import ListAPIView
from ingredients.models import Ingredient
from api.v1.ingredients.serializers import IngredientDisplaySerializer


class IngredientListAPI(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDisplaySerializer
