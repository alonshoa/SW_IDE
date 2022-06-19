import tkinter as tk
import os
import os.path
from tkinter import filedialog
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
        self.file_list = tk.Listbox(self)
        self.file_list.pack(side="top")

        self.open_button = tk.Button(self)
        self.open_button["text"] = "Open"
        self.open_button["command"] = self.open_file
        self.open_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_file(self):
        file = self.file_list.get(self.file_list.curselection())
        if file:
            os.startfile(file.path)

    def populate_file_list(self):
        self.file_list.delete(0, tk.END)
        files = self.get_files()
        for file in files:
            self.file_list.insert(tk.END, file)

    def get_files(self):
        files = set()
        for root, dirs, file_names in os.walk(os.getcwd()):
            for file_name in file_names:
                files.add(File(file_name, os.path.join(root, file_name)))
        return files


root = tk.Tk()
app = FileExplorer(master=root)
app.populate_file_list()
app.mainloop()

