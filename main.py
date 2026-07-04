from config import EXCEL_FILE
from src.excel_reader import ExcelReader


def main():

    reader = ExcelReader(EXCEL_FILE)

    recipes = reader.get_recipes()

    print(f"\nTotal Recipes : {len(recipes)}\n")

    for recipe in recipes:
        print("=" * 60)
        print(recipe.recipe_name)
        print(recipe.completed)


if __name__ == "__main__":
    main()