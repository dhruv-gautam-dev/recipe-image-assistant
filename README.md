# Recipe Image Assistant

A desktop workflow assistant that automates the repetitive tasks involved in AI recipe image generation.

Instead of manually copying prompts, renaming files, organizing folders, and compressing images, this application guides users through the workflow and automatically handles file management. The result is a faster, more consistent process with fewer human errors.

---

## Problem

Generating AI recipe images for multiple recipes is a repetitive and error-prone task.

For every recipe, an employee typically needs to:

- Open an Excel sheet
- Find the correct recipe
- Copy the correct prompt
- Paste it into an AI image generator
- Generate the image
- Download the image
- Rename the file correctly
- Create the correct folder structure
- Compress the image
- Repeat the same process for every recipe

When repeated across many recipes, this workflow becomes time-consuming and increases the chances of mistakes such as:

- Copying the wrong prompt
- Incorrect file names
- Missing images
- Wrong folder structure
- Large image sizes
- Inconsistent output between employees

---

## Solution

Recipe Image Assistant automates the repetitive parts of the workflow while allowing users to continue generating images using their preferred AI image generation tool.

The application automatically:

- Reads recipes from an Excel file
- Guides users through every prompt
- Copies the current prompt to the clipboard
- Tracks workflow progress
- Creates the required folder structure
- Renames downloaded images consistently
- Compresses PNG images
- Organizes all output automatically

The only manual steps remaining are:

1. Paste the prompt into your AI image generator.
2. Download the generated image.
3. Click **Image Downloaded**.

Everything else is handled automatically.

---

## Features

### Prompt Management

- Read recipes directly from Excel
- Automatic prompt navigation
- One-click prompt copying
- Progress tracking

### File Organization

- Automatic folder creation
- Automatic image renaming
- Consistent naming convention
- Organized output directory

### Image Processing

- Automatic PNG optimization
- Reduced image file size
- Consistent output format

### Productivity

- Eliminates repetitive file management
- Reduces human error
- Standardizes workflow
- Improves consistency across users

---

## Workflow

### Before

```
Open Excel
      ↓
Find Recipe
      ↓
Copy Prompt
      ↓
Open AI Tool
      ↓
Paste Prompt
      ↓
Generate Image
      ↓
Download Image
      ↓
Rename Image
      ↓
Create Folder
      ↓
Compress Image
      ↓
Repeat
```

### After

```
Launch Recipe Image Assistant
          ↓
Prompt is copied automatically
          ↓
Paste into AI Image Generator
          ↓
Generate Image
          ↓
Download Image
          ↓
Click "Image Downloaded"
          ↓
Image renamed automatically
Folder created automatically
PNG optimized automatically
Next prompt copied automatically
```

---

## Project Structure

```
recipe-image-assistant/
│
├── input/
├── downloads/
├── output/
├── logs/
├── src/
├── tests/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/recipe-image-assistant.git

cd recipe-image-assistant
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python main.py
```

---

## Usage

1. Set your browser's default download folder to the project's `downloads` directory.
2. Place your `recipes.xlsx` file inside the `input` folder.
3. Start the application.
4. Open your preferred AI image generation tool.
5. Paste the copied prompt.
6. Generate and download the image.
7. Click **Image Downloaded**.
8. Repeat until all recipes are completed.

The application automatically organizes the generated images into the correct folders.

---

## Output Structure

```
output/

Butter Chicken/
│
├── Butter Chicken ingredients.png
├── Butter Chicken steps.png
└── Butter Chicken final.png

Masala Dosa/
│
├── Masala Dosa ingredients.png
├── Masala Dosa steps.png
└── Masala Dosa final.png
```

---

## Technologies Used

- Python
- CustomTkinter
- OpenPyXL
- Pillow

---

## Future Improvements

- Automatic download detection
- Browser automation
- Resume previous session
- Multiple AI provider support
- Standalone executable
- Configuration panel

---

## License

This project is licensed under the MIT License.
