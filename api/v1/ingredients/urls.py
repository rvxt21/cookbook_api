from django.urls import path
from api.v1.ingredients.views import (
    IngredientListAPI,
    IngredientCreateAPI,
    IngredientUpdateAPI,
    IngredientDeleteAPI,
    IngredientDetailAPI,
)

urlpatterns = [
    path("", IngredientListAPI.as_view(), name="ingredient-list"),
    path("create/", IngredientCreateAPI.as_view(), name="ingredient-create"),
    path(
        "<int:pk>/update/",
        IngredientUpdateAPI.as_view(),
        name="ingredient-update",
    ),
    path(
        "<int:pk>/delete/",
        IngredientDeleteAPI.as_view(),
        name="ingredient-delete",
    ),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailAPI.as_view(),
        name="ingredient-detail",
    ),
]
