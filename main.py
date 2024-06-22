from tkinter import *
from functools import partial
from tkinter import PhotoImage
import os
import fnmatch

# Example data
data = {
    'place': ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
    'Associate': [
        'Associate_1', 'Associate_2', 'Associate_3', 'Associate_4',
        'Associate_5', 'Associate_6', 'Associate_7', 'Associate_8'
    ],
    'Points': [50, 70, 80, 60, 90, 30, 40, 85, 95, 65]
}

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
# Specify the directory to search and the pattern
directory_to_search = 'waka_ama_db'  # Current directory; change this to the directory you want to search
file_pattern = '*Final*'  # Pattern to match files containing "Final" in their name

# Find files
file_type_all = Create_file_type_all(directory_to_search)
file_type_match = Create_file_type_match(file_type_all, file_pattern)

class CanvasTable:
    def __init__(self, master, data, file_type_all, file_type_match):
        # input var's
        self.master = master
        self.data = data
        self.file_all = file_type_all
        self.file_match = file_type_match
        # setting var's
        self.master.title("CanvasTable")
        self.master.configure(borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.text_font_6 = ("Arial", "12", "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        button_fg = "white"
        button_bg = "#004C99"
        # frames
        self.table_frame = Frame(self.parent_frame, bg="#FFFF99")
        self.table_frame.grid(row=1, column=0, padx=(0, 5), pady=10, sticky="N")
        self.file_frame = Frame(self.parent_frame, bg="#B3FF66")
        self.file_frame.grid(row=1, column=1, padx=(5, 0), pady=10, sticky="N")
        # create_child_widgets
        self.create_table_widgets()
        self.create_file_widgets()

    #<<<<<        table_widgets        >>>>>
    def create_table_widgets(self):
        # table var's
        self.row_height = 30
        self.column_widths = [60, 100, 60]
        self.heading = 'full culb points'
        self.headers = ['Place', 'Associate', ' Total\nPoints']
        self.num_rows = len(data['place'])
        self.num_headers = len(self.headers)

        # Calculate canvas dimensions
        self.canvas_width = sum(self.column_widths)
        self.canvas_height = (self.num_rows + 2) * self.row_height  # +2 for extra row and headers

        # Create canvas with the exact size
        self.canvas = Canvas(self.table_frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(expand=False, fill=None)

        # Draw table
        self.draw_extra_row()
        self.draw_3_header()

        for i, (place, associate, points) in enumerate(zip(data['place'], data['Associate'], data['Points'])):
            y = (i + 2) * self.row_height  # Adjust y position by +2 to account for extra row and headers
            self.draw_8_rows(y, place, associate, points)

    def draw_extra_row(self):
        x_start = 0
        y_start = 0
        x_end = self.canvas_width
        y_end = self.row_height

        self.canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="lightgreen", outline="black", width=1)
        self.canvas.create_text(x_end / 2, y_end / 2, text="Extra Row", font=("Arial", 10, "bold"))

    def draw_3_header(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill="lightgray", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"))
        self.canvas.create_line(0, 2 * self.row_height, self.canvas_width, 2 * self.row_height, fill="black")

    def draw_8_rows(self, y, place, associate, points):
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, fill="lightgray", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=value, font=("Arial", 10))

    #<<<<<      file_widgets       >>>>>
    def create_file_widgets(self):
        # Create a Text widget
        self.text_box = Text(self.file_frame, width=40, height=10)
        self.text_box.pack(pady=20, padx=20)
        # Insert files with icons into the Text widget
        for file_name, file_path in self.file_match.items():
            self.text_box.image_create(tk.END, image=self.file_icon())
            self.text_box.insert(tk.END, f" {file_name}\n")

        # Bind mouse click event to the text widget
        self.text_box.tag_configure("filename", foreground="blue", underline=True)
        self.text_box.tag_bind("filename", "<Button-1>", self.open_file)

        # Add tags to the filenames in the text box
        for file_name in file_type_match.keys():
            start_idx = self.text_box.search(file_name, "1.0", tk.END)
            end_idx = f"{start_idx} + {len(file_name)}c"
            self.text_box.tag_add("filename", start_idx, end_idx)
    def file_icon(self):
        # Load file icons
        file_icon_path = "file-icon.png"  # Replace with your file icon path
        file_icon = PhotoImage(file=file_icon_path)
        file_icon_resized = file_icon.subsample(10, 10)  # Adjust the subsampling factors as needed
        return file_icon_resized
    def open_file(self, event):
        index = self.text_box.index(tk.CURRENT)
        line_start = self.text_box.index(f"{index} linestart")
        line_end = self.text_box.index(f"{index} lineend")
        file_name = self.text_box.get(line_start, line_end).strip().split("\n")[0]
        file_path = file_type_match.get(file_name)
        if file_path:
            with open(file_path, 'r') as file:
                file_data = file.read()
            new_window = Toplevel(root)
            new_window.title(file_name)
            new_text_box = Text(new_window, width=40, height=10)
            new_text_box.pack(pady=20, padx=20)
            new_text_box.insert(tk.END, file_data)

if __name__ == "__main__":
    root = Tk()
    app = CanvasTable(root, data, file_type_all, file_type_match)
    root.mainloop()