from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.ingredients.views import (
    IngredientListAPI,
    IngredientCreateAPI,
    IngredientUpdateAPI,
    IngredientDeleteAPI,
    IngredientDetailAPI,
    IngredientTypeViewSet,
    RecipeIngredientCreateAPI,
    RecipeIngredientDeleteAPI,
)

router = DefaultRouter()

router.register(
    r"ingredient_types", IngredientTypeViewSet, basename="ingredient_type"
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
        "<int:pk>/",
        IngredientDetailAPI.as_view(),
        name="ingredient-detail",
    ),
    path("recipe_ingredients/create/", RecipeIngredientCreateAPI.as_view()),
    path(
        "recipe_ingredients/<int:pk>/delete/",
        RecipeIngredientDeleteAPI.as_view(),
    ),
] + router.urls
