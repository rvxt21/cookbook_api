from rest_framework.routers import DefaultRouter

from api.v1.ingredient_types.views import (
    IngredientTypeViewSet,
)

router = DefaultRouter()

router.register(
    r"ingredient_types", IngredientTypeViewSet, basename="ingredient_type"
)

urlpatterns = [*router.urls]
