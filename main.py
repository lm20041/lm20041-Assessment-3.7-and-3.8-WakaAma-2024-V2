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
    extracted_data = {}
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # strip top line
        first_line = file.readline().strip()
        remaining_lines = file.readlines()
        # extract data from remaining lines
        for line in remaining_lines:
            parts = line.strip().split(',') # strip remove, Split() line by ' , ' 
            if len(parts) >= 6:  # Ensure there are enough
                Place = parts[0] # Place
                Association = parts[5] # Association
                extracted_data[Association] = Place
    return extracted_data
def analyse_file_data(extracted_data):
    points = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    association_points = {}
    # {Association name: points}
    # Analyzing File Data
    # go through each associative add in their total points depending on place
    for association, place in extracted_data.items():
        if place in points:
            #check if name is in diary
            if association in association_points:
                association_points[association] += points[place]
            else:
                association_points[association] = points[place]
    return association_points
# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "flower" in their name

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)


# Print matching files and extract information
if matching_files:
    print("Found the following files:")
    for filename, file_path in matching_files.items():
        print(f"\nFilename: {filename}")
        print(f"File Path: {file_path}")
        extracted_data = extract_information_from_file(file_path)
        for association, place in extracted_data.items():
            print(f"Association: {association}")
            print(f"Place: {place}")
        association_points = analyse_file_data(extracted_data)
        print(f"Association Points: {association_points}\n")
else:
    print(f"No files found with {file_pattern} in the name.")