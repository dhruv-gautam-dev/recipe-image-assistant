import customtkinter as ctk
from tkinter import messagebox

from src.prompt_manager import PromptManager
from src.file_manager import FileManager


class RecipeAssistantGUI:

    def __init__(self, recipes):

        self.manager = PromptManager(recipes)
        self.file_manager = FileManager()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()

        self.app.title("Recipe Image Assistant")
        self.app.geometry("900x700")

        self.build_ui()

        self.refresh()

        self.copy_current_prompt()

        self.bind_shortcuts()

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

        copy_btn = ctk.CTkButton(
            button_frame,
            text="📋 Copy Prompt",
            command=self.copy_prompt,
            width=180,
        )
        copy_btn.grid(row=0, column=0, padx=10)

        downloaded_btn = ctk.CTkButton(
            button_frame,
            text="✅ Image Downloaded",
            command=self.image_downloaded,
            width=220,
        )
        downloaded_btn.grid(row=0, column=1, padx=10)

    def bind_shortcuts(self):

        self.app.bind("<Escape>", lambda e: self.app.destroy())

        self.app.bind("<Control-c>", lambda e: self.copy_prompt())

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

    def image_downloaded(self):

        recipe = self.manager.current_recipe()

        success, result = self.file_manager.save_image(
            recipe.recipe_name,
            self.manager.current_prompt_name(),
        )

        if not success:
            messagebox.showwarning(
                "Warning",
                result,
            )
            return

        has_next = self.manager.next_prompt()

        if not has_next:
            messagebox.showinfo(
                "Completed",
                "🎉 All recipes have been completed!"
            )
            return

        self.refresh()

        self.copy_current_prompt()

    def copy_prompt(self):

        self.copy_current_prompt()

        messagebox.showinfo(
            "Copied",
            "Prompt copied to clipboard."
        )

    def run(self):

        self.app.mainloop()