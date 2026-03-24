from django.core.management.base import BaseCommand
import kagglehub
import csv
import os
import shutil
from config.django.base import BASE_DIR
from ingredients.models import Ingredient

INGREDIENTS_CSV_FILE_NAME = "ingredients_dataset.csv"


class Command(BaseCommand):
    help = (
        "Downloads the ingredient dataset from Kaggle to the project root and"
        "filling database with the ingredients data"
    )

    def _download_kaggle_dataset(self):
        self.stdout.write("Downloading dataset...")
        path = kagglehub.dataset_download(
            "uom190346a/food-ingredients-and-allergens"
        )

        current_dir = BASE_DIR
        actual_file_name = "food_ingredients_and_allergens.csv"
        source_file = os.path.join(path, actual_file_name)
        destination_file = os.path.join(current_dir, INGREDIENTS_CSV_FILE_NAME)

        if os.path.exists(source_file):
            shutil.copy2(source_file, destination_file)
            self.stdout.write(
                self.style.SUCCESS(f"File saved to: {destination_file}")
            )
        else:
            self.stdout.write(self.style.ERROR("Could not find the file."))

    def _get_ingredients_from_csv(self) -> set[str] | None:
        ingredients = set()
        file_path = os.path.join(BASE_DIR, INGREDIENTS_CSV_FILE_NAME)

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return None

        with open(file=file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if len(row) > 1:
                    ingredients.add(row[1])

        return ingredients

    def _create_ingredients(self, ingredients: set[str]):
        self.stdout.write("Creating ingredients...")

        created_ingredients = 0
        for name in ingredients:
            _, created = Ingredient.objects.get_or_create(name=name)
            if created:
                created_ingredients += 1
                self.stdout.write(f"Created: {name}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {created_ingredients} ingredients!"
            )
        )

    def _delete_ingredients_csv_file(self):
        csv_file_path = os.path.join(BASE_DIR, INGREDIENTS_CSV_FILE_NAME)

        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
            self.stdout.write(
                self.style.WARNING(f"Deleted temporary file: {csv_file_path}")
            )

    def handle(self, *args, **options):
        self._download_kaggle_dataset()
        ingredients = self._get_ingredients_from_csv()
        if ingredients is not None:
            self._create_ingredients(ingredients=ingredients)
            self._delete_ingredients_csv_file()
