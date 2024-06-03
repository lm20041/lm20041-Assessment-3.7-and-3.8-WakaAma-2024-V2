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
    # Define entry labels
    entry_labels = ["username", "password"]
    self.entry_boxes = []
    # row0
    self.heading_label = Label(self.parent_frame, text="Waka Ama", font=("Arial", "16", "bold"))
    self.heading_label.grid(row=0)
    # row1
    txt="if Wakana culb member please enter password below"
    self.text_label = Label(self.parent_frame, text=txt, font=("Arial", "10"))
    self.text_label.grid(row=1)

    # row2 Create entry labels and boxes
    for i, label in enumerate(entry_labels):
      # Create and place the label above the entry box
      Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i, column=0, sticky=W, padx=5, pady=(10, 0))
      entry_box = Entry(self.parent_frame, font=self.text_font_6)
      entry_box.grid(row=i, column=1, pady=5)
      self.entry_boxes.append(entry_box) 
    # row3
if __name__ == "__main__":
  root = Tk()
  app = Password(root)
  root.mainloop()