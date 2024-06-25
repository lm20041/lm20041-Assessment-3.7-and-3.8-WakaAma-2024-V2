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
# <<<< Pasword Class >>>>
#
if __name__ == "__main__":
  root = Tk()
  app = MainWindow(root)
  root.mainloop()