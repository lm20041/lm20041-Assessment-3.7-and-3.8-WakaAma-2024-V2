from tkinter import *
from tkinter import messagebox, filedialog
import os

class FileBrowserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Browser GUI")

        self.create_widgets()
        self.grid_widgets()

    def create_widgets(self):
        # Resize the text box
        new_height = 20  # New height in rows
        new_width = 80   # New width in columns
        self.path_label = Label(self.root, text="Select a directory:").grid(row=0, column=0, padx=10, pady=10)
        self.path_entry = Entry(self.root, width=50).grid(row=0, column=1, padx=10, pady=10)
        self.browse_button = Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=10)

        self.output_text = Text(self.root, height=20, width=80).grid(row=1, column=0, columnspan=3, padx=10, pady=10, height=new_height, width=new_width)
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_entry.delete(0, END)
            self.path_entry.insert(0, directory)
            self.display_directory_contents(directory)
    def display_directory_contents(self, path):
        try:
            contents = os.listdir(path)
            self.output_text.delete('1.0', END)
            for item in contents:
                item_path = os.path.join(path, item)
                self.output_text.insert(END, item_path + '\n')
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    app = FileBrowserGUI(root)
    root.mainloop()