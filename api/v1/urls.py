from django.urls import path, include


urlpatterns = [
    path("recipes/", include("api.v1.recipes.urls")),
    path("ingredients/", include("api.v1.ingredients.urls")),
    path("recipe-ingredients/", include("api.v1.recipe_ingredients.urls")),
    path("", include("api.v1.ingredient_types.urls")),
]
