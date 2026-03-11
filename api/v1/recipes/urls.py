from django.urls import path
from api.v1.recipes.views import RecipeListAPI

urlpatterns = [
    path("", RecipeListAPI.as_view(), name="recipes-list"),
]
