from tkinter import *
from functools import partial

# Example data
data = {
    'place': ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
    'Associate': [
        'Associate_1', 'Associate_2', 'Associate_3', 'Associate_4',
        'Associate_5', 'Associate_6', 'Associate_7', 'Associate_8'
    ],
    'Points': [50, 70, 80, 60, 90, 30, 40, 85, 95, 65]
}

class CanvasTable:
    def __init__(self, master, data):
        # input var's
        self.master = master
        self.data = data
        # setting var's
        self.master.title("CanvasTable")
        self.master.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
        self.text_font_6 = ("Arial", "12", "bold")
        self.text_fg = "#FFFFFF"
        self.background = "white"
        self.parent_frame = Frame(self.master, bg=self.background)
        self.parent_frame.grid(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        button_fg = "white"
        button_bg = "#004C99"
        #frames
        self.table_frame = Frame(self.parent_frame, bg=self.background)
        self.table_frame.grid(row=1, column=0,padx=10 , pady=10)
        self.file_frame = Frame(self.parent_frame, bg=self.background)
        self.file_frame.grid(row=1, column=1,padx=10 , pady=10)
        # create_child_widgets
        self.create_table_widgets()
        self.create_file_widgets()
#<<<<<        table_widgets        >>>>>
    def create_table_widgets(self):
        self.canvas = Canvas(self.table_frame, bg="white")
        self.canvas.pack(expand=True, fill=BOTH)
         # table var's
        self.row_height = 30
        self.column_widths = [60, 100, 60]
        self.heading = 'full culb points'
        self.headers = ['Place', 'Associate', ' Total\nPoints']
        # draw table
        self.draw_extra_row()
        self.draw_3_header()

        for i, (place, associate, points) in enumerate(zip(data['place'], data['Associate'], data['Points'])):
            y = (i + 2) * self.row_height  # Adjust y position by +2 to account for extra row and headers
            self.draw_8_rows(y, place, associate, points)
    def draw_extra_row(self):
        x_start = 0
        y_start = 0
        x_end = sum(self.column_widths)
        y_end = self.row_height

        self.canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="lightgreen", outline="black", width=1)
        self.canvas.create_text(x_end / 2, y_end / 2, text="Extra Row", font=("Arial", 10, "bold"))
    def draw_3_header(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill="lightgray", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"))
        self.canvas.create_line(0, 2 * self.row_height, sum(self.column_widths), 2 * self.row_height, fill="black")
    def draw_8_rows(self, y, place, associate, points):
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, fill="lightgray", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=value, font=("Arial", 10))
#<<<<<      file_widgets       >>>>>
    def create_file_widgets(self): 
        self.text_box = Text(self.file_frame, width=40, height=10)
        self.text_box.pack(pady=20, padx=20)
if __name__ == "__main__":
    root = Tk()
    app = CanvasTable(root, data)
    root.mainloop()