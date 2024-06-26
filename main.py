import os
import fnmatch
from tkinter import *
from functools import partial

# <<<< Convertor >>>>
class Convertor:
    def __init__(self, partner):
        # Vars
        self.text_font_6 = ("Arial", 12, "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.convertor_box = Toplevel()

        # Disable to_convertor button (uncomment when using with the main app)
        # partner.to_convertor_button.config(state=DISABLED)

        # If users press cross at top, close convertor and 'release' password button
        self.convertor_box.protocol('WM_DELETE_WINDOW', partial(self.close_convertor, partner))

        self.parent_frame = Frame(self.convertor_box, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets(partner)

    def create_widgets(self, partner):
        # Vars
        button_fg = "white"
        button_bg = "#004C99"

        # Define entry labels
        entry_labels = ["Folder Name:", "File Name:"]
        self.entry_boxes = []

        # Heading
        self.heading_label = Label(self.parent_frame, text="Convertor", font=self.text_font_6, bg=self.background)
        self.heading_label.grid(row=0, columnspan=2)

        # Instruction text
        txt = "Please enter folder name and file name so we can begin. Press 'Check' to validate the information. If valid, press 'Results'."
        self.text_label = Label(self.parent_frame, text=txt, font=("Arial", 10), bg=self.background, wraplength=400)
        self.text_label.grid(row=1, columnspan=2)

        # Entry labels and boxes
        for i, label in enumerate(entry_labels):
            Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i+2, column=0, sticky=W, padx=5, pady=(10, 0))
            entry_box = Entry(self.parent_frame, font=self.text_font_6)
            entry_box.grid(row=i+2, column=1, pady=5)
            entry_box.config(highlightthickness=2, highlightbackground="grey", highlightcolor="blue")
            self.entry_boxes.append(entry_box)

        # Error label
        self.error_label = Label(self.parent_frame, text="", font=("Arial", 10), wraplength=400, bg=self.background, fg="red")
        self.error_label.grid(row=4, columnspan=2)

        # Buttons
        self.check_button = Button(self.parent_frame, width=8, height=1, text="Check", bg=button_bg, fg=button_fg, font=self.text_font_6, command=self.open_filepath)
        self.check_button.grid(row=5, column=0)

        self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=lambda: self.to_help(partner))
        self.help_button.grid(row=5, column=1)

    def open_filepath(self):
        folder_name = self.entry_boxes[0].get()
        file_name = self.entry_boxes[1].get()

        # check folder_name exists
        if not os.path.isdir(folder_name):
            self.error_label.config(text="Invalid folder path.")
            return
        #> record all and  matching file lists and their pathway
        # file_type_all
        self.file_type_all = self.create_file_type_all(folder_name)
        # check
        if not self.file_type_all:
            self.error_label.config(text="No matching files found.")

        # file_type_match
        self.file_type_match = self.create_file_type_match(self.file_type_all, file_name)
        # check
        if not self.file_type_match:
            self.error_label.config(text="No matching files found.")
        else:
            self.error_label.config(text=f"Found {len(self.file_type_match)} matching files.")

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

    def close_convertor(self, partner):
        # Put to_convertor button back to normal (uncomment when using with the main app)
        # partner.to_convertor_button.config(state=NORMAL)
        self.convertor_box.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()