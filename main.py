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
        # row 1
        self.entry_label = Label(self.parent_frame, text="This is a label", font=self.bold_font_12)
        self.entry_label.grid(row=1, column=0, padx=20, pady=20)
        entry_box = Entry(self.parent_frame, font=self.text_font_6)
        entry_box.grid(row=1, column=1, pady=5)

        # Create a button widget using .grid
        self.button = Button(self.parent_frame, text="Click Me!", font=self.bold_font_12, command=self.on_button_click)
        self.button.grid(row=2, columnspan=2, padx=20, pady=10)

    def on_button_click(self):
        print("Button Clicked!")

# Create the main window and run the application
if __name__ == "__main__":
    root = Tk()
    app = MyFirstWindow(root)
    root.mainloop()