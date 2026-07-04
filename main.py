from config import EXCEL_FILE
from src.excel_reader import ExcelReader
from src.gui import RecipeAssistantGUI


def main():

    reader = ExcelReader(EXCEL_FILE)

    recipes = reader.get_recipes()

    app = RecipeAssistantGUI(recipes)

    app.run()


if __name__ == "__main__":
    main()