from tkinter import *
from tkinter import PhotoImage
from functools import partial
import tkinter.font as tkFont
import os
import fnmatch
import csv
from tkinter import filedialog

# <<<< class MainWindow >>>>
class MainWindow:
    def __init__(self, master):
        self.master = master #Using this in windows settings to allow easy placement of frames
        self.master.title("App Waka Culb")
        self.master.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.text_font_6 = ("Arial", "12", "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        # Track if Help window is open
        self.help_window_open = False
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)
    
        self.create_widgets()
    def create_widgets(self):
        #var
        button_fg = "white"
        button_bg = "#004C99"
        # row 0 text
        self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=self.text_font_6, bg=self.background)
        self.heading_label.grid(row=0, columnspan=2)
    
        # row 1 Load the image
        image_path = "images.png"
        image = PhotoImage(file=image_path)
        # Resize the image to roughly 50x50 pixels
        image = image.subsample(image.width() // 150, image.height() // 80)
        # Create a label to display the image
        self.image_label = Label(self.parent_frame, image=image)
        self.image_label.image = image  # Store a reference to the PhotoImage object
        self.image_label.grid(row=1, columnspan=2, padx=20, pady=20)
        # row 2 text
        txt = "this program is created to help the Waka Ama club sort through their recorded files from the race to determine the associated winner of place. This app is only to be used by the Waka Ama club therefore a password will be needed to access this app. if you were kind of club and you have not received the password please contact {phone number}."
        self.text_label = Label(self.parent_frame, text=txt, font=("Arial", "8"), wraplength=350, bg=self.background)
        self.text_label.grid(row=2, columnspan=2)
        # row 4
        self.to_password_button = Button(self.parent_frame, width=8, height=1, text="Start", font=self.text_font_6, bg=button_bg, fg=button_fg, command=self.to_password)
        self.to_password_button.grid(row=4, column=0, pady=10)
        self.to_help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command= self.open_help)
        self.to_help_button.grid(row=4, column=1)
    def to_password(self):
        Password(self)
    def open_help(self):
        self.help_manager = Help(self)
        self.help_manager.open_help()

# <<<< class password >>>>
class Password:
    def __init__(self, partner):
        # Var's
        self.text_font_6 = ("Arial", "12", "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        # add <partner>
        self.password_box = Toplevel()
        partner.to_password_button.config(state=DISABLED)
        self.password_box.protocol('WM_DELETE_WINDOW', partial(self.close_password, partner))
        # parent_frame
        self.parent_frame = Frame(self.password_box, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)
    
        self.create_widgets()
    def create_widgets(self):
        #var
        button_fg = "white"
        # Define entry labels
        entry_labels = ["username", "password"]
        self.entry_boxes = []
        # row0
        self.heading_label = Label(self.parent_frame, text="Waka Ama", font=self.text_font_6, bg=self.background)
        self.heading_label.grid(row=0, columnspan=2)
        # row1
        txt="if Wakana culb member please enter password below"
        self.text_label = Label(self.parent_frame, text=txt, font=("Arial", "10"), bg=self.background)
        self.text_label.grid(row=1, columnspan=2)
    
        # row2 Create entry labels and boxes
        for i, label in enumerate(entry_labels):
            # Create and place the label above the entry box
            Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i+2, column=0, sticky=W, padx=5, pady=(10, 0))
            entry_box = Entry(self.parent_frame, font=self.text_font_6)
            show_char = '*' if label == "password" else ''
            entry_box.grid(row=i+2, column=1, pady=5)
            entry_box.config(highlightthickness=2, show=show_char, highlightbackground="grey", highlightcolor="blue")
            
            self.entry_boxes.append(entry_box) 
        # row4 Create validate button
        self.validate_button = Button(self.parent_frame, text="Validate", bg="#004C99", fg=button_fg, font=self.text_font_6, command=self.validate_entries)
        self.validate_button.grid(row=4, columnspan=2)
        # row5
        self.error_label = Label(self.parent_frame, text="", font=self.text_font_6,wraplength=400, bg=self.background, fg="red")
        self.error_label.grid(row=5, columnspan=2, sticky=W)

    def validate_entries(self):
        # Define correct values
        correct_values = ["overseers", "W@k@C1ub3234", "correct"]
        error_messages = [
          "Please enter in your user and password before continuing",
          "Sorry, no space allowed",
          "Invalid username",
          "Invalid password"
          ]
    
        all_valid = True
        error_message = "Errors:"
        for i, entry_box in enumerate(self.entry_boxes):
            entry_value = entry_box.get()
            # Check if the entry value is empty
            if entry_value == "":  
                entry_box.config(bg="red")
                error_message = error_messages[0]
                all_valid = False
                break
            elif ' ' in entry_value:
                entry_box.config(bg="red")
                error_message = error_messages[1]
                all_valid = False
                break
            elif entry_value != correct_values[i]:
                entry_box.config(bg="red")
                error_message = error_messages[i+2]
                all_valid = False
                break
            else:
                entry_box.config(bg="green")
        if all_valid:
            self.to_convertor()
        else:
            self.error_label.config(text=error_message, fg="red")
            for entry_box in self.entry_boxes:
                entry_box.config(bg="red", highlightbackground="pink", highlightcolor="black")
    def close_password(self, partner):
        partner.to_password_button.config(state=NORMAL)
        self.password_box.destroy()
    def to_convertor(self):
        Convertor(self)

