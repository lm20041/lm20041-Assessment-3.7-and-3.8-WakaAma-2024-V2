import os
import fnmatch
from tkinter import *
from functools import partial

# <<<< Convertor >>>>
class Convertor:
    def __init__(self):
        self.open_filepath()

    def open_filepath(self):
        folder_name = 'waka_ama_db' #self.entry_boxes[0].get()
        file_name = '*Final*' #self.entry_boxes[1].get()
        #> record all and  matching file lists and their pathway
        # file_type_all
        self.file_type_all = self.create_file_type_all(folder_name)
        # check
        if not self.file_type_all:
            print("No matching files found.")
    
        # file_type_match
        self.file_type_match = self.create_file_type_match(self.file_type_all, file_name)
        # check
        if not self.file_type_match:
            print("No matching files found.")
        else:
            # activate calculate file data <<<<<
            print(self.file_type_all)
            print("\n\n\n\n\n\n\n")
            print(self.file_type_match)
            
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

if __name__ == "__main__":
    root = Tk()
    app = Convertor()
    root.mainloop()