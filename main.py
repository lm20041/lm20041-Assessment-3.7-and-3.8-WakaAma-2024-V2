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

        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.tree['columns'] = ('Points',)

        # Define column headings
        self.tree.heading('#0', text='Associate', anchor=tk.W)
        self.tree.heading('Points', text='Points', anchor=tk.W)

        # Define column width and alignment
        self.tree.column('#0', width=150, anchor=tk.W)
        self.tree.column('Points', width=100, anchor=tk.W)

        # Insert data into the tree
        for associate, points in zip(data['Associate'], data['Points']):
            self.tree.insert('', 'end', text=associate, values=(points,))

if __name__ == "__main__":
    app = TableGraph(data)
    app.mainloop()