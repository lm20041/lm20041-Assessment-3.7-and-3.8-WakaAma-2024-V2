import os
import fnmatch
import random

directory_to_search = 'waka_ama_db'  # Folder name input
file_pattern = '*Final*'  # File name input
matching_files = []

# Traverse the directory and find matching files
for root, _, files in os.walk(directory_to_search):
    for filename in files:
        if fnmatch.fnmatch(filename, file_pattern):
            file_path = os.path.join(root, filename)
            matching_files.append(file_path)

# If matching files are found, select one randomly and process it
if matching_files:
    file_path = random.choice(matching_files)
    print(f"\nRandomly Selected File: {file_path}\n")

    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        remaining_lines = file.readlines()

    # Print the first line
    print(f"First Line: {first_line}\n")

    # Process and print the remaining lines
    print("Remaining Lines (1st and 6th parts):")
    for line in remaining_lines:
        parts = line.strip()
        if len(parts) >= 6:
            first_part = parts[0]
            sixth_part = parts[5]
            print(f"1st Part: {first_part}, 6th Part: {sixth_part}")
        else:
            print("Line does not have enough parts:", line.strip())
else:
    print("No files found with the specified pattern.")