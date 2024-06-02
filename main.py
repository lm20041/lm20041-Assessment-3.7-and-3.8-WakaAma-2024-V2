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

        # Create entry labels and boxes
        for i, label in enumerate(entry_labels):
            # Create and place the label above the entry box
            Label(self.parent_frame, text=label, font=self.text_font_6, bg=self.background).grid(row=i*2, column=0, sticky=W, padx=5, pady=(10, 0))
            entry_box = Entry(self.parent_frame, font=self.text_font_6)
            entry_box.grid(row=i*2+1, column=0, pady=5)
            self.entry_boxes.append(entry_box)

        # Create validate button
        self.validate_button = Button(self.master, text="Validate", command=self.validate_entries)
        self.validate_button.pack(pady=20)

        # Create error message label
        self.error_message_label = Label(self.master, text="", font=self.text_font_6, fg="red", bg=self.background)
        self.error_message_label.pack(pady=10)

    def validate_entries(self):
        # Define correct values
        correct_values = ["correct_folder", "correct_file", "correct_points"]
        error_messages = [
            "Invalid folder name.",
            "Invalid file name.",
            "Invalid points value."
        ]

        # Initialize error message
        all_valid = True
        error_message = "Errors:"

        # Validate each entry
        for i, entry_box in enumerate(self.entry_boxes):
            if entry_box.get() == correct_values[i]:
                entry_box.config(bg="green")
            else:
                entry_box.config(bg="red")
                all_valid = False
                error_message += f" {error_messages[i]}"

        # Display summary message
        if all_valid:
            self.error_message_label.config(text="All entries are valid.", fg="green")
        else:
            self.error_message_label.config(text=error_message, fg="red")

if __name__ == "__main__":
    root = Tk()
    app = EntryValidationApp(root)
    root.mainloop()