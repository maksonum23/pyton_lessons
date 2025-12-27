#!/usr/bin/env python3
import os
import shutil
import sys

# English comments as requested
# 1. Check if the user passed the directory path
if len(sys.argv) < 2:
    print("ERROR: Please provide the folder path")
    print("Usage: python3 cleaner.py <folder_path>")
    sys.exit()

target_folder = sys.argv[1]

# 2. Check if the path exists
if not os.path.exists(target_folder):
    print(f"Error: Folder '{target_folder}' not found!")
    sys.exit()

# 3. List all items in the folder
files = os.listdir(target_folder)

for file in files:
    full_path = os.path.join(target_folder, file)
    
    # Skip directories to avoid recursion errors
    if os.path.isdir(full_path):
        continue
        
    # Get extension (e.g., "vacation.jpg" -> "jpg")
    name, extension = os.path.splitext(file)
    folder_name = extension.lower().replace(".", "")
    
    # Handle files without extensions
    if not folder_name:
        folder_name = "other"

    # 4. Create destination folder based on extension
    dest_dir = os.path.join(target_folder, folder_name)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # 5. Move the file
    shutil.move(full_path, os.path.join(dest_dir, file))
    print(f"Moved {file} to {folder_name}/")
print("Cleaning complete!")
