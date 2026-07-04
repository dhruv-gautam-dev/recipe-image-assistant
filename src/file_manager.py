from pathlib import Path
import shutil

from config import DOWNLOAD_DIR, OUTPUT_DIR


class FileManager:

    IMAGE_NAMES = {
        "Ingredients": "ingredients.png",
        "Steps": "steps.png",
        "Final Dish": "final.png",
    }

    IMAGE_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }

    def latest_image(self):

        images = [
            file
            for file in DOWNLOAD_DIR.iterdir()
            if file.is_file()
            and file.suffix.lower() in self.IMAGE_EXTENSIONS
        ]

        if not images:
            return None

        return max(
            images,
            key=lambda image: image.stat().st_mtime,
        )

    def save_image(self, recipe_name, prompt_type):

        image = self.latest_image()

        if image is None:
            return False, "No image found."

        recipe_folder = OUTPUT_DIR / recipe_name

        recipe_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination = (
            recipe_folder /
            self.IMAGE_NAMES[prompt_type]
        )

        shutil.move(
            str(image),
            str(destination),
        )

        return True, destination