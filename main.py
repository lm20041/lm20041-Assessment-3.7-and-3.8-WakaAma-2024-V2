import os
import fnmatch

directory_to_search = 'waka_ama_db'  # folder name input
file_pattern = '*Final*'  # file name input

for root, _, files in os.walk(directory_to_search):
    for filename in files:
        if fnmatch.fnmatch(filename, file_pattern): #pattern matching
            print(filename)