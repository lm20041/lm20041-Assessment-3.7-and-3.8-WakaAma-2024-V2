from tkinter import *
from tkinter import messagebox, filedialog
import os
import tkinter.font as tkFont

class ComplexDataStructuresGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex Data Structures GUI")

        self.stack = []
        self.queue = []
        self.bst = None
        self.current_folder = "waka_ama_db"  # Initialize the current folder

        self.create_widgets()
        self.grid_widgets()

        # Load icons
        self.file_icon = PhotoImage(file="file-icon.png")
        self.folder_icon = PhotoImage(file="folder-icon.png")

    def create_widgets(self):
        # Existing widgets
        self.input_label = Label(self.root, text="Enter an integer:")
        self.input_entry = Entry(self.root, width=20)
        self.push_button = Button(self.root, text="Push to Data Structures", command=self.push_to_data_structures)
        self.output_text = Text(self.root, height=10, width=50)
        self.output_text.tag_configure("folder", foreground="blue", underline=True)  # Configure 'folder' tag
        self.output_text.tag_bind("folder", "<Button-1>", self.open_folder)  # Bind click event to 'folder' tag
        self.read_button = Button(self.root, text="Read from File", command=self.read_from_file)
        self.write_button = Button(self.root, text="Write to File", command=self.write_to_file)

        # New button to show folder contents
        self.show_folder_button = Button(self.root, text="Show Folder Contents", command=self.show_folder_contents)

    def grid_widgets(self):
        # Existing widgets layout
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)
        self.push_button.grid(row=0, column=2, padx=10, pady=10)
        self.output_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.read_button.grid(row=2, column=0, padx=10, pady=10)
        self.write_button.grid(row=2, column=1, padx=10, pady=10)

        # Placing the new button in the grid
        self.show_folder_button.grid(row=2, column=2, padx=10, pady=10)

    def push_to_data_structures(self):
        value_str = self.input_entry.get().strip()
        if not value_str.isdigit():
            messagebox.showwarning("Warning", "Please enter a valid integer.")
            return

        value = int(value_str)
        self.stack.append(value)
        self.queue.append(value)
        self.insert_into_bst(value)

        self.update_output()

    def insert_into_bst(self, value):
        if self.bst is None:
            self.bst = BSTNode(value)
        else:
            self.bst.insert(value)

    def update_output(self):
        stack_str = 'Stack: ' + ', '.join(map(str, self.stack))
        queue_str = 'Queue: ' + ', '.join(map(str, self.queue))
        bst_str = 'BST (in-order traversal): ' + str(self.bst.in_order_traversal()) if self.bst else ''

        self.output_text.delete('1.0', END)  # Clear previous content
        self.output_text.insert(END, stack_str + '\n' + queue_str + '\n' + bst_str)

    def write_to_file(self):
        content = self.output_text.get("1.0", END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Information", "Data written to file successfully.")

    def read_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.output_text.delete('1.0', END)
                self.output_text.insert(END, content)
            messagebox.showinfo("Information", "Data read from file successfully.")

    def show_folder_contents(self, folder_path="waka_ama_db"):
        self.current_folder = folder_path  # Update current folder
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            folder_contents = os.listdir(folder_path)
            self.output_text.delete('1.0', END)  # Clear previous content

            for item in folder_contents:
                full_path = os.path.join(folder_path, item)
                if os.path.isdir(full_path):
                    self.output_text.image_create(END, image=self.folder_icon)  # Insert folder icon
                    self.output_text.insert(END, " " + item + '/', ("folder",))  # Tag directories with 'folder'
                    self.output_text.insert(END, "\n")
                else:
                    self.output_text.image_create(END, image=self.file_icon)  # Insert file icon
                    self.output_text.insert(END, " " + item + "\n")
        else:
            display_str = "Folder '{}' does not exist.".format(folder_path)
            self.output_text.delete('1.0', END)
            self.output_text.insert(END, display_str)

    def open_folder(self, event):
        index = self.output_text.index("@%s,%s" % (event.x, event.y))
        line = self.output_text.get(index + " linestart", index + " lineend")
        folder_path = os.path.join(self.current_folder, line.strip('/'))
        self.show_folder_contents(folder_path)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        result = []
        if self.left:
            result.extend(self.left.in_order_traversal())
        result.append(self.value)
        if self.right:
            result.extend(self.right.in_order_traversal())
        return result

if __name__ == "__main__":
    root = Tk()
    app = ComplexDataStructuresGUI(root)
    root.mainloop()