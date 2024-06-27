import os
import fnmatch
from tkinter import Toplevel, Frame, Label, Entry, Button, W
from tkinter import Tk
from functools import partial

class Convertor:
    def __init__(self, partner):
        # Vars
        self.top_num = 8
        self.places = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        self.data = {
            'place': [],
            'Associate': [],
            'Points': []
        }
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
        # record all and matching file lists and their pathway
        self.file_type_all = self.create_file_type_all(folder_name)
        if not self.file_type_all:
            self.error_label.config(text="No matching files found.")

        self.file_type_match = self.create_file_type_match(self.file_type_all, file_name)
        if not self.file_type_match:
            self.error_label.config(text="No matching files found.")
        else:
            data = self.cal_file_data(self.file_type_match, self.top_num)
            self.check_button.config(text="Results", bg="black", command=lambda:self.to_resultsexport(data, self.file_type_all, self.file_type_match))

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

    def cal_file_data(self, file_match, top_n):
        self.extracted_data = self.extracted_file_data(file_match)
        self.association_points = self.analyse_file_data(self.extracted_data)
        self.all_association_points = self.sum_up_points(self.association_points)
        self.top_association = self.get_top_associations(self.all_association_points, top_n)

        sorted_associates = sorted(self.top_association.items(), key=lambda item: item[1], reverse=True)
        places = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        data = {
            'place': [],
            'Associate': [],
            'Points': []
        }
        for place, (associate, points) in zip(places, sorted_associates):
            data['place'].append(place)
            data['Associate'].append(associate)
            data['Points'].append(points)

        return data

    def extracted_file_data(self, file_match):
        extracted_data = {}
        for filename, file_path in file_match.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file.readline().strip()  # Skip the first line
                    remaining_lines = file.readlines()
                    for line in remaining_lines:
                        parts = line.strip().split(',')
                        if len(parts) >= 6:
                            try:
                                place = int(parts[0])
                                association = parts[5].strip()
                                extracted_data[association] = place
                            except ValueError:
                                print(f"Invalid data in line: {line.strip()}")
            except UnicodeDecodeError:
                print(f"Cannot decode file: {file_path}")
        return extracted_data

    def analyse_file_data(self, extracted_data):
        association_points = {}
        for association, place in extracted_data.items():
            points = self.place_to_points(place)
            if association in association_points:
                association_points[association].append(points)
            else:
                association_points[association] = [points]
        return association_points

    def sum_up_points(self, association_points):
        total_points = {association: sum(points) for association, points in association_points.items()}
        return total_points

    def get_top_associations(self, total_points, top_n):
        top_associations = dict(sorted(total_points.items(), key=lambda item: item[1], reverse=True)[:top_n])
        return top_associations

    def place_to_points(self, place):
        points_dict = {
            1: 8,
            2: 7,
            3: 6,
            4: 5,
            5: 4,
            6: 3,
            7: 2,
            8: 1
        }
        return points_dict.get(place, 0)

    def to_resultsexport(self, data, file_all, file_match):
        print(data)
        #ResultsExport(self, data, file_all, file_match)

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