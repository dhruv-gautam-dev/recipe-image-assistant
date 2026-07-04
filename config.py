from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Project Directories
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
DOWNLOAD_DIR = BASE_DIR / "downloads"
LOG_DIR = BASE_DIR / "logs"

# Excel
EXCEL_FILE = INPUT_DIR / "recipes.xlsx"