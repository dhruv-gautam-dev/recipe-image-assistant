from dataclasses import dataclass


@dataclass
class Recipe:
    employee: str
    recipe_name: str
    ingredients_prompt: str
    steps_prompt: str
    final_prompt: str
    completed: bool