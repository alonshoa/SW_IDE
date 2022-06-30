import os
import os.path
import tkinter as tk
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


def get_file_size(file_path):
    return os.path.getsize(file_path)


class FileExplorer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.open_file_event = None
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

        self.tree.bind("<Double-Button-1>", self.open_file)
        self.tree.bind("<Return>", self.open_file)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_file(self, event=None):
        cur_item = self.tree.focus()
        if self.tree.item(cur_item)["values"][1] == 'directory':
            if self.tree.item(cur_item, "open"):
                self.tree.item(cur_item, open=False)
            else:
                self.tree.item(cur_item, open=True)
        else:
            file_path = self.tree.item(cur_item)["values"][0]
            if self.open_file_event is not None:
                self.open_file_event(file_path)
            else:
                os.startfile(file_path)

    def populate_file_list(self, file_path=os.getcwd()):
        self.tree.delete(*self.tree.get_children())
        self.populate_tree(file_path)

    def populate_tree(self, root_path):
        self.tree.insert("", "end", root_path, text=root_path, open=True)
        for file in os.listdir():
            self.tree.insert("", "end", file, text=file)
            if os.path.isdir(file):
                for sub in os.listdir(file):
                    file_sub = file + "/" + sub
                    self.tree.insert(file, "end", file_sub, values=(file_sub, "file", get_file_size(file_sub)),
                                     text=file_sub)


if __name__ == '__main__':
    root = tk.Tk()
    app = FileExplorer(master=root)
    app.populate_file_list()
    app.mainloop()
