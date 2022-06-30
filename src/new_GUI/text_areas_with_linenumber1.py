import tkinter as tk
from tkinter import ttk
from tkinter import font

# from utils import highlight_code


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
        self.text = CustomText(self)
        self.linenumbers = LineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

    def _on_change(self, event):

        self.linenumbers.redraw()

class BreakableTextarea(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.text = tk.Text(self, **kwargs)
        # self.breakpoint_area = tk.Canvas(self, width=100, **kwargs)
        # width_ = self.text.cget("width") / 10
        # print(width_)
        self.breakpoint_area = tk.Canvas(self, width=10, **kwargs)
        # self.breakpoint_area.tag_raise()
        self.breakpoint_area.pack(side=tk.LEFT,ipadx=5, fill=tk.BOTH,expand=True)
        self.breakpoint_area.bind("<Button-1>", self.toggle_breakpoint)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.breakpoints = set()
        self.text.bind("<F8>", self.step_over)

    def step_over(self, event):
        self.text.event_generate("<<step-over>>")

    def toggle_breakpoint(self, event):
        line_number = self.text.index("@%s,%s linestart" % (event.x, event.y)).split(".")[0]
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
        else:
            self.breakpoints.add(line_number)
        self.draw_breakpoints()

    def draw_breakpoints(self):
        self.breakpoint_area.delete("all")
        for line_number in self.breakpoints:
            y = self.text.bbox(line_number + ".0")[1]
            self.breakpoint_area.create_oval(2, y + 2, 18, y + 18, fill="red")

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.draw_breakpoints()

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)
        self.draw_breakpoints()

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)
        self.draw_breakpoints()

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    # def tag_names(self, *args, **kwargs):
    #     return self.text.tag_names(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

    def tag_has(self, *args, **kwargs):
        return self.text.tag_has(*args, **kwargs)

import tkinter as tk
from tkinter import ttk
from tkinter import font

# from utils import highlight_code


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
        self.text = CustomText(self)
        self.linenumbers = LineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

    def _on_change(self, event):
        self.linenumbers.redraw()

class BreakableTextarea(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.text = tk.Text(self, **kwargs)
        # self.breakpoint_area = tk.Canvas(self, width=100, **kwargs)
        # width_ = self.text.cget("width") / 10
        # print(width_)
        self.breakpoint_area = tk.Canvas(self, width=10, **kwargs)
        # self.breakpoint_area.tag_raise()
        self.breakpoint_area.pack(side=tk.LEFT,ipadx=5, fill=tk.BOTH,expand=True)
        self.breakpoint_area.bind("<Button-1>", self.toggle_breakpoint)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.breakpoints = set()
        self.text.bind("<F8>", self.step_over)

    def step_over(self, event):
        self.text.event_generate("<<step-over>>")

    def toggle_breakpoint(self, event):
        line_number = self.text.index("@%s,%s linestart" % (event.x, event.y)).split(".")[0]
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
        else:
            self.breakpoints.add(line_number)
        self.draw_breakpoints()

    def draw_breakpoints(self):
        self.breakpoint_area.delete("all")
        for line_number in self.breakpoints:
            y = self.text.bbox(line_number + ".0")[1]
            self.breakpoint_area.create_oval(2, y + 2, 18, y + 18, fill="red")

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.draw_breakpoints()

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)
        self.draw_breakpoints()

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)
        self.draw_breakpoints()

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    # def tag_names(self, *args, **kwargs):
    #     return self.text.tag_names(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

    def tag_has(self, *args, **kwargs):
        return self.text.tag_has(*args, **kwargs)

import tkinter as tk
from tkinter import ttk
from tkinter import font

# from utils import highlight_code


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
        self.text = CustomText(self)
        self.linenumbers = LineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        # self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

        # def tag_has(self, *args, **kwargs):
        #     return self.text.tag_has(*args, **kwargs)


class BreakableTextarea(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.text = tk.Text(self, **kwargs)
        # self.breakpoint_area = tk.Canvas(self, width=100, **kwargs)
        # width_ = self.text.cget("width") / 10
        # print(width_)
        self.breakpoint_area = tk.Canvas(self, width=10, **kwargs)
        # self.breakpoint_area.tag_raise()
        self.breakpoint_area.pack(side=tk.LEFT,ipadx=5, fill=tk.BOTH,expand=True)
        self.breakpoint_area.bind("<Button-1>", self.toggle_breakpoint)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.breakpoints = set()
        self.text.bind("<F8>", self.step_over)

    def step_over(self, event):
        self.text.event_generate("<<step-over>>")

    def toggle_breakpoint(self, event):
        line_number = self.text.index("@%s,%s linestart" % (event.x, event.y)).split(".")[0]
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
        else:
            self.breakpoints.add(line_number)
        self.draw_breakpoints()

    def draw_breakpoints(self):
        self.breakpoint_area.delete("all")
        for line_number in self.breakpoints:
            y = self.text.bbox(line_number + ".0")[1]
            self.breakpoint_area.create_oval(2, y + 2, 18, y + 18, fill="red")

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.draw_breakpoints()

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)
        self.draw_breakpoints()

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)
        self.draw_breakpoints()

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

    # def tag_has(self, *args, **kwargs):
    #     return self.text.tag_has(*args, **kwargs)


