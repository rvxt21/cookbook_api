from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ingredients.models import Ingredient, IngredientType, RecipeIngredient
from api.v1.ingredients.serializers import (
    IngredientDisplaySerializer,
    IngredientCreateSerializer,
    IngredientTypeSerializer,
    RecipeIngredientCreateSerializer,
    RecipeIngredientDisplaySerializer,
)


class IngredientListAPI(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDisplaySerializer


class IngredientCreateAPI(GenericAPIView):
    def post(self, request: Request) -> Response:
        serializer = IngredientCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientUpdateAPI(GenericAPIView):
    def put(self, request: Request, pk: int) -> Response:
        ingredient = get_object_or_404(Ingredient, pk=pk)

        serializer = IngredientCreateSerializer(
            instance=ingredient, data=request.data
        )
        if serializer.is_valid():
            ingredient = serializer.save()

            return Response(
                IngredientDisplaySerializer(ingredient).data,
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDeleteAPI(GenericAPIView):
    def delete(self, request: Request, pk: int):
        ingredient = get_object_or_404(Ingredient, pk=pk)

        ingredient.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientDetailAPI(GenericAPIView):
    def get(self, request: Request, pk: int) -> Response:
        ingredient = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientDisplaySerializer(ingredient)

        return Response(serializer.data)


class IngredientTypeViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientTypeSerializer
    queryset = IngredientType.objects.all()


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
