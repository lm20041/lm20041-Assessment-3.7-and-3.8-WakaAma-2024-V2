from tkinter import *
from functools import partial

class Convertor:
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
    # row5 Create buttons
    self.to_resultsexport_button = Button(self.parent_frame, width=8, height=1, text="check", bg=button_bg, fg=button_fg, font=self.text_font_6, command=self.to_resultsexport)
    self.to_resultsexport_button.grid(row=5, column=0)
    self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=self.to_help)
    self.help_button.grid(row=5, column=1)
  def to_resultsexport(self):
    ResultsExport(self)
  def to_help(self):
    pass
class ResultsExport:
  def __init__(self, partner):
    #vars
    self.text_font_12 = ("Arial", "12", "bold")
    self.text_font_6 = ("Arial", "6")
    self.text_fg = "#FFFFFF"
    self.background = "white"
    self.resultsexport_box = Toplevel()

    # disable to_resultsexport_button
    partner.to_resultsexport_button.config(state=DISABLED)

    # If users press cross at top, closes convertor and 'releases' convertor button
    self.resultsexport_box.protocol('WM_DELETE_WINDOW', partial(self.close_resultsexport, partner))

    self.parent_frame = Frame(self.resultsexport_box, bg=self.background)
    self.parent_frame.grid(padx=10, pady=10)

    self.create_widgets(partner)
  def create_widgets(self, partner):
    #var
    button_fg = "white"
    button_bg = "#004C99"
    # Define entry labels
    entry_labels = ["folder name:", "file name:"]
    self.entry_boxes = []
    # row 2 frame

    # row 4 label, entry box, button
    self.entry_label = Label(self.parent_frame, text="name your results:", font=self.text_font_12, bg=self.background).grid(row=4, column=0, sticky=W, padx=5)
    self.entry_box = Entry(self.parent_frame, font=self.text_font_6).grid(row=4, column=1, padx=5)
    self.Export_button = Button(self.parent_frame, width=8, height=1, text="Export", bg="#004C99", fg=button_fg, font=self.text_font_6, command=self.export).grid(row=4, column=2)

    # row 5 error message
    self.error_label = Label(self.parent_frame, text="", font=self.text_font_6,wraplength=400, bg=self.background, fg="red")
    self.error_label.grid(row=4, columnspan=3)
    # row 6 button
    self.end_program_button = Button(self.parent_frame, width=8, height=1, text="End Program", bg="black", fg=button_fg, font=self.text_font_6, command=self.end_program)
    self.end_program_button.grid(row=6, column=0)
    self.help_button = Button(self.parent_frame, width=8, height=1, text="Help", bg="#F4A434", fg=button_fg, font=self.text_font_6, command=self.to_help)
    self.help_button.grid(row=6, column=2)
  def export(self):
    pass
  def end_program(self):
    pass
  def to_help(self):
    pass
  def close_resultsexport(self, partner):
    partner.to_resultsexport_button.config(state=NORMAL)
    self.resultsexport_box.destroy()
if __name__ == "__main__":
  root = Tk()
  app = Convertor(root)
  root.mainloop()