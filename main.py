from tkinter import *
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open a File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_box.delete(1.0, END)  # Clear the text box
                text_box.insert(END, content)  # Insert file content into text box
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def switch_files():
    global current_list_index
    current_list_index = (current_list_index + 1) % 2  # Toggle between 0 and 1
    if current_list_index == 0:
        text_box.delete(1.0, END)
        text_box.insert(END, '\n'.join(file_list_1))
    else:
        text_box.delete(1.0, END)
        text_box.insert(END, '\n'.join(file_list_2))

def create_gui():
    global current_list_index
    current_list_index = 0  # Start with file_list_1

    root = Tk()
    root.title("File Viewer")

    # Sample lists for demonstration
    file_list_1 = ["File 1 Line 1", "File 1 Line 2", "File 1 Line 3"]
    file_list_2 = ["File 2 Line 1", "File 2 Line 2", "File 2 Line 3"]

    # Create a text box with a scrollbar
    text_box_scrollbar = Scrollbar(root)
    text_box_scrollbar.grid(row=0, column=1, sticky=N+S)

    global text_box
    text_box = Text(root, wrap=WORD, yscrollcommand=text_box_scrollbar.set)
    text_box.grid(row=0, column=0, sticky=N+S+E+W)

    text_box_scrollbar.config(command=text_box.yview)

    # Create buttons
    open_button = Button(root, text="Open File", command=open_file)
    open_button.grid(row=1, column=0, pady=5)

    switch_button = Button(root, text="Switch Files", command=switch_files)
    switch_button.grid(row=1, column=1, pady=5)

    # Configure grid to expand properly
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()