# <<<< Convertor >>>>
class Convertor:
    def __init__(self, partner):
        # Vars
        self.text_font_6 = ("Arial", 12, "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.convertor_box = Toplevel()

        # Disable to_convertor button (uncomment when using with the main app)
        partner.validate_button.config(state=DISABLED)

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

        self.to_help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command= self.open_help)
        self.to_help_button.grid(row=5, column=1)
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

    def open_help(self):
        self.help_manager = Help(self)
        self.help_manager.open_help()

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
        self.results_export_box.geometry("500x350")
        # Disable to_convertor button (uncomment when using with the main app)
        partner.check_button.config(state=DISABLED)
        self.results_export_box.protocol('WM_DELETE_WINDOW', partial(self.close_results_export, partner))

        # Create canvas and scrollbar
        self.canvas = Canvas(self.results_export_box, bg=self.background)
        self.scrollbar = Scrollbar(self.results_export_box, orient=VERTICAL, command=self.canvas.yview)
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
        self.heading_label = Label(self.parent_frame, text='Results/Export', font=self.text_font_12, wraplength=350, bg=self.background)
        self.heading_label.grid(row=0, columnspan=6, sticky="W")
        # row 1 text
        intro_txt = "This program has produced a table results on the left hand side of the window. displaying the top eight associate places we search from all files in your chosen folder {}. Files that match up with the file name of your choice {}. You can save your table result into the file browser on the right hand side of the window. Make sure to enter a name for it and the entry box down below or just collect exploits button and the default name will be set. The file browser can display all your files in the folder or just the ones you called on. Each name shown in the files will have an attachment link that when click on will open a window displaying the file contents. You can also use it to search up pacific names in your name files"
        self.intro_label = Label(self.parent_frame, text=intro_txt, font=self.text_font_6, wraplength=450, bg=self.background)
        self.intro_label.grid(row=1, columnspan=6, padx=10)
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
        self.text_label = Label(self.parent_frame, text=entry_txt, font=self.text_font_6, wraplength=350, bg=self.background)
        self.text_label.grid(row=3, columnspan=6)
        # row 4 lable, enrty, button
        self.entry_label = Label(self.parent_frame, text="Name your results:", font=("Arial", "8", "bold"), bg=self.background) 
        self.entry_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=5)
        self.entry_box = Entry(self.parent_frame, font=self.text_font_6)
        self.entry_box.grid(row=4, column=2, columnspan=2, padx=5)
        self.export_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Export", bg=button_bg, fg=button_fg, font=self.but_font_8, command=self.export)
        self.export_button.grid(row=4, column=4, columnspan=2)
        # row 5 text 
        self.error_label = Label(self.parent_frame, width=self.but_width, height=self.but_height, text="", font=self.text_font_6, wraplength=400, bg=self.background, fg="red")
        self.error_label.grid(row=5, columnspan=6, pady=5)
        # row 6 buttons
        self.end_program_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="End Program", bg="black", fg=button_fg, font=self.but_font_8, command=self.close_results_export)
        self.end_program_button.grid(row=6, column=0, columnspan=3)
        self.to_help_button = Button(self.parent_frame, width=self.but_width, height=self.but_height, text="Help", bg="#F4A434", fg=button_fg, font=self.but_font_8, command=self.open_help)
        self.to_help_button.grid(row=6, column=3,  columnspan=3)
    #<<<<<        table_widgets        >>>>>
    def create_table_widgets(self):
        # Table vars
        self.frame_heading = "#CCCCCC" 
        self.frame_body = "#EDEDED"
        self.row_height = 30
        self.total_table_width = 230  # Fixed total table width
        self.column_widths = [50, 120, 60]  # Example: middle column is 80 pixels wide
        self.heading = 'Full Club Points'
        self.headers = ['Place', 'Associate', 'Total\nPoints']
        self.num_rows = min(len(self.data['place']), 8)  # Ensure we only display up to 8 rows
        self.num_headers = len(self.headers)

        # Calculate canvas dimensions
        self.canvas_width = self.total_table_width
        self.canvas_height = (self.num_rows + 2) * self.row_height  # +2 for extra row and headers

        # Create canvas with the exact size
        self.table_canvas = Canvas(self.table_frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.table_canvas.pack(expand=False, fill=None)

        # Draw table
        self.draw_extra_row()
        self.draw_3_header()

        for i, (place, associate, points) in enumerate(zip(self.data['place'], self.data['Associate'], self.data['Points'])):
            if i >= 8:  # Limit the display to 8 rows
                break
            y = (i + 2) * self.row_height  # Adjust y position by +2 to account for extra row and headers
            self.draw_8_rows(y, place, associate, points)

    def draw_extra_row(self):
        x_start = 0
        y_start = 0
        x_end = self.canvas_width
        y_end = self.row_height

        self.table_canvas.create_rectangle(x_start, y_start, x_end, y_end, fill=self.frame_heading, outline="black", width=1)
        self.table_canvas.create_text(x_end / 2, y_end / 2, text="Full Club Points", font=("Arial", 10, "bold"), anchor="center")

    def draw_3_header(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.table_canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill=self.frame_body, outline="black", width=1)
            self.table_canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"), anchor="center")
        self.table_canvas.create_line(0, 2 * self.row_height, self.canvas_width, 2 * self.row_height, fill="black")

    def draw_8_rows(self, y, place, associate, points):
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            cell_width = self.column_widths[col]

            # Create rectangle for the cell
            self.table_canvas.create_rectangle(x, y, x + cell_width, y + self.row_height, fill=self.frame_body, outline="black", width=1)
            # Adjust wrap length based on cell width
            wrap_length = cell_width - 10  # Adjust as needed
            if col == 1:  # Adjust font size for the 'Associate' column
                font_size = ("Arial", 8)  # Adjust as needed specifically for Associate column
            else:
                font_size = ("Arial", 10)  # Adjust as needed for other columns

            # Create text with wrapping inside the cell
            text_id = self.table_canvas.create_text(x + cell_width / 2, y + self.row_height / 2, text=value, font=font_size, anchor="center", width=wrap_length)

            # Get current text dimensions
            text_bbox = self.table_canvas.bbox(text_id)
            text_height = text_bbox[3] - text_bbox[1]

            # Adjust cell height if text exceeds current row_height
            if text_height > self.row_height - 5:  # Adjust -5 for padding
                new_height = text_height + 10  # Adjust 10 for padding
                self.table_canvas.coords(text_id, x + cell_width / 2, y + new_height / 2)  # Move text to center of new height
                self.table_canvas.itemconfig(text_id, width=wrap_length)  # Update text wrapping width
                self.table_canvas.itemconfig(self.table_canvas.find_withtag("cell_rect"), height=new_height)  # Update cell height

    def export(self):
        filename = self.entry_box.get()
        if not filename:
            self.error_label.config(text="Please enter a filename.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=filename, filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not file_path:
            self.error_label.config(text="Save cancelled.")
            return
        # Check for invalid characters in the filename
        if re.search(r'[<>:"/\\|?*\s]', filename):
            self.error_label.config(text="Filename cannot contain spaces or any of the following characters: <>:\"/\\|?*")
            return
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                for place, associate, points in zip(self.data['place'], self.data['Associate'], self.data['Points']):
                    writer.writerow([place, associate, points])
            self.error_label.config(text="File saved successfully.", fg="green")
        except Exception as e:
            self.error_label.config(text=f"Error saving file: {e}", fg="red")

    def create_file_widgets(self):
        pass

    def close_results_export(self, partner):
        print("close_results_export called")  # Debugging print statement
        partner.check_button.config(state=NORMAL)
        self.results_export_box.destroy()
        print("Window should be destroyed")  # Debugging print statement

    def open_help(self):
        self.help_manager = Help(self)
        self.help_manager.open_help()
# <<<<           Help           >>>>
class Help:
    def __init__(self, partner):
        # Var's
        self.text_font_12 = ("Arial", "12", "bold")
        self.text_font_6 = ("Arial", "6")
        self.but_font_8 = ("Arial", "8", "bold")
        self.but_width = 8
        self.but_height = 1
        self.text_fg = "#FFFFFF"
        self.background = "#FFE0BD"
        # <<<< linke to all window <<<<
        #self.parent = partner  # Parent widget or window
        self.help_window = None  # Placeholder for the help window
        
        self.create_widgets()
    def create_widgets(self):
        # Method to open the help window
        if self.help_window is None:
            self.help_window = Toplevel()
            #self.help_window.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
            # parent_frame
            self.parent_frame = Frame(self.help_window, bg=self.background)
            self.parent_frame.grid(padx=10, pady=10)
            #var
            button_fg = "white"
            button_bg = "black"
            # row 0 text
            self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=self.text_font_12, bg=self.background)
            self.heading_label.grid(row=0)
            
            # row 1 text
            txt = "-Once you're done press the end program button and it will take you back to the collector window where again you can input a file and a file name to research about\n-To use this program simply enter the password and username you have been given you will only be given free tries once your free tries are up you'll be locked out.\n-Then input your folder and file name so that the program knows exactly what folder and what type of file does search inside it.\n-The export button will save your table results and put it into folder this change will be displayed on file browser.\n-You can use file browser diary this to scroll in and out of folders to get to the file.\n-Use file types to switch from displaying all files to files that match up with the chosen file name.\n-The search entry just below the screen can be used to search up any particular name of file displayed on browser.\n-Click on a file inside to open up a window displaying the file contents"
            self.text_label = Label(self.parent_frame, text=txt, font=self.text_font_6, wraplength=350, bg=self.background)
            self.text_label.grid(row=1)
            # row 2
            self.Dismissed_button = Button(self.parent_frame, width=8, height=1, text="Dismissed_button", font=self.but_font_8, bg=button_bg, fg=button_fg, command=self.close_help)
            self.Dismissed_button.grid(row=2, pady=10)

    def close_help(self):
        # Method to close the help window
        if self.help_window is not None:
            self.help_window.destroy()  # Destroy the help window
            self.help_window = None
            # Additional cleanup or actions related to closing the help window
if __name__ == "__main__":
  root = Tk()
  app = MainWindow(root)
  root.mainloop()