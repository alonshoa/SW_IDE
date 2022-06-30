import os
import tkinter as tk
from tkinter import ttk
# from script import load_script
from devince_codex_1.SW_IDE.utils.button_functionality import load_script


class FileExplorer(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_file_explorer()


    def create_file_explorer(self):
        try:
            self.file_explorer.destroy()
        except:
            pass
        self.file_explorer = ttk.Treeview(self)
        self.file_explorer.grid(row=1, column=0)
        self.file_explorer.insert("", "end", ".", text=".", open=True)
        for file in os.listdir():
            self.file_explorer.insert("", "end", file, text=file)
            if os.path.isdir(file):
                for sub in os.listdir(file):
                    self.file_explorer.insert(file, "end", file + "/"+sub, text=file + "/"+sub)

        self.file_explorer.bind("<Double-1>", lambda event: load_script(self.master, file=event.widget.item(event.widget.focus())["text"]))
        self.file_explorer.bind("<Return>", lambda event: load_script(self.master, file=event.widget.item(event.widget.focus())["text"]))
