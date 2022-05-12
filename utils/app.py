import tkinter as tk
import tkinter.filedialog

from .button_functionality import create_slide_menu, send_to_openai, save_result, \
    create_file_explorer, create_file_explorer2
# compare_code, \
# from devince_codex_1.utils.levenshtein_distance import compare_code
from .button_functionality import beyond_compare as compare_code

from .openai_utils import get_list_of_models_for_edit

def generate_drop_down_list(root):
    models = get_list_of_models_for_edit()
    variable = tk.StringVar(root)
    variable.set(models[0])

    w = tk.OptionMenu(root, variable, *models)
    root.dropdown_list = w
    return root


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.file_explorer = None
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)
        generate_drop_down_list(self)
        create_slide_menu(self)
        self.dropdown_list.grid(row=2, column=0)

    def create_widgets(self):
        self.instructions_label = tk.Label(self, text="Input Instructions:")
        self.file_label = tk.Label(self, text="File:")
        self.code_label = tk.Label(self, text="Input Code:")
        self.instructions_text = tk.Text(self, width=100, height=10)
        self.code_text = tk.Text(self, width=100, height=30)
        self.output_code_textbox = tk.Text(self, width=100, height=30, state="disabled")
        self.output_code_label = tk.Label(self, text="Output Code:")
        self.move_output_to_input_button = tk.Button(self, text="Move Output to Input", command=lambda: self.move_output_to_input())
        self.submit_button = tk.Button(self, text="Submit", command=lambda: send_to_openai(self))
        self.save_result_button = tk.Button(self, text="Save Result to File", command=lambda: save_result(self))
        self.compare_code_button = tk.Button(self, text="Compare Code", command=lambda: compare_code(self))

        self.instructions_label.grid(row=0, column=0)
        #self.code_label.grid(row=1, column=0)
        self.file_label.grid(row=1, column=0)
        self.instructions_text.grid(row=0, column=1)
        self.code_text.grid(row=1, column=1)
        self.output_code_label.grid(row=0, column=2)
        self.output_code_textbox.grid(row=1, column=2)
        self.submit_button.grid(row=2, column=1)
        self.save_result_button.grid(row=2, column=2)
        self.move_output_to_input_button.grid(row=3, column=2)
        create_file_explorer(self)
        self.compare_code_button.grid(row=2, column=4)

    def move_output_to_input(self):
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, self.output_code_textbox.get(1.0, tk.END))
