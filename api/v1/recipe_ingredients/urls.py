from django.urls import path
from api.v1.recipe_ingredients.views import (
    RecipeIngredientCreateAPI,
    RecipeIngredientDeleteAPI,
)

urlpatterns = [
    path(
        "create/",
        RecipeIngredientCreateAPI.as_view(),
        name="recipe-ingredient-create",
    ),
    path(
        "<int:pk>/delete/",
        RecipeIngredientDeleteAPI.as_view(),
        name="recipe-ingredient-delete",
    ),
]
