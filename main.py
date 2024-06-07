import os  # for file and directory operations
import fnmatch  # for matching file patterns
import csv  # for handling CSV files
from collections import defaultdict

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

def analyse_aggregated_data(all_extracted_data):
    points_for_place = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    association_points = defaultdict(int)

    # Aggregate points for each association
    for record in all_extracted_data:
        place = record["Place"]
        association = record["Association"]
        points_earned = points_for_place.get(place, 1)  # If place > 8, get 1 point

        association_points[association] += points_earned

    # Sort associations by total points
    sorted_associations = sorted(association_points.items(), key=lambda x: x[1], reverse=True)

    return sorted_associations[:10]  # Return only the top 10 associations

def aggregate_analysis(directory_to_search, file_pattern):
    all_extracted_data = []
    matching_files = find_files_with_name(directory_to_search, file_pattern)  # Find files
    for file_path in matching_files:
        extracted_data = extract_information_from_file(file_path)
        all_extracted_data.extend(extracted_data)

    # Analyse the combined data from all files
    combined_analysis = analyse_aggregated_data(all_extracted_data)

    # Print the combined results with ranking
    print(f"\nTop 10 Associations from all files:")
    for rank, (association, points) in enumerate(combined_analysis, start=1):
        print(f"{rank}. Association: {association}, Points: {points}")

# Input
aggregate_analysis("waka_ama_db", "*Final*")