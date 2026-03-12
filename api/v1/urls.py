from django.urls import path, include
from api.v1.ingredient_types.urls import router

urlpatterns = [
    path("recipes/", include("api.v1.recipes.urls")),
    path("ingredients/", include("api.v1.ingredients.urls")),
    path("recipe-ingredients/", include("api.v1.recipe_ingredients.urls")),
] + router.urls
