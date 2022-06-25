import tkinter as tk
import os
import os.path
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox


class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.path == other.path

    def __hash__(self):
        return hash((self.name, self.path))


class FileExplorer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("fullpath", "type", "size"))
        self.tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
        self.tree.column("fullpath", width=225, minwidth=225, stretch=tk.NO)
        self.tree.column("type", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("size", width=100, minwidth=100, stretch=tk.NO)

        self.tree.heading("#0", text="Name", anchor=tk.W)
        self.tree.heading("size", text="Size", anchor=tk.W)
        self.tree.heading("type", text="Type", anchor=tk.W)
        self.tree.heading("fullpath", text="Full Path", anchor=tk.W)

        self.tree.pack(side="top")

        self.open_button = tk.Button(self)
        self.open_button["text"] = "Open"
        self.open_button["command"] = self.open_file
        self.open_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_file(self):
        item = self.tree.selection()[0]
        file = self.tree.item(item)["values"][2]
        os.startfile(file)

    def populate_file_list(self):
        self.tree.delete(*self.tree.get_children())
        files = self.get_files()
        for root, dirs, file_names in os.walk(os.getcwd()):
            for file_name in file_names:
                if not file_name.startswith('.'):
                    file = File(file_name, os.path.join(root, file_name))
                    self.tree.insert("", tk.END, values=(file.name, "", file.path),text=file.name)

    def get_files(self):
        return []


root = tk.Tk()
app = FileExplorer(master=root)
app.populate_file_list()
app.mainloop()



