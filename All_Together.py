import os
import fnmatch
from tkinter import *
from functools import partial
from tkinter import *
from functools import partial
# <<<< class MainWindow >>>>
class MainWindow:
  def __init__(self, master):
    self.master = master #Using this in windows settings to allow easy placement of frames
    self.master.title("Entry Password")
    self.master.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
    self.text_font_6 = ("Arial", "12", "bold")
    self.text_fg = "#FFFFFF"
    self.background = "white"
    self.parent_frame = Frame(self.master, bg=self.background)
    self.parent_frame.grid(padx=10, pady=10)

    self.create_widgets()
  def create_widgets(self):
    #var
    button_fg = "white"
    button_bg = "#004C99"
    # row 0 text
    self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=self.text_font_6, bg=self.background)
    self.heading_label.grid(row=0)

    # row 1 Load the image
    image_path = "images.png"
    image = PhotoImage(file=image_path)
    # Resize the image to roughly 50x50 pixels
    image = image.subsample(image.width() // 150, image.height() // 80)
    # Create a label to display the image
    self.image_label = Label(self.parent_frame, image=image)
    self.image_label.image = image  # Store a reference to the PhotoImage object
    self.image_label.grid(row=1, padx=20, pady=20)
    # row 2 text
    txt = "this program is created to help the Waka Ama club sort through their recorded files from the race to determine the associated winner of place. This app is only to be used by the Waka Ama club therefore a password will be needed to access this app. if you were kind of club and you have not received the password please contact {phone number}."
    self.text_label = Label(self.parent_frame, text=txt, font=("Arial", "8"), wraplength=350, bg=self.background)
    self.text_label.grid(row=2)
    # row 4
    self.to_password_button = Button(self.parent_frame, width=8, height=1, text="Start", font=self.text_font_6, bg=button_bg, fg=button_fg, command=self.to_password)
    self.to_password_button.grid(row=4, pady=10)
  def to_password(self):
    Password(self)
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
            self.cal_file_data(self.file_type_match, self.top_num)

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
    # <<<< cal_file_data >>>>
    def cal_file_data(self, file_match, top_n):

        #  config check_button to Results_button
        self.check_button.config(text="Results", bg="black", command=lambda:self.to_resultsexport(data, file_all, file_match))

    def to_resultsexport(self, data, file_all, file_match):
        ResultsExport(self, data, file_all, file_match)

    def to_help(self):
        pass

    def close_convertor(self, partner):
        # Put to_convertor button back to normal (uncomment when using with the main app)
        # partner.to_convertor_button.config(state=NORMAL)
        self.convertor_box.destroy()

if __name__ == "__main__":
  root = Tk()
  app = MainWindow(root)
  root.mainloop()