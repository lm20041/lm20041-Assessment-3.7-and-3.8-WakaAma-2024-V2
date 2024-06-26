from tkinter import *
from functools import partial
from tkinter import PhotoImage
import os
import fnmatch
#
data = {}
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
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # var's
        button_fg = "white"
        button_bg = "#004C99"
        # row 0 text
        self.heading_label = Label(self.parent_frame, text='Results/Export', font=self.text_font_12, wraplength=350, bg=self.background)
        self.heading_label.grid(row=0, columnspan=3, sticky="W")
        # row 1 text
        intro_txt = "This program has produced a table results on the left hand side of the window. displaying the top eight associate places we search from all files in your chosen folder {}. Files that match up with the file name of your choice {}. You can save your table result into the file browser on the right hand side of the window. Make sure to enter a name for it and the entry box down below or just collect exploits button and the default name will be set. The file browser can display all your files in the folder or just the ones you called on. Each name shown in the files will have an attachment link that when click on will open a window displaying the file contents. You can also use it to search up pacific names in your name files"
        self.intro_label = Label(self.parent_frame, text=intro_txt, font=self.text_font_6, wraplength=350, bg=self.background)
        self.intro_label.grid(row=1, columnspan=3)
        # row 2 frames
        self.table_frame = Frame(self.parent_frame, bg="#FFFF99")
        self.table_frame.grid(row=2, column=0, padx=(0, 5), pady=10, sticky="N")
        self.file_frame = Frame(self.parent_frame, bg="#B3FF66")
        self.file_frame.grid(row=2, column=1, padx=(5, 0), pady=10, sticky="N")
        # create_child_widgets
        self.create_table_widgets() # put data here
        self.create_file_widgets() # put file lists here
        # row 3 text
        entry_txt = "if you want to save your table results into this folder please enter a name in your results or just press the exploit button and a default name will be set for it."
        self.text_label = Label(self.parent_frame, text=entry_txt, font=self.text_font_6, wraplength=350, bg=self.background)
        self.text_label.grid(row=3, columnspan=3)
        # row 4 lable, enrty, button
        self.entry_label = Label(self.parent_frame, text="Name your results:", font=("Arial", "8", "bold"), bg=self.background) 
        self.entry_label.grid(row=4, column=0, sticky=W, padx=5)
        self.entry_box = Entry(self.parent_frame, font=self.text_font_6)
        self.entry_box.grid(row=4, column=1, padx=5)
        self.export_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Export", bg=button_bg, fg=button_fg, font=self.but_font_8, command=self.export)
        self.export_button.grid(row=4, column=2)
        # row 5 text 
        self.error_label = Label(self.parent_frame, width=self.but_width, height=self.but_height, text="", font=self.text_font_6, wraplength=400, bg=self.background, fg="red")
        self.error_label.grid(row=5, columnspan=3, pady=5)
        # row 6 buttons
        self.end_program_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="End Program", bg="black", fg=button_fg, font=self.but_font_8, command=self.end_program)
        self.end_program_button.grid(row=6, column=0)
        self.help_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Help", bg="#F4A434", fg=button_fg, font=self.but_font_8, command=self.to_help)
        self.help_button.grid(row=6, column=2)
    #<<<<<        table_widgets        >>>>>
    def create_table_widgets(self):
        pass
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
    app = ResultsExport(root, data, file_type_all, file_type_match)
    root.mainloop()