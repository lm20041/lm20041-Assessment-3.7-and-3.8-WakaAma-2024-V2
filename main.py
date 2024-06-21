from tkinter import *

def create_table():
    root = Tk()
    root.title("Canvas Table")

    canvas = Canvas(root, width=600, height=400)
    canvas.grid(row=0, column=0)

    # Define table dimensions
    table_width = 200
    table_height = 200
    cell_width = table_width // 8
    cell_height = table_height // 12

    # Draw table borders
    canvas.create_rectangle(0, 0, table_width, table_height, outline='black')

    return root, canvas, cell_width, cell_height

def draw_extra_row(canvas, cell_width, cell_height):
    # Draw an extra row at the bottom
    canvas.create_rectangle(0, cell_height * 11, cell_width * 8, cell_height * 12, outline='black')

def draw_3_header(canvas, cell_width, cell_height):
    # Draw header row
    canvas.create_rectangle(0, 0, cell_width * 3, cell_height, outline='black')

def draw_8_rows(canvas, cell_width, cell_height):
    # Draw 8 rows
    for row in range(1, 9):
        y1 = row * cell_height
        y2 = (row + 1) * cell_height
        canvas.create_rectangle(0, y1, cell_width * 8, y2, outline='black')

def main():
    root, canvas, cell_width, cell_height = create_table()
    draw_extra_row(canvas, cell_width, cell_height)
    draw_3_header(canvas, cell_width, cell_height)
    draw_8_rows(canvas, cell_width, cell_height)
    root.mainloop()

if __name__ == "__main__":
    main()