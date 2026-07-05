import tempfile
from pathlib import Path
import unittest

import src.file_manager as file_manager_module
from src.file_manager import FileManager


class FileManagerTests(unittest.TestCase):
    def test_save_image_uses_recipe_name_with_space_before_prompt_type(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            download_dir = Path(tmpdir) / "downloads"
            output_dir = Path(tmpdir) / "output"
            download_dir.mkdir(parents=True, exist_ok=True)
            output_dir.mkdir(parents=True, exist_ok=True)

            sample_image = download_dir / "sample.png"
            sample_image.write_bytes(b"image-data")

            original_download_dir = file_manager_module.DOWNLOAD_DIR
            original_output_dir = file_manager_module.OUTPUT_DIR
            file_manager_module.DOWNLOAD_DIR = download_dir
            file_manager_module.OUTPUT_DIR = output_dir

            try:
                manager = FileManager()
                success, destination = manager.save_image(
                    "Dindigul Thalappakatti Biryani",
                    "Ingredients",
                )
            finally:
                file_manager_module.DOWNLOAD_DIR = original_download_dir
                file_manager_module.OUTPUT_DIR = original_output_dir

            self.assertTrue(success)
            self.assertEqual(
                destination.name,
                "Dindigul Thalappakatti Biryani ingredients.png",
            )
            self.assertTrue(destination.exists())
            self.assertFalse(sample_image.exists())


if __name__ == "__main__":
    unittest.main()
