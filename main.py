import tkinter as tk
from tkinter import ttk

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

        # Configure style
        style = ttk.Style(self)
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=25, font=("Arial", 10))
        style.map("Treeview", background=[("selected", "lightblue")], foreground=[("selected", "black")])

        self.tree = ttk.Treeview(self, style="Treeview")
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.tree['columns'] = ('Points',)

        # Define column headings
        self.tree.heading('#0', text='Associate', anchor=tk.W)
        self.tree.heading('Points', text='Points', anchor=tk.W)

        # Define column width and alignment
        self.tree.column('#0', width=200, anchor=tk.W)
        self.tree.column('Points', width=100, anchor=tk.W)

        # Insert data into the tree
        for i, (associate, points) in enumerate(zip(data['Associate'], data['Points'])):
            tags = ('oddrow',) if i % 2 == 0 else ('evenrow',)
            self.tree.insert('', 'end', text=associate, values=(points,), tags=tags)

        # Tag configurations for row colors
        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='#f0f0f0')

        # Add grid lines between cells
        self.add_grid_lines()

    def add_grid_lines(self):
        # Add lines between rows to create a grid line effect
        style = ttk.Style(self)
        style.configure("TreeviewSeparator", background="black", relief="solid")
        self.tree.tag_configure('separator', background='black')

        # Insert separators
        children = self.tree.get_children()
        for i in range(len(children) - 1):
            self.tree.insert('', i*2+1, text='', tags=('separator',))

if __name__ == "__main__":
    app = TableGraph(data)
    app.mainloop()