import tkinter as tk
from tkinter import messagebox

from devince_codex_1.SW_IDE.new_GUI.darkmode import DarkMode
from devince_codex_1.SW_IDE.new_GUI.tk_notebook import EditorNotebook


class NotebookApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # DarkMode(self)
        self.parent = parent
        self.notebook = EditorNotebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.parent.title("Text Editor")
        self.parent.geometry("1000x600")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.parent.bind("<Control-n>", self.new_file)
        self.parent.bind("<Control-o>", self.open_file)
        self.parent.bind("<Control-s>", self.save_file)
        self.parent.bind("<Control-q>", self.on_close)
        self.parent.bind("<Control-w>", self.close_file)

    def new_file(self, event=None):
        self.notebook.add_file()

    def open_file(self, event=None):
        self.notebook.add_file()

    def save_file(self, event=None):
        self.notebook.save(self.notebook.notebook.select())

    def close_file(self, event=None):
        self.notebook.close(self.notebook.notebook.select())

    def on_close(self, event=None):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookApplication(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
