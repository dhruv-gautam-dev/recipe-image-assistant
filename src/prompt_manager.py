class PromptManager:

    PROMPT_TYPES = [
        ("Ingredients", "ingredients_prompt"),
        ("Steps", "steps_prompt"),
        ("Final Dish", "final_prompt"),
    ]

    def __init__(self, recipes):
        self.recipes = recipes
        self.recipe_index = 0
        self.prompt_index = 0

    def current_recipe(self):
        return self.recipes[self.recipe_index]

    def current_prompt_name(self):
        return self.PROMPT_TYPES[self.prompt_index][0]

    def current_prompt(self):
        recipe = self.current_recipe()
        field = self.PROMPT_TYPES[self.prompt_index][1]
        return getattr(recipe, field)

    def next_prompt(self):

        if self.prompt_index < 2:
            self.prompt_index += 1

        elif self.recipe_index < len(self.recipes) - 1:
            self.recipe_index += 1
            self.prompt_index = 0

    def previous_prompt(self):

        if self.prompt_index > 0:
            self.prompt_index -= 1

        elif self.recipe_index > 0:
            self.recipe_index -= 1
            self.prompt_index = 2

    def progress(self):

        overall = self.recipe_index * 3 + self.prompt_index + 1

        return {
            "recipe": self.recipe_index + 1,
            "recipes": len(self.recipes),
            "prompt": self.prompt_index + 1,
            "overall": overall,
            "total": len(self.recipes) * 3,
        }