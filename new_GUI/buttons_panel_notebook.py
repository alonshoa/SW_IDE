import os
import pdb
import threading
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from utils.button_functionality_generelized import beyond_compare as compare_code
from utils.button_functionality_generelized import save_result, move_output_to_input
from utils.openai_utils import send_to_openai
from utils.feedback_window import FeedbackWindow


def get_all_templates():
    return [t for t in os.listdir(os.path.join(os.getcwd(),'templates')) if t.endswith('.tmlt')]



def get_template_code(template_name):
    with open(os.path.join(os.getcwd(),'templates',template_name),'r') as f:
        return f.read()


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

        self.move_output_to_input = tk.Button(self, text="Move output to input",
                              command=lambda : move_output_to_input(self.master
                                                                    ))
        self.move_output_to_input.grid(row=0, column=3, sticky=tk.NSEW)

        self.send_to_openai_button = tk.Button(self, text="Submit",
                                               command=lambda :self.send_to_openai(self.master))
        self.debug_button = tk.Button(self, text="Debug",
                                               command=lambda :pdb.set_trace())
        self.template_dropdown = ttk.Combobox(self, values=get_all_templates())
        self.template_dropdown.grid(row=0, column=6, sticky=tk.NSEW)

        self.debug_button.grid(row=8, column=0, sticky=tk.NSEW)
        self.send_to_openai_button.grid(row=0, column=4, sticky=tk.NSEW)
        self.use_template_button = tk.Button(self, text="Use Template",
                                               command=lambda :self.use_template(self.master))
        self.save_as_template_button = tk.Button(self, text="Save As Template",
                                                 command=lambda: self.save_as_template(self.master))

        self.save_as_template_button.grid(row=0, column=8, sticky=tk.NSEW)

        self.use_template_button.grid(row=0, column=7, sticky=tk.NSEW)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=0, column=5, sticky=tk.NSEW)

    def save_output_to_ipynb_notebook(self,event=None):
        self.master.save_result_to_notebook()

    def use_template(self, master):
        template_name = self.template_dropdown.get()
        template_code = get_template_code(template_name)
        master.set_code(template_code)

    def save_as_template(self, master):
        template_name = self.template_dropdown.get()
        template_code = master.get_code()
        with open(os.path.join(os.getcwd(),'templates',template_name),'w') as f:
            f.write(template_code)

    def send_to_openai(self, master):
        output_code = send_to_openai(master.get_instructions(),master.get_code())
        def wait_for_openai_and_pop_up_message():
            time.sleep(15)
            FeedbackWindow()

            # messagebox.showinfo("FeedbackWindow", "OpenAI is done")

        threading.Thread(target=wait_for_openai_and_pop_up_message).start()
        self.master.set_output_code(output_code)


