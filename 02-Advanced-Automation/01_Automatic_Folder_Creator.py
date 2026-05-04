import os
import shutil

base_path = input("Enter the full path of the folder you want to organize: ")

if not os.path.exists(base_path):
    print("Invalid path")
    exit()

folder_names = ["Movies", "Documents", "Images"]

for item in folder_names:
    new_path = os.path.join(base_path, item)
    if not os.path.exists(new_path):
        os.mkdir(new_path)

files = os.listdir(base_path)

for file in files:
    file_path = os.path.join(base_path, file)

    if os.path.isfile(file_path):
        file_lower = file.lower()

        if file_lower.endswith('.pdf'):
            dest = os.path.join(base_path, 'Documents', file)

        elif file_lower.endswith(('.jpg', '.jpeg', '.png')):
            dest = os.path.join(base_path, 'Images', file)

        elif file_lower.endswith(('.mkv', '.mp4')):
            dest = os.path.join(base_path, 'Movies', file)

        else:
            print(f"Skipped: {file}")
            continue

        if os.path.exists(dest):
            print(f"Skipping '{file}': already exists")
        else:
            shutil.move(file_path, dest)
            print(f"{file} → {dest}")

print("All files organized")