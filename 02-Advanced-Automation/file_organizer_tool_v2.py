import os
import shutil


# Get the folder path from the user
base_path = input("Enter the full path of the folder you want to organize: ")


# List of folders to be created
folder_names = ["Movies", "Documents", "Images", "Others"]

# Create the folders if they do not already exist
for item in folder_names:
    new_path = os.path.join(base_path, item)
    
    os.makedirs(new_path,exist_ok=True)

# Get a list of all files in the base directory
files = os.listdir(base_path)
count = 0
for file in files:
    file_path = os.path.join(base_path, file)

    # Check if the item is a file (not a folder)
    if os.path.isfile(file_path) and file not in folder_names:
        file_lower = file.lower()

        # Move PDF files to the Documents folder
        if file_lower.endswith('.pdf'):
            dest = os.path.join(base_path, 'Documents', file)
            if os.path.exists(dest):
                print(f"⚠️  Skipping '{file}': File already exists in the Documents folder.")
            else:
                shutil.move(file_path, dest)
                print(f"{file} → Documents")

        # Move image files (jpg, jpeg, png) to the Images folder
        elif file_lower.endswith(('.jpg', '.jpeg', '.png')):
            dest = os.path.join(base_path, 'Images', file)
            # Check if the file already exists in the destination to avoid errors
            if os.path.exists(dest):
                print(f"⚠️  Skipping '{file}': File already exists in the Images folder.")
            else:
                shutil.move(file_path, dest)
                print(f"{file} → Images")

        # Move video files (mkv, mp4) to the Movies folder
        elif file_lower.endswith(('.mkv', '.mp4')):
            dest = os.path.join(base_path, 'Movies', file)
            if os.path.exists(dest):
                print(f"⚠️  Skipping '{file}': File already exists in the Movies folder.")
            else:
                shutil.move(file_path, dest)
                print(f"{file} → Movies")
        else:
            dest = os.path.join(base_path, 'Others', file)
            if not os.path.exists(dest):
                shutil.move(file_path, dest)
                print(f"{file} → Others")
        count+=1
print("All files organized ✅")