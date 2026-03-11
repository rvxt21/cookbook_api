from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ParseError
from rest_framework import status
from recipes.models import Recipe
from api.v1.recipes.serializers import RecipeDisplaySerializer


class RecipeListAPI(ListAPIView):
    serializer_class = RecipeDisplaySerializer
    queryset = Recipe.objects.prefetch_related("recipe_steps").all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        meal_type_param = self.request.query_params.get("meal_type")
        if meal_type_param:
            if meal_type_param not in Recipe.MealType.values:
                raise ParseError(
                    detail=f"Invalid meal_type. Expected one of: {list(Recipe.MealType.values)}",
                    code=status.HTTP_400_BAD_REQUEST,
                )

            queryset = queryset.filter(meal_type=meal_type_param)

        return queryset
