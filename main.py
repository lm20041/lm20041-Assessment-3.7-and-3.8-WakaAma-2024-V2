import os
import fnmatch
from tkinter import *
from functools import partial

# <<<< Convertor >>>>
class Convertor:
    def __init__(self):
        self.open_filepath()
        self.file_contents = {}

    def open_filepath(self):
        folder_name = 'waka_ama_db' # self.entry_boxes[0].get()
        file_name = '*Final*' # self.entry_boxes[1].get()
        # Record all and matching file lists and their pathways
        # file_type_all
        self.file_type_all = self.create_file_type_all(folder_name)
        # Check
        if not self.file_type_all:
            print("No matching files found.")

        # file_type_match
        self.file_type_match = self.create_file_type_match(self.file_type_all, file_name)
        # Check
        if not self.file_type_match:
            print("No matching files found.")
        else:
            # Activate calculate file data <<<<<
            self.extracted_file_data(self.file_type_match)

    def create_file_type_all(self, folder):
        file_type_all = {}
        for root, _, files in os.walk(folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_type_all[filename] = file_path
        return file_type_all

    def create_file_type_match(self, file_dict, pattern):
        file_type_match = {}
        for filename in fnmatch.filter(file_dict.keys(), pattern):
            file_path = file_dict[filename]
            file_type_match[filename] = file_path
        return file_type_match

     # <<<< CAL file data >>>>
    def extracted_file_data(self, file_match):
        extracted_data = {}
        for filename, file_path in file_match.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file.readline().strip()  # Skip the first line
                    remaining_lines = file.readlines()
                    for line in remaining_lines:
                        parts = line.strip().split(',')
                        if len(parts) >= 6:
                            try:
                                place = int(parts[0])
                                association = parts[5].strip()
                                extracted_data[association] = place
                                print(extracted_data)
                            except ValueError:
                                print(f"Invalid data in line: {line.strip()}")
                                
                    print("\n\nfile--------------")
                    
            except UnicodeDecodeError:
                print(f"Cannot decode file: {file_path}")
        return extracted_data

if __name__ == "__main__":
    root = Tk()
    app = Convertor()
    root.mainloop()