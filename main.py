import os
import fnmatch
from tkinter import *
from functools import partial

class Convertor:
    def __init__(self, master):
        self.master = master
        self.master.title("Entry Password")
        self.master.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.text_font_6 = ("Arial", "12", "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        button_fg = "white"
        button_bg = "#004C99"

        self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=self.text_font_6, bg=self.background)
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=10)

        directory_to_search = 'waka_ama_db'
        file_pattern = '*Final*'

        self.file_type_all = self.create_file_type_all(directory_to_search)
        self.file_type_match = self.create_file_type_match(self.file_type_all, file_pattern)

        self.to_resultsexport_button = Button(self.parent_frame, width=8, height=1, text="Check", bg=button_bg, fg=button_fg, font=self.text_font_6, command=lambda: self.to_resultsexport(self.file_type_all, self.file_type_match))
        self.to_resultsexport_button.grid(row=5, column=0, pady=10)
        self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=self.to_help)
        self.help_button.grid(row=5, column=1, pady=10)

    def create_file_type_all(self, folder):
        file_type_all = {}
        for root, _, files in os.walk(folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_type_all[filename] = file_path
        return file_type_all

    def create_file_type_match(self, file_dict, pattern):
        file_type_match = {}
        for filename in fnmatch.filter(file_dict.keys(), pattern):
            file_path = file_dict[filename]
            file_type_match[filename] = file_path
        return file_type_match

    def to_resultsexport(self, file_all, file_match):
        ResultsExport(self, file_all, file_match)

    def to_help(self):
        pass
if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()