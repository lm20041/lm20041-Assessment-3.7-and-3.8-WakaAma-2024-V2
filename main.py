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

# Function to create the top 8 associations diary
def create_top_8_diary(total_points):
    sorted_associations = sorted(total_points.items(), key=lambda x: x[1], reverse=True)
    top_8_associations = sorted_associations[:8]
    return {assoc: points for assoc, points in top_8_associations}

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Directory to search
file_pattern = '*Final*'  # Pattern to match files

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)

# List to hold points from all files
all_association_points = []

# All file research diary
all_file_research_diary = []

# Namefile diary
namefile_diary = {}

# Print matching files and extract information
if matching_files:
    print("Found the following files:")
    for filename, file_path in matching_files.items():
        print(f"\nFilename: {filename}")
        print(f"File Path: {file_path}")
        extracted_data = extract_information_from_file(file_path)
        print(f"Extracted Data: {extracted_data}")  # Debugging statement
        association_points = analyse_file_data(extracted_data)
        print(f"Association Points: {association_points}\n")
        all_association_points.append(association_points)
        all_file_research_diary.append((filename, file_path))
        namefile_diary[filename] = file_path
else:
    print(f"No files found with {file_pattern} in the name.")

# Sum up points from all files
total_points = sum_up_points(all_association_points)
print(f"Total Points for All Associations: {total_points}")

# Create the top 8 associations diary
top_8_diary = create_top_8_diary(total_points)

# Print the top 8 associations diary
print("Top 8 Associations Diary:")
for association, points in top_8_diary.items():
    print(f"Association: {association}, Points: {points}")

# Print the all file research diary
print("All File Research Diary:")
for filename, file_path in all_file_research_diary:
    print(f"Filename: {filename}, File Path: {file_path}")

# Print the namefile diary
print("Namefile Diary:")
for filename, file_path in namefile_diary.items():
    print(f"Filename: {filename}, File Path: {file_path}")