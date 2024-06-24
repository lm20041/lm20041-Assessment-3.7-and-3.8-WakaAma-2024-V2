from tkinter import *
from tkinter import filedialog, messagebox

class FileReadWriteWindow:
    def __init__(self, parent):
        self.parent = parent
        self.file_path = None  # Variable to store the selected file path

        # Create widgets for the file read/write window
        self.label = Label(parent, text="File Read/Write")
        self.read_button = Button(parent, text="Read from File", command=self.read_from_file)
        self.write_button = Button(parent, text="Write to File", command=self.write_to_file)

        # Grid the widgets
        self.label.grid(row=0, column=0, pady=10)
        self.read_button.grid(row=1, column=0, pady=5)
        self.write_button.grid(row=2, column=0, pady=5)

    def read_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                messagebox.showinfo("File Content", content)

    def write_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            content = "Example content to write to file."
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Information", "Data written to file successfully.")

# Create the main Tkinter window
root = Tk()
root.title("File Read/Write Demo")

# Create an instance of FileReadWriteWindow inside the main window
file_read_write_window = FileReadWriteWindow(root)

# Start the main event loop
root.mainloop()