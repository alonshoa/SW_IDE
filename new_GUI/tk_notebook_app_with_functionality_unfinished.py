import tkinter as tk
from tkinter import messagebox
from devince_codex_1.SW_IDE.new_GUI.tk_notebook import EditorNotebook
from button_functionality import beyond_compare,highlight_code,move_output_to_input,run_output,load_script,refresh_file_explorer,save_result,open_gitgub_descktop


class NotebookApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
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
        self.parent.bind("<Control-b>", self.beyond_compare)
        self.parent.bind("<Control-h>", self.highlight_code)
        self.parent.bind("<Control-m>", self.move_output_to_input)
        self.parent.bind("<Control-r>", self.run_output)
        self.parent.bind("<Control-l>", self.load_script)
        self.parent.bind("<Control-f>", self.refresh_file_explorer)
        self.parent.bind("<Control-a>", self.save_result)
        self.parent.bind("<Control-g>", self.open_gitgub_descktop)
        self.parent.bind("<Control-e>", self.open_file_explorer)

    def new_file(self, event=None):
        self.notebook.add_file()

    def open_file(self, event=None):
        self.notebook.add_file()

    def save_file(self, event=None):
        self.notebook.save(self.notebook.notebook.select())

    def beyond_compare(self, event=None):
        beyond_compare()

    def highlight_code(self, event=None):
        highlight_code()

    def move_output_to_input(self, event=None):
        move_output_to_input()

    def run_output(self, event=None):
        run_output()

    def load_script(self, event=None):
        load_script()

    def refresh_file_explorer(self, event=None):
        refresh_file_explorer()

    def save_result(self, event=None):
        save_result()

    def open_gitgub_descktop(self, event=None):
        open_gitgub_descktop()

    # def open_file_explorer(self, event=None):
    #     open_file_explorer()

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
