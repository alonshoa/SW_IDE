import openai
import os
import tkinter as tk

openai.api_key = os.getenv("OPENAI_KEY")


def get_list_of_models():
    models = openai.Completion.models()
    return models

def get_list_of_models_for_edit():
    #models = openai.Edit. .models()
    models = ['code-davinci-edit-001','text-davinci-edit-001']
    return models

def generate_drop_down_list(root):
    models = get_list_of_models_for_edit()
    variable = tk.StringVar(root)
    variable.set(models[0])

    w = tk.OptionMenu(root, variable, *models)
    w.pack()
    return root
