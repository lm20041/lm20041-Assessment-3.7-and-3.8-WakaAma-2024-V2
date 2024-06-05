from tkinter import *
from functools import partial

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
    # row 0 text
    self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=self.text_font_6, bg=self.background)
    self.heading_label.grid(row=0)
    # row 1 image
    image_pathway="image here"
    self.image_label = Label(self.parent_frame, text=image_pathway, font=("Arial", "10"), bg=self.background)
    self.image_label.grid(row=1)
    # row 2 text
    txt = "this program is created to help the Waka Ama club sort through their recorded files from the race to determine the associated winner of place. This app is only to be used by the Waka Ama club therefore a password will be needed to access this app. if you were kind of club and you have not received the password please contact {phone number}."
    self.text_label = Label(self.parent_frame, text=txt, font=("Arial", "10"),wraplength=250, bg=self.background)
    self.text_label.grid(row=2)
    # row 4
    self.to_password_button = Button(self.parent_frame, text="Submit", command=self.to_password)
    self.to_password_button.grid(row=4, pady=10)
  def to_password(self):
    Password(self)

class Password:
  def __init__(self, partner):
    #set up dialogue box and background colour
    background = "#ffe6cc"
    self.password_box = Toplevel()

    # disable to_password button
    partner.to_password_button.config(state=DISABLED)

    # If users press cross at top, closes password and 'releases' password button
    self.password_box.protocol('WM_DELETE_WINDOW', partial(self.close_password, partner))

    
    self.parent_frame = Frame(self.password_box, bg=background)
    self.parent_frame.grid(padx=10, pady=10)

    self.create_widgets(partner)
  def create_widgets(self, partner):
    #var
    button_fg = "white"
    # row 0
    # row 1
    # row 2
    # row 4
    self.dismiss_password_button = Button(self.parent_frame, text="Submit", command=partial(self.close_password, partner))
    self.dismiss_password_button.grid(row=4, pady=10)
  # closes password dialogue (used by button and x at top of dialogue)
  def close_password(self, partner):
    #put help button back to normal...
    partner.to_password_button.config(state=NORMAL)
    self.password_box.destroy()

if __name__ == "__main__":
  root = Tk()
  app = MainWindow(root)
  root.mainloop()