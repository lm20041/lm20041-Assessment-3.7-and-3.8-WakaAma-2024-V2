from tkinter import *
from functools import partial
from tkinter import PhotoImage
import os
import fnmatch

# Example data for the table
data = {
    'place': ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
    'Associate': [
        'Associate_1', 'Associate_2', 'Associate_3', 'Associate_4',
        'Associate_5', 'Associate_6', 'Associate_7', 'Associate_8'
    ],
    'Points': [50, 70, 80, 60, 90, 30, 40, 85, 95, 65]
}
file_type_all = {}
file_type_match = {}

class ResultsExport:
    def __init__(self, master, data, file_type_all, file_type_match):
        # input var's
        self.master = master
        self.data = data
        self.file_type_all = file_type_all
        self.file_type_match = file_type_match
        self.current_list = file_type_match
        # Initialize a list to store image references
        self.image_refs = []  # This line initializes the list
        # setting var's
        self.master.title("ResultsExport")
        self.master.configure(borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.text_font_12 = ("Arial", "12", "bold")
        self.text_font_6 = ("Arial", "6")
        self.but_font_8 = ("Arial", "8", "bold")
        self.but_width = 8
        self.but_height = 1
        self.text_fg = "#FFFFFF"
        self.background = "white"

        # Create canvas and scrollbar
        self.canvas = Canvas(self.master, bg=self.background)
        self.scrollbar = Scrollbar(self.master, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a frame inside the canvas
        self.parent_frame = Frame(self.canvas, bg=self.background)
        self.canvas.create_window((0, 0), window=self.parent_frame, anchor="nw")

        self.parent_frame.bind("<Configure>", self.onFrameConfigure)

        self.create_widgets()

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):
        # var's
        button_fg = "white"
        button_bg = "#004C99"
        # row 0 text
        self.heading_label = Label(self.parent_frame, text='Results/Export', font=self.text_font_12, wraplength=450, bg=self.background)
        self.heading_label.grid(row=0, columnspan=6, sticky="W")
        # row 1 text
        intro_txt = "This program has produced a table results on the left hand side of the window. displaying the top eight associate places we search from all files in your chosen folder {}. Files that match up with the file name of your choice {}. You can save your table result into the file browser on the right hand side of the window. Make sure to enter a name for it and the entry box down below or just collect exploits button and the default name will be set. The file browser can display all your files in the folder or just the ones you called on. Each name shown in the files will have an attachment link that when click on will open a window displaying the file contents. You can also use it to search up pacific names in your name files"
        self.intro_label = Label(self.parent_frame, text=intro_txt, font=self.text_font_6, wraplength=450, bg=self.background)
        self.intro_label.grid(row=1, columnspan=6)
        # row 2 frames
        self.table_frame = Frame(self.parent_frame, bg="#FFFF99")
        self.table_frame.grid(row=2, column=0, columnspan=3, padx=(0, 5), pady=10, sticky="N")
        self.file_frame = Frame(self.parent_frame, bg="#B3FF66")
        self.file_frame.grid(row=2, column=3, columnspan=3, padx=(5, 0), pady=10, sticky="N")
        # create_child_widgets
        self.create_table_widgets() # put data here
        self.create_file_widgets() # put file lists here
        # row 3 text
        entry_txt = "if you want to save your table results into this folder please enter a name in your results or just press the exploit button and a default name will be set for it."
        self.text_label = Label(self.parent_frame, text=entry_txt, font=self.text_font_6, wraplength=450, bg=self.background)
        self.text_label.grid(row=3, columnspan=6)
        # row 4 lable, enrty, button
        self.entry_label = Label(self.parent_frame, text="Name your results:", font=("Arial", "8", "bold"), bg=self.background) 
        self.entry_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=(5,0))
        self.entry_box = Entry(self.parent_frame, font=self.text_font_6, width=20)
        self.entry_box.grid(row=4, column=2, columnspan=2, padx=(0,10))
        self.export_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Export", bg=button_bg, fg=button_fg, font=self.but_font_8, command=self.export)
        self.export_button.grid(row=4, column=5, columnspan=2)
        # row 5 text 
        self.error_label = Label(self.parent_frame, width=self.but_width, height=self.but_height, text="", font=self.text_font_6, wraplength=450, bg=self.background, fg="red")
        self.error_label.grid(row=5, columnspan=6, pady=5)
        # row 6 buttons
        self.end_program_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="End Program", bg="black", fg=button_fg, font=self.but_font_8, command=self.end_program)
        self.end_program_button.grid(row=6, column=0, columnspan=3)
        self.help_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Help", bg="#F4A434", fg=button_fg, font=self.but_font_8, command=self.to_help)
        self.help_button.grid(row=6, column=3, columnspan=3)
    #<<<<<        table_widgets        >>>>>
    def create_table_widgets(self):
        # table var's
        self.frame_heading = "#CCCCCC" 
        self.frame_body = "#EDEDED"
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
        self.table_canvas = Canvas(self.table_frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.table_canvas.pack(expand=False, fill=None)

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

        self.table_canvas.create_rectangle(x_start, y_start, x_end, y_end, fill=self.frame_heading, outline="black", width=1)
        self.table_canvas.create_text(x_end / 2, y_end / 2, text="Full Club Points", font=("Arial", 10, "bold"))

    def draw_3_header(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.table_canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill=self.frame_body, outline="black", width=1)
            self.table_canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"))
        self.table_canvas.create_line(0, 2 * self.row_height, self.canvas_width, 2 * self.row_height, fill="black")

    def draw_8_rows(self, y, place, associate, points):
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            self.table_canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, fill=self.frame_body, outline="black", width=1)
            self.table_canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=value, font=("Arial", 10))

    #<<<<<   export table to file_widgets      >>>>>
    def export(self):
        pass

    #<<<<<      file_widgets       >>>>>
    def create_file_widgets(self):
        pass
    #<<<<<      other button       >>>>>
    def end_program(self):
        pass
    def to_help(self):
        pass

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x350") # Adjust the width (500) and height (350) as needed
    app = ResultsExport(root, data, file_type_all, file_type_match)
    root.mainloop()