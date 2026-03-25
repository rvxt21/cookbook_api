from django.urls import path
from api.v1.recipes.views import (
    RecipeListAPI,
    RecipeDetailAPI,
    RecipeCreateAPI,
    RecipeCreateNestedAPI,
    RecipeUpdateAPI,
    RecipeDeleteAPI,
)

urlpatterns = [
    path("", RecipeListAPI.as_view(), name="recipes-list"),
    path("<int:pk>/", RecipeDetailAPI.as_view(), name="recipe-detail"),
    path("create/", RecipeCreateAPI.as_view(), name="recipe-create"),
    path(
        "create-nested/", RecipeCreateNestedAPI.as_view(), name="recipe-create"
    ),
    path("<int:pk>/update/", RecipeUpdateAPI.as_view(), name="recipe-update"),
    path("<int:pk>/delete/", RecipeDeleteAPI.as_view(), name="recipe-delete"),
]
