import os #open file
import fnmatch #search for file name

def Create_file_type_all(folder):
  file_type_all = {}
  for root, _, files in os.walk(folder):
    for filename in files:
      file_path = os.path.join(root, filename)
      file_type_all[filename] = file_path 
  return file_type_all

def Create_file_type_match(file_dict, pattern):
  file_type_match = {}
  for filename in fnmatch.filter(file_dict.keys(), pattern): 
    file_path = file_dict[filename]
    file_type_match[filename] = file_path
  return file_type_match

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "flower" in their name

# Find files
file_type_all = Create_file_type_all(directory_to_search)
file_type_match = Create_file_type_match(file_type_all, file_pattern)
# Print matching files
if file_type_all:
  print(f"file_type_all: {file_type_all}")
if file_type_match:
  print(f"file_type_match: {file_type_match}")
