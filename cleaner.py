#!/usr/bin/env python3
import os
import shutil
import sys
from datetime import datetime

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

# confirmation message
user_answer = input(f"Are you sure you want to clean the folder '{target_folder}'? (y/n): ").lower()
if user_answer != 'y':
    print("Operation cancelled by user.")
    sys.exit()

# 3. List all items in the folder
files = os.listdir(target_folder)

# counting moved files
moved_count = 0

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
    moved_count += 1
print("Cleaning complete! Total files moved:", moved_count)

# log the operation
# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path for the 'logs' folder
log_dir = os.path.join(script_dir, "logs")

# Create the 'logs' folder if it doesn't exist (exist_ok=True prevents errors)
os.makedirs(log_dir, exist_ok=True)

# Create the full path to the log file inside the logs folder
log_path = os.path.join(log_dir, "cleaner.log")

# Prepare the log entry with timestamp
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"{now} - Folder: {target_folder}, Moved: {moved_count} files.\n"

# Write to the file in the new location
with open(log_path, "a") as log_file:
    log_file.write(log_entry)

print(f"Cleaning complete! Results saved to: {log_path}")
