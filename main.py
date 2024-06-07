import os  # for file and directory operations
import fnmatch  # for matching file patterns

def find_files_with_name(directory, pattern):
    matching_files = []
    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            matching_files.append(os.path.join(root, filename))
    return matching_files

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "Final" in their name

# Find files
matching_files = find_files_with_name(directory_to_search, file_pattern)

# Print matching files
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
                with open(selected_file_path, 'r') as file:
                    contents = file.read()
                    print(contents)
            except Exception as e:
                print(f"Could not read file {selected_file_path}: {e}")
        else:
            print("Invalid selection. Please run the program again and select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the file you want to open.")
else:
    print(f"No files found with {file_pattern} in the name.")