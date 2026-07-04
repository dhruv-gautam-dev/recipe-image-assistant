import pandas as pd
from pathlib import Path

from src.models import Recipe


class ExcelReader:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found.")

        return pd.read_excel(self.file_path)

    def get_recipes(self):

        df = self.load()

        recipes = []

        for _, row in df.iterrows():

            recipes.append(
                Recipe(
                    employee=row["Employee"],
                    recipe_name=row["Recipes"],
                    ingredients_prompt=row["ingredients_prompt (ingredients)"],
                    steps_prompt=row["worksteps_prompt (steps)"],
                    final_prompt=row["Final_dish_prompt (final)"],
                    completed=row["Completed"],
                )
            )

        return recipes