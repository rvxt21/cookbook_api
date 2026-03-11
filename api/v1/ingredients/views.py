from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ingredients.models import Ingredient
from api.v1.ingredients.serializers import (
    IngredientDisplaySerializer,
    IngredientCreateSerializer,
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
