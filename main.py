import tkinter as tk

# Example data
data = {
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
        # Draw headers
        self.draw_headers()

        # Draw rows
        for i, (associate, points) in enumerate(zip(data['Associate'], data['Points'])):
            y = (i + 1) * self.row_height
            self.draw_row(y, associate, points)

    def draw_headers(self):
        for col, header in enumerate(self.headers):
            x = sum(self.column_widths[:col])
            self.canvas.create_text(x + self.column_widths[col] / 2, self.row_height / 2, text=header, font=("Arial", 10, "bold"))
            self.canvas.create_rectangle(x, 0, x + self.column_widths[col], self.row_height, outline="black", width=1)
        # Draw the bottom line of the header
        self.canvas.create_line(0, self.row_height, sum(self.column_widths), self.row_height, fill="black")

    def draw_row(self, y, associate, points):
        # Draw cells
        for col, value in enumerate([associate, points]):
            x = sum(self.column_widths[:col])
            self.canvas.create_text(x + self.column_widths[col] / 2, y + self.row_height / 2, text=value, font=("Arial", 10))
            self.canvas.create_rectangle(x, y, x + self.column_widths[col], y + self.row_height, outline="black", width=1)

if __name__ == "__main__":
    app = TableGraph(data)
    app.mainloop()