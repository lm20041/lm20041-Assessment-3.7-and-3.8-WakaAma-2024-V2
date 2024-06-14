import tkinter as tk
from tkinter import PhotoImage

# Create the main window
root = tk.Tk()
root.title("Text Box with File Icons")

# Create a Text widget
text_box = tk.Text(root, width=40, height=10)
text_box.pack(pady=20, padx=20)

# Load file icons
file_icon_path = "file-icon.png"  # Replace with your file icon path
file_icon = PhotoImage(file=file_icon_path)

# Insert file icons and text into the Text widget
file_items = [
    ("Document1.txt", file_icon),
    ("Image1.png", file_icon),
    ("Presentation1.pptx", file_icon)
]

for file_name, icon in file_items:
    text_box.image_create(tk.END, image=icon)
    text_box.insert(tk.END, f" {file_name}\n")

# Run the application
root.mainloop()