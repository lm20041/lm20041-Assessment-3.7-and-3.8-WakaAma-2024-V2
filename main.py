from tkinter import *

class MyFirstWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("My First Tkinter Window")
        #self.master.geometry("400x300")
        self.master.configure(bg="#FFFFFF", borderwidth=10, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.background = "white"
        self.bold_font_12 = ("Arial", 12, "bold")
        self.text_font_6 = ("Arial", 10)
        self.txt_fg = "black"
        self.create_widgets()

    def create_widgets(self):
        # Create the parent frame
        self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
        self.parent_frame.grid(padx=10, pady=10)
        # row 0 Create a label widget using .grid
        self.label = Label(self.parent_frame, text="Hello, Tkinter!", font=self.bold_font_12)
        self.label.grid(row=0, columnspan=2, padx=20, pady=20)
        # row 1 Entry labels and boxes
        entry_labels = ["Entry 1", "Entry 2", "Entry 3"]
        self.entry_boxes = []

        for i, label in enumerate(entry_labels):
          Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i, column=0, sticky=E)
          entry_box = Entry(self.parent_frame, font=self.text_font_6)
          entry_box.grid(row=i, column=1, pady=5)
          self.entry_boxes.append(entry_box)

        # Create a button widget using .grid
        self.button = Button(self.parent_frame, text="Click Me!", font=self.bold_font_12, command=self.on_button_click)
        self.button.grid(row=2, columnspan=2, padx=20, pady=10)

    def on_button_click(self):
        MySecondWindow(self.master)

class MySecondWindow:
    def __init__(self, master):
        # Create a new top-level window
        self.new_window = Toplevel(master)
        self.new_window.title("My Second Tkinter Window")
        self.new_window.configure(bg="#FFFFFF", borderwidth=10, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
    
        self.bold_font_12 = ("Arial", 12, "bold")
        self.text_font_6 = ("Arial", 10)
    
        self.create_widgets()
    
    def create_widgets(self):
        # Create the parent frame
        self.parent_frame = Frame(self.new_window, bg="lightgrey", borderwidth=2, relief="ridge")
        self.parent_frame.grid(padx=10, pady=10)
    
        # row 0 Create a label widget
        self.label = Label(self.parent_frame, text="Welcome to the second window!", font=self.bold_font_12)
        self.label.grid(row=0, columnspan=2, padx=20, pady=20)
        # row 2
    
        # row 3 Create another button to close the second window
        self.close_button = Button(self.parent_frame, text="Close", font=self.bold_font_12, command=self.new_window.destroy)
        self.close_button.grid(row=1, columnspan=2, padx=20, pady=10)

# Create the main window and run the application
if __name__ == "__main__":
    root = Tk()
    app = MyFirstWindow(root)
    root.mainloop()