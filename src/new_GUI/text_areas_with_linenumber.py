import tkinter as tk
from tkinter import ttk
from tkinter import font
from src.utils.button_functionality_generelized import highlight_code



class LineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class LinedText(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self)
        self.linenumbers = LineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.text.bind("<KeyRelease-Return>", self._on_change)
        self.text.bind("<BackSpace>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.bind("<MouseWheel>", self._on_change)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def insert(self,*args):
        self.text.insert(*args)

    def get(self,*args):
        return self.text.get(*args)

    def delete(self, param, END):
        self.text.delete(param,END)


