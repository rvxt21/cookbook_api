from django.urls import path
from api.v1.ingredients.views import IngredientListAPI

urlpatterns = [
    path("", IngredientListAPI.as_view(), name="ingredient-list"),
]
