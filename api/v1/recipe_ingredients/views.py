from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ingredients.models import RecipeIngredient
from api.v1.recipe_ingredients.serializers import (
    RecipeIngredientCreateSerializer,
    RecipeIngredientDisplaySerializer,
)


class RecipeIngredientCreateAPI(GenericAPIView):
    def post(self, request: Request) -> Response:
        serializer = RecipeIngredientCreateSerializer(data=request.data)

        if serializer.is_valid():
            recipe_ingredient = serializer.save()

            return Response(
                RecipeIngredientDisplaySerializer(recipe_ingredient).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeIngredientDeleteAPI(GenericAPIView):
    def delete(self, request: Request, pk: int) -> Response:
        recipe_ingredient = get_object_or_404(RecipeIngredient, pk=pk)

        recipe_ingredient.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
