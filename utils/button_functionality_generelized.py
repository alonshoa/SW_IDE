import os
import re
import tkinter
import tkinter as tk
from idlelib import colorizer as ic, percolator as ip
from tkinter import ttk as ttk, filedialog

import subprocess
import tempfile

import openai
from .mylogger import MyLogger
from pygments.lexers import guess_lexer

from .git_functionality import init_git,pull_from_git,open_gitgub_descktop
from .openai_utils import get_list_of_models_for_edit



def save_result(text_to_save):
    file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is None:
        return
    text = text_to_save#app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()


def beyond_compare(text1,text2):
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        f.write(text1)
        f.seek(0)
        with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f2:
            f2.write(text2)
            f2.seek(0)
            subprocess.call(["C:\\Program Files\\Beyond Compare 4\\BCompare.exe", f.name, f2.name, "/ro1", "/ro2"])



def run_output(code_to_run):
    file = filedialog.asksaveasfile(mode="w", defaultextension=".py")
    if file is None:
        return
    text = code_to_run#app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()
    subprocess.call(["python", file.name])



def highlight_code(ta_in,ta_out):
    # language=detect_language(app.code_text.get("1.0", "end-1c"))
    cdg_i = ic.ColorDelegator()
    cdg_i.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
    cdg_i.idprog = re.compile(r'\s+(\w+)', re.S)

    cdg_i.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

    cdg_o = ic.ColorDelegator()
    cdg_o.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
    cdg_o.idprog = re.compile(r'\s+(\w+)', re.S)

    cdg_o.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

    ip.Percolator(ta_in).insertfilter(cdg_i)
    ip.Percolator(ta_out).insertfilter(cdg_o)



def move_output_to_input(frame):
    frame.set_code(frame.get_output_code())
    # app.code_text.insert(tk.END, app.output_code_textbox.get(1.0, tk.END))


def detect_language(code):
    return guess_lexer(code).name
