from django.contrib import admin
from recipes.models import Recipe, RecipeStep


class RecipeStepTabularAdmin(admin.TabularInline):
    model = RecipeStep
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeStepTabularAdmin,
    ]
    list_display = ["name", "description", "cooking_time", "meal_type"]
    list_filter = ["meal_type"]


class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ["order", "description", "recipe"]
    raw_id_fields = ["recipe"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeStep, RecipeStepAdmin)
