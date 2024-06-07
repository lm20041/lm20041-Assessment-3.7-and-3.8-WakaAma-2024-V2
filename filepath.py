import os
import fnmatch

def find_files_with_name(directory, pattern):
  matching_files = []
  for root, _, files in os.walk(directory):
      for filename in fnmatch.filter(files, pattern): # file_pattern in fouder
          matching_files.append(os.path.join(root, filename))
  return matching_files

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "flower" in their name

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)

# Print matching files
if matching_files:
  print("Found the following files:")
  for file_path in matching_files:
      print(file_path)
else:
  print(f"No files found with {file_pattern} in the name.")