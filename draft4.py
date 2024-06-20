# unknown drag,  we need to work from scratch
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

class ResultsExport:
    def __init__(self, partner, file_all, file_match):
        self.text_font_12 = ("Arial", "12", "bold")
        self.text_font_6 = ("Arial", "6")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.resultsexport_box = Toplevel()

        partner.to_resultsexport_button.config(state=DISABLED)
        self.resultsexport_box.protocol('WM_DELETE_WINDOW', partial(self.close_resultsexport, partner))

        self.parent_frame = Frame(self.resultsexport_box, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets(partner, file_all, file_match)

    def create_widgets(self, partner, file_all, file_match):
        button_fg = "white"
        button_bg = "#004C99"

        self.create_table(file_match)
        self.create_file_screen(file_match, file_all)

        self.entry_label = Label(self.parent_frame, text="Name your results:", font=self.text_font_12, bg=self.background)
        self.entry_label.grid(row=4, column=0, sticky=W, padx=5)
        self.entry_box = Entry(self.parent_frame, font=self.text_font_6)
        self.entry_box.grid(row=4, column=1, padx=5)
        self.export_button = Button(self.parent_frame, width=8, height=1, text="Export", bg=button_bg, fg=button_fg, font=self.text_font_6, command=self.export)
        self.export_button.grid(row=4, column=2)

        self.error_label = Label(self.parent_frame, text="", font=self.text_font_6, wraplength=400, bg=self.background, fg="red")
        self.error_label.grid(row=5, column=0, columnspan=3, pady=5)

        self.end_program_button = Button(self.parent_frame, width=8, height=1, text="End Program", bg="black", fg=button_fg, font=self.text_font_6, command=self.end_program)
        self.end_program_button.grid(row=6, column=0)
        self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=self.to_help)
        self.help_button.grid(row=6, column=2)

    def create_file_screen(self, file_match, file_all):
        print('<<<<<file_all>>>>')
        for filename, file_path in file_all.items():
            print(f'file_all: {filename}')
            print(f'{file_path}\n\n')
        print('<<<<<file_match>>>>')
        for filename, file_path in file_match.items():
            print(f'file_match: {filename}')
            print(f'{file_path}\n\n')

    def create_table(self, file_match):
        button_fg = "white"
        button_bg = "#004C99"
        top_n = 8

        self.table_frame = Frame(self.parent_frame, bg=self.background)
        self.table_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        # table drawing
        self.canvas = Canvas(self.table_frame, bg="white")
        self.canvas.pack(expand=True, fill=BOTH)
        self.row_height = 30
        self.column_widths = self.calculate_column_widths(data)
        self.headers = ['Place', 'Associate', 'Total Points']

        #cal file data
        self.cal_file_data(file_match)
        # create table data
        self.create_table_data(data)
    def cal_file_data(self, file_match):
        self.extracted_data = self.extracted_file_data(file_match)
        self.association_points = self.analyse_file_data(self.extracted_data)
        self.all_association_points = self.sum_up_points(self.association_points)
        self.top_association = self.get_top_associations(self.all_association_points, top_n)
    def create_table_data(self, data):
        # Draw extra row on top
        self.draw_extra_row()

        # Draw headers
        self.draw_headers()

        # Draw rows
        for i, (place, associate, points) in enumerate(zip(data['place'], data['Associate'], data['Points'])):
            y = (i + 2) * self.row_height
            self.draw_row(y, place, associate, points)
# <<<< CAL file data >>>>
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
        points = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
        association_points = {}
        for association, place in extracted_data.items():
            if place in points:
                if association in association_points:
                    association_points[association] += points[place]
                else:
                    association_points[association] = points[place]
        return association_points

    def sum_up_points(self, association_points):
        total_points = {}
        for association, points in association_points.items():
            if association in total_points:
                total_points[association] += points
            else:
                total_points[association] = points
        return total_points

    def get_top_associations(self, total_points, top_n=8):
        sorted_associations = sorted(total_points.items(), key=lambda item: item[1], reverse=True)
        top_associations = dict(sorted_associations[:top_n])
        return top_associations
#<<<<   draw table   >>>>>>
    def calculate_column_widths(self, data):
        # Calculate maximum content width for each column
        max_widths = [
            max(len(str(item)) for item in data[key]) for key in data.keys()
        ]
        # Ensure columns are wide enough for headers as well
        header_widths = [len(header) for header in self.headers]

        # Final column widths with some padding
        column_widths = [max(content, header) * 10 + 10 for content, header in zip(max_widths, header_widths)]

        return column_widths
    def draw_extra_row(self):
        # Define the extra row content and position
        x_start = 0
        y_start = 0
        x_end = sum(self.column_widths)
        y_end = self.row_height

        # Draw the rectangle using those x, y points
        self.canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="#CCCCCC", outline="black", width=1)
        # Draw the text centered in the row
        self.canvas.create_text(x_end / 2, y_end / 2, text="Full Club Points", font=("Arial", 10, "bold"))
    def draw_headers(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill="#EDEDED", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"))
        self.canvas.create_line(0, 2 * self.row_height, sum(self.column_widths), 2 * self.row_height, fill="black")
    def draw_row(self, y, place, associate, points):
        # Draw cells
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            wrapped_text = self.wrap_text(str(value), self.column_widths[col])
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=wrapped_text, font=("Arial", 10), anchor="center")
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, outline="black", width=1)

#<<<<       >>>>>
    def export(self):
        print('export')

    def end_program(self):
        print('end program')

    def to_help(self):
        print('help')

    def close_resultsexport(self, partner):
        partner.to_resultsexport_button.config(state=NORMAL)
        self.resultsexport_box.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()