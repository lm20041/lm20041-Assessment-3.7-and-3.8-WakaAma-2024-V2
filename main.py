import os
import fnmatch

def find_files_with_name(directory, pattern):
    matching_files = []
    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            matching_files.append(os.path.join(root, filename))
    return matching_files

def extract_information_from_file(file_path):
    extracted_data = []

    with open(file_path, 'r') as file:
        contents = file.readlines()

    for line in contents:
        parts = line.strip().split()  # Split the line by spaces (or other delimiter)
        if len(parts) >= 6:  # Ensure there are enough parts to extract the required information
            place = parts[0]  # First place (index 0)
            team_name = parts[3]  # Fourth place (index 3)
            association = parts[5]  # Sixth place (index 5)
            extracted_data.append({
                "Place": place,
                "Team Name": team_name,
                "Association": association
            })

    return extracted_data

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "Final" in their name

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)

# Print matching files and their contents
if matching_files:
    print("Found the following files:")
    for idx, file_path in enumerate(matching_files):
        print(f"{idx + 1}: {file_path}")

    # Ask the user to select a file to open
    try:
        selected_index = int(input("\nEnter the number of the file you want to open: ")) - 1
        if 0 <= selected_index < len(matching_files):
            selected_file_path = matching_files[selected_index]
            print(f"\nOpening file: {selected_file_path}\n")
            try:
                extracted_info = extract_information_from_file(selected_file_path)
                print("Extracted Information:")
                for info in extracted_info:
                    print(info)
            except Exception as e:
                print(f"Could not read file {selected_file_path}: {e}")
        else:
            print("Invalid selection. Please run the program again and select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the file you want to open.")
else:
    print(f"No files found with {file_pattern} in the name.")