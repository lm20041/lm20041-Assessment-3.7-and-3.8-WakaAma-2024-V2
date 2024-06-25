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
    self.parent_frame = Frame(self.master, bg=self.background)
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
      self.error_label.config(text="All entries are valid.", fg="green")
      for entry_box in self.entry_boxes:
        entry_box.config(bg="green", highlightbackground="lime", highlightcolor="black")
    else:
      self.error_label.config(text=error_message, fg="red")
      for entry_box in self.entry_boxes:
        entry_box.config(bg="red", highlightbackground="pink", highlightcolor="black")
  def close_password(self, partner):
    partner.to_password_button.config(state=NORMAL)
    self.password_box.destroy()
if __name__ == "__main__":
  root = Tk()
  app = MainWindow(root)
  root.mainloop()