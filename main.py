from tkinter import *
from tkinter import filedialog, messagebox

# Create the main Tkinter window
root = Tk()

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        content = "Example content to write to file."
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Information", "Data written to file successfully.")

# Create a button to open the file dialog for writing
write_button = Button(root, text="Save File", command=save_file)
write_button.pack()

# Start the main event loop
root.mainloop()