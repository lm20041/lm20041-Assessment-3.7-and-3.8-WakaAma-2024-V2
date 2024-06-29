from tkinter import *
from functools import partial
from tkinter import PhotoImage
import os
import fnmatch
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
# <<<< create_file type_all, type_match >>>>
    def open_filepath(self):
        folder_name = self.entry_boxes[0].get()
        file_name = self.entry_boxes[1].get()
        # put ** in file_name so def create_file_type_match has an easier time searching for files that match with that pattern.
        file_name = f"*{file_name}*"

        self.file_type_all = self.create_file_type_all(folder_name)
        if not self.file_type_all:
            self.error_label.config(text="No matching files found.", fg="red")
            return

        self.file_type_match = self.create_file_type_match(self.file_type_all, file_name)
        if not self.file_type_match:
            self.error_label.config(text="No matching files found.", fg="red")
            return
        else:
            top_num = 8  # Define how many top associations you want to pick
            data = self.cal_file_data(self.file_type_match, top_num)

        # Check if data was created successfully
        if data and data['place']:  # Check if the data dictionary is not empty
            self.check_button.config(text="Results", bg="black", command=lambda: self.to_resultsexport(data, self.file_type_all, self.file_type_match))
            self.error_label.config(text="Data is ready. Click 'Results' to proceed.", fg="green")
        else:
            self.error_label.config(text="Data not true", fg="red")
    
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
    # <<<< NEW CAL DATA >>>>
    def cal_file_data(self, file_match, top_num):
        # contain results from all files
        add_on_file_results = {}
        for file in file_match.values():
            # collect file_results as {associates names: total points}
            file_results = self.loop_through_files(file)
            # add file_results points to any existing associates name in add_on_file_results
            for association, points in file_results.items():
                # check if there is an existing associates
                if association in add_on_file_results:
                    add_on_file_results[association].extend(points)
                else:
                    add_on_file_results[association] = points
        # points_sum_up again
        files_results = self.points_sum_up(add_on_file_results)
        # Check if there are enough associates to meet the requested top_num
        if len(files_results) < top_num:
            top_num = len(files_results)
            self.error_label.config(text=f"Sorry, we could not round up the total that you requested. File content was too low, showing top {top_num} instead.")
        # pick out the top associates
        top_associations = self.get_top_associations(files_results, top_num)
        # Step 2: Sort the associates by points
        sorted_associates = sorted(top_associations.items(), key=lambda item: item[1], reverse=True)
        # Step 3: Generate the places list based on the number of top associates
        places = [f"{i + 1}th" for i in range(top_num)]
        if top_num >= 1:
            places[0] = "1st"
        if top_num >= 2:
            places[1] = "2nd"
        if top_num >= 3:
            places[2] = "3rd"
        
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
        # return your data as {'place': [], 'Associate': [], 'Points': []}
        return data
    
    def loop_through_files(self, file_data):
        # extracted {associate name:place number}
        associate_place = self.extracted_file_data(file_data)
        # exchange places for points earned {associate name:point number}
        associate_points = self.place_to_points(associate_place)
        # add points number to their associate name {associate name:point number, number, number}
        return associate_points
    
    def extracted_file_data(self, file_data):
        extracted_data = {}
        try:
            with open(file_data, 'r', encoding='utf-8') as file:
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
            print(f"Cannot decode file: {file_data}")
        return extracted_data
    
    def place_to_points(self, associate_place):
        association_points = {}
        # what number of place earns what points
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
        # convert associate_place list to associate_points
        for association, place in associate_place.items():
            association_points[association] = [points_dict.get(place, 0)]
        return association_points
    
    def add_points_together(self, associate_points):
        associate_add_point = {}
        for association, points in associate_points.items():
            if association in associate_add_point:
                associate_add_point[association].append(points)
            else:
                associate_add_point[association] = points
        return associate_add_point
    
    def points_sum_up(self, associate_add_point):
        total_points = {association: sum(points) for association, points in associate_add_point.items()}
        return total_points
    
    def get_top_associations(self, total_points, top_n):
        top_associations = dict(sorted(total_points.items(), key=lambda item: item[1], reverse=True)[:top_n])
        return top_associations
    def to_resultsexport(self, data, file_all, file_match):
        ResultsExport(self, data, file_all, file_match)
    
    def to_help(self):
        pass
    
    def close_convertor(self, partner):
        # Put to_convertor button back to normal (uncomment when using with the main app)
        # partner.to_convertor_button.config(state=NORMAL)
        self.convertor_box.destroy()
# <<<< ResultsExport >>>>
class ResultsExport:
    def __init__(self, partner, data, file_type_all, file_type_match):
        # input var's
        self.data = data
        self.file_type_all = file_type_all
        self.file_type_match = file_type_match
        self.current_list = file_type_match
        # Initialize a list to store image references
        self.image_refs = []  # This line initializes the list
        # setting var's
        self.text_font_12 = ("Arial", "12", "bold")
        self.text_font_6 = ("Arial", "6")
        self.but_font_8 = ("Arial", "8", "bold")
        self.but_width = 8
        self.but_height = 1
        self.text_fg = "#FFFFFF"
        self.background = "white"
        # << partner >>
        self.results_export_box = Toplevel()
        # Disable to_convertor button (uncomment when using with the main app)
        partner.check_button.config(state=DISABLED)
        self.results_export_box.protocol('WM_DELETE_WINDOW', partial(self.close_results_export, partner))

        self.parent_frame = Frame(self.results_export_box, bg=self.background)
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
        self.end_program_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="End Program", bg="black", fg=button_fg, font=self.but_font_8, command=self.close_results_export)
        self.end_program_button.grid(row=6, column=0)
        self.help_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Help", bg="#F4A434", fg=button_fg, font=self.but_font_8, command=self.to_help)
        self.help_button.grid(row=6, column=2)
    #<<<<<        table_widgets        >>>>>
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
    def close_results_export(self, partner):
        partner.check_button.config(state=NORMAL)
        self.results_export_box.destroy()
    def to_help(self):
        pass

if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()