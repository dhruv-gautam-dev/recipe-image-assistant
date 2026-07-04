import customtkinter as ctk

from src.prompt_manager import PromptManager


class RecipeAssistantGUI:

    def __init__(self, recipes):

        self.manager = PromptManager(recipes)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()

        self.app.title("Recipe Image Assistant")
        self.app.geometry("900x700")

        self.build_ui()

        self.refresh()

        self.copy_current_prompt()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.app,
            text="Recipe Image Assistant",
            font=("Arial", 24, "bold"),
        )
        title.pack(pady=15)

        self.recipe_label = ctk.CTkLabel(
            self.app,
            text="",
            font=("Arial", 18),
        )
        self.recipe_label.pack()

        self.progress_label = ctk.CTkLabel(
            self.app,
            text="",
            font=("Arial", 14),
        )
        self.progress_label.pack(pady=5)

        self.prompt_type_label = ctk.CTkLabel(
            self.app,
            text="",
            font=("Arial", 16, "bold"),
        )
        self.prompt_type_label.pack(pady=10)

        self.prompt_box = ctk.CTkTextbox(
            self.app,
            width=820,
            height=420,
            wrap="word",
        )
        self.prompt_box.pack(pady=10)

        button_frame = ctk.CTkFrame(self.app)
        button_frame.pack(pady=15)

        previous_btn = ctk.CTkButton(
            button_frame,
            text="⬅ Previous",
            command=self.previous_prompt,
        )
        previous_btn.grid(row=0, column=0, padx=10)

        copy_btn = ctk.CTkButton(
            button_frame,
            text="📋 Copy Prompt",
            command=self.copy_prompt,
        )
        copy_btn.grid(row=0, column=1, padx=10)

        next_btn = ctk.CTkButton(
            button_frame,
            text="Next ➜",
            command=self.next_prompt,
        )
        next_btn.grid(row=0, column=2, padx=10)

    def copy_current_prompt(self):

        self.app.clipboard_clear()
        self.app.clipboard_append(self.manager.current_prompt())
        self.app.update()

    def refresh(self):

        recipe = self.manager.current_recipe()
        progress = self.manager.progress()

        self.recipe_label.configure(
            text=f"Recipe {progress['recipe']}/{progress['recipes']}\n\n{recipe.recipe_name}"
        )

        self.progress_label.configure(
            text=f"Prompt {progress['prompt']}/3      Overall {progress['overall']}/{progress['total']}"
        )

        self.prompt_type_label.configure(
            text=self.manager.current_prompt_name()
        )

        self.prompt_box.delete("1.0", "end")
        self.prompt_box.insert(
            "1.0",
            self.manager.current_prompt(),
        )

    def next_prompt(self):

        self.manager.next_prompt()

        self.refresh()

        self.copy_current_prompt()

    def previous_prompt(self):

        self.manager.previous_prompt()

        self.refresh()

        self.copy_current_prompt()

    def copy_prompt(self):

        self.copy_current_prompt()

    def run(self):

        self.app.mainloop()