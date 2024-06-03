from tkinter import *

class Password:
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
      entry_box.grid(row=i+2, column=1, pady=5)
      self.entry_boxes.append(entry_box) 
    # row4 Create validate button
    self.validate_button = Button(self.parent_frame, text="Validate", bg="#004C99", fg=button_fg, font=self.text_font_6, command=self.validate_entries)
    self.validate_button.grid(row=4, columnspan=2)

  def validate_entries(self):
    # Define correct values
    correct_values = ["overseers", "W@k@C1ub3234", "correct"]

    # Validate each entry
    for i, entry_box in enumerate(self.entry_boxes):
      if entry_box.get() == correct_values[i]:
        entry_box.config(bg="green")
      else:
        entry_box.config(bg="red")
        error =f"{entry_box} not correct"
        print(error)
if __name__ == "__main__":
  root = Tk()
  app = Password(root)
  root.mainloop()