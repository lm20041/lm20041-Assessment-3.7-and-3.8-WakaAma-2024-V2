import os
import fnmatch
import random

directory_to_search = 'waka_ama_db'  # folder name input
file_pattern = '*Final*'  # file name input
matching_files = []

for root, _, files in os.walk(directory_to_search):
    for filename in files:
        if fnmatch.fnmatch(filename, file_pattern):
            file_path = os.path.join(root, filename)
            matching_files.append(file_path)

if matching_files:
    file_path = random.choice(matching_files)
    print(f"\nRandomly Selected File: {file_path}\n")

    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
else:
    print("No files found with the specified pattern.")