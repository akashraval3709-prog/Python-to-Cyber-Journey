import os
import shutil
import subprocess
import datetime

base_path = input("Enter source folder path: ")
backup_root = r"D:\Backup"

folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup = os.path.join(backup_root, folder_name)

os.makedirs(backup, exist_ok=True)

try:
    files = os.listdir(base_path)
except FileNotFoundError:
    print("Source folder not found ")
    exit()

file_count = 0
folder_count = 0
for file in files:
    print(f"Copying: {file}")
    src_path = os.path.join(base_path, file)
    dst_path = os.path.join(backup, file)

    if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path)
        file_count += 1
    elif os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        folder_count+=1
        
print(f"{file_count} files and {folder_count} folder backed up successfully ✅")

res = subprocess.run(['cmd', '/c', 'dir', backup], capture_output=True, text=True)
print(res.stdout)
