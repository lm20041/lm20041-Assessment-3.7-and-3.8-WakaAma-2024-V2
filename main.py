import os
import fnmatch

# Function to find files with a specific name pattern
def find_files_with_name(directory, pattern):
    matching_files = {}
    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            file_path = os.path.join(root, filename)
            matching_files[filename] = file_path
    return matching_files

# Function to extract Place and Association from files
def extract_information_from_file(file_path):
    extracted_data = {}
    with open(file_path, 'r') as file:
        # Strip top line
        first_line = file.readline().strip()
        remaining_lines = file.readlines()
        # Extract data from remaining lines
        for line in remaining_lines:
            parts = line.strip().split(',')  # Split line by ','
            if len(parts) >= 6:  # Ensure there are enough parts
                try:
                    Place = int(parts[0])  # Convert Place to integer
                    Association = parts[5].strip()  # Strip any extra whitespace
                    extracted_data[Association] = Place
                except ValueError:
                    print(f"Invalid data in line: {line.strip()}")  # Handle invalid data
    return extracted_data

# Function to analyze extracted data and calculate points
def analyse_file_data(extracted_data):
    points = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    association_points = {}
    # Go through each associative and add their total points depending on place
    for association, place in extracted_data.items():
        if place in points:
            if association in association_points:
                association_points[association] += points[place]
            else:
                association_points[association] = points[place]
    return association_points

# Function to sum up points across multiple files
def sum_up_points(all_association_points):
    total_points = {}
    for association_points in all_association_points:
        for association, points in association_points.items():
            if association in total_points:
                total_points[association] += points
            else:
                total_points[association] = points
    return total_points

# Function to get the top 8 associations with the highest points
def get_top_associations(total_points, top_n=8):
    sorted_associations = sorted(total_points.items(), key=lambda item: item[1], reverse=True)
    top_associations = dict(sorted_associations[:top_n])
    return top_associations

# Function to list all files and folders
def list_all_files_and_folders(directory):
    all_files_folders = {}
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            file_path = os.path.join(root, name)
            all_files_folders[name] = file_path
    return all_files_folders

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Directory to search
file_pattern = '*Final*'  # Pattern to match files

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)

# List to hold points from all files
all_association_points = []

# Print matching files and extract information
if matching_files:
    for filename, file_path in matching_files.items():
        extracted_data = extract_information_from_file(file_path)
        association_points = analyse_file_data(extracted_data)
        all_association_points.append(association_points)
else:
    print(f"No files found with {file_pattern} in the name.")

# Sum up points from all files
total_points = sum_up_points(all_association_points)
print(f"Total Points for All Associations: {total_points}")

# Get the top 8 associations with the highest points
top_associations = get_top_associations(total_points)
print(f"Top Associations: {top_associations}")

# Get the name and file paths of all research files
name_file_types = find_files_with_name(directory_to_search, '*Research*')
print(f"Research Files: {name_file_types}")

# Get the name and file paths of all files and folders
all_file_types = list_all_files_and_folders(directory_to_search)
print(f"All Files and Folders: {all_file_types}")