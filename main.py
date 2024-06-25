import os
import fnmatch
from tkinter import *
from functools import partial
# <<<< Convertor >>>>
class Convertor:
  def __init__(self, partner):
    #vars
    self.text_font_6 = ("Arial", "12", "bold")
    self.text_fg = "#FFFFFF"
    self.background = "white"
    self.convertor_box = Toplevel()

    # disable to_convertor button
    #partner.to_convertor_button.config(state=DISABLED)

    # If users press cross at top, closes convertor and 'releases' password button
    self.convertor_box.protocol('WM_DELETE_WINDOW', partial(self.close_convertor, partner))

    self.parent_frame = Frame(self.convertor_box, bg=self.background)
    self.parent_frame.grid(padx=10, pady=10)

    self.create_widgets(partner)
  def create_widgets(self, partner):
    #var
    button_fg = "white"
    button_bg = "#004C99"
    # Define entry labels
    entry_labels = ["folder name:", "file name:"]
    self.entry_boxes = []
    # row0
    self.heading_label = Label(self.parent_frame, text="Convertor", font=self.text_font_6, bg=self.background)
    self.heading_label.grid(row=0, columnspan=2)
    # row1
    txt="please enter folder name and file name so we can begin. please press check to see if this information is valid. if it is press reults."
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
    # row4
    self.error_label = Label(self.parent_frame, text="", font=("Arial", "10"),wraplength=400, bg=self.background, fg="red")
    self.error_label.grid(row=4, columnspan=2)
    # row5 Create buttons
    self.check_button = Button(self.parent_frame, width=8, height=1, text="check", bg=button_bg, fg=button_fg, font=self.text_font_6, command=self.open_filepath)
    self.check_button.grid(row=5, column=0)
    self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=self.validate_entries)
    self.help_button.grid(row=5, column=1)
  def open_filepath():
    pass
  def list_filepath():
    pass
  def to_help(self, partner):
    pass
  def close_convertor(self, partner):
    #put to_convertor button back to normal
    #partner.to_convertor_button.config(state=NORMAL)
    self.convertor_box.destroy()
if __name__ == "__main__":
    root = Tk()
    app = Convertor(root)
    root.mainloop()