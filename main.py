import os
directory_to_search = 'waka_ama_db' # folder name input
directory = directory_to_search
for root, _, files in os.walk(directory):
    for filename in files:
        print(file)