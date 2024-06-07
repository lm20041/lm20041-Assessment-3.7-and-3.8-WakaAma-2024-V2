import os
directory_to_search = 'waka_ama_db' # folder name input
file_pattern = '*Final*' # file name input
directory = directory_to_search
filename = file_pattern
for root, _, files in os.walk(directory):
    for filename in files:
        print(file)