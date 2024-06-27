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
            self.read_files()

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

    def read_files(self):
        for filename, filepath in self.file_type_match.items():
            with open(filepath, 'r') as file:
                self.file_contents[filename] = file.read()
        print("\nFile contents:\n")
        for filename, content in self.file_contents.items():
            print(f"Contents of {filename}:\n{content}\n")

if __name__ == "__main__":
    root = Tk()
    app = Convertor()
    root.mainloop()