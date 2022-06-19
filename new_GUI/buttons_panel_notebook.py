import pdb
import tkinter as tk

from devince_codex_1.SW_IDE.utils.button_functionality_generelized import beyond_compare as compare_code
from devince_codex_1.SW_IDE.utils.button_functionality_generelized import save_result, move_output_to_input
from devince_codex_1.SW_IDE.utils.openai_utils import send_to_openai


class ButtonsPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.grid(row=0, column=1, sticky=tk.NSEW)
        self.create_widgets()

    def create_widgets(self):

        self.save_result_button = tk.Button(self, text="Save Result",
                                            command=lambda :save_result(self.master.get_output_code()))
        self.save_result_button.grid(row=0, column=0, sticky=tk.NSEW)

        # self.highlight_code_button = tk.Button(self, text="Highlight Code",
        #                                        command=highlight_code)
        # self.highlight_code_button.grid(row=3, column=0, sticky=tk.NSEW)

        self.compare_code_button = tk.Button(self, text="Compare Code",
                                             command=lambda :compare_code(self.master.get_code(),self.master.get_output_code()))
        self.compare_code_button.grid(row=0, column=1, sticky=tk.NSEW)

        self.save_output_to_ipynb_notebook_button = tk.Button(self, text="Save Output to Notebook",
                                                              command=self.save_output_to_ipynb_notebook)
        self.save_output_to_ipynb_notebook_button.grid(row=0, column=2, sticky=tk.NSEW)

        # self.get_list_of_models_for_edit_button = tk.Button(self, text="Get List of Models for Edit",
        #                                                     command=get_list_of_models_for_edit)
        # self.get_list_of_models_for_edit_button.grid(row=6, column=0, sticky=tk.NSEW)
        self.move_output_to_input = tk.Button(self, text="Move output to input",
                              command=lambda : move_output_to_input(self.master
                                                                    ))
        self.move_output_to_input.grid(row=0, column=3, sticky=tk.NSEW)

        self.send_to_openai_button = tk.Button(self, text="Submit",
                                               command=lambda :self.send_to_openai(self.master))
        self.debug_button = tk.Button(self, text="Debug",
                                               command=lambda :pdb.set_trace())
        self.debug_button.grid(row=8, column=0, sticky=tk.NSEW)
        self.send_to_openai_button.grid(row=0, column=4, sticky=tk.NSEW)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=0, column=5, sticky=tk.NSEW)

    def save_output_to_ipynb_notebook(self,event=None):
        self.master.save_result_to_notebook()

    def send_to_openai(self, master):
        output_code = send_to_openai(master.get_instructions(),master.get_code())
        self.master.set_output_code(output_code)


