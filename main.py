import tkinter as tk

# Example data
data = {
    'place': ['1st','2st','3st','4st','5st','6st','7st','8st'],
    'Associate': [
        'Associate_1', 'Associate_2', 'Associate_3', 'Associate_4',
        'Associate_5', 'Associate_6', 'Associate_7', 'Associate_8',
        'Associate_9', 'Associate_10'
    ],
    'Points': [50, 70, 80, 60, 90, 30, 40, 85, 95, 65]
}

class TableGraph(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Table Graph")
        self.geometry("400x300")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.row_height = 30
        self.column_widths = [60,100, 60]
        self.headers = ['place','Associate', 'total Points']

        self.create_table(data)

    def create_table(self, data):
        # Draw extra row on top
        self.draw_extra_row()
        
        # Draw headers
        self.draw_headers()

        # Draw rows
        for i, (place, associate, points) in enumerate(zip(data['place'], data['Associate'], data['Points'])):
            y = (i + 2) * self.row_height
            self.draw_row(y, place, associate, points)
    def draw_extra_row(self):
        # Define the extra row content and position
        x_start = 0
        y_start = 0
        x_end = sum(self.column_widths)
        y_end = self.row_height

        # Draw the rectangle using those x, y points
        self.canvas.create_rectangle(x_start, y_start, x_end, y_end)
        # Draw the text centered in the row
        self.canvas.create_text(x_end / 2, y_end / 2, text="Full Club Points", font=("Arial", 10, "bold"), fill="#CCCCCC", outline="black", width=1)
    
    def draw_headers(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.canvas.create_rectangle(x, self.row_height, x + self.column_widths[col], 2 * self.row_height, fill="#EDEDED", outline="black", width=1)
            self.canvas.create_text(x + self.column_widths[col] / 2, 1.5 * self.row_height, text=header, font=("Arial", 10, "bold"))
        self.canvas.create_line(0, 2 * self.row_height, sum(self.column_widths), 2 * self.row_height, fill="black")

    def draw_row(self, y, place, associate, points):
        # Draw cells
        for col, value in enumerate([place, associate, points]):
            x = sum(self.column_widths[:col])
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=value, font=("Arial", 10))
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, outline="black", width=1)

if __name__ == "__main__":
    app = TableGraph(data)
    app.mainloop()