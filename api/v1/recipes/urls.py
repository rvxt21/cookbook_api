from django.urls import path
from api.v1.recipes.views import RecipeListAPI, RecipeDetailAPI, RecipeCreateAPI

urlpatterns = [
    path("", RecipeListAPI.as_view(), name="recipes-list"),
    path("<int:pk>/", RecipeDetailAPI.as_view(), name="recipe-detail"),
    path("create/", RecipeCreateAPI.as_view(), name="recipe-create"),
]
