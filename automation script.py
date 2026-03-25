import os
import shutil


folder_path = r"C:\Users\abdul\OneDrive\Desktop"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"]
}


for folder in file_types:
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

# Sort files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                print(f"Moved: {file} → {folder}")
