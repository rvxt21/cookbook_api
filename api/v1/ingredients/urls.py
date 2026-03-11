from django.urls import path
from api.v1.ingredients.views import (
    IngredientListAPI,
    IngredientCreateAPI,
    IngredientUpdateAPI,
)

urlpatterns = [
    path("", IngredientListAPI.as_view(), name="ingredient-list"),
    path("create/", IngredientCreateAPI.as_view(), name="ingredient-create"),
    path("<int:pk>/update/", IngredientUpdateAPI.as_view()),
]
