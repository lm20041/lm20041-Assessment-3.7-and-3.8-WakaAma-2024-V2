import tkinter as tk
from tkinter import PhotoImage
import os #open file
import fnmatch #search for file name

# Create the main window
root = tk.Tk()
root.title("Text Box with File Icons")

# Create a Text widget
text_box = tk.Text(root, width=40, height=10)
text_box.pack(pady=20, padx=20)

def Create_file_type_all(folder):
  file_type_all = {}
  for root, _, files in os.walk(folder):
    for filename in files:
      file_path = os.path.join(root, filename)
      file_type_all[filename] = file_path 
  return file_type_all

def Create_file_type_match(file_dict, pattern):
  file_type_match = {}
  for filename in fnmatch.filter(file_dict.keys(), pattern): 
    file_path = file_dict[filename]
    file_type_match[filename] = file_path
  return file_type_match

# Load file icons
file_icon_path = "file-icon.png"  # Replace with your file icon path
file_icon = PhotoImage(file=file_icon_path)
file_icon_reside = file_icon.subsample(10, 10)  # Adjust the subsampling factors as needed

# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "flower" in their name

# Find files
file_type_all = Create_file_type_all(directory_to_search)
file_type_match = Create_file_type_match(file_type_all, file_pattern)


for file_name, file_path in file_type_match.items():
    text_box.image_create(tk.END, image=file_icon_reside)
    text_box.insert(tk.END, f" {file_name}\n{file_path}")

# Run the application
root.mainloop()