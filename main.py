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
file_icon_reside = file_icon.subsample(10, 10)  # Adjust the subsampling factors as needed


# Insert file icons and text into the Text widget
file_items = [
    ("Document1.txt", file_icon_reside),
    ("Image1.png", file_icon_reside),
    ("Presentation1.pptx", file_icon_reside)
]

for file_name, icon in file_items:
    text_box.image_create(tk.END, image=icon)
    #text_box.image_create.append(icon)  # Store a reference to the PhotoImage object
    text_box.insert(tk.END, f" {file_name}\n")

# Run the application
root.mainloop()