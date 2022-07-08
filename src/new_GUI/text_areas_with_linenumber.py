import tkinter as tk
from tkinter import ttk
from tkinter import font

# from utils import highlight_code
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


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
                args[0:3] == ("mark", "set", "insert") or
                args[0:2] == ("xview", "moveto") or
                args[0:2] == ("xview", "scroll") or
                args[0:2] == ("yview", "moveto") or
                args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result



class LinedText(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self)
        self.linenumbers = LineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.text.bind("<<Modified>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

    def _on_change(self, event):
        print("modified")
        self.linenumbers.redraw()

    def insert(self,*args):
        self.text.insert(*args)

    def get(self,*args):
        return self.text.get(*args)

    def delete(self, param, END):
        self.text.delete(param,END)



class ThreeTextAreas(tk.Frame):
    def __init__(self, parent, filename):
        tk.Frame.__init__(self, parent)
        self.filename = filename
        self.parent = parent
        self.onCodeModifiedEvents = []
        self.initUI()

    def registerCodeModifiedEvent(self, onCodeModifiedEvent):
        self.onCodeModifiedEvents.append(onCodeModifiedEvent)

    def initUI(self):
        self.pack(fill=tk.BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.lblA = tk.Label(self, text="Instructions")
        self.lblB = tk.Label(self, text="Code")
        self.lblC = tk.Label(self, text="Output Code")

        self.areaA = tk.Text(self)
        self.areaB = LinedText(self)
        self.areaC = LinedText(self)

        # self.linenumbers = LineNumbers(self, width=30)
        # self.linenumbers.attach(self.areaB)
        # self.linenumbers.attach(self.areaC)

        # self.areaB.bind("<<Change>>", self._on_change)
        # self.areaC.bind("<<Change>>", self._on_change)
        # self.areaB.bind("<Configure>", self._on_change)
        # self.areaC.bind("<Configure>", self._on_change)

        highlight_code(self.areaB.text, self.areaC.text)
        self.areaB.bind("<<Modified>>", self.onCodeModified)

        self.lblA.grid(sticky=tk.W, pady=4, padx=5, row=0, column=0)
        self.lblB.grid(sticky=tk.W, pady=4, padx=5, row=0, column=1)
        self.lblC.grid(sticky=tk.W, pady=4, padx=5, row=0, column=2)

        # self.linenumbers.grid(row=1, column=3, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.areaA.grid(row=1, column=0, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.areaB.grid(row=1, column=1, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.areaC.grid(row=1, column=2, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)

    def onCodeModified(self, event):
        for callback in self.onCodeModifiedEvents:
            callback(event)

    def set_code(self, content):
        self.areaB.insert(1.0, content)

    def get_code(self):
        return self.areaB.get(1.0, tk.END)

    def get_instructions(self):
        self.areaC.delete(1.0, tk.END)
        return self.areaA.get(1.0, tk.END)

    def set_output_code(self, content):
        self.areaC.insert(1.0, content)

    def get_output_code(self):
        return self.areaC.get(1.0, tk.END)


def main():
    root = tk.Tk()

    def onCodeModifiedEvent(event):
        print("modified")

    ex = ThreeTextAreas(root, "test")
    root.geometry("600x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()



