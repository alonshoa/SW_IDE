import tkinter as tk
from tkinter import messagebox, filedialog

from .buttons_panel_notebook import ButtonsPanel
from .tk_notebook import EditorNotebook
# from buttons_panel import ButtonsPanel

class NotebookApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.notebook = EditorNotebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.buttons_panel = ButtonsPanel(self)
        self.buttons_panel.pack(fill=tk.X)
        self.parent.title("Text Editor")
        self.parent.geometry("1000x600")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.parent.bind("<Control-n>", self.new_file)
        self.parent.bind("<Control-o>", self.open_file)
        self.parent.bind("<Control-s>", self.save_file)
        self.parent.bind("<Control-q>", self.on_close)
        self.parent.bind("<Control-w>", self.close_file)

    def new_file(self, event=None):
        self.notebook.add_file(file_name="New File")
        # self.notebook.notebook.tab(self.notebook.notebook.select(), text=)
        self.notebook.set_modified(self.notebook.notebook.select())

    # def open_file(self, event=None):
        # self.notebook.add_file()
    def open_file(self, event=None):
        file_name = filedialog.askopenfilename(filetypes=(("Python", "*.py"), ("All files", "*.*")))
        if file_name:
            with open(file_name, "r") as file:
                content = file.read()
            self.notebook.add_file(file_name=file_name, content=content)

    def save_file(self, event=None):
        self.notebook.save(self.notebook.notebook.select())

    def close_file(self, event=None):
        self.notebook.close(self.notebook.notebook.select())

    def on_close(self, event=None):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.parent.destroy()

    def get_instructions(self):
        return self.notebook.get_instructions()

    def get_code(self):
        return self.notebook.get_code()

    def get_output_code(self):
        return self.notebook.get_output_code()

    def set_output_code(self, output_code):
        self.notebook.set_output_code(output_code)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookApplication(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
