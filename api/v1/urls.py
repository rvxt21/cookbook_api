from django.urls import path, include

urlpatterns = [
    path("recipes/", include("api.v1.recipes.urls")),
]
