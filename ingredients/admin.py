from django.contrib import admin
from ingredients.models import Ingredient, IngredientType, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name"]


class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ["recipe", "ingredient", "ingredient_type", "count"]
    raw_id_fields = ["recipe", "ingredient", "ingredient_type"]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
