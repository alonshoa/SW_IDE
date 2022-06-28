import tkinter as tk
from tkinter import messagebox, filedialog, Menu

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
        self.create_menu()
        self.parent.title("Text Editor")
        self.parent.geometry("1000x600")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.parent.bind("<Control-n>", self.new_file)
        self.parent.bind("<Control-o>", self.open_file)
        self.parent.bind("<Control-s>", self.save_file)
        self.parent.bind("<Control-q>", self.on_close)

    def create_menu(self):
        self.menu = Menu(self.parent)
        self.parent.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Close", command=self.close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_close)

        self.edit_menu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.find)
        self.edit_menu.add_command(label="Replace", command=self.replace)

        self.run_menu = Menu(self.menu)
        self.menu.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run", command=self.run)
        self.run_menu.add_command(label="Run with input", command=self.run_with_input)
        self.run_menu.add_command(label="Run with output", command=self.run_with_output)

        self.help_menu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

    def undo(self):
        pass

    def redo(self):
        pass

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def find(self):
        pass

    def replace(self):
        pass

    def run(self):
        pass

    def run_with_input(self):
        pass

    def run_with_output(self):
        pass

    def about(self):
        pass

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

