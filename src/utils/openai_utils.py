from tkinter import messagebox

import openai
import os
import tkinter as tk

# from .button_functionality import  get_response
from .mylogger import MyLogger

openai.api_key = os.getenv("OPENAI_KEY")
logger = MyLogger()


def get_response(instruction, code):
    try:
        response = openai.Edit.create(
            engine="code-davinci-edit-001",
            input=code,
            instruction=instruction,
            temperature=0,
            top_p=1
        )
        return response
    except Exception as e:
        messagebox.showerror("Error", str(e))



def get_list_of_models():
    models = openai.Completion.models()
    return models

def get_list_of_models_for_edit():
    #models = openai.Edit.models() # this was a madeup function (dont exist that maybe will be implemented later)
    models = ['code-davinci-edit-001','text-davinci-edit-001']
    return models

def generate_drop_down_list(root):
    models = get_list_of_models_for_edit()
    variable = tk.StringVar(root)
    variable.set(models[0])

    w = tk.OptionMenu(root, variable, *models)
    w.pack()
    return root


def send_to_openai(instructions,code):
    # instructions = app.instructions_text.get("1.0", "end-1c")
    # code = app.code_text.get("1.0", "end-1c")
    logger.log_info(['the instructions and the code',instructions,code])
    response = get_response(instructions, code)
    logger.log_info(f'the response - {response}')
    logger.log_info(f'the outcode- {response["choices"][0]["text"]}')
    return response["choices"][0]["text"]
    # app.output_code_textbox.config(state="normal")
    # app.output_code_textbox.delete("1.0", "end")
    # app.output_code_textbox.insert("1.0", response["choices"][0]["text"])
    # app.output_code_textbox.config(state="disabled")

def send_to_openai_app(app):
    instructions = app.instructions_text.get("1.0", "end-1c")
    code = app.code_text.get("1.0", "end-1c")
    logger.log_info(['the instructions and the code', instructions, code])
    response = get_response(instructions, code)
    logger.log_info(f'the response - {response}')
    logger.log_info(f'the outcode- {response["choices"][0]["text"]}')
    # return response
    app.output_code_textbox.config(state="normal")
    app.output_code_textbox.delete("1.0", "end")
    app.output_code_textbox.insert("1.0", response["choices"][0]["text"])
    app.output_code_textbox.config(state="disabled")

