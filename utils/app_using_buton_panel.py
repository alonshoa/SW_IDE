import tkinter as tk
import tkinter.filedialog

from .button_functionality import create_slide_menu, save_result, \
     move_output_to_input, generate_drop_down_list,  highlight_code,   create_file_explorer
# from .maybe_working_button_functionality import highlight_code
from .file_explorer import FileExplorer
from .button_functionality import beyond_compare as compare_code
from .buttons_panel import ButtonsPanel
from .jupyter_notebook_utils import save_output_to_ipynb_notebook  # gets name and code
from .openai_utils import send_to_openai
from .undo import Undo


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.file_explorer = FileExplorer(self)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.buttons_panel = ButtonsPanel(self)
        self.create_widgets()
        create_slide_menu(self)
        generate_drop_down_list(self)
        self.dropdown_list.grid(row=0, column=0)
        self.bind('<Shift-Return>', self.submit)
        self.undo = Undo()
        self.file_explorer.create_file_explorer()
        highlight_code(self)
        # self.code_text.bind("<KeyRelease>", lambda event: highlight_code(self))

    def update_file_explorer(self, event):
        self.file_explorer.create_file_explorer()

    def create_widgets(self):
        self.instructions_label = tk.Label(self, text="Input Instructions:")
        self.code_label = tk.Label(self, text="Input Code:")
        self.instructions_text = tk.Text(self, width=100, height=10)
        self.instructions_text.bind('<Key>', self.key)
        self.code_text = tk.Text(self, width=100, height=30)
        self.output_code_textbox = tk.Text(self, width=100, height=30, state="disabled")
        self.output_code_label = tk.Label(self, text="Output Code:")
        self.move_output_to_input_button = tk.Button(self, text="Move Output to Input",
                                                     command=lambda: self.move_output_to_input())
        # self.submit_button = tk.Button(self, text="Submit", command=self.submit)

        self.instructions_label.grid(row=1, column=0)
        self.code_label.grid(row=2, column=0)
        self.instructions_text.grid(row=1, column=1)
        self.code_text.grid(row=2, column=1)
        self.output_code_label.grid(row=1, column=2)
        self.output_code_textbox.grid(row=2, column=2)
        # self.submit_button.grid(row=2, column=1)

    def key(self, event):
        if event.keysym == 'z' and event.state == 4:
            self._undo()
        else:
            self.undo.addState(self.instructions_text.get(1.0, tk.END))

    def _undo(self):
        if len(self.undo.states) > 0:
            self.instructions_text.delete(1.0, tk.END)
            self.instructions_text.insert(1.0, self.undo.getState())

    def save_result_to_notebook(self):
        notebook_name = tk.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(
                                                          ("jupyter notebooks", "*.ipynb"), ("all files", "*.*")))
        save_output_to_ipynb_notebook(notebook_name, self.output_code_textbox.get(1.0, tk.END))

    def move_output_to_input(self):
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, self.output_code_textbox.get(1.0, tk.END))

    def submit(self, event=None):
        print("hit")
        # send_to_openai(self)
