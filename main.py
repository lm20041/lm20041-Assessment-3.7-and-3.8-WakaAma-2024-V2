import os #open file
import fnmatch #search for file name
# matching_files{{filename, file_path, Association, Place}}

def find_files_with_name(directory, pattern):
  matching_files = {}
  for root, _, files in os.walk(directory):
      for filename in fnmatch.filter(files, pattern): # file_pattern in fouder
          file_path = os.path.join(root, filename)
          matching_files[filename] = file_path
  return matching_files
def extract_information_from_file(file_path):  # for each file in list
    extracted_data = []
    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split() # Split the line to 2 parts place & Association.
            if len(parts) >= 6:  # Ensure there are enough
                Place = parts[0] # Place
                Association = parts[5] # Association
                extracted_data[Association] = Place
    return extracted_data
def analyse_file_data(extracted_data):
    points = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    association_points = {}
# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "flower" in their name

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)
extracted_data = extract_information_from_file(matching_files[filename])

# Print matching files
if matching_files:
    print("Found the following files:")
    for filename, file_path in matching_files.items():
        print(f"filename:{filename} \nfile_path: {file_path}\n")
else:
    print(f"No files found with {file_pattern} in the name.")