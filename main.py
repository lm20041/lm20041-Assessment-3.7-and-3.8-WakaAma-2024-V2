import os
import fnmatch
import random

directory_to_search = 'waka_ama_db'  # folder name input
file_pattern = '*Final*'  # file name input
matching_files = {}
for root, _, files in os.walk(directory_to_search):
    for filename in files:
        if fnmatch.fnmatch(filename, file_pattern):
            file_path = os.path.join(root, filename)
            print(file_path)
            matching_files.append(file_path)

file_path = random.choice(matching_files)
with open(file_path, 'r') as file:
    print(file) 