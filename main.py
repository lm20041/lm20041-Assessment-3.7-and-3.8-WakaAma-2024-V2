from tkinter import *

class EntryValidationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Entry Validation")

        self.text_font_6 = ("Helvetica", 12)
        self.background = "white"
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.pack(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Define entry labels
        entry_labels = ["Folder", "File", "Points"]
        self.entry_boxes = []
        self.error_labels = []

        # Create entry labels, boxes, and error labels
        for i, label in enumerate(entry_labels):
            # Create and place the label above the entry box
            Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i*3, column=0, sticky=W, padx=5, pady=(10, 0))
            entry_box = Entry(self.parent_frame, font=self.text_font_6)
            entry_box.grid(row=i*3+1, column=0, pady=5)
            self.entry_boxes.append(entry_box)
            error_label = Label(self.parent_frame, text="", font=self.text_font_6, bg=self.background, fg="red")
            error_label.grid(row=i*3+2, column=0, sticky=W, padx=5)
            self.error_labels.append(error_label)

        # Create validate button
        self.validate_button = Button(self.master, text="Validate", command=self.validate_entries)
        self.validate_button.pack(pady=20)

    def validate_entries(self):
        # Define correct values
        correct_values = ["correct_folder", "correct_file", "correct_points"]
        error_messages = [
            "Invalid folder name.",
            "Invalid file name.",
            "Invalid points value."
        ]

        # Validate each entry
        for i, entry_box in enumerate(self.entry_boxes):
            if entry_box.get() == correct_values[i]:
                entry_box.config(bg="green")
                self.error_labels[i].config(text="")
            else:
                entry_box.config(bg="red")
                self.error_labels[i].config(text=error_messages[i])

if __name__ == "__main__":
    root = Tk()
    app = EntryValidationApp(root)
    root.mainloop()