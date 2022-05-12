import os
import re
import subprocess
import tkinter as tk
from idlelib import colorizer as ic, percolator as ip
from tkinter import ttk as ttk

import openai
from utils.mylogger import MyLogger

from utils.git_functionality import init_git,pull_from_git,open_gitgub_descktop
logger = MyLogger()

def send_to_openai(app):
    instructions = app.instructions_text.get("1.0", "end-1c")
    code = app.code_text.get("1.0", "end-1c")
    logger.log_info(['the instructions and the code',instructions,code])
    response = get_response(instructions, code)
    logger.log_info(f'the response - {response}')
    app.output_code_textbox.config(state="normal")
    app.output_code_textbox.delete("1.0", "end")
    app.output_code_textbox.insert("1.0", response["choices"][0]["text"])
    app.output_code_textbox.config(state="disabled")


def save_result(app):
    file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is None:
        return
    text = app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()

# def compare_code(app):
#     input_code = app.code_text.get("1.0", "end-1c")
#     output_code = app.output_code_textbox.get("1.0", "end-1c")
#     input_code_lines = input_code.split("\n")
#     output_code_lines = output_code.split("\n")
#     if len(input_code_lines) != len(output_code_lines):
#         print("The input and output code are not aligned")
#         return
#     app.output_code_textbox.tag_config("diff", background="red")
#     for i in range(len(input_code_lines)):
#         if input_code_lines[i] != output_code_lines[i]:
#             app.output_code_textbox.tag_add("diff", str(i+1) + ".0", str(i+1) + ".end")
#     subprocess.call(["byondcompare", "input.txt", "output.txt"])

# def beyond_compare(app):
#     subprocess.call(["C:\\Program Files\\Beyond Compare 4\\BCompare.exe", app.code_text.get("1.0", "end-1c"), app.output_code_textbox.get("1.0", "end-1c")])
import subprocess
import tempfile

# def beyond_compare(app):
#     with tempfile.NamedTemporaryFile(mode='w+t') as f:
#         f.write(app.code_text.get("1.0", "end-1c"))
#         f.seek(0)
#         with tempfile.NamedTemporaryFile(mode='w+t') as f2:
#             f2.write(app.output_code_textbox.get("1.0", "end-1c"))
#             f2.seek(0)
#             subprocess.call(["C:\\Program Files\\Beyond Compare 4\\BCompare.exe", f.name, f2.name])


def beyond_compare(app):
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        f.write(app.code_text.get("1.0", "end-1c"))
        f.seek(0)
        with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f2:
            f2.write(app.output_code_textbox.get("1.0", "end-1c"))
            f2.seek(0)
            subprocess.call(["C:\\Program Files\\Beyond Compare 4\\BCompare.exe", f.name, f2.name, "/ro1", "/ro2"])


def compare_code(app):
    input_code = app.code_text.get("1.0", "end-1c")
    output_code = app.output_code_textbox.get("1.0", "end-1c")
    input_code_lines = input_code.split("\n")
    output_code_lines = output_code.split("\n")
    if len(input_code_lines) != len(output_code_lines):
        print("The input and output code are not aligned")
        return
    app.output_code_textbox.tag_config("diff", background="red")
    for i in range(len(input_code_lines)):
        if input_code_lines[i] != output_code_lines[i]:
            app.output_code_textbox.tag_add("diff", str(i+1) + ".0", str(i+1) + ".end")


def run_output(app):
    file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".py")
    if file is None:
        return
    text = app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()
    subprocess.call(["python", file.name])


def load_script(app,file=None):
    if file is None:
        file = tk.filedialog.askopenfile(mode="r")
    if type(file) is str:
        # file = tk.filedialog.
        file = open(file)
    text = file.read()
    app.code_text.delete("1.0", "end")
    app.code_text.insert("1.0", text)
    file.close()


def highlight_code(app):
    cdg = ic.ColorDelegator()
    cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
    cdg.idprog = re.compile(r'\s+(\w+)', re.S)

    cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

    ip.Percolator(app.code_text).insertfilter(cdg)


def create_file_explorer(app):
    app.file_explorer = ttk.Treeview(app)
    app.file_explorer.grid(row=1, column=0)
    app.file_explorer.insert("", "end", ".", text=".", open=True)
    for file in os.listdir():
        app.file_explorer.insert("", "end", file, text=file)
        if os.path.isdir(file):
            for sub in os.listdir(file):
                app.file_explorer.insert(file, "end", file + "/"+sub, text=file + "/"+sub)

    app.file_explorer.bind("<Double-1>", lambda event: load_script(app, file=event.widget.item(event.widget.focus())["text"]))
    highlight_code(app)

def create_file_explorer2(app):
    app.file_explorer = ttk.Treeview(app)
    app.file_explorer.grid(row=1, column=0)
    app.file_explorer.insert("", "end", ".", text=".", open=True)
    for root, dirs, files in os.walk("."):
        for file in files:
            app.file_explorer.insert("", "end", file, text=file)
        for dir in dirs:
            app.file_explorer.insert("", "end", dir, text=dir)
            app.file_explorer.insert(dir, "end", dir + "/", text=".")
    app.file_explorer.bind("<Double-1>", lambda event: load_script(app, file=event.widget.item(event.widget.focus())["text"]))
    highlight_code(app)


def create_slide_menu(app):
    app.slide_menu = tk.Menu(app.master)
    app.master.config(menu=app.slide_menu)
    app.file_menu = tk.Menu(app.slide_menu)
    app.slide_menu.add_cascade(label="File", menu=app.file_menu)
    app.file_menu.add_command(label="Load Script", command=lambda: load_script(app))
    app.file_menu.add_command(label="Save Result to File", command=lambda: save_result(app))
    app.edit_menu = tk.Menu(app.slide_menu)
    app.slide_menu.add_cascade(label="Edit", menu=app.edit_menu)
    app.file_menu.add_command(label="Run Output", command=lambda: run_output(app))
    app.file_menu.add_command(label="Set Working Directory", command=lambda: os.chdir(tk.filedialog.askdirectory()))
    app.git_menu = tk.Menu(app.slide_menu)
    app.git_menu.add_command(label="Open Github Desktop", command=lambda: open_gitgub_descktop(os.getcwd()))
    app.git_menu.add_command(label="Pull from Git", command=lambda: pull_from_git(os.getcwd()))
    app.slide_menu.add_cascade(label="Git", menu=app.git_menu)
    app.git_menu.add_command(label="Init Git", command=lambda: init_git(os.getcwd()))


def get_response(instruction, code):
    response = openai.Edit.create(
        engine="code-davinci-edit-001",
        input=code,
        instruction=instruction,
        temperature=0,
        top_p=1
    )
    return response
