from tkinter import *
root = Tk() # Step 1: Create the main window

root.title("My First Tkinter Window") # Step 2: Set window title

root.geometry("400x300") # Step 3: Set window size (width x height)

# Step 4: Add a label widget using .grid
label = Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.grid(row=0, column=0, padx=20, pady=20)

# Step 5: Add a button widget using .grid
button = Button(root, text="Click Me!", font=("Helvetica", 14), command=lambda: print("Button Clicked!"))
button.grid(row=1, column=0, padx=20, pady=10)


root.mainloop() # Step 6: Run the application