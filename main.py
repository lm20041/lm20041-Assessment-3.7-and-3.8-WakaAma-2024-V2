import os  # for file and directory operations
import fnmatch  # for matching file patterns
import csv  # for handling CSV files

def find_files_with_name(directory, pattern):
    matching_files = []
    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            matching_files.append(os.path.join(root, filename))
    return matching_files

def extract_information_from_file(file_path):  # for each file in list
    extracted_data = []

    with open(file_path, 'r', encoding='latin-1') as file:  # Use 'latin-1' to handle encoding issues
        reader = csv.reader(file)  # Use csv.reader to handle comma-separated values
        for row in reader:
            if len(row) >= 6:  # Ensure there are enough columns
                try:
                    place = int(row[0])  # Convert place to integer
                    team_name = row[3]
                    association = row[5]
                    extracted_data.append({
                        "Place": place,
                        "Team Name": team_name,
                        "Association": association
                    })
                except ValueError as e:
                    print(f"Error parsing row: {row}. Error: {e}")
    return extracted_data

def analyse_file_data(extracted_data):
    points = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    association_points = {}

    # Sort data by place to ensure we are dealing with top 10
    extracted_data_sorted = sorted(extracted_data, key=lambda x: x["Place"])

    for record in extracted_data_sorted[:10]:  # Consider only the top 10 records
        place = record["Place"]
        association = record["Association"]
        points_earned = points.get(place, 1)  # If place > 8, get 1 point

        if association not in association_points:
            association_points[association] = 0
        association_points[association] += points_earned

    return association_points

def aggregate_analysis(directory_to_search, file_pattern):
    all_extracted_data = []
    matching_files = find_files_with_name(directory_to_search, file_pattern)  # Find files
    for file_path in matching_files:
        extracted_data = extract_information_from_file(file_path)
        all_extracted_data.extend(extracted_data)

    # Analyse the combined data from all files
    combined_analysis = analyse_file_data(all_extracted_data)

    # Print the combined results
    print(f"\nCombined Results from all files:")
    sorted_associations = sorted(combined_analysis.items(), key=lambda x: x[1], reverse=True)
    for association, points in sorted_associations:
        print(f"Association: {association}, Points: {points}")

# Input
aggregate_analysis("waka_ama_db", "*Final*")