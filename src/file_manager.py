from pathlib import Path

from PIL import Image

from config import DOWNLOAD_DIR, OUTPUT_DIR


class FileManager:

    IMAGE_NAMES = {
        "Ingredients": "ingredients",
        "Steps": "steps",
        "Final Dish": "final",
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

    def optimize_png(self, source, destination):

        image = Image.open(source)

        # Convert images with transparency correctly
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA")

        image.save(
            destination,
            format="PNG",
            optimize=True,
            compress_level=9,
        )

        image.close()

        source.unlink()

    def save_image(self, recipe_name, prompt_type):

        image = self.latest_image()

        if image is None:
            return False, "No image found."

        recipe_folder = OUTPUT_DIR / recipe_name

        recipe_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination_name = (
            f"{recipe_name} {self.IMAGE_NAMES[prompt_type]}.png"
        )

        destination = recipe_folder / destination_name

        self.optimize_png(
            image,
            destination,
        )

        return True, destination