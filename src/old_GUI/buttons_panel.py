import tkinter as tk
import tkinter.filedialog

from .application_shortcut_binder import AppShortcuts
# from .button_functionality import create_slide_menu, save_result, \
#     create_file_explorer, highlight_code, move_output_to_input
#
# from .button_functionality import beyond_compare as compare_code
# from .jupyter_notebook_utils import save_output_to_ipynb_notebook  # gets name and code
# from .openai_utils import get_list_of_models_for_edit, send_to_openai
from ..utils.button_functionality import save_result, move_output_to_input
from ..utils.levenshtein_distance import compare_code
from ..utils.openai_utils import send_to_openai, send_to_openai_app


class ButtonsPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=0, sticky=tk.NSEW)
        self.create_widgets()

    def create_widgets(self):

        self.save_result_button = tk.Button(self, text="Save Result",
                                            command=lambda :save_result(self.master))
        self.save_result_button.grid(row=1, column=0, sticky=tk.NSEW)

        # self.highlight_code_button = tk.Button(self, text="Highlight Code",
        #                                        command=highlight_code)
        # self.highlight_code_button.grid(row=3, column=0, sticky=tk.NSEW)

        self.compare_code_button = tk.Button(self, text="Compare Code",
                                             command=lambda :compare_code(self.master))
        self.compare_code_button.grid(row=4, column=0, sticky=tk.NSEW)

        self.save_output_to_ipynb_notebook_button = tk.Button(self, text="Save Output to Notebook",
                                                              command=self.save_output_to_ipynb_notebook)
        self.save_output_to_ipynb_notebook_button.grid(row=5, column=0, sticky=tk.NSEW)

        # self.get_list_of_models_for_edit_button = tk.Button(self, text="Get List of Models for Edit",
        #                                                     command=get_list_of_models_for_edit)
        # self.get_list_of_models_for_edit_button.grid(row=6, column=0, sticky=tk.NSEW)
        self.move_output_to_input = tk.Button(self, text="Move output to input",
                              command=lambda : move_output_to_input(self.master))
        self.move_output_to_input.grid(row=6, column=0, sticky=tk.NSEW)

        self.send_to_openai_button = tk.Button(self, text="Submit",
                                               command=lambda :send_to_openai_app(self.master))
        self.send_to_openai_button.grid(row=7, column=0, sticky=tk.NSEW)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=8, column=0, sticky=tk.NSEW)

    def save_output_to_ipynb_notebook(self,event=None):
        self.master.save_result_to_notebook()





