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

class BarChart(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Bar Chart")
        self.geometry("800x600")
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack()
        self.draw_chart(data)

    def draw_chart(self, data):
        associates = data['Associate']
        points = data['Points']

        # Define some parameters
        bar_width = 40
        spacing = 20
        margin = 50
        max_height = 400
        max_points = max(points)

        # Draw bars
        for i, (associate, point) in enumerate(zip(associates, points)):
            x0 = margin + i * (bar_width + spacing)
            y0 = margin + max_height - (point / max_points) * max_height
            x1 = x0 + bar_width
            y1 = margin + max_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            self.canvas.create_text((x0 + x1) / 2, y1 + 10, text=associate, anchor=tk.N, angle=45)
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(point), anchor=tk.S)

if __name__ == "__main__":
    app = BarChart(data)
    app.mainloop()