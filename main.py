from tkinter import *
from tkinter import filedialog, messagebox
import os

class FileFolderDisplay:
    def __init__(self, parent):
        self.parent = parent
        self.current_folder = "waka_ama_db"  # Default folder

        # Create widgets
        self.label = Label(parent, text="Files and Folders:")
        self.output_text = Text(parent, height=10, width=50)
        self.load_button = Button(parent, text="Load Files/Folders", command=self.load_files_folders)

        # Grid widgets
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.output_text.grid(row=1, column=0, padx=10, pady=10)
        self.load_button.grid(row=2, column=0, padx=10, pady=10)

    def load_files_folders(self):
        folder_path = filedialog.askdirectory(initialdir=self.current_folder, title="Select Folder")
        if folder_path:
            self.current_folder = folder_path  # Update current folder
            folder_contents = os.listdir(folder_path)
            self.output_text.delete('1.0', END)  # Clear previous content

            for item in folder_contents:
                full_path = os.path.join(folder_path, item)
                if os.path.isdir(full_path):
                    self.output_text.insert(END, f"Folder: {item}\n")
                else:
                    self.output_text.insert(END, f"File: {item}\n")

# Create the main Tkinter window
root = Tk()
root.title("File and Folder Display")

# Create an instance of FileFolderDisplay inside the main window
file_folder_display = FileFolderDisplay(root)

# Start the main event loop
root.mainloop()