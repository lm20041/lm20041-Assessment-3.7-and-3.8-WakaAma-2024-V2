from tkinter import *

class MyFirstWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My First Tkinter Window")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Create a label widget using .grid
        self.label = Label(self.root, text="Hello, Tkinter!", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # Create a button widget using .grid
        self.button = Button(self.root, text="Click Me!", font=("Helvetica", 14), command=self.on_button_click)
        self.button.grid(row=1, column=0, padx=20, pady=10)

    def on_button_click(self):
        print("Button Clicked!")

# Create the main window and run the application
if __name__ == "__main__":
    root = Tk()
    app = MyFirstWindow(root)
    root.mainloop()