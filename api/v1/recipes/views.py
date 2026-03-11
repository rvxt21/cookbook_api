from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    GenericAPIView,
)
from rest_framework.exceptions import ParseError
from rest_framework import status
from recipes.models import Recipe
from api.v1.recipes.serializers import (
    RecipeDisplaySerializer,
    RecipeCreateSerializer,
    RecipeUpdateSerializer,
)


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


class RecipeDetailAPI(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDisplaySerializer


class RecipeCreateAPI(GenericAPIView):
    def post(self, request: Request) -> Response:
        serializer = RecipeCreateSerializer(data=request.data)

        if serializer.is_valid():
            recipe = serializer.save()

            return Response(
                data=RecipeDisplaySerializer(recipe).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeUpdateAPI(GenericAPIView):
    def patch(self, request: Request, pk: int) -> Response:
        recipe = get_object_or_404(Recipe, pk=pk)

        serializer = RecipeUpdateSerializer(
            instance=recipe, data=request.data, partial=True
        )

        if serializer.is_valid():
            recipe = serializer.save()

            return Response(
                data=RecipeDisplaySerializer(recipe).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDeleteAPI(GenericAPIView):
    def delete(self, request: Request, pk: int) -> Response:
        recipe = get_object_or_404(Recipe, pk=pk)

        recipe.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
