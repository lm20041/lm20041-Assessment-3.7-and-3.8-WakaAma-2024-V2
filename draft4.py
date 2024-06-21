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
        self.headers = ['Place', 'Associate', 'Total Points']
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
        #cal file data and create table diary
        table_diary = self.cal_file_data(file_match, top_n)
        # create table data
        self.table_frame = Frame(self.parent_frame, bg=self.background)
        self.table_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        # table drawing
        self.canvas = Canvas(self.table_frame, bg="white")
        self.canvas.pack(expand=True, fill=BOTH)
        self.row_height = 30
        column_widths = self.calculate_column_widths(file_match)

        # Other code remains the same but replace 'self.column_widths' with 'column_widths'
        # ...
        self.column_widths = column_widths  # Store in self if needed elsewhere
        self.headers = ['Place', 'Associate', 'Total Points']

        # create table data
        self.create_table_data(table_diary)

    def cal_file_data(self, file_match, top_n):
        self.extracted_data = self.extracted_file_data(file_match)
        self.association_points = self.analyse_file_data(self.extracted_data)
        self.all_association_points = self.sum_up_points(self.association_points)
        self.top_association = self.get_top_associations(self.all_association_points, top_n)
        # Step 2: Sort the associates by points
        sorted_associates = sorted(self.top_association.items(), key=lambda item: item[1], reverse=True)
        # Step 3: Generate the diary entry data
        places = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        data = {
            'place': [],
            'Associate': [],
            'Points': []
        }
        #
        for place, (associate, points) in zip(places, sorted_associates):
            data['place'].append(place)
            data['Associate'].append(associate)
            data['Points'].append(points)
        return data

    def create_table_data(self, data):
        # Draw extra row on top
        self.draw_extra_row()

        # Draw headers
        self.draw_headers()

        # Draw rows
        for i, (place, associate, points) in enumerate(zip(data['place'], data['Associate'], data['Points'])):
            y = (i + 2) * self.row_height
            print(f"Drawing row at y={y} with place={place}, associate={associate}, points={points}")  # Debug statement
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
            1: 10,
            2: 8,
            3: 6,
            4: 5,
            5: 4,
            6: 3,
            7: 2,
            8: 1
        }
        return points_dict.get(place, 0)

    def calculate_column_widths(self, data):
        data = self.cal_file_data(data, top_n=8)  # Or any appropriate value for 'top_n'
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
        # Placeholder for the top extra row
        self.canvas.create_rectangle(0, 0, sum(self.column_widths), self.row_height, fill="#D3D3D3", outline="black", width=1)
        self.canvas.create_text(sum(self.column_widths) / 2, self.row_height / 2, text="Extra Row", font=("Arial", 10, "bold"))

    def draw_headers(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            print(f"Drawing header '{header}' at x={x}")  # Debug statement
            self.canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill="#EDEDED", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 8, "bold"))

    def draw_row(self, y, place, associate, points):
        values = [place, associate, points]
        for col, value in enumerate(values):
            x = sum(self.column_widths[:col])
            print(f"Drawing cell with value='{value}' at x={x}, y={y}")  # Debug statement
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, outline="black", width=1)
            wrapped_text = self.wrap_text(str(value), self.column_widths[col])
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=wrapped_text, font=("Arial", 8))

    def wrap_text(self, text, width):
        # This is a simple implementation. You may need to adjust it according to your needs.
        words = text.split()
        wrapped_lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) > width // 10:  # Rough estimate
                wrapped_lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)

        if current_line:
            wrapped_lines.append(" ".join(current_line))

        return "\n".join(wrapped_lines)

    def close_resultsexport(self, partner):
        partner.to_resultsexport_button.config(state=NORMAL)
        self.resultsexport_box.destroy()

    def end_program(self):
        root.destroy()

    def to_help(self):
        print("Help function not implemented yet.")

    def export(self):
        print("Export function not implemented yet.")

if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()
